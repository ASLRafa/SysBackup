from tkinter import filedialog, messagebox
import os
from copiar import copiar_origem_destino

def deve_continuar():
    return messagebox.askyesno(title='Gerenciamento BACKUP', \
                               message='Gostaria de selecionar a origem e destino')


def gerar_arquivo_csv(nomearquivo, modo ='w'):
    with open(nomearquivo, modo) as dircsv:
        if modo == 'w':
            # cabeçalho do CSV
            dircsv.write('origem,destino\n')
        while deve_continuar():
            origem = filedialog.askdirectory()
            #origem = origem.replace("/", "\\")
            destino = filedialog.askdirectory()
            #destino = destino.replace("/", "\\")
            dircsv.write(f'{origem},{destino}\n')


if __name__ == "__main__":
    arquivo = os.path.join('input', 'diretorios.csv')
    gerar_arquivo_csv(arquivo)
    copiar_origem_destino(arquivo)
