from locust import HttpUser, task, between


host = "http://127.0.0.1:8000"
payload = {"test": "something"}


# HttpUser: It adds a client attribute which is used to make HTTP requests
class DefineYourClassName(HttpUser):
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(3, 5)
    @task()
    def predict_endpoint(self):
        response = self.client.post(f"{host}/api", json=payload)




