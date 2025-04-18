x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())
"""
НиПосередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов. Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота имеет координаты (
x
1
x 
1
​
 , 
y
1
y 
1
​
 ), северо-восточный угол – координаты (
x
2
x 
2
​
 , 
y
2
y 
2 
​
 ).

Пловец находится в точке с координатами (x, y). Определите, к какой стороне плота (северной, южной,
западной или восточной) или к какому углу плота (северо-западному, северо-восточному, юго-западному,
юго-восточному) пловцу нужно плыть, чтобы как можно скорее добраться до плота.

Формат ввода
Программа получает на вход шесть чисел в следующем порядке: 
x
1
x 
1
​
 , 
y
1
y 
1
​
  (координаты юго-западного угла плота), 
x
2
x 
2
​
 , 
y
2
y 
2
​
  (координаты северо-восточного угла плота), 
x
x, 
y
y (координаты пловца). Все числа целые и по модулю не превосходят 100. Гарантируется, что 
x
1
<
x
2
x 
1
​
 <x 
2
​
 , 
y
1
<
y
2
y 
1
​
 <y 
2
​
 , 
x
≠
x
1
x

=x 
1
​
 , 
x
≠
x
2
x

=x 
2
​
 , 
y
≠
y
1
y

=y 
1
​
 , 
y
≠
y
2
y

=y 
2
​
 , координаты пловца находятся вне плота.

 Формат вывода
Если пловцу следует плыть к северной стороне плота, программа должна вывести символ ”N”,
к южной — символ ”S”, к западной — символ ”W”, к восточной — символ ”E”. Если пловцу следует
плыть к углу плота, нужно вывести одну из следующих строк: ”NW”, ”NE”, ”SW”, ”SE”.
"""

def get_direction(x1: int, y1: int, x2: int, y2: int, x: int, y: int):
    if x1 <= x <= x2:
        if y > y2:
            return 'N'
        return 'S'
    if y1 <= y <= y2:
        if x > x2:
            return 'E'
        return 'W'
    if x < x1:
        if y < y1:
            return 'SW'
        return 'NW'
    if x > x2:
        if y > y2:
            return 'NE'
        return 'SE'


print(get_direction(x1, y1, x2, y2, x, y))

# top
x1, y1, x2, y2, x, y = -1, -2, 5, 3, 1, 5
print(get_direction(x1, y1, x2, y2, x, y), ' assert N')

x1, y1, x2, y2, x, y = -1, -2, 5, 3, 1, -4
print(get_direction(x1, y1, x2, y2, x, y), ' assert S')

x1, y1, x2, y2, x, y = -1, -2, 5, 3, -2, 2
print(get_direction(x1, y1, x2, y2, x, y), ' assert W')

x1, y1, x2, y2, x, y = -1, -2, 5, 3, 6, -1
print(get_direction(x1, y1, x2, y2, x, y), ' assert E')

x1, y1, x2, y2, x, y = -1, -2, 5, 3, -10, 10
print(get_direction(x1, y1, x2, y2, x, y), ' assert NW')

x1, y1, x2, y2, x, y = -1, -2, 5, 3, -10, -10
print(get_direction(x1, y1, x2, y2, x, y), ' assert SW')

x1, y1, x2, y2, x, y = -1, -2, 5, 3, 10, 10
print(get_direction(x1, y1, x2, y2, x, y), ' assert NE')

x1, y1, x2, y2, x, y = -1, -2, 5, 3, 60, -10
print(get_direction(x1, y1, x2, y2, x, y), ' assert SE')