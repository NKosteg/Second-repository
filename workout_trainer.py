# info = "We couldn't verify your mother's maiden name."
# intro = "Here is important information about your account security."
#
# first_name = 'Joffrey'
# greeting = 'Hello'
#
#
# what = greeting + ', ' + first_name + '!'
# print(what)
#
# print(intro + '\n' + info)
# from sys import prefix
# from operator import index???


# magic = '\nyou'
# print(magic[1])

# value = 'Hexlet'
# print(value [3:])  # 'let'
# print(value [:3])
#
# value = '12-08-2034'
#
# year = value[6:10]
# print(year)  # => 2034

# one = 'Naharis'
# two = 'Mormont'
# three = 'Sand'
#
# # BEGIN (write your solution here)
# print(f'{one[2]} {two[1]} {three[3]} {two[4]} {two[2]}')
# # END

# value = 2.9
# converted_value = int(value)
# converted_value1 = str(converted_value)
# print(converted_value1 + ' times')

# company1 = 'Apple'
# company2 = 'Samsung'

# result = len(company1 + company2)
# print(result)

# number = 255
# print(hex(number))

# text = 'Never forget what you are, for surely the world will not'

# print(text[0])
# print(text[-1])
# print(f'First: {text[0]}\nLast: {text[-1]}')

# from random import random
# print(round(random() * 10))

# text = 'Never forget what you are, for surely the world will not'
# print(str(text.find('N')))
# print(str(text.find(',')))
# print(f"Index Of N: {text.find('N')}\nIndex Of ,: {text.find(',')}")
#
# name = 'Tirion'
# # Чему равен результат такого вызова?
# print(name[1:5].upper().find('I'))

# text = 'When \t\n you play a \t\n game of thrones you win or you die.'
# print(text)
# print(len(text[4:16].strip()))

# def show_greeting():
#     text = 'Hello, Hexlet'
#     print(text)
# show_greeting()

# def run():
#     return 5
#     return 10
# print(run())

# def say_hurray_three_times():
#     word = 'hurray!'
#     return f'{word} {word} {word}'
# hurray = say_hurray_three_times()
# print(hurray)

# def say_hurray_three_times():
#     return 'hurray! hurray! hurray!'
# hurray = say_hurray_three_times()
# print(hurray)

# def truncate(text, length):
#     return text[:length] + '...'
#
# modified = truncate('hekslet', 2)
# print(modified)

# def truncate(text, length):
#     # BEGIN
#     result = f"{text[0:length]}..."
#     return result
# text = input('Введи текст: ')
# length = int(input('Сколько символов оставить: '))
# print(truncate(text, length))

# def get_hidden_card(number_card,rem = 4):
#     result = number_card.replace(number_card[:12], '*' * rem )
#     return result
# number_card = input('Введите номер карты: ')
# print(get_hidden_card(number_card,5))
## или
# def get_hidden_card(card_number, stars_count=4):
#     visible_digits_line = card_number[-4:]
#     return f"{'*' * stars_count}{visible_digits_line}"
# number_card = input('Введите номер карты: ')
# print(get_hidden_card(number_card,2))

# def trim_and_repeat(text, offset = 0, repetitions = 1):
#     crop_line = text[offset:] * repetitions
#     return crop_line
## или
# def trim_and_repeat(text, offset = 0, repetitions = 1):
#     return text[offset:] * repetitions
## или
# text = 'python'
# print(trim_and_repeat(text,2,3))

# def word_multiply(text: str, repetitions: int):
#     return f'{text * repetitions}'
# text = 'python'
# print(word_multiply(text, 2))
# print(word_multiply(text, 5))

# def is_pensioner(age):
#     return age >= 60
# print(is_pensioner(75))
# print(is_pensioner(18))

# def is_mister(text):
#     return text == 'Mister'
# print(is_mister('Mister'))
# print(is_mister('Missis'))

# def is_international(phone_num):
#     prefix = phone_num[0]
#     return prefix == '+'
# # или
# #     return phone_num[0] == '+'
# print(is_international('89998887766'))
# print(is_international('+79998887766'))

# def is_leap_year(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
# print(is_leap_year(2018))
# print(is_leap_year(2017))
# print(is_leap_year(2016))

# def is_palindrome(text):
#     return text.lower() == text[::-1].lower()
#
# def is_not_palindrome(text):
#     return not is_palindrome(text)
#
# print(is_palindrome("шалаш"))
# print(is_palindrome("хекслет"))
# print(is_palindrome("Довод"))
# print(is_palindrome("Фунуция"))
# print( '\n' )
# print(is_not_palindrome('шалаш')) # false
# print(is_not_palindrome('Ага')) # false
# print(is_not_palindrome('хекслет')) # tru

# def string_or_not(text):
#     return isinstance(text, str) and 'yes' or 'no'
#
# print(string_or_not('Hexlet'))
# print(string_or_not(10))
# print(string_or_not(''))
# print(string_or_not(False))

# def guess_number(num):
#     if num == 42:
#         return 'You win!'
#     return 'Try again!'
# print(guess_number(42))
# print()
# print(guess_number(61))

# def normalize_url(url):
#     if url[:8] == 'https://':
#         return url
#     else:
#         if url[:7] == 'http://':
#             return 'https://' + url[7:]
#         else:
#             return 'https://' + url
#     print(url[:8])
#     print(url[8:])
#
# print(normalize_url('https://ya.ru'))
# print(normalize_url('google.com'))
# print(normalize_url('http://ai.fi'))

# def who_is_this_house_to_starks(last_name):
#     if last_name == 'Karstark' or last_name == 'Tully':
#         return 'friend'
#     elif last_name == 'Lannister' or last_name == 'Frey':
#         return 'enemy'
#     else:
#         return 'neutral'
#
# print(who_is_this_house_to_starks('Karstark'))  # => 'friend'
# print(who_is_this_house_to_starks('Frey'))      # => 'enemy'
# print(who_is_this_house_to_starks('Joar'))      # => 'neutral'
# print(who_is_this_house_to_starks('Ivanov'))    # => 'neutral''
#
# def flip_flop(text):
#     return 'flop' if text == 'flip' else 'flip' if text == 'flop' else 'error'
# print(flip_flop('flip'))
# print(flip_flop('flop'))
# print(flip_flop('fghj'))
# #
# def get_number_explanation(num):
#     match num:
#         case 666:
#             return 'devil number'
#         case 42:
#             return 'answer for everything'
#         case 7:
#             return 'prime number'
#         case _:
#             return 'just a number'
# print(get_number_explanation(8))
# print(get_number_explanation(666))
# print(get_number_explanation(42))
# print(get_number_explanation(7))
# #
# def print_number(last_number):
#     i = last_number
#     while i >= 1:
#         print(i)
#         i = i - 1
#     print('finished!')
# print_number(4)
# #
# def multiply_numbers_from_range(start, finish):
#     i = start
#     multiply = 1
#     while i <= finish:
#         multiply = multiply * i
#         i = i + 1
#     return multiply
# #
# print(multiply_numbers_from_range(1, 5))
# print(multiply_numbers_from_range(2, 3))
# print(multiply_numbers_from_range(6, 6))
# print(multiply_numbers_from_range(0, 6))
# #
# def join_numbers_from_range(start, stop):
#     result = ''
#     i = start
#     while i <= stop:
#         result = result + str(i)
#         i = i + 1
#     return result
# print(join_numbers_from_range(1, 1))
# print(join_numbers_from_range(2, 3))
# print(join_numbers_from_range(5, 10))
# #
# def print_reversed_word_by_symbol(word):
#     i = len(word) - 1
#     while i >= 0:
#         print(word[i])
#         i = i - 1
# word = 'Hexlet'
# print_reversed_word_by_symbol(word)
# #
# def count_chars(string, char):
#     i = 0
#     count = 0
#     while i < len(string):
#         if string[i].upper() == char or string[i].lower() == char:
#             count = count + 1
#         i = i + 1
#     return count
# print(count_chars('HexlEt', 'e'))
# print(count_chars('HexlEt', 'E'))
# # ili
# def count_chars(string, char):
#     i = 0
#     count = 0
#     while i < len(string):
#         if string[i].upper() == char.upper():
#             count = count + 1
#         i = i + 1
#     return count
# print(count_chars('HexlEt', 'e'))
# print(count_chars('HexlEt', 'E'))
# #
# def sub_str(str, len):
#     index = 0
#     new_str = ''
#     while index < len:
#         current_char = str[index]
#         new_str =new_str + current_char
#         index = index + 1
#     return new_str
# string = 'If I look back I am lost'
# print(sub_str(string, 1)) # => 'I'
# print(sub_str(string, 9))
# #
# def is_arguments_for_substr_correct(string, index, len_result ):
#     if len_result < 0 or index < 0 or index > len(string) - 1 or len_result + index > len(string):
#         return False
#     else:
#         return True
#
# string = 'Sansa Stark'
# print(is_arguments_for_substr_correct(string, 2, -3))   # => False
# print(is_arguments_for_substr_correct(string, -1, 3))   # => False
# print(is_arguments_for_substr_correct(string, 4, 100))  # => False
# print(is_arguments_for_substr_correct(string, 10, 10))  # => False
# print(is_arguments_for_substr_correct(string, 11, 1))   # => False
# print(is_arguments_for_substr_correct(string, 3, 3))    # => True
# print(is_arguments_for_substr_correct(string, 0, 5))    # => True
# #
# def filter_string(string, char):
#     modified_string =''
#     index = 0
#     while index < len(string):
#         if string[index] != char:
#             modified_string = modified_string + string[index]
#         index += 1
#     return modified_string
#
# text = 'If I look back I am lost'
# print(filter_string(text, 'I'))  # 'f  look back  am lost'
# print(filter_string(text, 'o'))  # 'If I lk back I am lst
# #
# def is_contains_char(text, char):
#     index = 0
#     while index < len(text):
#         if text[index] == char:
#             return True
#         index += 1
#     return False
#
# print(is_contains_char('Hexlet', 'H'))  # => True
# print(is_contains_char('Hexlet', 'h'))  # => False
# print(is_contains_char('Awesomeness', 'm'))  # => True
# print(is_contains_char('Awesomeness', 'd'))  # => False
# #
# def filter_string(text, char):
#     result = ''
#     for current_char in text:
#         if current_char.lower() != char.lower():
#             result += current_char
#     return result
# text = 'If I look forward I win'
# print(filter_string(text, 'i')) # 'f  look forward  wn'
# print(filter_string(text, 'O')) # 'If I lk frward I win'
# #
# def print_table_of_squares(fr, to):
#     for i in range(fr, to + 1):
#         print(f'square of {i} is {i ** 2}')
# print_table_of_squares(1, 3)
# #



