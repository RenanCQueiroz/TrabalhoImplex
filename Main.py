

#De forma análoga, o algoritmo de Arrefecimento Simulado substitui a solução atual por uma solução próxima (i.e., na sua vizinhança no espaço de soluções), 
# escolhida de acordo com uma função objetivo e com uma variável T (dita Temperatura, por analogia). 
# Quanto maior for T, maior a componente aleatória que será incluída na próxima solução escolhida. 
#À medida que o algoritmo progride, o valor de T é decrementado, começando o algoritmo a convergir para uma solução ótima, necessariamente local.'

from CalculaDistancia import CalculaDistancia

print(CalculaDistancia.calcula(10,20,30,50))


