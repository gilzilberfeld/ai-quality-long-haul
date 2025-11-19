# New Requirement

The Product Manager now wants the agent to be smarter. For every 'Happy Path' test case it generates, it must also generate a valid, ready-to-use JSON payload that could be used as the request body for that test.

## POST /tickets

```json
    {
        "title": "Issue with login",
        "description": "Unable to login with correct credentials",
        "priority": "high",
    }
```

If the JSON is not valid, the returned test plan will include a message that no valid JSON payload could be generated.