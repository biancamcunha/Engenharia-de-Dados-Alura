import os
import requests
import base64
from dotenv import load_dotenv

load_dotenv()

class ManipulaRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base_url = "https://api.github.com"
        self.access_token = os.getenv('GITHUB_ACCESS_TOKEN')
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def cria_repo(self, nome_repo):
        data = {
            'name': nome_repo,
            'description': 'Dados dos repositórios de algumas empresas',
            'private': False
        }

        response = requests.post(f"{self.api_base_url}/user/repos", headers=self.headers, json=data)
        print(f'status_code de criação do repositório: {response.status_code}')

    def add_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):
        with open(caminho_arquivo, 'rb') as file:
            file_content= file.read()
        encoded_content = base64.b64encode(file_content)

        data = {
            'message': 'Adicionando um novo arquivo',
            'content': encoded_content.decode('utf-8')
        }

        response = requests.put(f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{nome_arquivo}',
                                headers=self.headers, json=data)
        print(f'satus_code do upload do arquivo: {response.status_code}')

novo_repo = ManipulaRepositorios('biancamcunha')

nome_repo = 'linguagens-repositorios-empresas'
novo_repo.cria_repo(nome_repo)

novo_repo.add_arquivo(nome_repo, 'linguagens_amzn.csv', 'dados/linguagens_amzn.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_netflix.csv', 'dados/linguagens_netflix.csv')
novo_repo.add_arquivo(nome_repo, 'linguagens_spotify.csv', 'dados/linguagens_spotify.csv')
