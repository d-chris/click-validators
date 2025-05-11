"""
.. include:: ../README.md
"""

from typing import Optional

import click
import validators

from .decorator import click_validatortype


def amex() -> click.ParamType:
    """
    Return whether or not given value is a valid American Express card number.

    Returns a `click.ParamType` instance which wraps `validators.amex`.
    """
    return click_validatortype(validators.amex)()


def base16() -> click.ParamType:
    """
    Return whether or not given value is a valid base16 encoding.

    Returns a `click.ParamType` instance which wraps `validators.base16`.
    """
    return click_validatortype(validators.base16)()


def base32() -> click.ParamType:
    """
    Return whether or not given value is a valid base32 encoding.

    Returns a `click.ParamType` instance which wraps `validators.base32`.
    """
    return click_validatortype(validators.base32)()


def base58() -> click.ParamType:
    """
    Return whether or not given value is a valid base58 encoding.

    Returns a `click.ParamType` instance which wraps `validators.base58`.
    """
    return click_validatortype(validators.base58)()


def base64() -> click.ParamType:
    """
    Return whether or not given value is a valid base64 encoding.

    Returns a `click.ParamType` instance which wraps `validators.base64`.
    """
    return click_validatortype(validators.base64)()


def bsc_address() -> click.ParamType:
    """
    Return whether or not given value is a valid binance smart chain address.

    Returns a `click.ParamType` instance which wraps `validators.bsc_address`.
    """
    return click_validatortype(validators.bsc_address)()


def btc_address() -> click.ParamType:
    """
    Return whether or not given value is a valid bitcoin address.

    Returns a `click.ParamType` instance which wraps `validators.btc_address`.
    """
    return click_validatortype(validators.btc_address)()


def calling_code() -> click.ParamType:
    """
    Validates given calling code.

    Returns a `click.ParamType` instance which wraps `validators.calling_code`.
    """
    return click_validatortype(validators.calling_code)()


def card_number() -> click.ParamType:
    """
    Return whether or not given value is a valid generic card number.

    Returns a `click.ParamType` instance which wraps `validators.card_number`.
    """
    return click_validatortype(validators.card_number)()


def country_code(
    *,
    iso_format: str = "auto",
    ignore_case: bool = False,
) -> click.ParamType:
    """
    Validates given country code.

    Returns a `click.ParamType` instance which wraps `validators.country_code`.
    """
    return click_validatortype(validators.country_code)(**locals())


def cron() -> click.ParamType:
    """
    Return whether or not given value is a valid cron string.

    Returns a `click.ParamType` instance which wraps `validators.cron`.
    """
    return click_validatortype(validators.cron)()


def currency(
    *,
    skip_symbols: bool = True,
    ignore_case: bool = False,
) -> click.ParamType:
    """
    Validates given currency code.

    Returns a `click.ParamType` instance which wraps `validators.currency`.
    """
    return click_validatortype(validators.currency)(**locals())


def cusip() -> click.ParamType:
    """
    Return whether or not given value is a valid CUSIP.

    Returns a `click.ParamType` instance which wraps `validators.cusip`.
    """
    return click_validatortype(validators.cusip)()


def diners() -> click.ParamType:
    """
    Return whether or not given value is a valid Diners Club card number.

    Returns a `click.ParamType` instance which wraps `validators.diners`.
    """
    return click_validatortype(validators.diners)()


def discover() -> click.ParamType:
    """
    Return whether or not given value is a valid Discover card number.

    Returns a `click.ParamType` instance which wraps `validators.discover`.
    """
    return click_validatortype(validators.discover)()


def domain(
    *,
    consider_tld: bool = False,
    rfc_1034: bool = False,
    rfc_2782: bool = False,
) -> click.ParamType:
    """
    Return whether or not given value is a valid domain.

    Returns a `click.ParamType` instance which wraps `validators.domain`.
    """
    return click_validatortype(validators.domain)(**locals())


def email(
    *,
    ipv6_address: bool = False,
    ipv4_address: bool = False,
    simple_host: bool = False,
    rfc_1034: bool = False,
    rfc_2782: bool = False,
) -> click.ParamType:
    """
    Validate an email address.

    Returns a `click.ParamType` instance which wraps `validators.email`.
    """
    return click_validatortype(validators.email)(**locals())


def es_cif() -> click.ParamType:
    """
    Validate a Spanish CIF.

    Returns a `click.ParamType` instance which wraps `validators.es_cif`.
    """
    return click_validatortype(validators.es_cif)()


def es_doi() -> click.ParamType:
    """
    Validate a Spanish DOI.

    Returns a `click.ParamType` instance which wraps `validators.es_doi`.
    """
    return click_validatortype(validators.es_doi)()


def es_nie() -> click.ParamType:
    """
    Validate a Spanish NIE.

    Returns a `click.ParamType` instance which wraps `validators.es_nie`.
    """
    return click_validatortype(validators.es_nie)()


def es_nif() -> click.ParamType:
    """
    Validate a Spanish NIF.

    Returns a `click.ParamType` instance which wraps `validators.es_nif`.
    """
    return click_validatortype(validators.es_nif)()


def eth_address() -> click.ParamType:
    """
    Return whether or not given value is a valid ethereum address.

    Returns a `click.ParamType` instance which wraps `validators.eth_address`.
    """
    return click_validatortype(validators.eth_address)()


def fi_business_id() -> click.ParamType:
    """
    Validate a Finnish Business ID.

    Returns a `click.ParamType` instance which wraps `validators.fi_business_id`.
    """
    return click_validatortype(validators.fi_business_id)()


def fi_ssn(
    *,
    allow_temporal_ssn: bool = True,
) -> click.ParamType:
    """
    Validate a Finnish Social Security Number.

    Returns a `click.ParamType` instance which wraps `validators.fi_ssn`.
    """
    return click_validatortype(validators.fi_ssn)(**locals())


def fr_department() -> click.ParamType:
    """
    Validate a french department number.

    Returns a `click.ParamType` instance which wraps `validators.fr_department`.
    """
    return click_validatortype(validators.fr_department)()


def fr_ssn() -> click.ParamType:
    """
    Validate a french Social Security Number.

    Returns a `click.ParamType` instance which wraps `validators.fr_ssn`.
    """
    return click_validatortype(validators.fr_ssn)()


def hostname(
    *,
    skip_ipv6_addr: bool = False,
    skip_ipv4_addr: bool = False,
    may_have_port: bool = True,
    maybe_simple: bool = True,
    consider_tld: bool = False,
    private: Optional[bool] = None,
    rfc_1034: bool = False,
    rfc_2782: bool = False,
) -> click.ParamType:
    """
    Return whether or not given value is a valid hostname.

    Returns a `click.ParamType` instance which wraps `validators.hostname`.
    """
    return click_validatortype(validators.hostname)(**locals())


def iban() -> click.ParamType:
    """
    Return whether or not given value is a valid IBAN code.

    Returns a `click.ParamType` instance which wraps `validators.iban`.
    """
    return click_validatortype(validators.iban)()


def ind_aadhar() -> click.ParamType:
    """
    Validate an indian aadhar card number.

    Returns a `click.ParamType` instance which wraps `validators.ind_aadhar`.
    """
    return click_validatortype(validators.ind_aadhar)()


def ind_pan() -> click.ParamType:
    """
    Validate a pan card number.

    Returns a `click.ParamType` instance which wraps `validators.ind_pan`.
    """
    return click_validatortype(validators.ind_pan)()


def ipv4(
    *,
    cidr: bool = True,
    strict: bool = False,
    private: Optional[bool] = None,
    host_bit: bool = True,
) -> click.ParamType:
    """
    Returns whether a given value is a valid IPv4 address.

    Returns a `click.ParamType` instance which wraps `validators.ipv4`.
    """
    return click_validatortype(validators.ipv4)(**locals())


def ipv6(
    *,
    cidr: bool = True,
    strict: bool = False,
    host_bit: bool = True,
) -> click.ParamType:
    """
    Returns if a given value is a valid IPv6 address.

    Returns a `click.ParamType` instance which wraps `validators.ipv6`.
    """
    return click_validatortype(validators.ipv6)(**locals())


def isin() -> click.ParamType:
    """
    Return whether or not given value is a valid ISIN.

    Returns a `click.ParamType` instance which wraps `validators.isin`.
    """
    return click_validatortype(validators.isin)()


def jcb() -> click.ParamType:
    """
    Return whether or not given value is a valid JCB card number.

    Returns a `click.ParamType` instance which wraps `validators.jcb`.
    """
    return click_validatortype(validators.jcb)()


def mac_address() -> click.ParamType:
    """
    Return whether or not given value is a valid MAC address.

    Returns a `click.ParamType` instance which wraps `validators.mac_address`.
    """
    return click_validatortype(validators.mac_address)()


def mastercard() -> click.ParamType:
    """
    Return whether or not given value is a valid Mastercard card number.

    Returns a `click.ParamType` instance which wraps `validators.mastercard`.
    """
    return click_validatortype(validators.mastercard)()


def md5() -> click.ParamType:
    """
    Return whether or not given value is a valid MD5 hash.

    Returns a `click.ParamType` instance which wraps `validators.md5`.
    """
    return click_validatortype(validators.md5)()


def mir() -> click.ParamType:
    """
    Return whether or not given value is a valid Mir card number.

    Returns a `click.ParamType` instance which wraps `validators.mir`.
    """
    return click_validatortype(validators.mir)()


def ru_inn() -> click.ParamType:
    """
    Validate a Russian INN (Taxpayer Identification Number).

    Returns a `click.ParamType` instance which wraps `validators.ru_inn`.
    """
    return click_validatortype(validators.ru_inn)()


def sedol() -> click.ParamType:
    """
    Return whether or not given value is a valid SEDOL.

    Returns a `click.ParamType` instance which wraps `validators.sedol`.
    """
    return click_validatortype(validators.sedol)()


def sha1() -> click.ParamType:
    """
    Return whether or not given value is a valid SHA1 hash.

    Returns a `click.ParamType` instance which wraps `validators.sha1`.
    """
    return click_validatortype(validators.sha1)()


def sha224() -> click.ParamType:
    """
    Return whether or not given value is a valid SHA224 hash.

    Returns a `click.ParamType` instance which wraps `validators.sha224`.
    """
    return click_validatortype(validators.sha224)()


def sha256() -> click.ParamType:
    """
    Return whether or not given value is a valid SHA256 hash.

    Returns a `click.ParamType` instance which wraps `validators.sha256`.
    """
    return click_validatortype(validators.sha256)()


def sha384() -> click.ParamType:
    """
    Return whether or not given value is a valid SHA384 hash.

    Returns a `click.ParamType` instance which wraps `validators.sha384`.
    """
    return click_validatortype(validators.sha384)()


def sha512() -> click.ParamType:
    """
    Return whether or not given value is a valid SHA512 hash.

    Returns a `click.ParamType` instance which wraps `validators.sha512`.
    """
    return click_validatortype(validators.sha512)()


def slug() -> click.ParamType:
    """
    Validate whether or not given value is valid slug.

    Returns a `click.ParamType` instance which wraps `validators.slug`.
    """
    return click_validatortype(validators.slug)()


def trx_address() -> click.ParamType:
    """
    Return whether or not given value is a valid tron address.

    Returns a `click.ParamType` instance which wraps `validators.trx_address`.
    """
    return click_validatortype(validators.trx_address)()


def unionpay() -> click.ParamType:
    """
    Return whether or not given value is a valid UnionPay card number.

    Returns a `click.ParamType` instance which wraps `validators.unionpay`.
    """
    return click_validatortype(validators.unionpay)()


def url(
    *,
    skip_ipv6_addr: bool = False,
    skip_ipv4_addr: bool = False,
    may_have_port: bool = True,
    simple_host: bool = False,
    strict_query: bool = True,
    consider_tld: bool = False,
    private: Optional[bool] = None,
    rfc_1034: bool = False,
    rfc_2782: bool = False,
    **kwargs,
) -> click.ParamType:
    """
    Return whether or not given value is a valid URL.

    Returns a `click.ParamType` instance which wraps `validators.url`.
    """
    return click_validatortype(validators.url)(**locals())


def uuid() -> click.ParamType:
    """
    Return whether or not given value is a valid UUID-v4 string.

    Returns a `click.ParamType` instance which wraps `validators.uuid`.
    """
    return click_validatortype(validators.uuid)()


def visa() -> click.ParamType:
    """
    Return whether or not given value is a valid Visa card number.

    Returns a `click.ParamType` instance which wraps `validators.visa`.
    """
    return click_validatortype(validators.visa)()


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
    "mir",
    "ru_inn",
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
