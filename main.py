#! /bin/env python
import time

import menu.Menu
from sort import *
from menu import Menu


def menu_init():
    ret = Menu.Menu()

    ret.add_entry('h',
                  'Heap Sort',
                  Menu.SubMenu(heapsort)) \
        .add_entry('i',
                   'Insertion Sort',
                   Menu.SubMenu(insertion_sort)) \
        .add_entry('m',
                   'Merge Sort',
                   Menu.SubMenu(mergesort)) \
        .add_entry('q',
                   'Quick Sort',
                   Menu.SubMenu(quicksort)) \
        .add_entry('se',
                   'Selection Sort',
                   Menu.SubMenu(selection_sort)) \
        .add_entry('sh',
                   'shell Sort',
                   Menu.SubMenu(shell_sort)) \
        .add_entry('t',
                   'Tree Sort',
                   Menu.SubMenu(tree_sort)) \
        .add_entry('c',
                   'Comparison between algorithms above',
                   lambda: compare(ret.menu_dict)) \
        .add_entry('ex',
                   'exit the program.',
                   lambda: exit(0))

    return ret


def sanitize_input(input_, ignore=',[]', sep=' '):
    ret = input_
    for i in ignore:
        ret = ret.replace(i, sep)
    ret = ret.split(sep)
    ret = filter(''.__ne__, ret)
    return list(map(int, ret))


def compare(menu_dict, arr_len=10e3):
    from sys import setrecursionlimit
    from math import log2
    setrecursionlimit(int(arr_len * log2(arr_len)))
    sample = sorted(range(int(arr_len)), reverse=True)
    print(f'{"_" * 16}\nArray length: {arr_len}')

    for _, (name, f) in menu_dict.items():
        if type(f) == menu.Menu.SubMenu:
            print(f'Executed {name}, runtime: {f(sample[:]).runtime}s')


def exec_order(submenu, user_input):
    if type(submenu) == menu.Menu.SubMenu:
        if user_input:
            submenu(sanitize_input(user_input))
            print(f'{submenu.last_return}\ntime: {submenu.runtime}s\n\n')
        else:
            try:
                submenu(sanitize_input(
                    input('please enter an array (eg: 1, 2, 3, 4 or 1 2 4 5): ')))
                print(f'{submenu.last_return}\ntime: {submenu.runtime}s\n\n')
            except ValueError:
                print('Array above contains non integers.')
    else:
        submenu()


def main():
    ui = menu_init()
    while 1:
        try:
            exec_order(*ui.show_menu()
                       .prompt()
                       .get_input()
                       .parse_order())
        except NotImplementedError:
            print(f'Requested functionality is not implemented.')
    return 0


if __name__ == '__main__':
    exit(main())
