import inspect
import re
from typing import Generator, Tuple

import validators

import clicktypes


def docstrings() -> Generator[str, None, None]:
    """docstrings from all clicktypes validators."""

    yield from (
        inspect.getdoc(getattr(validators, validator))
        for validator in clicktypes.__all__
        if validator not in ("base58", "country_code")
    )


def testdata(doc: str) -> Generator[Tuple[str, str, int], None, None]:

    for match in re.findall(
        r">>> (\w+)\(\'(.*?)\'\)$\s+# \w+: (.*?)$",
        doc,
        re.MULTILINE,
    ):
        yield (match[0], match[1], 0 if match[2] == "True" else 2)


def validator_data():
    for doc in docstrings():
        for validator, value, expected in testdata(doc):
            yield (validator, value, {}, expected)

    for data, result in [
        ("cUSECaVvAiV3srWbFRvVPzm5YzcXJwPSwZfE7veYPHoXmR9h6YMQ", 0),
        ("18KToMF5ckjXBYt2HAj77qsG3GPeej3PZn", 0),
        ("n4FFXRNNEW1aA2WPscSuzHTCjzjs4TVE2Z", 0),
        ("38XzQ9dPGb1uqbZsjPtUajp7omy8aefjqj", 0),
        ("ThisIsAReallyLongStringThatIsDefinitelyNotBase58Encoded", 2),
        ("abcABC!@#", 2),
        ("InvalidBase58!", 2),
    ]:
        yield ("base58", data, {}, result)

    for data, kwarg, expected in [
        ("ISR", "auto", 0),
        ("US", "alpha2", 0),
        ("USA", "alpha3", 0),
        ("840", "numeric", 0),
        ("", "auto", 2),
        ("123456", "auto", 2),
        ("XY", "alpha2", 2),
        ("PPP", "alpha3", 2),
        ("123", "numeric", 2),
        ("us", "auto", 2),
        ("uSa", "auto", 2),
        ("US ", "auto", 2),
        ("U.S", "auto", 2),
        ("1ND", "unknown", 2),
    ]:
        yield ("country_code", data, {"iso_format": kwarg}, expected)
