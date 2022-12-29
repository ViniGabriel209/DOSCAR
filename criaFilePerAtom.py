n = int(input('Escolha a quantidade de átomos: '))

for a in range(1, n + 1):

    doscar = open('DOSCAR')
    linhas = doscar.read().split('\n')

    dados = []

    i = 3007 + 3000 * (a - 1) + a - 1
    f = 6007 + 3000 * (a - 1) + a - 1

    for c in range(i, f):
        try:
            dados.append(linhas[c])
        except:
            break

    if a > len(dados):
        break

    arquivo = open(f'PDOS{a}', 'w')         # Cria arquivo e apaga o conteúdo caso já exista

    for c in range(len(dados)):
        arquivo.write(f'{dados[c]} \n')

    
