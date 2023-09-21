"""You can specify the user class if you don't want to execute all at once, e.g.,

locust -f test/test_load/custom_spawn_rate.py HeavyUser
"""

from locust import HttpUser, task, between


host = "http://127.0.0.1:8000"
payload1 = {"test": "something1"}
payload2 = {"test": "something2"}
payload3 = {"test": "something3"}


class HeavyUser(HttpUser):
    wait_time = between(3, 5)
    @task()
    def predict_endpoint1(self):
        response = self.client.post(f"{host}/api2", json=payload1)
        response = self.client.post(f"{host}/api", json=payload1)
        

class LightUser(HttpUser):
    wait_time = between(3, 5)
    @task()
    def predict_endpoint1(self):
        response = self.client.post(f"{host}/api3", json=payload1)
