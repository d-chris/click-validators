import sys
from pathlib import Path

import click
import pytest
from click.testing import CliRunner

import clicktypes


@pytest.mark.parametrize(
    "value,kwargs,expected",
    [
        [
            ("python"),
            {
                "resolve_path": True,
                "executable": True,
            },
            0,
        ],
        [
            ("python2"),
            {
                "resolve_path": True,
                "executable": True,
            },
            2,
        ],
        [
            ("python"),
            {},
            1,
        ],
        [
            (Path(sys.executable).as_posix()),
            {},
            0,
        ],
    ],
    ids=repr,
)
def test_path(value, kwargs, expected):

    @click.command(name="path", help="path validator")
    @click.argument(
        "path",
        type=clicktypes.Path(**kwargs),
    )
    def cli(path: Path) -> None:

        if path.is_file():
            click.echo(f"valid {path=}")
        else:
            click.echo(f"invalid {path=}", err=True)
            raise SystemExit(1)

    runner = CliRunner()
    result = runner.invoke(cli, value)
    assert result.exit_code == expected
