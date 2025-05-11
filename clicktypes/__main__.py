import inspect
from pathlib import Path
from typing import Any, Callable, Dict, List

import black
import jinja2
import validators


def overload_info(func: Callable) -> Dict[str, Any]:
    """inspect function and return name, params and docstring."""

    sig = inspect.signature(func)

    param_lst: List[str] = []
    kwargs = False
    for param in sig.parameters.values():
        if param.name == "value":
            continue
        if callable(param.default):
            kwargs = True
            continue

        param_lst.append(str(param))
    else:
        if kwargs:
            param_lst.append("**kwargs")

    params = ",".join(param_lst)
    params = (params.rstrip(",") + ",") if params else ""

    doc = inspect.getdoc(func) or ""
    docstring, *_ = doc.split("\n", maxsplit=1)

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


def main() -> None:
    """Generate the __init__.py file."""

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader("templates"),
        autoescape=jinja2.select_autoescape(["py", "md"]),
        keep_trailing_newline=True,
    )

    info = validators_info()

    for file in map(
        Path,
        (
            "clicktypes/__init__.py",
            "README.md",
        ),
    ):
        try:
            template = env.get_template(file.name + ".jinja2")
            content = template.render(
                validators=info,
            )

            if file.suffix == ".py":
                content = black.format_file_contents(
                    content,
                    fast=False,
                    mode=black.FileMode(),
                )

            file.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"Error {file}: {e}")
            continue
        else:
            print(f"Generated {file}")


if __name__ == "__main__":
    main()
