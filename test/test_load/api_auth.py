"""
https://stackoverflow.com/questions/52007848/locust-passing-headers
# You can also use on_start method so all subsequent clients will use the same authorization

class User(HttpUser):

    def on_start(self):
        self.client.headers = {'Authorization': 'my-auth-token'}

    @task
    def my_authenticated_task(self):
        self.client.post('enspoint')
"""

import os

from locust import HttpUser, task, between


host = "http://127.0.0.1:8000"
payload = {"test": "something"}
apikey = os.environ['API_KEY']

class DefineYourClassName(HttpUser):
    wait_time = between(3, 5)
    @task()
    def predict_endpoint(self):
        response = self.client.post(f"{host}/api", 
                                    headers={"x-api-key": apikey}, 
                                    json=payload)




