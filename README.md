# click-validators

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/click-validators)](https://pypi.org/project/click-validators/)
[![PyPI - Version](https://img.shields.io/pypi/v/click-validators)](https://pypi.org/project/click-validators/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/click-validators)](https://pypi.org/project/click-validators/)
[![PyPI - License](https://img.shields.io/pypi/l/click-validators)](https://raw.githubusercontent.com/d-chris/click-validators/main/LICENSE)
[![GitHub - Pytest](https://img.shields.io/github/actions/workflow/status/d-chris/click-validators/pytest.yml?logo=github&label=pytest)](https://github.com/d-chris/click-validators/actions/workflows/pytest.yml)
[![GitHub - Page](https://img.shields.io/website?url=https%3A%2F%2Fd-chris.github.io%2Fclick-validators&up_message=pdoc&logo=github&label=documentation)](https://d-chris.github.io/click-validators)
[![GitHub - Release](https://img.shields.io/github/v/tag/d-chris/click-validators?logo=github&label=github)](https://github.com/d-chris/click-validators)
[![codecov](https://codecov.io/gh/d-chris/click-validators/graph/badge.svg?token=WY062DFVTR)](https://codecov.io/gh/d-chris/click-validators)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://raw.githubusercontent.com/d-chris/click-validators/main/.pre-commit-config.yaml)

---

Additional `click` parameter types are built on top of the `validators` library, providing a wide range of validation options for various data types, including email addresses, IP addresses, credit card numbers, and more. This package simplifies the process of adding robust validation to your Click-based CLI applications.

- `clicktypes.amex()`
- `clicktypes.base16()`
- `clicktypes.base32()`
- `clicktypes.base58()`
- `clicktypes.base64()`
- `clicktypes.bsc_address()`
- `clicktypes.btc_address()`
- `clicktypes.calling_code()`
- `clicktypes.card_number()`
- `clicktypes.country_code()`
- `clicktypes.cron()`
- `clicktypes.currency()`
- `clicktypes.cusip()`
- `clicktypes.diners()`
- `clicktypes.discover()`
- `clicktypes.domain()`
- `clicktypes.email()`
- `clicktypes.es_cif()`
- `clicktypes.es_doi()`
- `clicktypes.es_nie()`
- `clicktypes.es_nif()`
- `clicktypes.eth_address()`
- `clicktypes.fi_business_id()`
- `clicktypes.fi_ssn()`
- `clicktypes.fr_department()`
- `clicktypes.fr_ssn()`
- `clicktypes.hostname()`
- `clicktypes.iban()`
- `clicktypes.ind_aadhar()`
- `clicktypes.ind_pan()`
- `clicktypes.ipv4()`
- `clicktypes.ipv6()`
- `clicktypes.isin()`
- `clicktypes.jcb()`
- `clicktypes.mac_address()`
- `clicktypes.mastercard()`
- `clicktypes.md5()`
- `clicktypes.mir()`
- `clicktypes.ru_inn()`
- `clicktypes.sedol()`
- `clicktypes.sha1()`
- `clicktypes.sha224()`
- `clicktypes.sha256()`
- `clicktypes.sha384()`
- `clicktypes.sha512()`
- `clicktypes.slug()`
- `clicktypes.trx_address()`
- `clicktypes.unionpay()`
- `clicktypes.url()`
- `clicktypes.uuid()`
- `clicktypes.visa()`

## Install

```cmd
pip install click-validators
```

for `clicktypes.eth_address()` validation, additional package `eth-hash[pycryptodome]>=0.7.0` is required.

[![PyPI - eth-hash](https://img.shields.io/pypi/v/eth-hash?logo=pypi&logoColor=white&label=eth-hash[pycryptodome])](https://pypi.org/project/eth-hash/)

```cmd
pip install click-validators[eth]
```

## Usage

import the module `clicktypes` and use the validators as types in click commands.

```python
import click

import clicktypes


@click.command(
    help="validate email address",
)
@click.argument(
    "email",
    type=clicktypes.email(),
)
def main(email):
    click.echo(f"valid {email=}")


if __name__ == "__main__":
    main()
```

### Example

```cmd
$ main.py fu@bar.com

valid email='fu@bar.com'
```

```cmd
$ main.py fu.bar.com

Usage: main.py [OPTIONS] EMAIL
Try 'main.py --help' for help.

Error: Invalid value for 'EMAIL': 'fu.bar.com'.
```

## Dependencies

[![PyPI - click](https://img.shields.io/pypi/v/click?logo=pypi&logoColor=white&label=click)](https://pypi.org/project/click/)
[![PyPI - validators](https://img.shields.io/pypi/v/validators?logo=pypi&logoColor=white&label=validators)](https://pypi.org/project/validators/)

---
