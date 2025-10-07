def calculate_quality_score(plan: str) -> (int, int):
    score = 12
    max_score = 12

    # A simple check: if the plan is missing the "Security" section, deduct points.
    if "security & privacy" not in plan.lower():
        score -= 4 # Major deduction for a missing critical section

    return score, max_score
