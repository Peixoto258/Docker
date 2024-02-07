from locust import HttpUser, task, between

class GoogleUser(HttpUser):
    # Define o tempo de espera entre as tarefas de cada usuário simulado
    wait_time = between(1, 5)

    @task
    def load_google_homepage(self):
        # Realiza uma requisição GET para a página inicial do Google
        self.client.get("/")