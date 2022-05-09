def parse_block():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hi! :wave: You can use me to display *real-time statistics* :bar_chart: from your contact center :phone: in Slack!\n\nI currently support the following commands:\n`/tr-stats workspace` to show workspace stats\n`/tr-stats workflow` to show workflow stats\n`/tr-stats taskqueue` to show taskqueue stats\n`/tr-stats help` to show this help message\n",
            },
        }
    ]
