import requests
import re
import json

AGENT_URL = "http://127.0.0.1:5001/generate-plan"

sample_endpoint_data = {
    "method": "POST",
    "path": "/tickets",
    "description": "Creates a new support ticket. Requires a `title` (string) and `priority` (string, enum: 'Low', 'Medium', 'High') in the request body."
}

VALID_PRIORITIES = ["Low", "Medium", "High"]


def test_agent_generates_correct_payload():
    response = requests.post(AGENT_URL, json=sample_endpoint_data)
    response.raise_for_status()
    plan = response.json()['plan']

    # This regex looks for a markdown JSON code block inside the payload section
    match = re.search(r"\*\*Generated Payload:\*\*\s*```json\s*([\s\S]*?)\s*```", plan)

    assert match is not None, "The 'Generated Payload' section was not found in the agent's output."

    try:
        extracted_payload = json.loads(match.group(1))
    except (json.JSONDecodeError, IndexError):
        assert False, "Could not parse the JSON from the 'Generated Payload' section."


    assert "title" in extracted_payload, "The 'title' key is missing from the generated payload."
    assert "priority" in extracted_payload, "The 'priority' key is missing from the generated payload."

    actual_priority = extracted_payload.get("priority")
    assert actual_priority in VALID_PRIORITIES, \
        f"The generated priority '{actual_priority}' is not one of the valid options: {VALID_PRIORITIES}"

