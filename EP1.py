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

  Nome :BRUNO KLEINE MOLLICA
  NUSP :14562470
  Turma:51
  Prof.:RENATA WASSERMANN

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

n = int(input('Digite o numero N de pokebolas: '))
g = int(input('Digite o valor da gravidade: '))
xp = int(input('Digite a coordenada x (inteiro >= 0) do pokemon: '))
yp = int(input('Digite a coordenada y (inteiro >= 0) do pokemon: '))
print(' ')
tent = 1

while n > 0: 
    
    print('Tentativa %d:' %tent ,'\n')
    xt = int(input('Digite a coordenada x (inteiro >= 0) do treinador: ' ))
    yt = int(input('Digite a coordenada y (inteiro >= 0) do treinador: ' ))
    vyb = int(input('Digite a componente y da velocidade de lancamento: '))
    vxb = 1
    vybi = vyb 
    xb = xt       # xb inicial == x treinador      
    yb = yt       # yb inicial == y treinador 
    t = 0          
    
    while yb > 0 and xb < xp : 
    
        xb = xt + vxb*t
        yb = yt + vybi*t - g/2 * t*t
        vyb = vybi - g * t
        print('> t= ',int(t), 'vy= ',int(vyb),    'x= ',int(xb), 'y= ',int(yb))
        t = t + 1 
    
    if yt == 0 :  #caso em que a bola inicia com y = 0 
        print('> t= ',int(t), 'vy= ',int(vyb),    'x= ',int(xb), 'y= ',int(yb))
        print ('A pokebola nao atingiu o pokemon.')
        n = n - 1           #continuar laço até acabar as pokebolas
        tent = tent + 1 
        
    elif xt == xp and yt == yp:   #caso em que bola inicia com mesmas cordenadas que o pokemom 
        print('> t= ',int(t), 'vy= ',int(vyb),    'x= ',int(xb), 'y= ',int(yb))
        print ('A pokebola atingiu o pokemon.')
        n = 0     #parar laço 
    
    elif xb == xp and yb == yp : 
        
            print ('A pokebola atingiu o pokemon.')
            n = 0     #parar laço 
    
    
    else:
        
        print ('A pokebola nao atingiu o pokemon.')
        n = n - 1           #continuar laço até acabar as pokebolas
        tent = tent + 1 
    
    

