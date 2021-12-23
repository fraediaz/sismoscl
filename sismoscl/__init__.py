# type: ignore[attr-defined]
"""Sismos ocurridos en Chile, casi en tiempo real"""

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


from .sismos import sismos

version: str = get_version()
