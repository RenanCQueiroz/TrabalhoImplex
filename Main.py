

#De forma análoga, o algoritmo de Arrefecimento Simulado substitui a solução atual por uma solução próxima (i.e., na sua vizinhança no espaço de soluções), 
# escolhida de acordo com uma função objetivo e com uma variável T (dita Temperatura, por analogia). 
# Quanto maior for T, maior a componente aleatória que será incluída na próxima solução escolhida. 
#À medida que o algoritmo progride, o valor de T é decrementado, começando o algoritmo a convergir para uma solução ótima, necessariamente local.'

from CalculaDistancia import CalculaDistancia
from SimulatedAnnealing import SimulatedAnnealing 


print(SimulatedAnnealing.calcula(10,0.95,20,5) )#Esse é o Caso A,não consegui fazer essa funcao receber os arquivos .txt,eu coloquei o arquivo dentro do metodo pra simular o processo correto
print(SimulatedAnnealing.calcula(100,0.9,25,10)) # Caso B   
print(SimulatedAnnealing.calcula(38,0.66,40,8)) # Esse é o caso C,com parametros decididos por mim