# Bazsalya András Vizsgaremek Feladat: New Data
# -Regisztráció  (sign_up_func(usern, email, pwd, result1)
#  Érvényes:    TC1-1-001-5
#  Érvénytelen: TC1-0-001-5
# -Bejelentkezés (login_func(email, pwd, logged_in, e_result))
#  Érvényes:    TC2-1-001-5
#  Érvénytelen: TC2-0-001-5
# -Adatkezelési nyilatkozat használata
#  TC3-001
# -Adatok listázása
#  TC4-001
# -Több oldalas lista bejárása
#  TC5-001
# -Új adat bevitel
#  TC6-001
# -Ismételt és sorozatos adatbevitel adatforrásból (new_article_func(uzenetszam))
#  TC7-001
# -Meglévő adat módosítás (your_settings_func())
#  TC8-001
# -Adat vagy adatok törlése
#  TC9-001
# -Adatok lementése felületről
#  TC10-001
# -Kijelentkezés
#  TC11-001

# Már megvan:
# Érvényes Felhasználók regisztrációja (Sign up/register TC1-5 + logout)
# Hibás adatú regisztrációk
# Hibás bejelentkezések (login TC1-7)


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from pprint import pprint
import csv
import random
import string
import time

# def test_c_new_data_and_modify():
# egységesen állítható time.sleep
dly = 0  # késleltetés korábbi(0) vagy egységes(!=0)
ts = 3
i = 0
Y = "Head"

if Y == "Headless":
    # A
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver.get("http://localhost:1667")
    # B
    # WebDriverManager.chromedriver().setup();
    # ChromeOptions chromeOptions = new ChromeOptions();
    # chromeOptions.addArguments("--no-sandbox");
    # chromeOptions.addArguments("--headless");
    # chromeOptions.addArguments("disable-gpu");
    # #C
    # from selenium.webdriver.chrome.options import Options
    # opt = Options()
    # opt.headless = True
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
else:
    # opt.headless = False
    # # In order for ChromeDriverManager to work you must pip install it in your own environment.
    driver = webdriver.Chrome(ChromeDriverManager().install())


# 4 beviteli mezőt tartalmaz: Email, Password, a kijelzett login ellenőrzéséhez, az elvárt üzenet assertnél URL1, 2
def login_func(email, pwd, logged_in, e_result):
    print("Login_func: Start")
    # Home: http://localhost:1667/#/
    ##############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    ##############
    sign_in_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="#/login"]')
    sign_in_button_p1_x.click()
    ##############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    ##############
    # Login: http://localhost:1667/#/login
    email_input_field = driver.find_element_by_xpath(
        '//fieldset/input[@class="form-control form-control-lg"][@placeholder="Email"]')  # URL1,2
    pwd_input_field = driver.find_element_by_xpath(
        '//fieldset/input[@class="form-control form-control-lg"][@placeholder="Password"]')  # URL1,2
    sign_in_button_p2_x = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    # email input field clear + set email param
    email_input_field.clear()
    email_input_field.send_keys(email)
    ##############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    ##############
    # pwd input field clear + set pwd param
    pwd_input_field.clear()
    pwd_input_field.send_keys(pwd)
    ##############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    ##############
    # sign_in email & pwd data
    sign_in_button_p2_x.click()
    ##############
    if dly == 0:
        time.sleep(4)
    else:
        time.sleep(ts)
    ##############
    # nincs logged_in esetén
    user_logged_in_text_x = driver.find_elements_by_xpath('/div[@class="swal-modal"][@role="dialog"]')
    if len(user_logged_in_text_x) != 0:
        result = driver.find_element_by_xpath('/div[@class="swal-text"]').text
        print("E_result: ", result)
        assert result == e_result
        # bezárja a figyelmeztető hiba ablakot
        # login_failed_ok_button_p3_x = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
        time.sleep(2)
        login_failed_ok_button_p3_x = driver.find_element_by_xpath(
            '/button[@class="swal-button swal-button--confirm"]')
        login_failed_ok_button_p3_x.click()
        # logged in esetén leellenőrzi, a

    #####################################
    # user_logged_in_text_x = driver.find_elements_by_xpath('/html/body/div[1]/nav/div/ul/li[4]/a')
    # if len(user_logged_in_text_x) == 0:
    #     # megnezi van-e figyelmeztető hiba ablak
    #     #login_failed_window_p3_x = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]')
    #     login_failed_window_p3_x = driver.find_elements_by_xpath('//div[@class="swal-modal"]')
    #     # ha van figyelmeztető hiba ablak összehasonlítja az e_result paraméter értékével
    #     if len(login_failed_window_p3_x) != 0:
    #         result = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]').text
    #         print("E_result: ", result)
    #         assert result == e_result
    #         # bezárja a figyelmeztető hiba ablakot
    #         #login_failed_ok_button_p3_x = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    #         login_failed_ok_button_p3_x = driver.find_element_by_xpath(
    #             '//button[@class="swal-button swal-button--confirm"]')
    #         login_failed_ok_button_p3_x.click()
    # # logged in esetén leellenőrzi, a
    # else:
    #     print("Logged_in: ", driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li[4]/a').text)
    #     assert driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li[4]/a').text == logged_in
    ##############################################
    # user_logged_in_text_x = driver.find_elements_by_xpath('/html/body/div[1]/nav/div/ul/li[4]/a')
    # if len(user_logged_in_text_x) == 0:
    # login_failed_window_x = driver.find_elements_by_xpath('//div[@class="swal-modal"]')
    # # ha fan felugró login Failed ablak
    # if len(login_failed_window_x) != 0:
    #     dialog_text = driver.find_element_by_xpath('//div[@class="swal-text"]').text
    #     print("Login_result: ", dialog_text)
    #     assert dialog_text == e_result
    #     # a felugró hibaablakot le kell OK-zni
    #     login_failed_ok_button_p3_x = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
    #     #login_failed_ok_button_p3_x = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    #     login_failed_ok_button_p3_x.click()
    ##############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    ##############


def logout_func():
    print("Logout_func: Start")
    log_out_button_p1_x = driver.find_elements_by_xpath('/html/body/div[1]/nav/div/ul/li[5]/a')
    if len(log_out_button_p1_x) != 0:
        log_out_button_p1_x = driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li[5]/a')
        log_out_button_p1_x.click()


# 3 beviteli mezőt tartalmaz: Username, Email, Password
def sign_up_func(usern, email, pwd, result):
    # Register (sign up): http://localhost:1667/#/register
    print("Sign_up_func: Start")
    ##############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    ##############
    sign_up_button_p1_x = driver.find_element_by_xpath('//li/a[@href="#/register"]')

    sign_up_button_p1_x.click()
    signup_text_usern_p2_x = driver.find_element_by_xpath(
        '//fieldset[@class="form-group"]/input[@placeholder="Username"]')
    signup_text_usern_p2_x.send_keys(usern)
    signup_text_email_p2_x = driver.find_element_by_xpath('//fieldset[@class="form-group"]/input[@placeholder="Email"]')
    signup_text_email_p2_x.send_keys(email)
    signup_text_pwd_p2_x = driver.find_element_by_xpath(
        '//fieldset[@class="form-group"]/input[@placeholder="Password"]')
    signup_text_pwd_p2_x.send_keys(pwd)
    signup_subm_btn_p2_x = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    signup_subm_btn_p2_x.click()
    ##############
    if dly == 0:
        time.sleep(4)
    else:
        time.sleep(ts)
    ##############
    welcome_reg_failed_window_x = driver.find_elements_by_xpath('//div[@class="swal-modal"]')
    dialog = driver.find_element_by_xpath('//div[@class="swal-text"]').text
    print("Reg_result: ", dialog)
    if dialog == "Email already taken.":
        if result == "Your registration was successful!":
            print(
                "Reg_result: Mivel az email cím már létezik és a beállítás hibátlan bevitelre vonatkozott, ezért az assert kihagyva!")
        else:
            print(
                "Reg_result: Mivel az email cím már létezik, a funkció igy nem vizsgálható, ezért az assert kihagyva!")
    else:
        assert driver.find_element_by_xpath('//div[@class="swal-text"]').text == result
    # ha fan felugró Reg Failed ablak
    if len(welcome_reg_failed_window_x) != 0:
        reg_failed_ok_btn_x = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
        reg_failed_ok_btn_x.click()


def your_settings_write_func(a, b, c, d, e):
    print("Your_settings_write_func: Start")
    # Your settings
    ##############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    ##############
    your_settings_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="#/settings"]')
    # your_settings_button_p1_x = driver.find_element_by_xpath('//a[@class="nav-link"][@href="#/settings"]')
    your_settings_button_p1_x.click()
    ##############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    ##############
    pict_url_field_x = driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]')
    user_name_field_x = driver.find_element_by_xpath('//input[@placeholder="Your username"]')
    short_about_you_field_x = driver.find_element_by_xpath('//textarea[@placeholder="Short bio about you"]')
    email_field_x = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    pwd_field_x = driver.find_element_by_xpath(
        '//input[@class="form-control form-control-lg"][@placeholder="Password"]')
    ###############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    ##############
    if a != '':
        pict_url_field_x.clear()
        pict_url_field_x.send_keys(a)
    if b != '':
        user_name_field_x.clear()
        user_name_field_x.send_keys(b)
    if c != '':
        short_about_you_field_x.clear()
        short_about_you_field_x.send_keys(c)
    if d != '':
        email_field_x.clear()
        email_field_x.send_keys(d)
    if e != '':
        pwd_field_x.clear()
        pwd_field_x.send_keys(e)
    ###############
    if dly == 0:
        time.sleep(5)
    else:
        time.sleep(ts)
    ###############
    updt_sett_button_x = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    print("Gomb: ", driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').text)
    updt_sett_button_x.click()
    ###############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    ###############
    update_pop_up_window_x = driver.find_elements_by_xpath('//div[@class="swal-modal"][@role="dialog"]')
    print("Dialog window: ", len(update_pop_up_window_x))
    if len(update_pop_up_window_x) != 0:
        x = driver.find_element_by_xpath('//div[@class="swal-modal"]/div[@class="swal-title"]').text
        print("Window message: ", x)
        assert x == "Update successful!"
        update2_pop_up_button_x = driver.find_element_by_xpath(
            '//button[@class="swal-button swal-button--confirm"]')
        update2_pop_up_button_x.click()
        print("Pop-up button: Clicked")


def your_settings_read_func(a, b, c, d):
    print("Your_settings_read_func: Start")
    # Your settings
    ##############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    ##############
    your_settings_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="#/settings"]')
    your_settings_button_p1_x.click()
    ##############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    ##############
    pict_url_field_x = driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]')
    user_name_field_x = driver.find_element_by_xpath('//input[@placeholder="Your username"]')
    short_about_you_field_x = driver.find_element_by_xpath('//textarea[@placeholder="Short bio about you"]')
    email_field_x = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    pwd_field_x = driver.find_element_by_xpath(
        '//input[@class="form-control form-control-lg"][@placeholder="Password"]')
    ###############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    ##############

    if a != "":
        d1 = pict_url_field_x.get_attribute('value')
        assert d1 == a
        print("URL of profile picture mező értéke:", d1)
    if b != "":
        d2 = user_name_field_x.get_attribute('value')
        assert d2 == b
        print("Your username értéke:", d2)
    if c != "":
        d3 = short_about_you_field_x.get_attribute('value')
        if dly == 0:
            time.sleep(3)
        else:
            time.sleep(ts)
        print("Short bio about you mező értéke:", d3)
        assert d3 == c
        if dly == 0:
            time.sleep(3)
        else:
            time.sleep(ts)
    if d != "":
        d4 = email_field_x.get_attribute('value')
        assert d4 == d
        print("Email mező értéke:", d4)
    ###############
    if dly == 0:
        time.sleep(5)
    else:
        time.sleep(ts)
    ###############
    # Home_button_x = driver.find_element_by_xpath('//html/body/div[1]/nav/div/ul/li[1]/a')
    Home_button_x = driver.find_element_by_xpath('//a[@class="nav-link"][@href="#/"]')
    # Home_button_x = driver.find_element_by_class_name('/html/body/div[1]/nav/div/ul/li[1]/a')
    print("Gomb: ", Home_button_x.text)
    Home_button_x.click()
    ###############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)


try:
    URL1 = "http://localhost:1667/#/"
    driver.get(URL1)

    #############
    if dly == 0:
        time.sleep(5)
    else:
        time.sleep(ts)
    ###############################################################################
    #    TESZTEK KEZDETE
    ###############################################################################
    # Érvényes Felhasználók regisztrációja (Sign up/register TC1-1-001-005 + logout)
    # sign_up_func(username, email, password, URL1: result)
    # print("1 db érvényes felhasználó regisztrációja")
    sign_up_func("Carol1", "carol1@example.com", "Ab123451", "Your registration was successful!")  #
    #############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)

    print("Felhasználó adatainak beállítása")
    # x felhasználó adatainak módosítása
    b1 = ""
    b2 = ""
    b3 = "Barmi erdekes rolam ..."
    b4 = ""
    b5 = ""
    # b1 = "https://barmi/boci-csoki.jpg"
    # b2 = "Carol1"
    # b3 = "Barmi erdekes rolam ..."
    # b4 = "carol1@example.com"
    # b5 = "Ab123451"
    # b5 = "Ab111111"
    your_settings_write_func(b1, b2, b3, b4, b5)
    #############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    #############
    logout_func()
    #############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    #############
    login_func("carol1@example.com", "Ab123451", "carol1", "")
    #############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    #############
    your_settings_read_func(b1, b2, b3, b4)
    print("Felhasználó adatainak beállítása")
    # x felhasználó adatainak módosítása
    c1 = ""
    c2 = ""
    c3 = "Semmi érdekeset nem tudok írni magamról ..."
    c4 = ""
    c5 = ""
    # c1 = "https://static.productionready.io/images/smiley-cyrus.jpg"
    # c2 = "Carol1"
    # c3 = "Semmi érdekeset nem tudok írni magamról ..."
    # c4 = "carol1@example.com"
    # c5 = "Ab123451"
    your_settings_write_func(c1, c2, c3, c4, c5)
    #############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    #############
    logout_func()
    #############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    #############
    login_func("carol1@example.com", "Ab123451", "carol1", "")
    #############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    #############
    your_settings_read_func(c1, c2, c3, c4)
    #############
    if dly == 0:
        time.sleep(3)
    else:
        time.sleep(ts)
    #############
    logout_func()

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    # pass
    driver.close()
    driver.quit()
