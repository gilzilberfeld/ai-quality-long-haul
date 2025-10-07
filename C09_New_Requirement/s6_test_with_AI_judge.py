import requests
import re

from AIJudge import AIJudge

AGENT_URL = "http://127.0.0.1:5001/generate-plan"

sample_endpoint_data = {
    "method": "POST",
    "path": "/tickets",
    "description": "Creates a new support ticket. Requires a `title` (string) and `priority` (string, enum: 'Low', 'Medium', 'High') in the request body."
}

VALID_PRIORITIES = ["Low", "Medium", "High"]


def test_agent_payload_with_ai_judge():
    response = requests.post(AGENT_URL, json=sample_endpoint_data)
    response.raise_for_status()
    plan = response.json()['plan']
    match = re.search(r"\*\*Generated Payload:\*\*\s*```json\s*([\s\S]*?)\s*```", plan)
    assert match is not None, "Could not find the payload to judge."

    generated_payload_str = match.group(1)

    json_schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string", "minLength": 10},
            "priority": {"type": "string", "enum": ["Low", "Medium", "High"]}
        },
        "required": ["title", "priority"]
    }

    judge = AIJudge()
    conforms, reasoning = judge.validate_payload(generated_payload_str, json_schema)

    assert conforms is True, \
        f"AI Judge found the payload to be non-conformant. Reasoning: {reasoning}"
