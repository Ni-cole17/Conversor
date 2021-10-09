import os
from pathlib import Path


diretorio_atual = os.path.dirname(os.path.realpath(__file__))
os.chdir(diretorio_atual)
print(diretorio_atual)
atributo = input('Digite o tipo de conversão: (.wav,.mp3,.mp4,.txt,...)\n')
lista_pastas = []

for i in os.listdir():
    fileobj = Path(i)
    if fileobj.is_file() is False:
        lista_pastas.append(i)


for j in lista_pastas:
    print(j)
    diretorio_da_pasta = diretorio_atual + '\\' + j
    print("diretorio",diretorio_da_pasta)
    os.chdir(diretorio_da_pasta)
    print(os.listdir())
    for k in os.listdir():
        p = Path(k)
        p.rename(p.with_suffix(atributo))

print(os.listdir())

