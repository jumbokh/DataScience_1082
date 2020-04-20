import math
class Shape:
    def __init__(self,  xPoint = 0,  yPoint = 0):
        self.__xPoint = xPoint
        self.__yPoint = yPoint

    def getPoint(self):
        return self.__xPoint, self.__yPoint

    def setPoint(self,  xPoint,  yPoint):
        self.__xPoint = xPoint
        self.__yPoint = yPoint

    def __str__(self):
        print('xPoint = %d, yPoint = %d'%(self.__xPoint, self.__yPoint))