from .TRStatistics import TRStatistics
from .utils import create_chart_config


class TaskQueueStatistics(TRStatistics):
    def set_data(self):
        self.data = self.tr_client.get_taskqueue_statistics(
            self.params["taskqueue_select"]["value"]
        )[0]["result"]

    def TasksByStatus(self):
        labels = []
        data = []

        for k, v in self.data["tasks_by_status"].items():
            labels.append(k)
            data.append(v)

        datasets = [
            {
                "label": "Status",
                "data": data,
                "backgroundColor": "rgba(55, 166, 230, 0.5)",
                "borderColor": "rgb(55, 166, 230)",
                "borderWidth": 1,
            }
        ]

        self.chart_config = create_chart_config(
            chart_type="bar",
            title=f"Task Queue - {self.params['taskqueue_select']['text']}: Tasks by status",
            labels=labels,
            datasets=datasets,
        )

    def TasksByPriority(self):
        labels = []
        data = []

        for k, v in self.data["tasks_by_priority"].items():
            labels.append(k)
            data.append(v)

        datasets = [
            {
                "label": "Priority",
                "data": data,
                "backgroundColor": "rgba(55, 166, 230, 0.5)",
                "borderColor": "rgb(55, 166, 230)",
                "borderWidth": 1,
            }
        ]

        self.chart_config = create_chart_config(
            chart_type="bar",
            title=f"Task Queue - {self.params['taskqueue_select']['text']}: Tasks by priority",
            labels=labels,
            datasets=datasets,
        )

    def ActivityStatistics(self):
        labels = []
        data = []

        for i in self.data["activity_statistics"]:
            labels.append(i["friendly_name"])
            data.append(i["workers"])

        datasets = [
            {
                "label": "Activity",
                "data": data,
                "backgroundColor": "rgba(55, 166, 230, 0.5)",
                "borderColor": "rgb(55, 166, 230)",
                "borderWidth": 1,
            }
        ]

        self.chart_config = create_chart_config(
            chart_type="bar",
            title=f"Task Queue - {self.params['taskqueue_select']['text']}: Activity statistics",
            labels=labels,
            datasets=datasets,
        )

    def TotalAvailableWorkers(self):
        labels = ["Total available workers"]
        data = [self.data["total_available_workers"]]

        datasets = [
            {
                "label": "Available workers",
                "data": data,
                "backgroundColor": "rgba(55, 166, 230, 0.5)",
                "borderColor": "rgb(55, 166, 230)",
                "borderWidth": 1,
            }
        ]

        self.chart_config = create_chart_config(
            chart_type="bar",
            title=f"Task Queue - {self.params['taskqueue_select']['text']}: Total available workers",
            labels=labels,
            datasets=datasets,
        )

    def TotalEligibleWorkers(self):
        labels = ["Total eligible workers"]
        data = [self.data["total_eligible_workers"]]

        datasets = [
            {
                "label": "Eligible workers",
                "data": data,
                "backgroundColor": "rgba(55, 166, 230, 0.5)",
                "borderColor": "rgb(55, 166, 230)",
                "borderWidth": 1,
            }
        ]

        self.chart_config = create_chart_config(
            chart_type="bar",
            title=f"Task Queue - {self.params['taskqueue_select']['text']}: Total eligible workers",
            labels=labels,
            datasets=datasets,
        )

    def TotalTasks(self):
        labels = ["Total tasks"]
        data = [self.data["total_tasks"]]

        datasets = [
            {
                "label": "Tasks",
                "data": data,
                "backgroundColor": "rgba(55, 166, 230, 0.5)",
                "borderColor": "rgb(55, 166, 230)",
                "borderWidth": 1,
            }
        ]

        self.chart_config = create_chart_config(
            chart_type="bar",
            title=f"Task Queue - {self.params['taskqueue_select']['text']}: Total tasks",
            labels=labels,
            datasets=datasets,
        )
