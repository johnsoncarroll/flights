import os
from abc import ABC, abstractmethod

from ..querying import Query

try:
    import dotenv  # pyright: ignore [reportMissingImports]; pip install python-dotenv

    dotenv.load_dotenv()  # pyright: ignore [reportUnknownMemberType]

except ModuleNotFoundError:
    pass


class Integration(ABC):
    """Represents an integration."""

    @abstractmethod
    def fetch_html(self, q: Query | str, /) -> str:
        """Fetch the flights page HTML from a query.

        Args:
            q: The query.
        """
        raise NotImplementedError


def get_env(k: str, /) -> str:
    """(utility) Get environment variable.

    If nothing found, raises an error.

    Returns:
        str: The value.
    """
    try:
        return os.environ[k]
    except KeyError:
        raise OSError(f"could not find environment variable: {k!r}")
