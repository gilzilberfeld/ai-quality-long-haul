# Golden Dataset for API Test Plan Agent

This document serves as the source of truth for the quality of our AI-powered API Test Plan Agent. This represents a curated example of a high-quality input and its corresponding ideal output, along with a scoring rubric.

## Example API
-   Method: GET
-   Path: ```/users/{id}```
-   Description: Get a user by ID.

# Golden Test Plan:

## API Endpoint Test Plan: GET /users/{id}
# API Endpoint Test Plan: GET /users/{id}

```
1.  **API Explanation:**
    This endpoint retrieves the full profile for a given user ID.

2.  **Happy Path:**
    * **Test Case 1: Valid User ID:** Verify that providing a valid, existing user ID (e.g., "1138") returns a 200 OK response with the correct user data in the expected JSON format.
    * **Test Case 2: All Fields Populated:** Verify that a user with all optional fields populated returns a complete and valid response.

3.  **Unhappy Path:**
    * **Test Case 1: Non-existent user ID:** Verify that providing a non-existent user ID (e.g., "99999") returns a 404 Not Found response.
    * **Test Case 2: Invalid user ID format:** Verify that providing a non-integer user ID (e.g., "abc") returns a 400 Bad Request response.

4.  **Edge Cases:**
    * **Test Case 1: Very Large User ID:** Verify that the system handles a request with a user ID at the maximum integer limit without errors.

5.  **Security & Privacy:**
    * **Test Case 1: PII Masking:** Verify that when the endpoint returns user data, any sensitive PII fields like `credit_card_number` are appropriately masked (e.g., showing only the last 4 digits, `************4444`) and not returned in plaintext.
```

## Quality Scorecard (After Fix):

Clarity (1-3): 3 - The plan is clear and follows the required structure.

Completeness (1-3): 3 - The agent's new output is now complete and includes the critical Security & Privacy section.

Correctness (1-3): 3 - The sections that are present are still technically correct.

Security & Privacy (1-3): 3 - The agent's new output addresses security issues.

**Total Score**: 12/12