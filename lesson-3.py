# Основы Python. GU_Data_Engineering_1542 (31.01.2022)
# Выполнил: Фролов Виктор Сергеевич;
# Урок 3.


'''
1.Написать функцию num_translate(),
переводящую числительные от 0 до 10 c англи йского на русский язык.Например:

'''


def num_translate(i):
    translate_book = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
        "eleven": "одиннадцать",
        "twelve": "двенадцать",
        "thirteen": "тринадцать",
        "fourteen": "четырнадцать",
        "fifteen": "пятнадцать",
    }
    if i.istitle():
        return translate_book[i.lower()].title()
    else:
        return translate_book[i]


score = input('Value:')
print(num_translate(score))


# Другое решение:

eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(eng_word):
    return eng_rus_dict.get(eng_word)


print(num_translate('seven'))


# Ещё одно другое решение:

eng_rus_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(eng_word):
    if eng_word[0].isupper():
        eng_word = eng_word.lower()
        return eng_rus_dict[eng_word].capitalize()
    else:
        return eng_rus_dict[eng_word]


print(num_translate_adv('seven'))
print(num_translate_adv('Seven'))

'''
3.Написать функцию thesaurus(),
принимающую в качестве аргументов имена сотрудни ков и возвращающую словарь,
в котором ключи — первые буквы имён,
а значения — сп иски,
содержащие имена,
начинающиеся с соответствующей буквы.Например: thesaurus("Иван", "Мария", "Петр", "Илья") { "И": ["Иван", "Илья"],
"М": ["Мария"],
"П": ["Петр"] } Подумайте: полезен ли будет вам оператор распаковки ? Как поступить,
если потребу ется сортировка по ключам ? Можно ли использовать словарь в этом случае ?

'''
def thesaurus(*names):
    name_list = [*names]
    res = {}
    for name in name_list:
        name.capitalize()
        capital = name[0]
        if capital in res.keys():
            res[capital].append(name)
        else:
            res_1 = [name]
            res[capital] = res_1

    return res


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


# Другое решение:

def thesaurus(*names):
    out_dict = dict()
    for name in names:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))

'''
3.1.Написать функцию thesaurus_adv(),
принимающую в качестве аргументов строки в формате « Имя Фамилия » и возвращающую словарь,
в котором ключи — первые буквы фамилий,
а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы.Например: thesaurus_adv(
    "Иван Сергеев",
    "Инна Серова",
    "Петр Алексеев",
    "Илья Иванов",
    "Анна Савельева"
) { "А": { "П": ["Петр Алексеев"] },
"С": { "И": ["Иван Сергеев", "Инна Серова"],
"А": ["Анна Савельева"] } }

'''


def thesaurus_adv(*names_surnames):
    out_dict = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        out_dict.setdefault(surname[0], {})
        out_dict[surname[0]].setdefault(name[0], [])
        out_dict[surname[0]][name[0]].append(name_surname)
    # sorted dict
    sorted_dict = {x: out_dict[x] for x in sorted(out_dict)}  
    return out_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов",
                    "Анна Савельева"))

'''
5.Реализовать функцию get_jokes(),
возвращающую n шуток,
сформированных из трех случайных слов,
взятых из трёх списков (по одному из каждого): nouns = ["автомобиль", "лес", "огонь", "город", "дом"] adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"] adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"] Например: get_jokes(2) ["лес завтра зеленый", "город вчера веселый"]

'''


import random as rd


def get_jokes(joke_count):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    spc = ' '
    while i != joke_count:
        joke = nouns[rd.randint(0, 4)] + spc + adverbs[rd.randint(0, 4)] + spc + adjectives[rd.randint(0, 4)]
        print(joke)
        i += 1


get_jokes(6)


# Другое решение:

import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num):
    joke_list = []
    for i in range(num):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        joke_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return joke_list


print(get_jokes(1))
print(get_jokes(2))


def get_jokes_adv(num, repeats=True):
    joke_list = []

    if not repeats:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return 'No way'
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(num):
                joke_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')

    else:
        for i in range(num):
            cur_nouns = random.choice(nouns)
            cur_adverbs = random.choice(adverbs)
            cur_adjectives = random.choice(adjectives)
            joke_list.append(f'{cur_nouns} {cur_adverbs} {cur_adjectives}')
    return joke_list


print(get_jokes_adv(4, False))
print(get_jokes_adv(5, False))
print(get_jokes_adv(6, False))





