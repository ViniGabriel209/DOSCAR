def commentgraphics():

    for layer in range(1, 22 + 1):
        
        file = open(f'camada{layer}.py', 'r')
        lines = file.read().split('\n')

        for line in range(len(lines)):
            if 'plt' in lines[line]:
                lines[line] = '# ' + lines[line]
        
        newfile = open(f'camada{layer}.py', 'w')

        for c in range(len(lines)):
            newfile.write(f'{lines[c]} \n')


def descommentgraphics():

    for layer in range(1, 22 + 1):
        
        file = open(f'camada{layer}.py', 'r')
        lines = file.read().split('\n')

        for line in range(len(lines)):
            if '#' in lines[line] and 'plt' in lines[line]:
                lines[line] = lines[line][2:]
        
        newfile = open(f'camada{layer}.py', 'w')

        for c in range(len(lines)):
            newfile.write(f'{lines[c]} \n')


commentgraphics()
# descommentgraphics()