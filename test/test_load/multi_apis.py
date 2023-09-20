import requests
from locust import HttpUser, task, between


host = "http://127.0.0.1:8000"
payload1 = {"test": "something1"}
payload2 = {"test": "something2"}
payload3 = {"test": "something3"}


# HttpUser: It adds a client attribute which is used to make HTTP requests
class HeavyUser(HttpUser):
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(3, 5)
    @task(3)
    def predict_endpoint1(self):
        response = self.client.post(f"{host}/api2", json=payload1)
        response = self.client.post(f"{host}/api", json=payload1)
    # @task(1)
    # def predict_endpoint1(self):
        

class LightUser(HttpUser):
    wait_time = between(3, 5)
    @task(3)
    def predict_endpoint1(self):
        response = self.client.post(f"{host}/api2", json=payload1)
