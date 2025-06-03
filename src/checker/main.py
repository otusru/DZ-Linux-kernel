#!/usr/bin/env python3

import argparse
from checker import Checker

def main():
    parser = argparse.ArgumentParser(description='Проверка параметров модуля ядра.')
    parser.add_argument('module_name', type=str, help='Имя модуля для проверки')
    args = parser.parse_args()

    with Checker(args.module_name) as checker:
        print("Проверка str_buf:", checker.check_str_buf())
        print("Проверка ch_val:", checker.check_ch_val())
        print("Проверка idx:", checker.check_idx())

if __name__ == '__main__':
    main()
