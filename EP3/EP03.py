"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome :Bruno Kleine Mollica
  NUSP :14562470
  Turma:51
  Prof.:Renata Wassermann

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

import math

DELTA_T = 0.1
GRAVIDADE = 2

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP3.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

def leArquivo(nomeArquivo = 'entrada.txt'):
    '''
    Esta função lê um arquivo ('entrada.txt' por default) e
    retorna uma lista de listas.
    Entrada: arquivo cujo nome está armazenado em nomeArquivo.
             Por default, é 'entrada.txt'
    Saída: uma lista de listas, onde o primeiro elemento é uma
           lista de inteiros [m, n] (dimensões da matriz) e os
           elementos subsequentes são listas que representam as
           característica lidas dos Pokémons na forma:
           [nome, raio, x, y]
    '''
    resultado = []
    arquivo = open(nomeArquivo, 'r')

    # Cria lista de dimensões da matriz
    dimensoes = arquivo.readline().split(' ')
    for i in range(len(dimensoes)):
        dimensoes[i] = int(dimensoes[i])
    resultado.append(dimensoes)

    # Cria listas de características de Pokémons
    pokemons = arquivo.readlines()
    for pokemon in pokemons:
        pokemon = pokemon.split(' ')
        for i in range(1, len(pokemon)):
            pokemon[i] = int(pokemon[i])
        resultado.append(pokemon)
    arquivo.close()

    return resultado


def criaMatriz(m, n):
    '''
    Esta função cria e retorna uma lista de listas.
    Entrada: dois inteiros que representam o número de linhas e
             o número de colunas da matriz.
    Saída: uma lista de m listas, cada uma com n elementos, todos
           inicializados com zeros.
    '''
    matriz = []
    for i in range(m):
        linha = [] 
        for j in range(n):
            linha.append(0)
        matriz.append(linha)
        
    return matriz


def populaMatriz(matriz, pokemons):
    '''
    Esta função recebe uma matriz e uma lista contendo listas que
    representam os pokémons na forma [nome, raio, x, y] e preenche-a
    os pokémons conforme a representação retangular considerando os
    raios da representação.
    Entrada: matriz representada por uma lista de listas
    Saída: A matriz fornecida é modificada.
    '''
    
    ind = 1 
    while ind < len(pokemons) + 1:
        raio = pokemons[ind - 1][1]
        x = pokemons[ind - 1][2] + 1
        y = pokemons[ind - 1][3] + 1
        matriz = preenchePokemon(matriz, ind, x, y, raio)
        ind += 1
        
    return matriz


def preenchePokemon(matriz, ind, x, y, raio):
    '''
    Esta função é auxiliar da função populaMatriz. Ela insere
    um Pokémon na matriz de acordo com sua representação retangular
    baseada no raio ao redor do ponto central (x,y)
    Entrada: matriz representada por uma lista de listas
             id é o número a preencher a matriz; para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente.
             x,y são as coordenadas do ponto central
             raio é a distância a ser guardada a partir do
             ponto central.
    Saída: A matriz fornecida é modificada.
    '''
    
    for lin in range(y - raio - 1, y + raio):
        for col in range(x - raio - 1, x + raio):
            matriz[lin][col] = ind
    
    
    return matriz 
    
    
    
def removePokemon(matriz, ind, pokemons):
    '''
    Esta função recebe uma matriz, o numeral que representa o pokémon
    a ser removido da matriz (id) e a lista contendo as listas que
    representam pokémons, substituindo os numerais id por zero
    Entrada: matriz representada por uma lista de listas;
             id é o número a preencher a matriz, para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente;
             pokemons lista contendo as listas que representam pokémons.
    Saída: A matriz fornecida é modificada.
    '''
    for lin in range(len(matriz)):
        for col in range(len(matriz[0])):
            if matriz[lin][col] == ind:
                matriz[lin][col] = 0
        
    return matriz        
        
def imprimeMatriz(matriz):
    '''
    Esta função imprime a matriz dada.
    Note que a matriz deve ser impressa com espelhamento vertical, 
    pois a primeira linha representa o chão.
    Entrada: matriz representada por uma lista de listas.
    '''
    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            if matriz[lin][col] == 0:
                matriz[lin][col] = '.'
                
    for lin in range(len(matriz) - 1, -1, -1):
        for col in range(len(matriz[lin])):
            print(matriz[lin][col], end='')
        print()
                

def insere(xt, matriz):
    
    matriz[0][round(xt)] = 'T'
    return matriz

def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    novo_x = x + vx * dt
    novo_y = y + vy * dt - (GRAVIDADE*dt*dt)/2
    
    return novo_x, novo_y



def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    novo_vx = vx  # Não há alteração na velocidade horizontal
    novo_vy = vy - GRAVIDADE * dt 
    
    return novo_vx, novo_vy
    

def grau2Radiano(theta):
    '''
    Esta função converte o ângulo theta em graus para radianos.
    Entrada: ângulo theta.
    Saída: ângulo theta em radianos.
    '''
    theta_radianos = math.radians(theta)
    
    return theta_radianos
  
  
def copia(matriz):
    matriz1 = []
    for i in range(len(matriz)):
        linha = [] 
        for j in range(len(matriz[0])):
            linha.append(matriz[i][j])
        matriz1.append(linha)
        
    return matriz1

def main():
    
    nome = input("Digite o nome do arquivo: ")
    N = int(input("Digite o numero N de pokebolas: "))
    #xt = float("Digite a coordenada x do treinandor: ")
    xt = float(input("Digite a coordenada x do treinador: "))
    
    info = leArquivo(nome)
    m = info[0][0]
    n = info[0][1]
    matriz = criaMatriz(m, n)
    pokemons = info[1:]
    k = len(pokemons)
    
    matriz = populaMatriz(matriz, pokemons)
    
    
    capturou = False 

    while N > 0 and k > 0:
        
        if k < len(pokemons):
            xt = xpok
        print("pokebolas disponiveis = ", N)
        print("Estado atual do jogo:")
        
    
        
        matriz = insere(xt, matriz)
           
        imprimeMatriz(matriz)
       
        v = float(input("Digite a velocidade de lancamento em m/s: "))
        theta = float(input("Digite o angulo de lancamento em graus: "))
        
        
        matriz_lanc = copia(matriz)

        theta = grau2Radiano(theta) 
        vx = v * math.cos(theta)
        vy = v * math.sin(theta)
        colidiu  = False
    
        (x, y) = (xt, 0)
    
        print("Representacao grafica do lancamento: ")
        
        while round(y) >= 0 and 0 <= round(x) <= n - 1 and not colidiu :
            if round(y) < m and matriz_lanc[round(y)][round(x)] != 'T' :
                if matriz_lanc[round(y)][round(x)] != '.' and matriz_lanc[round(y)][round(x)] != 'o':
                    indi = matriz_lanc[round(y)][round(x)]
                    xpok = round(x)
                    colidiu = True
            
                
                matriz_lanc[round(y)][round(x)] = 'o'
            (x, y) = atualizaPosicao(x, y, vx, vy, dt=DELTA_T)
            (vx, vy) = atualizaVelocidade(vx, vy, dt=DELTA_T)
        
        imprimeMatriz(matriz_lanc)
        
        N -= 1
    
        if colidiu == True:
            nome = info[indi][0]
            print(f"Um {nome} foi capturado!")
            k = k - 1
            matriz = removePokemon(matriz, indi, pokemons)
            matriz[0][round(xt)] = '.'
            xt = xpok
            
        if colidiu == False: 
            print("O lancamento nao capturou pokemon algum")
            matriz[0][round(xt)] = '.'
            if N > 0 and k > 0 :
                xt = float(input("Digite a coordenada x do treinador: "))
            
        if k == 0:
            print("Parabens! Todos pokemons foram capturados")
            
    
        
     
        
        if N == 0 and k != 0 :
            print("Jogo encerrado")
        
        


main()