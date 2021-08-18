# Bazsalya András Vizsgaremek Feladat Adatkezelési nyilatkozat használata
# -Regisztráció  (sign_up_func(usern, email, pwd, result1)
#  Érvényes:    TC1-1-001-5
# -Bejelentkezés (login_func(email, pwd, logged_in, e_result))
#  Érvényes:    TC2-1-001-5
# -Adatkezelési nyilatkozat használata
#  TC3-001
# -Kijelentkezés
#  TC11-001

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

# def test_d_cookie():
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
    user_logged_in_text_x = driver.find_elements_by_xpath('/html/body/div[1]/nav/div/ul/li[4]/a')
    if len(user_logged_in_text_x) == 0:
        # megnezi van-e figyelmeztető hiba ablak
        login_failed_window_p3_x = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]')
        # ha van figyelmeztető hiba ablak összehasonlítja az e_result paraméter értékével
        if len(login_failed_window_p3_x) != 0:
            print("E_result: ", driver.find_element_by_xpath('/html/body/div[2]/div/div[2]').text)
            assert driver.find_element_by_xpath('/html/body/div[2]/div/div[2]').text == e_result
            # bezárja a figyelmeztető hiba ablakot
            login_failed_ok_button_p3_x = driver.find_element_by_xpath('/html/body/div[2]/div/div[4]/div/button')
            login_failed_ok_button_p3_x.click()
    # logged in esetén leellenőrzi, a
    else:
        print("Logged_in: ", driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li[4]/a').text)
        assert driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li[4]/a').text == logged_in
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


try:
    URL1 = "http://localhost:1667/#/"
    driver.get(URL1)

    # p_home = driver.window_handles[0]

    # conduit_home = driver.find_element_by_class_name('home-page')
    # conduit_login = driver.find_element_by_class_name('home-page')
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
    ###########################################################################
    sign_up_func("Carol1", "carol1@example.com", "Ab123451", "Your registration was successful!")  #
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    logout_func()
    ##################################################
    # localhost-os alkalmazás regisztrált felhasználóinak érvényes bejelentkezése (1-5)
    login_func("carol1@example.com", "Ab123451", "Carol1", "")
    logout_func()

    # cookie panel függvény
    def cookie_policy_panel_exist_func(e_count):
        panel = driver.find_elements_by_id('cookie-policy-panel')
        assert len(panel) == int(e_count)

    # Ugrás az oldal aljára
    web_page = driver.find_element_by_tag_name('html')
    web_page.send_keys(Keys.END)

    # Step2: adatvédelmi nyilatkozat elolvasása
    main_window = driver.window_handles[0]
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    # Az adatkezelési nyilatkozat elolvasáshoz kiválasztása
    Learn_more = driver.find_element_by_xpath('//div[@id="cookie-policy-panel"]//a')
    Learn_more.click()
    # Az adatkezelési nyilatkozat megjelenítése
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    assert len(driver.window_handles) == 2
    driver.close()
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    assert len(driver.window_handles) == 1
    driver.switch_to.window(main_window)
    cookie_policy_panel_exist_func(1)

    # kattintás az adatvédelmi nyilatkozat elfogadása gombra
    i_accept_btn = driver.find_element_by_xpath('//div[@id="cookie-policy-panel"]//button[2]')
    i_accept_btn.click()
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    # tartalom frissítése
    driver.refresh()
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    # a cookie lap már nem létezik ellenőrzése
    cookie_policy_panel_exist_func(0)
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    # pass
    driver.close()
    driver.quit()
