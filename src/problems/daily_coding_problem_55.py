from hashlib import sha256
from typing import Optional


class UrlShortener:
    """
    Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url.
    If no such shortened string exists, return null.

    Hint: What if we enter the same URL twice?
    """

    def __init__(self) -> None:
        self.url_map = {}

    def shorten(self, url: str) -> str:
        shortened = self._do_shorten(url)
        if shortened not in self.url_map:
            self.url_map[shortened] = url
        return shortened

    def _do_shorten(self, url):
        return sha256(url.encode()).hexdigest()[:6]

    def restore(self, shortened: str) -> Optional[str]:
        return self.url_map.get(shortened, None)
