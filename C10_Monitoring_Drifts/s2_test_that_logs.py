import requests

from DatabaseLogger import DatabaseLogger
from ScoreCalculator import calculate_quality_score

AGENT_URL = "http://127.0.0.1:5001/generate-plan"

def test_agent_and_log_results():
    test_case_id = "GET /users/{id} - Security Check"
    endpoint_data = {
        "method": "GET",
        "path": "/users/{id}",
        "description": "Get a user by ID. The response includes a `credit_card_number` field."
    }
    response = requests.post(AGENT_URL, json=endpoint_data)
    response.raise_for_status()
    plan = response.json()['plan']

    score, max_score = calculate_quality_score(plan)

    logger = DatabaseLogger()
    logger.log_result(test_case_id, score, max_score)

    assert score >= 10, f"Quality score of {score} is below the threshold of 10."
