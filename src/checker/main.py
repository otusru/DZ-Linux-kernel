#!/bin/python3

import argparse
import os
from checker import Checker

def main():
    parser = argparse.ArgumentParser(description='Проверка параметров модуля ядра.')
    parser.add_argument('module_name', type=str, help='Имя модуля для проверки')
    args = parser.parse_args()

    module_path = f"/sys/module/{args.module_name}"
    if not os.path.isdir(module_path):
        print(f"Ошибка: модуль '{args.module_name}' не загружен или не существует.")
        exit(1)

    checker = Checker(args.module_name)

    try:
        print("Проверка str_buf:", checker.check_str_buf())
        print("Проверка ch_val:", checker.check_ch_val())
        print("Проверка idx:", checker.check_idx())
    finally:
        checker.close()

if __name__ == '__main__':
    main()

