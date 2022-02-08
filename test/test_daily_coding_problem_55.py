from problems.daily_coding_problem_55 import UrlShortener


def test_shortening():
    url_shortener = UrlShortener()
    url = "https://pl.wikipedia.org/wiki/Friedrich_Nietzsche"
    shortened = url_shortener.shorten(url)
    assert len(shortened) == 6
    unshortened = url_shortener.restore(shortened)
    assert url == unshortened


def test_restoring_non_existing():
    url_shortener = UrlShortener()
    unshortened = url_shortener.restore("f8eioh")
    assert unshortened == None
