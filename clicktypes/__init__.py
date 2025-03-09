"""
.. include:: ../README.md
"""

from typing import overload

import click
import validators

from .decorator import click_validatortype


@overload
def amex() -> click.ParamType:
    """Return whether or not given value is a valid American Express card number."""
    ...


amex = click_validatortype(validators.amex)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.amex` function."""


@overload
def base16() -> click.ParamType:
    """Return whether or not given value is a valid base16 encoding."""
    ...


base16 = click_validatortype(validators.base16)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.base16` function."""


@overload
def base32() -> click.ParamType:
    """Return whether or not given value is a valid base32 encoding."""
    ...


base32 = click_validatortype(validators.base32)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.base32` function."""


@overload
def base58() -> click.ParamType:
    """Return whether or not given value is a valid base58 encoding."""
    ...


base58 = click_validatortype(validators.base58)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.base58` function."""


@overload
def base64() -> click.ParamType:
    """Return whether or not given value is a valid base64 encoding."""
    ...


base64 = click_validatortype(validators.base64)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.base64` function."""


@overload
def bsc_address() -> click.ParamType:
    """Return whether or not given value is a valid binance smart chain address."""
    ...


bsc_address = click_validatortype(validators.bsc_address)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.bsc_address` function."""


@overload
def btc_address() -> click.ParamType:
    """Return whether or not given value is a valid bitcoin address."""
    ...


btc_address = click_validatortype(validators.btc_address)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.btc_address` function."""


@overload
def calling_code() -> click.ParamType:
    """Validates given calling code."""
    ...


calling_code = click_validatortype(validators.calling_code)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.calling_code` function."""


@overload
def card_number() -> click.ParamType:
    """Return whether or not given value is a valid generic card number."""
    ...


card_number = click_validatortype(validators.card_number)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.card_number` function."""


@overload
def country_code(iso_format="auto", ignore_case=False) -> click.ParamType:
    """Validates given country code."""
    ...


country_code = click_validatortype(validators.country_code)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.country_code` function."""


@overload
def cron() -> click.ParamType:
    """Return whether or not given value is a valid cron string."""
    ...


cron = click_validatortype(validators.cron)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.cron` function."""


@overload
def currency(skip_symbols=True, ignore_case=False) -> click.ParamType:
    """Validates given currency code."""
    ...


currency = click_validatortype(validators.currency)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.currency` function."""


@overload
def cusip() -> click.ParamType:
    """Return whether or not given value is a valid CUSIP."""
    ...


cusip = click_validatortype(validators.cusip)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.cusip` function."""


@overload
def diners() -> click.ParamType:
    """Return whether or not given value is a valid Diners Club card number."""
    ...


diners = click_validatortype(validators.diners)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.diners` function."""


@overload
def discover() -> click.ParamType:
    """Return whether or not given value is a valid Discover card number."""
    ...


discover = click_validatortype(validators.discover)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.discover` function."""


@overload
def domain(consider_tld=False, rfc_1034=False, rfc_2782=False) -> click.ParamType:
    """Return whether or not given value is a valid domain."""
    ...


domain = click_validatortype(validators.domain)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.domain` function."""


@overload
def email(
    ipv6_address=False,
    ipv4_address=False,
    simple_host=False,
    rfc_1034=False,
    rfc_2782=False,
) -> click.ParamType:
    """Validate an email address."""
    ...


email = click_validatortype(validators.email)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.email` function."""


@overload
def es_cif() -> click.ParamType:
    """Validate a Spanish CIF."""
    ...


es_cif = click_validatortype(validators.es_cif)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.es_cif` function."""


@overload
def es_doi() -> click.ParamType:
    """Validate a Spanish DOI."""
    ...


es_doi = click_validatortype(validators.es_doi)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.es_doi` function."""


@overload
def es_nie() -> click.ParamType:
    """Validate a Spanish NIE."""
    ...


es_nie = click_validatortype(validators.es_nie)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.es_nie` function."""


@overload
def es_nif() -> click.ParamType:
    """Validate a Spanish NIF."""
    ...


es_nif = click_validatortype(validators.es_nif)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.es_nif` function."""


@overload
def eth_address() -> click.ParamType:
    """Return whether or not given value is a valid ethereum address."""
    ...


eth_address = click_validatortype(validators.eth_address)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.eth_address` function."""


@overload
def fi_business_id() -> click.ParamType:
    """Validate a Finnish Business ID."""
    ...


fi_business_id = click_validatortype(validators.fi_business_id)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.fi_business_id` function."""


@overload
def fi_ssn(allow_temporal_ssn=True) -> click.ParamType:
    """Validate a Finnish Social Security Number."""
    ...


fi_ssn = click_validatortype(validators.fi_ssn)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.fi_ssn` function."""


@overload
def fr_department() -> click.ParamType:
    """Validate a french department number."""
    ...


fr_department = click_validatortype(validators.fr_department)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.fr_department` function."""


@overload
def fr_ssn() -> click.ParamType:
    """Validate a french Social Security Number."""
    ...


fr_ssn = click_validatortype(validators.fr_ssn)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.fr_ssn` function."""


@overload
def hostname(
    skip_ipv6_addr=False,
    skip_ipv4_addr=False,
    may_have_port=True,
    maybe_simple=True,
    consider_tld=False,
    private=None,
    rfc_1034=False,
    rfc_2782=False,
) -> click.ParamType:
    """Return whether or not given value is a valid hostname."""
    ...


hostname = click_validatortype(validators.hostname)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.hostname` function."""


@overload
def iban() -> click.ParamType:
    """Return whether or not given value is a valid IBAN code."""
    ...


iban = click_validatortype(validators.iban)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.iban` function."""


@overload
def ind_aadhar() -> click.ParamType:
    """Validate an indian aadhar card number."""
    ...


ind_aadhar = click_validatortype(validators.ind_aadhar)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.ind_aadhar` function."""


@overload
def ind_pan() -> click.ParamType:
    """Validate a pan card number."""
    ...


ind_pan = click_validatortype(validators.ind_pan)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.ind_pan` function."""


@overload
def ipv4(cidr=True, strict=False, private=None, host_bit=True) -> click.ParamType:
    """Returns whether a given value is a valid IPv4 address."""
    ...


ipv4 = click_validatortype(validators.ipv4)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.ipv4` function."""


@overload
def ipv6(cidr=True, strict=False, host_bit=True) -> click.ParamType:
    """Returns if a given value is a valid IPv6 address."""
    ...


ipv6 = click_validatortype(validators.ipv6)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.ipv6` function."""


@overload
def isin() -> click.ParamType:
    """Return whether or not given value is a valid ISIN."""
    ...


isin = click_validatortype(validators.isin)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.isin` function."""


@overload
def jcb() -> click.ParamType:
    """Return whether or not given value is a valid JCB card number."""
    ...


jcb = click_validatortype(validators.jcb)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.jcb` function."""


@overload
def mac_address() -> click.ParamType:
    """Return whether or not given value is a valid MAC address."""
    ...


mac_address = click_validatortype(validators.mac_address)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.mac_address` function."""


@overload
def mastercard() -> click.ParamType:
    """Return whether or not given value is a valid Mastercard card number."""
    ...


mastercard = click_validatortype(validators.mastercard)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.mastercard` function."""


@overload
def md5() -> click.ParamType:
    """Return whether or not given value is a valid MD5 hash."""
    ...


md5 = click_validatortype(validators.md5)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.md5` function."""


@overload
def sedol() -> click.ParamType:
    """Return whether or not given value is a valid SEDOL."""
    ...


sedol = click_validatortype(validators.sedol)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.sedol` function."""


@overload
def sha1() -> click.ParamType:
    """Return whether or not given value is a valid SHA1 hash."""
    ...


sha1 = click_validatortype(validators.sha1)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.sha1` function."""


@overload
def sha224() -> click.ParamType:
    """Return whether or not given value is a valid SHA224 hash."""
    ...


sha224 = click_validatortype(validators.sha224)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.sha224` function."""


@overload
def sha256() -> click.ParamType:
    """Return whether or not given value is a valid SHA256 hash."""
    ...


sha256 = click_validatortype(validators.sha256)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.sha256` function."""


@overload
def sha384() -> click.ParamType:
    """Return whether or not given value is a valid SHA384 hash."""
    ...


sha384 = click_validatortype(validators.sha384)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.sha384` function."""


@overload
def sha512() -> click.ParamType:
    """Return whether or not given value is a valid SHA512 hash."""
    ...


sha512 = click_validatortype(validators.sha512)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.sha512` function."""


@overload
def slug() -> click.ParamType:
    """Validate whether or not given value is valid slug."""
    ...


slug = click_validatortype(validators.slug)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.slug` function."""


@overload
def trx_address() -> click.ParamType:
    """Return whether or not given value is a valid tron address."""
    ...


trx_address = click_validatortype(validators.trx_address)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.trx_address` function."""


@overload
def unionpay() -> click.ParamType:
    """Return whether or not given value is a valid UnionPay card number."""
    ...


unionpay = click_validatortype(validators.unionpay)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.unionpay` function."""


@overload
def url(
    skip_ipv6_addr=False,
    skip_ipv4_addr=False,
    may_have_port=True,
    simple_host=False,
    strict_query=True,
    consider_tld=False,
    private=None,
    rfc_1034=False,
    rfc_2782=False,
) -> click.ParamType:
    """Return whether or not given value is a valid URL."""
    ...


url = click_validatortype(validators.url)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.url` function."""


@overload
def uuid() -> click.ParamType:
    """Return whether or not given value is a valid UUID-v4 string."""
    ...


uuid = click_validatortype(validators.uuid)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.uuid` function."""


@overload
def visa() -> click.ParamType:
    """Return whether or not given value is a valid Visa card number."""
    ...


visa = click_validatortype(validators.visa)
"""A custom parameter type derived from `click.types.ParamType` that uses the `validators.visa` function."""


__all__ = [
    "amex",
    "base16",
    "base32",
    "base58",
    "base64",
    "bsc_address",
    "btc_address",
    "calling_code",
    "card_number",
    "country_code",
    "cron",
    "currency",
    "cusip",
    "diners",
    "discover",
    "domain",
    "email",
    "es_cif",
    "es_doi",
    "es_nie",
    "es_nif",
    "eth_address",
    "fi_business_id",
    "fi_ssn",
    "fr_department",
    "fr_ssn",
    "hostname",
    "iban",
    "ind_aadhar",
    "ind_pan",
    "ipv4",
    "ipv6",
    "isin",
    "jcb",
    "mac_address",
    "mastercard",
    "md5",
    "sedol",
    "sha1",
    "sha224",
    "sha256",
    "sha384",
    "sha512",
    "slug",
    "trx_address",
    "unionpay",
    "url",
    "uuid",
    "visa",
]
