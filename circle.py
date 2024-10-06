import math

def area(r):
    '''
      Возвращает площадь окружности

      Параметры: a (int): радиус окружности

      Возвращаемое значение: площадь окружности
     '''
    return math.pi * r * r


def perimeter(r):
    '''
       Возвращает периметр окружности

       Параметры: a (int): радиус окружности

       Возвращаемое значение: периметр окружности
      '''
    return 2 * math.pi * r


print ( perimeter(6))