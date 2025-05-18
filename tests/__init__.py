import ast
import inspect
import re
from typing import Generator
from typing import Tuple

import validators

import clicktypes


def docstrings() -> Generator[str, None, None]:
    """docstrings from all clicktypes validators."""

    for validator in clicktypes.__all__:
        try:
            func = getattr(validators, validator)
        except AttributeError:
            continue

        yield inspect.getdoc(func) or ""


def testdata(doc: str) -> Generator[Tuple[str, str, int], None, None]:

    def parse_call(s: str):
        tree = ast.parse(s.strip(), mode="eval")
        if not isinstance(tree.body, ast.Call):
            raise ValueError("Not a function call")
        func_name = (
            ast.unparse(tree.body.func)
            if hasattr(ast, "unparse")
            else tree.body.func.id  # type: ignore[attr-defined]
        )
        args = [ast.literal_eval(arg) for arg in tree.body.args]
        kwargs = {kw.arg: ast.literal_eval(kw.value) for kw in tree.body.keywords}
        return func_name, tuple(args), kwargs

    for match in re.findall(
        r">>>\s*(\w+\(.*?\))$\s+(.*?)$",
        doc,
        re.MULTILINE,
    ):
        yield (*parse_call(match[0]), 0 if match[1] == "True" else 2)


def validator_data():
    for doc in docstrings():
        yield from testdata(doc)
