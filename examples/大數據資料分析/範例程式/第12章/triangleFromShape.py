from shape import Shape
import math

class Triangle(Shape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def getCoordinate(self):
        return self.__x1, self.__y1, self.__x2, self.__y2
    

    def setCoordinate(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def getArea(self):
        x, y = super().getPoint()
        s1 = math.sqrt((self.__x1-x)**2 + (self.__y1-y)**2)
        s2 = math.sqrt((self.__x2-self.__x1)**2 + (self.__y2-self.__y1)**2)
        s3 = math.sqrt((self.__x2-x)**2 + (self.__y2-y)**2)
        print('s1 = %d, s2 = %d, s3 = %d'%(s1, s2, s3))
        s = (s1 + s2 + s3) / 2
        area = math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
        return area

    def getPerimeter(self):
        x, y = super().getPoint()
        s1 = math.sqrt((self.__x1-x)**2 + (self.__y1-y)**2)
        s2 = math.sqrt((self.__x2-self.__x1)**2 + (self.__y2-self.__y1)**2)
        s3 = math.sqrt((self.__x2-x)**2 + (self.__y2-y)**2)
        print(s1, s2, s3)
        return s1+s2+s3

    def __str__(self):
        super().__str__()
        x , y = super().getPoint()
        print('(%d, %d), (%d, %d), (%d, %d)'
            %(x, y, self.__x1, self.__y1, self.__x2, self.__y2))