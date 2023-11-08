from aim import Repo
from aim.sdk.configs import get_aim_repo_name
from aim.sdk.types import QueryReportMode

from performance.utils import timing, MLFLOW_CLIENT, FASTTRACK_CLIENT


# @timing()
# def random_access_metric_values(repo: Repo, query, density):
#     traces = repo.query_metrics(query=query, report_mode=QueryReportMode.DISABLED)
#     for trace in traces.iter():
#         values = trace.values
#         values_length = len(values)
#         step = len(values)//density

#         accessed_values = []
#         for i in range(0, values_length, step):
#             accessed_values.append(trace.values[i])


# @timing()
# def iterative_access_metric_values(repo:Repo, query):
#     traces = repo.query_metrics(query=query, report_mode=QueryReportMode.DISABLED)
#     for trace in traces.iter():
#         _ = trace.values.values_numpy()


# def collect_sequence_containers():
#     repo = Repo.default_repo()
#     return [run.hash for run in repo.iter_runs()]