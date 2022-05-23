perguntas = {'p1':'Qual e a capital do Rio de janeiro'}

respostas = ['1:Brasília','2:São Paulo','3:Amazona']

def jogo():
    print(20*'=')
    print('Jogo das Perguntas')
    print(20*'=')
    pontos = 1
    print()             
    print(perguntas['p1'])
    
    print(20*"_")
    print("Opções de Resposta")
    print(respostas[0], respostas[1],respostas[2])
    print(20*"_")
    
    res = int(input("responder:"))
    
    if res == 1:
        print('Parabéns Você Acertou')
        pontos + 1
    elif res == 2 or res == 3:
        print('Você Errou')
        jogo()
        
    
        
jogo()