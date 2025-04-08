import json
import re
from evaluations.evaluation import Evaluation
from evaluations.evaluation_result import EvaluationResult


class ModifyJsonEvaluation(Evaluation):
    def prepare_test_case(self, test_instance_path):
        """
        Loads the original JSON data and ground truth from the dataset instance.
        """
        with open(test_instance_path, "r", encoding="utf-8") as f:
            test_data = json.load(f)

        return {
            "data": test_data.get("data"),
            "instructions": test_data.get("instructions"),
            "ground_truth": test_data.get("ground_truth"),
            "name": test_data.get("name", test_instance_path),
        }

    def format_for_llm(self, test_case):
        """
        Formats the input for the LLM.
        """
        return [
            {
                "role": "system",
                "content": "You are a helpful assistant that modifies JSON objects based on given instructions. Output only the modified JSON with no other text or explanations."
            },
            {
                "role": "user",
                "content": f"Given the following JSON: ```json\n{json.dumps(test_case['data'], indent=2)}\n``` Modify the JSON as instructed: {test_case['instructions']}"
            },
            {
                "role": "assistant",
                "content": ""
            }
        ]

    def metric_function(self, test_case, llm_result):
        """
        Compares the LLM's output to the expected ground truth JSON.
        """
        cleaned_json = re.sub(r"```json\s*|\s*```", "", llm_result).strip()
        try:
            llm_output = json.loads(cleaned_json)
            ground_truth = test_case.get('ground_truth')

            if ground_truth is None:
                return EvaluationResult(score=1, explanation="No ground truth provided. Output is assumed valid.")

            if llm_output == ground_truth:
                return EvaluationResult(score=1, explanation="The JSON was modified correctly.")
            else:
                return EvaluationResult(score=0, explanation="The JSON modification was incorrect.")

        except json.JSONDecodeError as e:
            return EvaluationResult(score=0, explanation=f"Invalid JSON format: {e}")

