from locust import HttpUser, task, between


host = "http://127.0.0.1:8000"
payload1 = {"test": "something1"}
payload2 = {"test": "something2"}
payload3 = {"test": "something3"}


class TestUser(HttpUser):
    wait_time = between(3, 5)
    @task(4)
    def endpoint1(self):
        response = self.client.post(f"{host}/api", json=payload1)
    @task(1)
    def endpoint2(self):
        response = self.client.post(f"{host}/api2", json=payload2)
    @task(2)
    def endpoint3(self):
        response = self.client.post(f"{host}/api3", json=payload3)
