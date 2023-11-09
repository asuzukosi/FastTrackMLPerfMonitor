from parameterized import parameterized

from aim import Repo

from performance.base import StorageTestBase
from performance.utils import get_baseline, write_baseline
from performance.storage.utils import random_access_metric_values_aim, \
                                      random_access_metric_values_mlflow, \
                                      random_access_metric_value_fasttrack


class TestRandomAccess(StorageTestBase):
    @parameterized.expand({0: 50, 1: 250, 2: 500}.items())
    def test_random_access(self, test_key, density):
        test_name = f'test_random_access_{test_key}'
        repo = Repo.default_repo()
        query = 'metric.name == "metric 0"'
        aim_execution_time = random_access_metric_values_aim(repo, query, density)
        mlflow_execution_time = random_access_metric_values_mlflow(query)
        fasttrack_exection_time = random_access_metric_value_fasttrack(query)
        baseline = get_baseline(test_name)
        if baseline:
            self.assertInRange(aim_execution_time, baseline)
        else:
            write_baseline(test_name, aim_execution_time)