#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def brackets_order_checker(sequence, stack=[]):
    if not sequence:
        return not stack

    char = sequence[0]

    # Если открывающая скобка, то кладем ее в стек
    if char in "([":
        return brackets_order_checker(sequence[1:], stack + [char])
    # Если закрывающая скобка, проверяем, соответствует ли она последней открывающей в стеке
    elif char in ")]":
        # Не пуст ли стек и соответствуют ли скобоки
        if stack and ((char == ")" and stack[-1] == "(") or (char == "]" and stack[-1] == "[")):
            return brackets_order_checker(sequence[1:], stack[:-1])
        else:
            return False
    else:
        # Пропуск пробелов
        return brackets_order_checker(sequence[1:], stack)


if __name__ == '__main__':
    seq = input("Введите последовательность из скобок: ")
    result = brackets_order_checker(seq)
    print(result)
