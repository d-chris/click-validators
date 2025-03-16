import functools
from typing import Callable, Type

import click


def click_validatortype(func: Callable[..., bool]) -> Type[click.ParamType]:

    cls_name = f"{func.__name__.capitalize()}ValidatorType"

    def __init__(self, **kwargs):
        super(click.ParamType, self).__init__()
        self._func = functools.partial(func, **kwargs)

    def convert(self, value, param, ctx):
        if self._func(value) is not True:
            self.fail(repr(value), param, ctx)
        return value

    return type(
        cls_name,
        (click.ParamType,),
        {
            "name": func.__name__,
            "__init__": __init__,
            "convert": convert,
            "__doc__": func.__doc__,
        },
    )
