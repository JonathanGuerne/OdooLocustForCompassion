from locust import task, between, HttpUser


class HTTP(HttpUser):
    wait_time = between(5, 10)

    @task(5)
    def muskathlon(self):
        self.client.get(f"http://{self.host}/event/muskathlon-kilimanjaro-june-2022-2673/") 
    
    @task(10)
    def together_homepage(self):
        self.client.get(f"http://together.{self.host}/homepage")