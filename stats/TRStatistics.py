from quickchart import QuickChart


class TRStatistics:
    def __init__(self, stat, params, tr_client):
        self.data = None
        self.chart_config = None
        self.stat = stat
        self.params = params
        self.tr_client = tr_client

        self.set_data()

        getattr(self, stat)()

    def set_data(self):
        raise NotImplementedError

    def chart(self):
        chart = QuickChart()
        chart.config = self.chart_config

        return chart.get_url()
