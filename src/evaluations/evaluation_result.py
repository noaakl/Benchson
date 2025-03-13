from typing import Optional


class EvaluationResult:
    def __init__(
        self, score: int, explanation: str, ground_truth: Optional[str] = None
    ):
        if score not in [0, 1]:
            raise ValueError("Score must be either 0 or 1.")

        self.score = score
        self.explanation = explanation
        self.ground_truth = ground_truth

    def __repr__(self):
        return f"EvaluationResult(score={self.score}, explanation={self.explanation}, ground_truth={self.ground_truth})"
