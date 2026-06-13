class LearningVisibilityEngine:

    def build_snapshot(self, brain_score, risk, evolution, world_score, mutation_rate):

        return {
            "learning_confidence": brain_score,
            "risk": risk,
            "world_score": world_score,
            "mutation_rate": mutation_rate
        }
