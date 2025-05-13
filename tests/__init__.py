import inspect
import re
from typing import Generator, Tuple

import validators

import clicktypes


def docstrings() -> Generator[str, None, None]:
    """docstrings from all clicktypes validators."""

    yield from (
        inspect.getdoc(getattr(validators, validator)) or ""
        for validator in clicktypes.__all__
        if validator not in ("base58", "country_code")
    )


def testdata(doc: str) -> Generator[Tuple[str, str, int], None, None]:

    for match in re.findall(
        r">>> (\w+)\(\'(.*?)\'\)$\s+(.*?)$",
        doc,
        re.MULTILINE,
    ):
        yield (match[0], match[1], 0 if match[2] == "True" else 2)


def validator_data():
    for doc in docstrings():
        for validator, value, expected in testdata(doc):
            yield (validator, value, {}, expected)
