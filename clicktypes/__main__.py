import inspect
from pathlib import Path
from typing import Any, Callable, Dict, List

import black
import jinja2
import validators


def overload_info(func: Callable) -> Dict[str, Any]:
    """inspect function and return name, params and docstring."""

    sig = inspect.signature(func)
    params = ", ".join(
        (
            f"{param.name} = {repr(param.default)}"
            if param.default is not param.empty
            else f"{param.name}"
        )
        for param in sig.parameters.values()
        if param.kind not in (param.VAR_POSITIONAL, param.VAR_KEYWORD)
        and param.name != "value"  # noqa: W503
    )
    docstring, _ = inspect.getdoc(func).split("\n", maxsplit=1) or ("", None)

    return {
        "name": func.__name__,
        "params": params,
        "docstring": docstring,
    }


def validators_info() -> List[Dict[str, Any]]:
    """Return a list of dictionaries with information about the validators."""
    return sorted(
        (
            overload_info(getattr(validators, validator))
            for validator in filter(
                lambda f: (
                    f
                    not in (
                        "ValidationError",
                        "validator",
                        "between",
                        "length",
                    )
                ),
                validators.__all__,
            )
        ),
        key=lambda d: d["name"],
    )


def init() -> None:
    """Generate the __init__.py file."""

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("templates"),
        autoescape=jinja2.select_autoescape(["py"]),
    )

    file = Path("clicktypes/__init__.py")

    template = env.get_template(file.name + ".jinja2")

    content = black.format_file_contents(
        template.render(
            validators=validators_info(),
        ),
        fast=False,
        mode=black.FileMode(),
    )

    file.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    init()
