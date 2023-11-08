import mlflow
import random

# Set the tracking URI to the FastTrackML server
# mlflow.set_tracking_uri("http://localhost:8000")
# Set the experiment name
mlflow.set_experiment("my-first-experiment")

# Start a new run
with mlflow.start_run():
    # Log a parameter
    mlflow.log_param("param1", random.randint(0, 100))

    # Log a metric
    mlflow.log_metric("foo", random.random())
    # metrics can be updated throughout the run
    mlflow.log_metric("foo", random.random() + 1)
    mlflow.log_metric("foo", random.random() + 2)
    

# List all experiments
runs = mlflow.tracking.MlflowClient().search_runs("577243075391975043")



# mlflow_client = mlflow.tracking.MlflowClient()
# fasttrack_client = mlflow.tracking.MlflowClient()

# mlflow_runs = mlflow_client.search_runs("758823355255162064")
# fasttrack_runs = fasttrack_client.search_runs("758823355255162064")

# print("Mlflow runs: ")
# print(mlflow_runs)
# print("FastTrack runs")
# print(fasttrack_runs)
print("num runs: ", runs)
for run in runs:
    print(run.data.to_dictionary())
# Iterate through and print experiment names and IDs
# for experiment in experiments:
#     print(f"Experiment Name: {experiment.name}, Experiment ID: {experiment.experiment_id}")

    
# runs = mlflow.search_runs(experiment_ids="my-first-experiment")
# print(len(runs))
# runs_dict = {}
# for index, row in runs.iterrows():
#     runs_dict[index] = {
#         'run_id' : row['run_id'],
#         'metrics': row['metrics'],
#         'params': row['params'],
#         'start_time' : row['start_time'],
#         'end_time' : row['end_time']
        
#     }
# print("The result is ")
# print(runs_dict)