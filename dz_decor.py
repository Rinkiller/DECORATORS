# Напишите следующие функции:
# ○Нахождение корней квадратного уравнения
# ○Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения с 
# каждой тройкой чисел из csv файла.
# ○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import math
import os
import random
import json
import csv
from typing import Callable

# ○Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def deco_date_save_json(func) -> None:
    def wrapper(*args , **kwargs):
        dict_wrap = {}
        dict_wrap['a'] = args[0]
        dict_wrap['b'] = args[1]
        dict_wrap['c'] = args[2]
        dict_wrap['result'] = func(*args , **kwargs)
        with open('date.json' , 'a' , encoding='utf-8') as file:
            json.dump(dict_wrap , file, ensure_ascii=False , indent=4)
        return dict_wrap['result']
    return wrapper



# ○Декоратор, запускающий функцию нахождения корней квадратного уравнения с 
# каждой тройкой чисел из csv файла.

def deco_square_root_equation(func) -> Callable:
    """Декоратор, запускающий функцию нахождения корней квадратного уравнения с 
    каждой тройкой чисел из csv файла."""
    def open_csv_file_and_run_square_root_equation(file_name:str) ->list[list[float]]:
        with open(file_name , 'r' , encoding='utf-8') as file:
            date = csv.DictReader(file)
            count = 0
            result_list =[]
            for row in date:
                result_list.append(func(int(row["a"]) , int(row["b"]) , int(row["c"])))
        return result_list
    return open_csv_file_and_run_square_root_equation





@deco_square_root_equation
@deco_date_save_json
def get_square_root_equation(a:int , b:int , c:int)-> list[float]:
    """Нахождение корней квадратного уравнения """
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return [x1 , x2]
    elif discr == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return None
    
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def get_random_numbers_and_write_in_csv(file_name:str) -> None:
    """Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк."""
    with open(file_name , 'w' , encoding='utf-8') as file:
        count_of_lines = random.randint(100, 1000)
        
        csv_writer = csv.DictWriter(file , fieldnames=['a' , 'b' , 'c'], restval='None',dialect='excel',quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        date = []
        for _ in range(count_of_lines + 1):
            work_dict = {}
            work_dict['a'] = random.randint(1 , 100)
            work_dict['b'] = random.randint(1 , 100)
            work_dict['c'] = random.randint(1 , 100)
            date.append(work_dict)
        csv_writer.writerows(date)




get_random_numbers_and_write_in_csv('dat.csv')
lst = get_square_root_equation('dat.csv')
print(lst)
