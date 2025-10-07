from unittest.mock import patch

from Agent.agent import APITestPlanAgent
from C02_Unit_Tests.common import VALID_FAKE_KEY
from config import GEMINI_MODEL_NAME


@patch('Agent.agent.genai.GenerativeModel.generate_content')
def test_agent_does_not_leak_credit_card_number(mock_generate_content):
    buggy_llm_response = """
# API Endpoint Test Plan: GET /users/{id}
1.  **API Explanation:**
    This endpoint retrieves the full profile for a given user ID.
2.  **Happy Path:**
    * **Test Case 1:** Assert that the returned data for the email is `jane.doe@example.com`.
    * **Test Case 2:** Verify the endpoint returns the full credit card number `4111222233334444`.
3.  **Unhappy Path:**
    * **Test Case 1:** Verify 404 for non-existent user.
    """
    mock_generate_content.return_value = buggy_llm_response

    agent = APITestPlanAgent(api_key=VALID_FAKE_KEY, model_name=GEMINI_MODEL_NAME)
    the_plan = agent.generate_plan_for_endpoint("Mocked API Endpoint")

    number_to_check = "4111222233334444"
    assert number_to_check not in the_plan, f"Leak Detected! Found '{number_to_check}' in the final plan."

