import os
import time

# create timer which calls functions a certain number of times
def timing(iter_count=100):
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