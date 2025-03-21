import os

def listar_arquivos_e_pastas(diretorio='.'):
    arquivos = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
    pastas = [f for f in os.listdir(diretorio) if os.path.isdir(os.path.join(diretorio, f))]
    
    with open('lista_arquivos.txt', 'w', encoding='utf-8') as file:
        for pasta in pastas:
            file.write(pasta + '/\n')  # Indica que é uma pasta
        for arquivo in arquivos:
            file.write(arquivo + '\n')
    
    print("Lista de arquivos e pastas salva em 'lista_arquivos.txt'")

if __name__ == "__main__":
    listar_arquivos_e_pastas()
