from .TRStatistics import TRStatistics
from .utils import create_chart_config


class WorkflowStatistics(TRStatistics):
    def set_data(self):
        self.data = self.tr_client.get_workflow_statistics(
            self.params["workflow_select"]["value"]
        )[0]["result"]

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
            title=f"Workflow - {self.params['workflow_select']['text']}: Tasks by status",
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
            title=f"Workflow - {self.params['workflow_select']['text']}: Total tasks",
            labels=labels,
            datasets=datasets,
        )
