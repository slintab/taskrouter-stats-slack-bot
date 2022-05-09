from . import (
    help_command,
    workflow_command,
    workspace_command,
    taskqueue_command,
)


class CommandResponse:
    def __init__(self, options, tr_client):
        self.options = options
        self.tr_client = tr_client
        self.data = {}

        self.initialize()

    def create_message(self):
        message = {"text": self.build_text(), "blocks": self.build_blocks()}
        return message

    def build_text(self):
        return ""

    def build_blocks(self):
        return []

    def initialize(self):
        # Can be override for parsing, setup, etc.
        pass


class HelpCommandResponse(CommandResponse):
    def build_blocks(self):
        return help_command.parse_block()


class WorkspaceCommandResponse(CommandResponse):
    def initialize(self):
        self.set_report_options()

    def set_report_options(self):
        self.data.update({"reports": self.options["workspace"]})

    def build_blocks(self):
        return workspace_command.parse_block(self.data)


class WorkflowCommandResponse(CommandResponse):
    def initialize(self):
        self.set_report_options()
        self.set_workflow_options()

    def set_report_options(self):
        self.data.update({"reports": self.options["workflow"]})

    def set_workflow_options(self):
        options = []
        workflows = self.tr_client.get_all_workflows()

        for i in workflows:
            if "workflows" in i:
                options += i["workflows"]

        self.data.update({"workflows": options})

    def build_blocks(self):
        return workflow_command.parse_block(self.data)


class TaskQueueCommandResponse(CommandResponse):
    def initialize(self):
        self.set_report_options()
        self.set_taskqueue_options()

    def set_report_options(self):
        self.data.update({"reports": self.options["taskqueue"]})

    def set_taskqueue_options(self):
        options = []
        task_queues = self.tr_client.get_all_taskqueues()

        for i in task_queues:
            if "task_queues" in i:
                options += i["task_queues"]

        self.data.update({"task_queues": options})

    def build_blocks(self):
        return taskqueue_command.parse_block(self.data)
