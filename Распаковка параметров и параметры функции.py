def print_params(a=1, b='строка', c=True):
    print(a, b, c)

    # Функция с параметрами по умолчанию:

print_params()
print_params(5)
print_params(47, ';)', False)
print_params(b=25)
print_params(c=[1,2,3])

    # Распаковка параметров:

values_list = [4, 'lee', False]
values_dict = {'a': 54, 'b': 'Kirill', 'c': False}

   # Распаковка + отдельные параметры:

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3, 'Rik']
print_params(*values_list_2, 42)
