import os

arquivoTXTAserCondensado = ""

# Abra o arquivo para leitura
for value in os.listdir(os.getcwd()):
    if value != "main.py" and value != 'StringCondensada.txt':
        arquivoTXTAserCondensado = value

with open(arquivoTXTAserCondensado, 'r', encoding='utf-8') as arquivo:
    # Leia todas as linhas do arquivo
    linhas = arquivo.readlines()

# Remova linhas vazias
linhas = [linha.strip() for linha in linhas if linha.strip()]

# Junte todas as linhas em uma única linha
texto_condensado = ' '.join(linhas)

# Escreva o texto condensado em um novo arquivo ou imprima na tela
print(texto_condensado)

with open('StringCondensada.txt', 'w', encoding='utf-8') as arquivo2:
    arquivo2.write(texto_condensado)