import distutils.dir_util
import os
import pathlib
from csv import DictReader

def copiar_origem_destino(arquivo):
    with open(arquivo) as meucsv:
        reader = DictReader(meucsv)
        print('Iniciando Backup,por favor aguarde.\n\n\n')
        for linha in reader:
            origem = linha['origem']
            destino = linha['destino']
            if os.path.exists(destino):
                nome = pathlib.PurePath(origem).name
                destino = os.path.join(destino,nome)
            #faz a copia da pasta
            distutils.dir_util.copy_tree(origem,destino)
            print('-' * 30)
            print("BACKUP FINALIZADO!")
            print('-'*30)


if __name__ == "__main__":
    arquivo = os.path.join('input', 'diretorios.csv')
    copiar_origem_destino(arquivo)