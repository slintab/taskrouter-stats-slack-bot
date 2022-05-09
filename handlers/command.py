import config
from .utils import load_report_options, parse_command_arg
from common.TaskRouterAdapter import TaskRouterAdapter
from commands.ResponseFactory import ResponseFactory


def command_handler(ack, say, command):
    # Acknowledge command request
    ack()

    command = parse_command_arg(command)
    options = load_report_options(config.REPORT_DEFINITION_FILE)

    resp = ResponseFactory(
        options=options,
        tr_client=TaskRouterAdapter(
            account_sid=config.TWILIO_ACCOUNT_SID,
            auth_token=config.TWILIO_AUTH_TOKEN,
            workspace_id=config.TASKROUTER_WORKSPACE_SID,
        ),
    ).create(command)

    msg = resp.create_message()

    say(**msg)


def register(app):
    app.command("/tr-stats")(command_handler)
