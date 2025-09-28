# GitHub ↔ Jira Automation

A tiny Flask-based service to create Jira issues with a single POST request. Ideal as a simple bridge between GitHub workflows, bots, or any automation that needs to open Jira tickets programmatically.

This repository contains a single script, `github-jira-automation.py`, that demonstrates how to call the Jira REST API to create an issue. The code intentionally keeps things minimal so you can quickly adapt it to your environment.

Highlights
- Single endpoint: POST /createJira
- Minimal dependencies: Flask and requests
- Easy to customize payload (summary, description, project key, issue type)
- Good starting point for integrating with GitHub Actions, webhooks or CI systems

Quick start

1. Clone
```bash
git clone https://github.com/AnirbanB13/github-jira-automation.git
cd github-jira-automation
```

2. Install dependencies
```bash
python -m pip install --user flask requests
```

3. Configure credentials
Open `github-jira-automation.py` and replace the placeholders:
- url — your Jira API endpoint, e.g. `https://your-domain.atlassian.net/rest/api/3/issue`
- API_TOKEN — your Jira API token
- HTTPBasicAuth username — your Jira account email

Recommendation: do NOT commit credentials. Instead export environment variables and update the script to read them (example env names below).

Environment variables (recommended)
- JIRA_URL — Jira create-issue endpoint
- JIRA_USER — Jira user email
- JIRA_API_TOKEN — Jira API token
- PROJECT_KEY — default project key (e.g. KAN)
- ISSUE_TYPE_ID — default issue type id (e.g. 10005)

You can export them before running:
```bash
export JIRA_URL="https://your-domain.atlassian.net/rest/api/3/issue"
export JIRA_USER="you@example.com"
export JIRA_API_TOKEN="your_api_token"
export PROJECT_KEY="KAN"
export ISSUE_TYPE_ID="10005"
```

Run
```bash
python github-jira-automation.py
```
By default the app listens on port 5001: http://0.0.0.0:5001/createJira

API: create a Jira issue
- Method: POST
- Path: /createJira
- Body: This demo ignores incoming request bodies and uses an in-file JSON payload. You should modify the script to accept and validate input in production.

Example payload used in the script (you can replace it with dynamic content)
```json
{
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Order entry fails when selecting supplier.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": { "key": "KAN" },
    "issuetype": { "id": "10005" },
    "summary": "Feature request: Slider required"
  },
  "update": {}
}
```

Example curl
```bash
curl -X POST http://localhost:5001/createJira
```

Production notes & improvements
- Do not keep credentials in source — use environment variables, vaults or secrets managers.
- Accept JSON request bodies and validate inputs instead of using a fixed payload.
- Add robust error handling and logging around the Jira API call.
- Protect the endpoint (authentication, IP allow-listing, GitHub webhook signature verification).
- Use connection pooling or persistent session for better performance with many requests.
- Consider running behind a WSGI server (gunicorn/uvicorn) and reverse proxy (nginx).
- Add retry/backoff for transient network errors when calling the Jira API.

Contributing
- Fixes, improvements and usage examples are welcome. Open an issue or submit a pull request.

License
- MIT

Author
- AnirbanB13 — https://github.com/AnirbanB13

Notes
This README documents the example script found in this repo. The sample is intentionally minimal to make it easy to adapt. If you'd like, I can:
- provide an improved version that reads config from environment variables and accepts a JSON body,
- add a Dockerfile and example GitHub Actions workflow,
- or implement authentication for the /createJira endpoint.

Which of these would you like next?
