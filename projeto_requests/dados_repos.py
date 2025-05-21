from math import ceil
import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = "https://api.github.com"
        self.access_token = os.getenv('GITHUB_ACCESS_TOKEN')
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def __busca_num_pags(self):
        url = f"https://api.github.com/users/{self.owner}"
        response = requests.get(url, headers=self.headers).json()
        n_pags = ceil(response['public_repos'] / 30)
        return n_pags 
        
    def lista_repositorios(self):
        repos_list = []

        n_pags = self.__busca_num_pags()

        for page_num in range(1, n_pags + 1):
            try:
                url = f"{self.api_base_url}/users/{self.owner}/repos?per_page=100&page={page_num}"
                response = requests.get(url, headers=self.headers)
                repos_list.extend(response.json())
            except:
                repos_list.append(None)
        return repos_list
    
    def nomes_repos(self, repos_list):
        repos_names = []

        for repo in repos_list:
            try:
                repos_names.append(repo['name'])
            except:
                pass
        return repos_names
    
    def nomes_linguagens(self, repos_list):
        repos_languages = []

        for repo in repos_list:
            try:
                repos_languages.append(repo['language'])
            except:
                pass
        return repos_languages
    
    def cria_df_linguagens(self):
        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        dados = pd.DataFrame()
        dados['repository_name'] = nomes
        dados['language'] = linguagens

        return dados
