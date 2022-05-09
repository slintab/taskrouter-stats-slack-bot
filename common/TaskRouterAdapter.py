import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class TaskRouterAdapter:
    def __init__(self, account_sid, auth_token, workspace_id=None):
        self.base_url = "https://taskrouter.twilio.com"
        self.session = requests.Session()
        self.default_workspace = workspace_id

        # add default headers
        self.add_header({"Content-Type": "application/json"})
        self.add_header({"Accept": "application/json"})

        self.add_auth(username=account_sid, password=auth_token)

    def add_header(self, header: dict):
        self.session.headers.update(header)

    def add_auth(self, username, password):
        self.session.auth = (username, password)

    def set_retries(self):
        retries = Retry(
            total=2, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def request(self, method: str, path: str, params={}, payload={}, timeout=3) -> list:
        results = []

        while True:
            resp = self.raw_request(
                method=method, path=path, params=params, json=payload, timeout=timeout
            )

            # if there is any error, terminate and return
            if "error" in resp:
                return [resp]

            # if results are not paginated, return the result
            if "meta" not in resp["result"]:
                return [resp]

            results.append(resp["result"])

            # if there is no next page, exit the loop
            if not resp["result"]["meta"]["next_page_url"]:
                break

            # update params with next page number
            params.update({"Page": resp["result"]["meta"]["page"] + 1})

        return results

    def raw_request(self, method, path, *args, **kwargs):
        results, resp = {}, None
        method = method.lower()

        if method != "get":
            raise NotImplementedError(
                f"Request type {method} is currently not supported!"
            )

        url = self.base_url + path

        try:
            resp = getattr(self.session, method)(url=url, *args, **kwargs)
        except Exception as e:
            print(e)

        if resp and resp.status_code == 200:
            results.update({"result": resp.json()})
        else:
            results.update({"error": True})

        return results

    def get_all_workspaces(self):
        path = "/v1/Workspaces"

        return self.request(method="GET", path=path)

    def get_all_workflows(self, workspace_id=None):
        if not workspace_id:
            workspace_id = self.default_workspace

        path = f"/v1/Workspaces/{workspace_id}/Workflows"

        return self.request(method="GET", path=path)

    def get_all_taskqueues(self, workspace_id=None):
        if not workspace_id:
            workspace_id = self.default_workspace

        path = f"/v1/Workspaces/{workspace_id}/TaskQueues"

        return self.request(method="GET", path=path)

    def get_workspace_statistics(self, workspace_id=None):
        if not workspace_id:
            workspace_id = self.default_workspace

        path = f"/v1/Workspaces/{workspace_id}/Statistics"

        return self.request(method="GET", path=path)

    def get_workflow_statistics(self, workflow_id, workspace_id=None):
        if not workspace_id:
            workspace_id = self.default_workspace

        path = f"/v1/Workspaces/{workspace_id}/Workflows/{workflow_id}/Statistics"

        return self.request(method="GET", path=path)

    def get_taskqueue_statistics(self, taskqueue_id, workspace_id=None):
        if not workspace_id:
            workspace_id = self.default_workspace

        path = f"/v1/Workspaces/{workspace_id}/TaskQueues/{taskqueue_id}/RealTimeStatistics"

        return self.request(method="GET", path=path)
