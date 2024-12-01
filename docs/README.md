# Общее
В нашем репозитории вы можете найти функции для вычесления площади и периметра геометрических фигур. 
Сейчас поддерживаются:
- Circle
- Square

# Формулы
## Площадь
- Circle: S = πR²
- Square: S = a²

## Периметр
- Circle: P = 2πR
- Square: P = 4a

# Доступные функции
## Circle (circle.py)
- area(r)
функция принимает r - радиус круга и возвращает его площадь

print(area(1)) # 3.141592653589793

- perimeter(r)
функция принимает r - радиус круга и возвращает его периметр

print(perimeter(1)) # 6.283185307179586

## Square (square.py)
- area(a)
функция принимает a - длину стороны квадрата и возвращает его площадь

print(area(1)) # 1

- perimeter(a)
функция принимает a - длину стороны квадрата и возвращает его периметр

print(perimeter(1)) # 4

# История изменения
### commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (HEAD -> main, origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

### commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added