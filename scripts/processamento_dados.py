import json
import csv

class Dados:

    def __init__(self, dados):
        self.dados = dados
        self.nomes_colunas = self.__get_columns()
        self.qtd_linhas = self.__size_data()

    @staticmethod
    def __leitura_json(path):
        with open(path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    @staticmethod
    def __leitura_csv(path):
        dados_csv = []
        with open(path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    @classmethod
    def leitura_dados(cls, path, tipo_dados):
        dados = []
        if tipo_dados == 'csv':
            dados = cls.__leitura_csv(path)
        elif tipo_dados == 'json':
            dados = cls.__leitura_json(path)
        return cls(dados)
    
    def __get_columns(self):
        return list(self.dados[-1].keys())

    def rename_columns(self, key_mapping):
        self.dados = [{key_mapping[old_key]: value for old_key, value in old_dict.items()} for old_dict in self.dados]
        self.nomes_colunas = self.__get_columns()

    def __size_data(self):
        return len(self.dados)

    @staticmethod
    def join(dadosA, dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        return Dados(combined_list)
    
    def __transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nomes_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nomes_colunas:
                linha.append(row.get(coluna, 'Indisponível'))
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela
    
    def salvando_dados(self, path):
        dados_combinados_tabela = self.__transformando_dados_tabela()
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)



    