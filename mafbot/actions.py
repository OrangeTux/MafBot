from mafbot.utils import get, click_captcha
from mafbot import driver

@get('/crimes')
def do_crime():
    crime = driver.find_element_by_xpath('//table[@class="content_table"]//input[@value="1"]')
    crime.click()

    click_captcha()
