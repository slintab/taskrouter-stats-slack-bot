from .utils import is_valid_selection, remove_button
import config
from common.TaskRouterAdapter import TaskRouterAdapter
from stats.TRStatisticsFactory import TRStatisticsFactory


def select_option(ack):
    ack()


def show_button(ack, respond, body):
    ack()

    if not is_valid_selection(body):
        return

    respond(replace_original=True, blocks=remove_button(body))

    stat = TRStatisticsFactory.create(
        body,
        tr_client=TaskRouterAdapter(
            account_sid=config.TWILIO_ACCOUNT_SID,
            auth_token=config.TWILIO_AUTH_TOKEN,
            workspace_id=config.TASKROUTER_WORKSPACE_SID,
        ),
    )

    chart = stat.chart()

    respond(blocks=[{"type": "image", "image_url": chart, "alt_text": "chart"}])


def register(app):
    app.action("workflow_select")(select_option)
    app.action("taskqueue_select")(select_option)
    app.action("workspace_select")(select_option)
    app.action("stat_select")(select_option)
    app.action("workflow_show_button")(show_button)
    app.action("workspace_show_button")(show_button)
    app.action("taskqueue_show_button")(show_button)
