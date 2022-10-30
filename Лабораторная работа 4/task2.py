def get_count_char(str_):
    first = "".join(main_str.split())
    second = first.lower()
    dic = {}
    for num in second:
        if num.isalpha():
            if not (num in dic.keys()):
                dic[num] = 1
            else:
                dic[num] += 1
    return dic


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

