#1 início
#2 t ← 0
#3 T ← Tmax
#4 seleciona um ponto corrente vc de forma aleatória
#5 aval(vc)
#6 repita
#7 t ← 0
#8 repita
#9 seleciona um novo ponto vn em N(vc)
#10 se aval(vn) < aval(vc) então
#11 vc ← vn
#12 fim
#13 senão
#14 se random[0, 1) < e
#aval(vc)−aval(vn)
#T então
#15 vc ← vn
#16 fim
#17 fim
#18 t ← t + 1
#19 até t = KT
#20 T ← k ∗ T
#21 até T < Tmin
#22 fim


# Caso A = 10 Tmax,0.95 k,20 KT e 5 Tmin
# Caso B = 100 Tmax,0.9 k,25 KT e 10 Tmin
# Caso C = eu decido Tmax,K,KT e Tmin

from random import randrange




class SimulatedAnnealing: 
    def calcula(TemperaturaMax,k,KT,TemperaturaMin): 
        LeitorDeArquivo = open("st70.tsp.txt")
        NumeroDeVertices=  len(LeitorDeArquivo.readlines())

        TemperaturaAtual=TemperaturaMax
        melhor_candidato= randrange(NumeroDeVertices) #indentificador de um vértice é escolhido aleatoriamente,todo candidato é um vértice
        while (TemperaturaAtual<TemperaturaMin):
          iteracoes=0
          while(iteracoes==KT):
                candidato_novo=randrange(NumeroDeVertices) #escolha de novo candidato
                if(candidato_novo<melhor_candidato):
                 melhor_candidato=candidato_novo
                else:
                    if(randrange(1)<((melhor_candidato-candidato_novo)/TemperaturaAtual)): #eu sei q essa linha de codigo ta errada,ta faltando o numero de euler
                        melhor_candidato=candidato_novo
                iteracoes=iteracoes+1
        TemperaturaAtual=TemperaturaAtual*k

        return melhor_candidato
