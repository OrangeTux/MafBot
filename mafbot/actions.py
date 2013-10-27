from mafbot.utils import get, captcha
from mafbot import driver

@get('/crimes')
@captcha
def do_crime(option=1):
    xpath = '//table[@class="content_table"]//input[@value="%s"]' % option
    crime = driver.find_element_by_xpath(xpath)
    crime.click()


@get('/cars/steal')
@captcha
def steal_car(option=1):
    xpath = '//table[@class="content_table"]//input[@value="%s"]' % option
    crime = driver.find_element_by_xpath(xpath)
    crime.click()
