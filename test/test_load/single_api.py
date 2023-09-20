import requests
from locust import HttpUser, task, between


host = "http://127.0.0.1:8000"
payload = {"test": "something"}

class DefineYourClassName(HttpUser):
    wait_time = between(3, 5)
    @task()
    def predict_endpoint(self):
        response = self.client.post(f"{host}/api", json=payload)




