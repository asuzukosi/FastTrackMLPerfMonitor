from aim.sdk import Repo
from aim.sdk.types import QueryReportMode
from aim.web.api.runs.utils import get_run_props
from performance.utils import timing, MLFLOW_EXPERIMENT_ID
import mlflow

# @timing()
# def collect_runs_data(query):
#     repo = Repo.default_repo()
#     runs = repo.query_runs(query, report_mode=QueryReportMode.DISABLED)
#     runs_dict = {}
#     for run_trace_collection in runs.iter_runs():
#         run = run_trace_collection.run
#         runs_dict[run.hash] = {
#             'params': run[...],
#             'traces': run.collect_sequence_info(sequence_types='metric'),
#             'props': get_run_props(run)
#         }


@timing()
def collect_runs_data(query):
    runs = mlflow.search_runs(experiment_ids=MLFLOW_EXPERIMENT_ID, filter_string=query)
    runs_dict = {}
    for index, row in runs.iterrows():
        runs_dict[index] = {
            'run_id' : row['run_id'],
            'metrics': row['metrics'],
            'params': row['params'],
            'start_time' : row['start_time'],
            'end_time' : row['end_time']
            
        }
    
@timing()
def collect_metrics_data(query):
    repo = Repo.default_repo()
    runs_dict = {}
    runs = repo.query_metrics(query=query, report_mode=QueryReportMode.DISABLED)
    for run_trace_collection in runs.iter_runs():
        run = None
        traces_list = []
        for trace in run_trace_collection.iter():
            if not run:
                run = run_trace_collection.run
            iters, values = trace.values.sparse_numpy()
            traces_list.append({
                'name': trace.name,
                'context': trace.context.to_dict(),
                'values': values,
                'iters': iters,
                'epochs': trace.epochs.values_numpy(),
                'timestamps': trace.timestamps.values_numpy()
            })
        if run:
            runs_dict[run.hash] = {
                'traces': traces_list,
                'params': run[...],
                'props': get_run_props(run),
            }


@timing()
def query_runs(query):
    repo = Repo.default_repo()
    runs = list(repo.query_runs(query=query, report_mode=QueryReportMode.DISABLED).iter_runs())


@timing()
def query_metrics(query):
    repo = Repo.default_repo()
    metrics = list(repo.query_metrics(query=query, report_mode=QueryReportMode.DISABLED).iter())