import os
import shutil
import tarfile
import time
from pathlib import Path

from aim.sdk.configs import AIM_REPO_NAME
from performance.utils import get_baseline_filename

TEST_REPO_PATHS = {
    'real_life_repo': '.aim_performance_repo_1',
    'generated_repo': '.aim_performance_repo_2'
}
# AIM_PERFORMANCE_BUCKET_NAME = 'aim-demo-logs'
# AIM_PERFORMANCE_LOG_FILE_NAME = 'performance-logs.tar.gz'


def _init_test_repos():
    pass


def _cleanup_test_repo(path):
    shutil.rmtree(path)


def pytest_sessionstart(session):
    pass
    # if os.environ.get('AIM_LOCAL_PERFORMANCE_TEST'):
    #     _init_test_repos()
    # else:
    #     # github actions performance tests on self hosted runner
    #     os.chdir('/home/ubuntu/performance_logs/')
    # time.sleep(10)

def print_current_baseline():
    print('==== CURRENT BASELINE ====')
    with open(get_baseline_filename(), 'r') as f:
        print(f.read())
    print('==========================')

def pytest_unconfigure(config):
    print_current_baseline()

def pytest_sessionfinish(session, exitstatus):
    if os.environ.get('AIM_LOCAL_PERFORMANCE_TEST'):
        for path in TEST_REPO_PATHS.values():
            _cleanup_test_repo(path)
    if os.environ.get(AIM_REPO_NAME):
        del os.environ[AIM_REPO_NAME]