#! /bin/env python3
from time import time_ns


class Menu:
    def __init__(self, prompt='~>'):
        self._prompt: str = prompt
        self._input: str = ''
        self._choices: {str: (str, callable)} = {}

    @property
    def menu_dict(self):
        return self._choices

    @property
    def last_input(self):
        return self._input

    def prompt(self):
        print(self._prompt, end=' ')
        return self

    def get_input(self, message=''):
        self._input = input(message) \
            .strip() \
            .lower()
        return self

    def clear_last_input(self):
        self._input = ''
        return self

    def add_entry(self, key: str, desc: str, func):
        self._choices[key] = (desc, func)
        return self

    def show_menu(self):
        print(
            '\n'.join((f'{k}: {v}' for k, (v, _) in self._choices.items()))
        )
        return self

    def parse_order(self):
        if self._input:
            order = self._input.split()[0]
            if order in self._choices:
                return self._choices[order][1], self._input[len(order):]
            else:
                raise NotImplementedError(f'Requested functionality "{order}" is not implemented.')

    def show_return_val(self):
        return self


class SubMenu:
    def __init__(self, func):
        self._func = func
        self._return = None
        self._args = None
        self._kwargs = None
        self._runtime = 0

    def __call__(self, *args, **kwargs):
        if self._args and self._kwargs:
            args, kwargs = self._args, self._kwargs
        elif self._args:
            args, kwargs = self._args, kwargs
        elif self._kwargs:
            args, kwargs = args, self._kwargs
        else:
            args, kwargs = args, kwargs

        self._runtime = time_ns()
        self._return = self._func(*args, **kwargs)
        self._runtime = (time_ns() - self._runtime) / 10e8

        return self

    @property
    def last_return(self):
        return self._return

    @property
    def args(self):
        return self._args

    @property
    def kwargs(self):
        return self._kwargs

    @property
    def runtime(self):
        return self._runtime

    @args.setter
    def args(self, argv):
        self._args = argv

    @kwargs.setter
    def kwargs(self, kw):
        self._kwargs = kw

    @args.deleter
    def args(self):
        self._args = None

    @kwargs.deleter
    def kwargs(self):
        self._kwargs = None


if __name__ == '__main__':
    raise Warning('Module is not meant to be executed directly.')
