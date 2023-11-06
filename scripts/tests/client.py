import time
from locust import HttpUser, User, wait_time, task, between

# TODO: add tags to the tests
    
class PerfTestMLFlowClient(User):
    wait_time = between(1, 5)
    
    def on_start(self):
        # set up mlflow client
        return super().on_start()
    @task
    def test_create_experiments(self):
        pass
    
    @task
    def test_get_experiments(self):
        pass
    
    @task
    def test_search_experiments(self):
        pass
    
    @task
    def test_delete_restore_experiments(self):
        pass
    
    @task
    def test_rename_experiments(self):
        pass
    
    @task
    def test_create_run(self):
        pass
    
    @task
    def test_create_run_with_default(self):
        pass
    
    @task
    def test_log_metrics_param_tags(self):
        pass
    
    @task
    def test_log_metric_validation(self):
        pass
    
    @task
    def test_log_param_validation(self):
        pass
    
    @task
    def test_log_param_with_empty_string_as_value(self):
        pass
    
    @task
    def test_set_tag_with_empty_string_as_value(self):
        pass
    
    @task
    def test_set_experiment_tag(self):
        pass
    
    @task
    def test_delete_tag(self):
        pass
    
    @task
    def test_log_batch(self):
        pass
    
    @task
    def test_log_batch_validation(self):
        pass
    
    @task
    def test_artifiacts(self):
        pass
    
    @task
    def test_get_experiments_by_name(self):
        pass
    
    @task
    def test_search_experiments(self):
        pass
    
    @task
    def test_get_metric_history(self):
        pass
    
    @task
    def test_search_dataset(self):
        pass
    
    @task
    def test_create_model(self):
        pass
    
    @task
    def test_log_inputs(self):
        pass
    
    @task
    def test_update_run_name(self):
        pass
    
    @task
    def test_upload_artifact(self):
        pass


class PerfTestFastTrackMLClient(User):
    wait_time = between(1, 5)
    def on_start(self):
        # set up fasttrack ml client
        return
    
    @task
    def test_create_experiments(self):
        pass
    
    @task
    def test_get_experiments(self):
        pass
    
    @task
    def test_search_experiments(self):
        pass
    
    @task
    def test_delete_restore_experiments(self):
        pass
    
    @task
    def test_rename_experiments(self):
        pass
    
    @task
    def test_create_run(self):
        pass
    
    @task
    def test_create_run_with_default(self):
        pass
    
    @task
    def test_log_metrics_param_tags(self):
        pass
    
    @task
    def test_log_metric_validation(self):
        pass
    
    @task
    def test_log_param_validation(self):
        pass
    
    @task
    def test_log_param_with_empty_string_as_value(self):
        pass
    
    @task
    def test_set_tag_with_empty_string_as_value(self):
        pass
    
    @task
    def test_set_experiment_tag(self):
        pass
    
    @task
    def test_delete_tag(self):
        pass
    
    @task
    def test_log_batch(self):
        pass
    
    @task
    def test_log_batch_validation(self):
        pass
    
    @task
    def test_artifiacts(self):
        pass
    
    @task
    def test_get_experiments_by_name(self):
        pass
    
    @task
    def test_search_experiments(self):
        pass
    
    @task
    def test_get_metric_history(self):
        pass
    
    @task
    def test_search_dataset(self):
        pass
    
    @task
    def test_create_model(self):
        pass
    
    @task
    def test_log_inputs(self):
        pass
    
    @task
    def test_update_run_name(self):
        pass
    
    @task
    def test_upload_artifact(self):
        pass
    


class PerfTestAimClient(User):
    wait_time = between(1, 5)
    def on_start(self):
        # set up aim client
        return
    
    @task
    def test_create_experiments(self):
        pass
    
    @task
    def test_get_experiments(self):
        pass
    
    @task
    def test_search_experiments(self):
        pass
    
    @task
    def test_delete_restore_experiments(self):
        pass
    
    @task
    def test_rename_experiments(self):
        pass
    
    @task
    def test_create_run(self):
        pass
    
    @task
    def test_create_run_with_default(self):
        pass
    
    @task
    def test_log_metrics_param_tags(self):
        pass
    
    @task
    def test_log_metric_validation(self):
        pass
    
    @task
    def test_log_param_validation(self):
        pass
    
    @task
    def test_log_param_with_empty_string_as_value(self):
        pass
    
    @task
    def test_set_tag_with_empty_string_as_value(self):
        pass
    
    @task
    def test_set_experiment_tag(self):
        pass
    
    @task
    def test_delete_tag(self):
        pass
    
    @task
    def test_log_batch(self):
        pass
    
    @task
    def test_log_batch_validation(self):
        pass
    
    @task
    def test_artifiacts(self):
        pass
    
    @task
    def test_get_experiments_by_name(self):
        pass
    
    @task
    def test_search_experiments(self):
        pass
    
    @task
    def test_get_metric_history(self):
        pass
    
    @task
    def test_search_dataset(self):
        pass
    
    @task
    def test_create_model(self):
        pass
    
    @task
    def test_log_inputs(self):
        pass
    
    @task
    def test_update_run_name(self):
        pass
    
    @task
    def test_upload_artifact(self):
        pass