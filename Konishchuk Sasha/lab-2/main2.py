# -*- coding: utf-8 -*-

# 2. Використання тернарного оператора для перевірки порожнього рядка
text = raw_input ("Input text:")
result = text if text != "" else 'None'
print(result)
