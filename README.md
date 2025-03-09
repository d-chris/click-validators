# click-validators

---

Additional `click` parameter types are built on top of the `validators` library, providing a wide range of validation options for various data types, including email addresses, IP addresses, credit card numbers, and more. This package simplifies the process of adding robust validation to your Click-based CLI applications.

- `clicktypes.amex()`
- `clicktypes.base16()`
- `clicktypes.base32()`
- `clicktypes.base58()`
- `clicktypes.base64()`
- `clicktypes.between()`
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
- `clicktypes.length()`
- `clicktypes.mac_address()`
- `clicktypes.mastercard()`
- `clicktypes.md5()`
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

## Usage

import the module `clicktypes` and use the validators as types in click commands.

```python
import click

import clicktypes


@click.command(
    help=clicktypes.email.__doc__.split("\n", maxsplit=1)[0],
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

## Dependencies

[![PyPI - click](https://img.shields.io/pypi/v/click?logo=pypi&logoColor=white&label=click)](https://pypi.org/project/click/)
[![PyPI - validators](https://img.shields.io/pypi/v/validators?logo=pypi&logoColor=white&label=validators)](https://pypi.org/project/validators/)

---
