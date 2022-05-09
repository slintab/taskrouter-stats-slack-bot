import os

# Slack config
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]

# Twilio config
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TASKROUTER_WORKSPACE_SID = os.environ["TASKROUTER_WORKSPACE_SID"]

# Report definition path
REPORT_DEFINITION_FILE = "reports.yml"
