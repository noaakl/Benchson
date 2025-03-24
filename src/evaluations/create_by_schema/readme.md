# CreateBySchema

This evaluation is a basic evaluation that loads a json schema from the dataset, and asks the llm to generate a json that conforms to the given schema.

The evaluation metric is 0 if the generated json is not valid against the schema and 1 if it is.

The expected output should be JSON or JSON wrapped with backticks (```{JSON object}``` or ```json{JSON object}```)

Any other text in addition will fail the evaluation.