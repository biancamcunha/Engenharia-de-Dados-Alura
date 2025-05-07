import os
import requests
import pandas as pd

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = "https://api.github.com"
        self.access_token = os.getenv('GITHUB_ACCESS_TOKEN')
        self.headers = {'Authorization': 'Bearer ' + self.access_token,
                        'X-GitHub-Api-Version': '2022-11-28'}
        
    def lista_repositorios(self):
        repos_list = []

        for page_num in range(1, 20):
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