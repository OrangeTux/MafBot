from functools import wraps

from mafbot.authentication import login


def get(query):
    """ Decorator to retrieve a page and if needed, log in.

    Args:
        query: The query string of the url.
    """
    from mafbot import driver

    def outer(f):
        @wraps(f)
        def inner(*args, **kwargs):
            url = 'http://www.maffiaworld.nl' + query
            driver.get(url)

            if 'Inloggen' in driver.title:
                login()

            driver.get(url)
            return f(*args, **kwargs)
        return inner
    return outer
