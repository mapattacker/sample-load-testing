""""
https://docs.locust.io/en/stable/custom-load-shape.html
https://stackoverflow.com/questions/62872079/locust-load-testing-change-hatch-rate-from-seconds-to-minutes
https://github.com/locustio/locust/blob/master/examples/custom_shape/step_load.py

# command must exclude user, spawn rate, run time
locust -f test/test_load/custom_spawn_rate.py \
                  --headless \
                  --host $HOST \
                  --html report.html \
                  --json
"""

from locust import HttpUser, task, between, LoadTestShape


host = "http://127.0.0.1:8000"
payload = {"test": "something"}


class DefineYourClassName(HttpUser):
    wait_time = between(3, 5)
    @task()
    def predict_endpoint(self):
        response = self.client.post(f"{host}/api", json=payload)



class SharpStepShape(LoadTestShape):
    increase_delay = 10  # 20s per increase in user
    increase_size = 2  # number of extra users per increase
    time_limit = 60 * 2 # runtime
    max_users = 20 # total user limit

    def tick(self):
        run_time = self.get_run_time()

        if run_time > self.time_limit:
            return None

        step_number = int(run_time / self.increase_delay) + 1
        user_limit = min(step_number * self.increase_size, self.max_users)
        
        # no max user limits
        # user_limit = int(step_number * self.increase_size)
        return user_limit, self.increase_size
