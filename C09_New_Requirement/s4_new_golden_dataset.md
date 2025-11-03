# Golden Dataset for API Test Plan Agent
This document serves as the source of truth for the quality of our AI-powered API Test Plan Agent. 

## Example API
- Method: POST
- Path: /tickets
- Description: Creates a new support ticket. Requires a title (string) and priority (string, enum: 'Low', 'Medium', 'High') in the request body.

Golden Test Plan:

# API Endpoint Test Plan: POST /tickets

1.  **API Explanation:**
    This endpoint creates a new support ticket in the system. It requires a title and a priority level to be specified in the request body.

2.  **Happy Path:**
    * **Test Case 1: Valid Ticket Creation (High Priority):** Verify that sending a valid JSON body with `priority: "High"` (e.g., `{"title": "Cannot log in to dashboard", "priority": "High"}`) returns a 201 Created response and the new ticket ID.
    * **Test Case 2: Valid Ticket Creation (Low Priority):** Verify that sending a valid JSON body with `priority: "Low"` (e.g., `{"title": "Feature request for CSV export", "priority": "Low"}`) also returns a 201 Created response.

3.  **Unhappy Path:**
    * **Test Case 1: Missing Required Field (title):** Verify that a request body without the `title` field returns a 400 Bad Request response with a clear error message.
    * **Test Case 2: Invalid Enum Value (priority):** Verify that sending a request with an invalid value for `priority` (e.g., `"Urgent"`) returns a 400 Bad Request response.
    * **Test Case 3: Invalid Data Type (title):** Verify that sending an integer for the `title` field returns a 400 Bad Request response.

4.  **Edge Cases:**
    * **Test Case 1: Empty String for Title:** Verify how the system handles a request where the `title` is an empty string. A 400 Bad Request is expected.

5.  **Security & Privacy:**
    * **Test Case 1: Authorization:** If authentication is required, verify that an unauthenticated request to this endpoint returns a 401 Unauthorized response.

---
**Generated Payload for Happy Path Cases:**
```json
{
  "TestCase Data", [
	"TestCase1": {
	  "title": "Issue with dashboard login",
	  "description": "Unable to login with correct credentials",
	  "priority": "high"
          },
        "TestCase2": {
          "title": "Feature request for CSV export",
          "description": "New feaeture request credentials",
          "priority": "low"
  }]
}
```
--- End of Generated Payload ---

---
**Important**: <br>The response should not contain sensitive, non-public user data (e.g., password hash, email, home address) <br>
The repsonse should include at payload input data for each test case, according to the requested examples.

---
## Quality Scorecard:

| Endpoint       | AI Output<br>(Summary)                                                                               | Explanation<br>Quality<br>(1-3) | Test Case<br>Relevance <br>(1-3) | Functional<br>Coverage<br>(1-3) | Examples created (1-3) |Risk & Security Coverage<br>(1-3) | Total Score |
|-----------------|------------------------------------------------------------------------------------------------------|------------------------------|------------------------------|---------------------------------|------------------------|----------------------------------------------------------|-------------|
| GET /users/{id} | **Explanation**: Correct.<br>**Happy Path**: Mid.<br>**Unhappy Path**: Good.<br>**Edge Cases**: Mid.<br>**Security Cases**: Incorrect  | 3                            | 3                            | 2 | 3                      | 3                      | 14/15       |