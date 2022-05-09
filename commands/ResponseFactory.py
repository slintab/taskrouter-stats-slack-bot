from .CommandResponse import *


class ResponseFactory:
    def __init__(self, tr_client, options):
        self.tr_client = tr_client
        self.options = options

    def create(self, cmd):
        if cmd == "workspace":
            return WorkspaceCommandResponse(
                tr_client=self.tr_client, options=self.options
            )

        if cmd == "workflow":
            return WorkflowCommandResponse(
                tr_client=self.tr_client, options=self.options
            )

        if cmd == "taskqueue":
            return TaskQueueCommandResponse(
                tr_client=self.tr_client, options=self.options
            )

        return HelpCommandResponse(tr_client=self.tr_client, options=self.options)
