from locust import User, wait_time, task, between
import time
import random

def add(a, b):
    time.sleep(random.randint(0, 3))
    return a + b

class TestSample(User):
    wait_time = between(1, 5)
    
    def on_start(self):
        print("starting the tests now...")
    
    @task
    def sample_test(self):
        for i in range(10):
            add(i, i+1)