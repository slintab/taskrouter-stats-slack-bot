from .utils import create_select_option


def parse_block(data):
    block = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Show workflow statistics",
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
            "block_id": "workflow",
            "elements": [
                {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select workflow",
                        "emoji": True,
                    },
                    "options": [],
                    "action_id": "workflow_select",
                },
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
                    "action_id": "workflow_show_button",
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

    for i in data["workflows"]:
        block[2]["elements"][0]["options"].append(
            create_select_option(text=i["friendly_name"], value=i["sid"])
        )

    for i in data["reports"]:
        block[2]["elements"][1]["options"].append(
            create_select_option(
                text=next(iter(i.values())), value=next(iter(i.keys()))
            )
        )

    return block
