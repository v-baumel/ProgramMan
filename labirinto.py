#layout do labirinto para o jogo

def criar_labirinto():
    """
    Tamanho: 31 linhas x 28 colunas (tamanho original do arcade)
     Legenda:
    # = Parede
    . = Caminho com pellet normal
    O = Power-up (pellet maior)
    X = Espaço vazio (sem pellet - área dos fantasmas)
    T = Túnel (teleporte entre bordas)
    P = Posição inicial do Pac-Man
    S = Saída (objetivo final - substituindo um pellet)
    """
    labirinto = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', 'P', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', 'O', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', 'O', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', 'X', 'X', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['T', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', 'X', 'X', 'X', 'X', 'X', 'X', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#'],
        ['#', 'O', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', 'S', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', 'O', '#'],
        ['#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#'],
        ['#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
        ['#', 'P', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
    
    return labirinto


def exibir_labirinto(labirinto):
    largura_labirinto = len(labirinto[0])
    espacos = (80 - largura_labirinto) // 2
    margem = ' ' * espacos
    
    for linha in labirinto:
        linha_str = ''
        for elemento in linha:
            linha_str += elemento
        print(margem + linha_str)


def exibir_labirinto_espacado(labirinto):
    #calcula o espaçamento para centralizar
    largura_labirinto = len(labirinto[0]) * 2  # *2 porque tem espaço entre caracteres
    espacos = (80 - largura_labirinto) // 2
    margem = ' ' * espacos
    
    for linha in labirinto:
        linha_str = ''
        for elemento in linha:
            linha_str += elemento + ' '
        print(margem + linha_str)


def contar_pellets(labirinto):
    total = 0
    for linha in labirinto:
        for elemento in linha:
            if elemento == '.':
                total += 1
    return total


def contar_powerups(labirinto):
    total = 0
    for linha in labirinto:
        for elemento in linha:
            if elemento == 'O':
                total += 1
    return total


def obter_posicoes_powerups(labirinto):
    posicoes = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 'O':
                posicoes.append([i, j])
    return posicoes


def obter_posicoes_tuneis(labirinto):
    posicoes = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 'T':
                posicoes.append([i, j])
    return posicoes


def obter_posicao_inicial(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 'P':
                return [i, j]
    return None


def obter_posicao_saida(labirinto):
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 'S':
                return [i, j]
    return None


def eh_parede(labirinto, linha, coluna):
    if linha < 0 or linha >= len(labirinto) or coluna < 0 or coluna >= len(labirinto[0]):
        return True
    return labirinto[linha][coluna] == '#'


def eh_tunel(labirinto, linha, coluna):
    if linha < 0 or linha >= len(labirinto) or coluna < 0 or coluna >= len(labirinto[0]):
        return False
    return labirinto[linha][coluna] == 'T'


def eh_caminho_valido(labirinto, linha, coluna):
    if linha < 0 or linha >= len(labirinto) or coluna < 0 or coluna >= len(labirinto[0]):
        return False
    return labirinto[linha][coluna] != '#'


def obter_espacos_vazios(labirinto):
    posicoes = []
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            if labirinto[i][j] == 'X':
                posicoes.append([i, j])
    return posicoes


def verificar_integridade_labirinto(labirinto):
    colunas_esperadas = 28
    linhas_corretas = 0
    linhas_erradas = []
    
    for i in range(len(labirinto)):
        if len(labirinto[i]) == colunas_esperadas:
            linhas_corretas += 1
        else:
            linhas_erradas.append([i, len(labirinto[i])])
    
    print(f'Total de linhas: {len(labirinto)}')
    print(f'Linhas corretas ({colunas_esperadas} colunas): {linhas_corretas}')
    if linhas_erradas:
        print(f'Linhas com problema: {linhas_erradas}')
    else:
        print('Todas as linhas estão corretas!')
    
    return len(linhas_erradas) == 0


#exemplo de uso 
if __name__ == '__main__':
    print('=== LABIRINTO PROGRAMMAN ===')
    print()
    
    lab = criar_labirinto()
    
    print('Verificando integridade do labirinto:')
    verificar_integridade_labirinto(lab)
    
    print()
    print('Visualização normal (sem espaços):')
    exibir_labirinto(lab)
    
    print()
    print('='*56)
    print()
    print('Visualização com espaçamento (melhor para ver):')
    exibir_labirinto_espacado(lab)
    
    print()
    print(f'Total de pellets normais: {contar_pellets(lab)}')
    print(f'Total de power-ups: {contar_powerups(lab)}')
    print(f'Posições dos power-ups: {obter_posicoes_powerups(lab)}')
    print(f'Posições dos túneis: {obter_posicoes_tuneis(lab)}')
    print(f'Posição inicial (P): {obter_posicao_inicial(lab)}')
    print(f'Posição da saída (S): {obter_posicao_saida(lab)}')
    print(f'Dimensões: {len(lab)} linhas x {len(lab[0])} colunas')