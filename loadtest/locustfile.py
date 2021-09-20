from locust import HttpUser, task, between


class BasicUser(HttpUser):
    wait_time = between(3, 5)

    @task
    def index(self):
        self.client.get("/")
    
    @task
    def locations(self):
        self.client.get("/destinations")
    
    @task
    def location_1(self):
        self.client.get("/destination/1")