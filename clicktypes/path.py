from __future__ import annotations

import pathlib
import shutil
import typing as t

import click


class Path(click.Path):

    def __init__(
        self,
        *,
        exists: bool = False,
        file_okay: bool = True,
        dir_okay: bool = True,
        writable: bool = False,
        readable: bool = True,
        resolve_path: bool | str = False,
        allow_dash: bool = False,
        path_type: t.Optional[t.Type[t.Any]] = pathlib.Path,
        executable: bool = False,
    ):
        """@private"""
        super().__init__(
            exists=exists,
            file_okay=file_okay,
            dir_okay=dir_okay,
            writable=writable,
            readable=readable,
            resolve_path=resolve_path,
            allow_dash=allow_dash,
            path_type=path_type,
            executable=executable,
        )

    def convert(
        self,
        value: t.Any,
        param: t.Optional[click.Parameter],
        ctx: t.Optional[click.Context],
    ) -> t.Any:
        """@private"""
        try:
            if self.resolve_path and self.executable:
                value = pathlib.Path(value).resolve(strict=True)

        except FileNotFoundError:
            path = (
                pathlib.Path(self.resolve_path).resolve()
                if isinstance(self.resolve_path, str)
                else None
            )
            value = shutil.which(value, path=path) or value

        finally:
            return super().convert(value, param, ctx)
