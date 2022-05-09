def create_chart_config(chart_type, title, labels, datasets):
    return {
        "type": chart_type,
        "options": {
            "title": {
                "display": True,
                "text": title,
            },
        },
        "data": {"labels": labels, "datasets": datasets},
    }
