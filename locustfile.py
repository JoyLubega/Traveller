from locust import HttpLocust, TaskSet, task


class UserActions(TaskSet):


    def on_start(self):
        self.login()


    def login(self)
  
        response = self.client.get('/api/login/')
        
        self.client.post('/api/login/',
                         {'username': 'username', 'password': 'password'})


    @task(1)
    def index(self):
        self.client.get('/')


    for i in range(4):
        @task(2)
        def first_page(self):
            self.client.get('/flights/')




    class ApplicationUser(HttpLocust):
        task_set = UserActions
        min_wait = 0
        max_wait = 0