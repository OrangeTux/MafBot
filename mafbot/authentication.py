import sys

from mafbot import driver, logger

try:
    from mafbot.conf import username, password
except ImportError:
    logger.error('Username and/or password are not defined in '
                 'mafboot/config.py')
    sys.exit()


def login():
    """ Login to the website. """
    form_fields = driver.find_elements_by_xpath('//form[@id="lf"]/input')

    form_fields[0].send_keys(username)
    form_fields[1].send_keys(password)

    form_fields[2].click()

    if 'Inloggen' in driver.title:
        logger.error('Fatal: Could not log in. Are username and password '
                     'correct?')
        sys.exit()
