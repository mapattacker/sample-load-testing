from locust import HttpUser, task, between


host = "http://127.0.0.1:8000"
payload1 = {"test": "something1"}
payload2 = {"test": "something2"}
payload3 = {"test": "something3"}


class HeavyUser(HttpUser):
    wait_time = between(3, 5)
    @task()
    def predict_endpoint1(self):
        response = self.client.post(f"{host}/api", json=payload1)
        response = self.client.post(f"{host}/api", json=payload2)
        response = self.client.post(f"{host}/api", json=payload3)
