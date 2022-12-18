from topologia import Topologia
import json

with open('rede_teste.json', 'r', encoding='utf-8') as arquivo_dados:
    dados = json.load(arquivo_dados)
rede1 = Topologia('rede 1', dados)

rede1.descrever_rede()
