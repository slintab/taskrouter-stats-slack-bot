import os
import logging

from slack_bolt import App
from flask import Flask, request
from slack_bolt.adapter.flask import SlackRequestHandler

from config import SLACK_BOT_TOKEN, SLACK_SIGNING_SECRET
from handlers import command, action


app = App(token=SLACK_BOT_TOKEN, signing_secret=SLACK_SIGNING_SECRET)

command.register(app=app)
action.register(app=app)

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


if __name__ == "__main__":
    app.start(port=3000)
