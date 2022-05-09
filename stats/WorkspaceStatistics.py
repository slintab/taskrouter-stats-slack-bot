from .TRStatistics import TRStatistics
from .utils import create_chart_config


class WorkspaceStatistics(TRStatistics):
    def set_data(self):
        self.data = self.tr_client.get_workspace_statistics()[0]["result"]

    def TasksByStatus(self):
        labels = []
        data = []

        for k, v in self.data["realtime"]["tasks_by_status"].items():
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
            title="Workspace: Tasks by status",
            labels=labels,
            datasets=datasets,
        )

    def ActivityStatistics(self):
        labels = []
        data = []

        for i in self.data["realtime"]["activity_statistics"]:
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
            title="Workspace: Activity statistics",
            labels=labels,
            datasets=datasets,
        )

    def TotalWorkers(self):
        labels = ["Total workers"]
        data = [self.data["realtime"]["total_workers"]]

        datasets = [
            {
                "label": "Workers",
                "data": data,
                "backgroundColor": "rgba(55, 166, 230, 0.5)",
                "borderColor": "rgb(55, 166, 230)",
                "borderWidth": 1,
            }
        ]

        self.chart_config = create_chart_config(
            chart_type="bar",
            title="Workspace: Total workers",
            labels=labels,
            datasets=datasets,
        )

    def TotalTasks(self):
        labels = ["Total tasks"]
        data = [self.data["realtime"]["total_tasks"]]

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
            title="Workspace: Total tasks",
            labels=labels,
            datasets=datasets,
        )
