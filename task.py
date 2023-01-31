def choose_coffee(*args):
    for i in args:
        if i == 'Эспрессо':
            if ingredients[0] >= 1:
                ingredients[0] -= 1
                return i
        if i == 'Капучино':
            if ingredients[0] >= 1 and ingredients[1] >= 3:
                ingredients[0] -= 1
                ingredients[1] -= 3
                return i
        if i == 'Маккиато':
            if ingredients[0] >= 2 and ingredients[1] >= 1:
                ingredients[0] -= 2
                ingredients[1] -= 1
                return i
        if i == 'Кофе по-венски':
            if ingredients[0] >= 1 and ingredients[2] >= 2:
                ingredients[0] -= 1
                ingredients[2] -= 2
                return i
        if i == 'Латте Маккиато':
            if ingredients[0] >= 1 and ingredients[1] >= 2 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[1] -= 2
                ingredients[2] -= 1
                return i
        if i == 'Кон Панна':
            if ingredients[0] >= 1 and ingredients[2] >= 1:
                ingredients[0] -= 1
                ingredients[2] -= 1
                return i
    return 'К сожалению, не можем предложить Вам напиток'


coffee = int(input('Сколько есть кофе: '))
milk = int(input('Сколько есть молока: '))
cream = int(input('Сколько есть сливок: '))
ingredients = [coffee, milk, cream]
print(choose_coffee('Эспрессо', 'Маккиато',
      'Капучино', 'Кон Панна', 'Кофе по-венски'))
print(choose_coffee('Эспрессо', 'Маккиато',
      'Капучино', 'Кон Панна', 'Кофе по-венски'))
print(choose_coffee('Эспрессо', 'Маккиато',
      'Капучино', 'Кон Панна', 'Кофе по-венски'))
