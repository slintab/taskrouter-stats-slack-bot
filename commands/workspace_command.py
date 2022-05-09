from .utils import create_select_option


def parse_block(data):
    block = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Show workspace statistics",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Select from the options below and click on *Show*.",
            },
        },
        {
            "type": "actions",
            "block_id": "workspace",
            "elements": [
                {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select statistic",
                        "emoji": True,
                    },
                    "options": [],
                    "action_id": "stat_select",
                },
                {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Show!", "emoji": True},
                    "value": "show_button",
                    "action_id": "workspace_show_button",
                },
            ],
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "plain_text",
                    "text": "It might take a few seconds for the stats to display.",
                    "emoji": True,
                }
            ],
        },
    ]

    for i in data["reports"]:
        block[2]["elements"][0]["options"].append(
            create_select_option(
                text=next(iter(i.values())), value=next(iter(i.keys()))
            )
        )

    return block
