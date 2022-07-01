import math


class CalculaDistancia:
    def  calcula(coordenada_x1,coordenada_y1,coordenada_x2,coordenada_y2):
        return  math.sqrt(  ((coordenada_x1-coordenada_x2)**2) + ((coordenada_y1-coordenada_y2)**2))