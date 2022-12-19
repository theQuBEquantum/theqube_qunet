import json
import os.path

i = 0
arquivo = 'dados.json'
while os.path.exists(arquivo):
    i += 1
    arquivo = 'dados' + str(i) + '.json'


def exportar_arquivo(dicionario):
    with open(arquivo, 'w', encoding='utf-8') as json_file:
        json.dump(dicionario, json_file, ensure_ascii=False)
