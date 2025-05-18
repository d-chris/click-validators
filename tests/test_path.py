import click
from click.testing import CliRunner

import clicktypes


@click.command(name="path", help="path validator")
@click.argument(
    "path",
    type=clicktypes.Path(resolve_path=True, executable=True),
)
def cli(path):

    if path.exists():
        click.echo(f"valid {path=}")
    else:
        click.echo(f"invalid {path=}", err=True)
        raise SystemExit(1)


def test_path():

    runner = CliRunner()
    result = runner.invoke(cli, ["python"])
    assert result.exit_code == 0


if __name__ == "__main__":
    cli()
