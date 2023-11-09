from aim import Repo

from performance.base import StorageTestBase
from performance.utils import get_baseline, write_baseline
from performance.storage.utils import iterative_access_metric_values_aim, \
                                      iterative_access_metric_values_mlflow, \
                                      iterative_access_metric_values_fasttrack
                                    


class TestIterativeAccessExecutionTime(StorageTestBase):
    def test_iterative_access(self):
        test_name = 'test_iterative_access'
        repo = Repo.default_repo()
        query = 'metric.name == "metric 0"'
        aim_execution_time = iterative_access_metric_values_aim(repo, query)
        mlflow_execution_time = iterative_access_metric_values_mlflow(query)
        fasttrack_execution_time = iterative_access_metric_values_fasttrack(query)
        baseline = get_baseline(test_name)
        if baseline:
            self.assertInRange(aim_execution_time, baseline)
        else:
            write_baseline(test_name, aim_execution_time)