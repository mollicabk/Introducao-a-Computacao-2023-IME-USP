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

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

GRAVIDADE = 9.81
EPSILON = 0.01
DELTA_T = 0.01
PI = 3.14159265358979323846

def seno(theta):
    
    '''
    Esta função aproxima o valor da função seno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do seno do ângulo theta.
    '''
    # Escreva aqui o corpo da função
    
    x = theta * PI /180
    termo = 1
    soma = 0 
    k = 1 
    a = 2
    while abs(termo) >= 1e-10 :
        termo = ((-1)**a)*(x**k)/(fat(k))
        soma += termo
        k += 2 
        a += 1
    return soma 
   
def cosseno(theta):
    '''
    Esta função aproxima o valor da função cosseno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do cosseno do ângulo theta.
    '''
    # Escreva aqui o corpo da função
    
    x = theta * PI /180
    termo = 1
    soma = 0
    k = 0
    a = 2
    while abs(termo) >= 1e-10 :
        termo = ((-1)**a)*(x**k)/(fat(k))
        soma += termo
        k += 2 
        a += 1 
        
    return soma


def raizQuadrada(x):
    '''
    Esta função aproxima o valor da raiz quadrada de x, através da
    fórmula de recorrência r_0 = x e r_{n+1} = 1/2 (r_n+ x/r_n)
    enquanto o módulo da diferença entre os dois últimos valores
    calculados for maior que 1e-10.
    Entrada: O valor de x
    Saída: A aproximação da raiz quadrada de x.
    '''
    # Escreva aqui o corpo da função

    rn = x
    rn1 = (rn+x/rn)/2

    while abs(rn-rn1) >= 1e-10:
        rn = rn1
        rn1 = (rn+x/rn)/2

    return rn1


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    # Escreva aqui o corpo da função
    
    x = x + vx * dt 
    y = y + vy * dt - (GRAVIDADE*dt**2)/2
    return(x, y)

def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    # Escreva aqui o corpo da função
    
    vy = vy - GRAVIDADE * dt
    return(vx, vy)


def distanciaPontos(x1, y1, x2, y2):
    '''
    Esta função calcula a distância entre dois pontos dados por
    (x1, y1) e (x2, y2).
    Entrada: As coordenadas de dois pontos no plano, x1, y1, x2, y2,
    em metros.
    Saída: A distância entre (x1, y1) e (x2, y2) em metros.
    '''
    # Escreva aqui o corpo da função
    
    dist = raizQuadrada(((x2-x1)**2)+((y2-y1)**2))
    return dist     


def houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r):
    '''
    Esta função calcula se houve ou não colisão entre a pokebola e o
    pokemon considerando-se um raio r.
    Entrada: posição x e y da pokebola, posição x e y do pokemon
    e o raio r, todas medidas em metros.
    Saída: Retorna True caso haja colisão, e False caso contrário.
    '''
    # Escreva aqui o corpo da função
    
    colid = False
    if distanciaPontos(xpokebola, ypokebola, xpokemon, ypokemon) <= r : 
        colid = True 
    
    return colid
    

def simula_lancamento (xpokebola, ypokebola,
                       vlancamento, angulolancamento,
                       xpokemon, ypokemon, r):
    '''
    Esta função simula o lançamento da bola até que ela atinja o
    pokemon, ou o solo a menos de EPSILON.
    Na simulação, considere as seguintes constantes:
    EPSILON é uma constante de precisão de 1.0e-2 metro.
    DELTAT é uma constante de precisão de 1.0e-2 segundo.
    Entrada: Posição inicial da pokebola (xpokebola e ypokebola)
    em metros.
    Posição do pokemon (xpokemon e ypokemon) em metros.
    Velocidade escalar em metros por segundo
    e ângulo de lançamento em graus.
    O raio r em metros.
    Saída: Três valores: Um booleano (True se o lançamento teve sucesso 
    e acertou o pokemon, ou False caso contrário) e as coordenadas finais
    x e y da pokébola.
    '''
    # Escreva aqui o corpo da função
    vx = vlancamento * cosseno(angulolancamento)
    vy = vlancamento * seno(angulolancamento) 
    while not atingiuSolo(yb) and not houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r): 
        vx, vy = atualizaVelocidade(vx, vy, dt=DELTA_T)
        xpokebola,  ypokebola = atualizaPosicao(x, y, vx, vy, dt=DELTA_T)
 
    return houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r) , xpokebola, ypokebola
 
        

def main():
    xpokemon = float(input("Digite a coordenada x do pokemon: "))
    ypokemon = float(input("Digite a coordenada y do pokemon: "))
    r  = float(input("Digite o raio do pokemon (> 0) em metros: "))
    # Complete aqui o corpo da função
    
    
    tent = 1 
    colid = False
    
    while tent <= 3 and not colid : 
        print('Tentativa ', tent)
        xpokebola = float(input('Digite a coordenada x do treinador: '))
        ypokebola= float(input('Digite a coordenada y do treinador: '))
        vlancamento = float(input('Digite a velocidade de lancamento em m/s: '))
        theta = float(input('Digite o angulo de lancamento em graus: '))
        vx = vlancamento * cosseno(theta)
        vy = vlancamento * seno(theta) 
        if houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r) :
            print('A pokebola antigiu o pokemon.')
            colid = True
        else:
            print('A pokebola nao atingiu o pokemom por ',distBolaPok(xpokemon,ypokemon,xpokebola, ypokebola))
        tent += 1


# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================

def fat(x):
    
    fat = 1
    while x > 0:
        fat = fat * x 
        x = x - 1
    return fat

def atingiuSolo(yb):
    
    atingiu = False 
    if yb < EPSILON :
        antigiu = True 
    
    return atingiu

def coordFinal(x, y, vlancamento, d=+DELTA_T) : 
    vx = vlancamento * cosseno(angulolancamento)
    vy = vlancamento * seno(angulolancamento) 
    while y > 0.01 and not houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r): 
        vx, vy = atualizaVelocidade(vx, vy, dt=DELTA_T)
        x,  y = atualizaPosicao(x, y, vx, vy, dt=DELTA_T)
        
    return (x, y)
    


def distBolaPok(xp, yp, x, y):
    x, y = coordFinal(x, y, vlancamento, d=+DELTA_T)
    return distanciaPontos(xp, yp, xb, yb)

# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN 
# ======================================================================
