from .WorkspaceStatistics import WorkspaceStatistics
from .WorkflowStatistics import WorkflowStatistics
from .TaskQueueStatistics import TaskQueueStatistics


class TRStatisticsFactory:
    @staticmethod
    def get_stat_category(message):
        return message["message"]["blocks"][2]["block_id"]

    @staticmethod
    def get_stat_params(message):
        params = {}
        values = message["state"]["values"]

        for i in values:
            for param in values[i]:
                value = values[i][param]["selected_option"]["value"]
                text = values[i][param]["selected_option"]["text"]["text"]

                params.update({param: {"value": value, "text": text}})

        return params

    @staticmethod
    def create(message, tr_client):
        params = TRStatisticsFactory.get_stat_params(message)
        category = TRStatisticsFactory.get_stat_category(message)

        stat = params.pop("stat_select")["value"]

        if category == "workspace":
            return WorkspaceStatistics(stat=stat, params=params, tr_client=tr_client)

        if category == "workflow":
            return WorkflowStatistics(stat=stat, params=params, tr_client=tr_client)

        if category == "task_queue":
            return TaskQueueStatistics(stat=stat, params=params, tr_client=tr_client)
