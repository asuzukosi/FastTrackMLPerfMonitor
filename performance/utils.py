import os
import time
import mlflow
import pandas as pd
import datetime

# set the data output file
DATA_OUTPUT_FILE = 'performance_data.csv'
# create timer which calls functions a certain number of times
def timing(iter_count=10):
    def inner(f):
        def wrapper(*args, **kwargs):
            ts = time.time()
            for _ in range(iter_count):
                f(*args, **kwargs)
            te = time.time()
            return (te-ts)/iter_count
        return wrapper
    return inner

# get the baseline from parent directory or read it from the environment variable
def get_baseline_filename():
    import performance
    performance_tests_path = os.path.dirname(performance.__file__)
    baseline_filename = os.path.join(performance_tests_path, 'BASELINE')
    if os.environ.get('PERFORMANCE_TESTS_BASELINE'):
        # for local performance testing
        baseline_filename = os.environ['PERFORMANCE_TESTS_BASELINE']

    return baseline_filename

# get currrent baseline based on test name
def get_baseline(test_name):
    filename = get_baseline_filename()
    if not os.path.exists(filename):
        return None
    # read baseline file line by line
    with open(filename, 'r') as f:
        for line in f:
            if test_name in line:
                return float(line.split()[1])

    return None

# write new baseline to baseline file
def write_baseline(test_name, exec_time):
    filename = get_baseline_filename()

    with open(filename, 'a+') as f:
        f.write(f'{test_name} {exec_time}\n')
        
# setup mlflow client
MLFLOW_CLIENT = mlflow.tracking.MlflowClient()

def get_mlflow_experiment():
    return os.environ.get('MLFLOW_EXPERIMENT_ID', '')

# setup fastrackml client
FASTTRACK_CLIENT = mlflow.tracking.MlflowClient(tracking_uri="http://fasttrackml:5000")
def get_fasttrack_experiment():
    return os.environ.get('FASTTRACK_EXPERIMENT_ID', '')


def write_data_points_to_csv(data_points):
    df = pd.DataFrame(data_points)
    df.to_csv(DATA_OUTPUT_FILE, mode='a', index=None, header=not os.path.exists(DATA_OUTPUT_FILE))
    
    
def add_tests_results(test_name, aim, mlflow, fasttrack):
    current_time = datetime.datetime.now()
    data_points = [
            {
                "test_name": test_name,
                "application": "aim",
                "value": aim,
                "timestamp": current_time
            },
            {
                "test_name": test_name,
                "application": "mlflow",
                "value": mlflow,
                "timestamp": current_time
            },
            {
                "test_name": test_name,
                "application": "fasttrack",
                "value": fasttrack,
                "timestamp": current_time
            },
            {
                "test_name": test_name,
                "application": "average",
                "value": sum([fasttrack, mlflow, aim])/3,
                "timestamp": current_time
            }
            
        ]
    
    write_data_points_to_csv(data_points)
        