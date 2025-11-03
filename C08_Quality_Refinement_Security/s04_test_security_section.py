import requests
import pytest

AGENT_URL = "http://127.0.0.1:5001/generate-plan"

api_spec = {
    "method": "GET",
    "path": "/users/{id}",
    "description": "Get a user by ID."
}

# These are the new key concepts we now EXPECT to see in a high-quality plan
expected_security_concepts = [
    "security",
    "privacy",
    "pii",
    "masking",
    "sensitive"
]

@pytest.mark.parametrize("concept", expected_security_concepts)
def test_plan_includes_security_and_privacy_concepts(concept):
    response = requests.post(AGENT_URL, json=api_spec)
    response.raise_for_status()
    plan = response.json()['plan'].lower()

    assert concept in plan, \
        f"Expected security concept '{concept}' not found in the generated test plan."

