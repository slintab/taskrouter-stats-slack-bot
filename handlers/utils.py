import yaml


def remove_button(message):
    del message["message"]["blocks"][2]["elements"][-1]

    return message["message"]["blocks"]


def is_valid_selection(message):
    values = message["state"]["values"]

    for i in values:
        for k in values[i]:
            if values[i][k]["selected_option"] is None:
                return False

    return True


def load_report_options(filename):
    reports = None

    with open(filename, "r") as f:
        try:
            reports = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)

    return reports


def parse_command_arg(command):
    if "text" not in command:
        return None

    return command["text"]
