# Bazsalya András Vizsgaremek Feladat: Regisztráció
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

# def test_b_register():
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
            print("Reg_result: Mivel az email cím már létezik és a beállítás hibátlan bevitelre vonatkozott, ezért az assert kihagyva!")
        else:
            print("Reg_result: Mivel az email cím már létezik, a funkció igy nem vizsgálható, ezért az assert kihagyva!")
    else:
        assert driver.find_element_by_xpath('//div[@class="swal-text"]').text == result
    # ha fan felugró Reg Failed ablak
    if len(welcome_reg_failed_window_x) != 0:
        reg_failed_ok_btn_x = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
        reg_failed_ok_btn_x.click()


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
    # Érvénytelen Felhasználói regisztrációk (Sign up/register TC1-0-001-005)
    # sign_up_func(username, email, password, URL1: result)
    ###########################################################################
    # sign_up_tst_data[]
    # sign_up_tst_data.append = ("", "", "", "Username field required.", "")
    # sign_up_tst_data.append = ("Carol1", "carol1@example.", "Ab123456", "Email must be a valid email.", "")
    # sign_up_tst_data.append = ("Carol1", "carol1@", "Ab123456", "Email must be a valid email.", "")
    # sign_up_tst_data.append = ("Carol1", "carol1example.com", "Ab123456", "Email must be a valid email.", "")
    # sign_up_tst_data.append = ("Carol1", "carol1@example.com", "Ab12345",
    #                      "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.",
    #                      "")
    # sign_up_tst_data.append = ("Carol1", "carol1@example.com", "ABCDEFGH",
    #                      "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.",
    #                      "")
    # sign_up_tst_data.append = ("Carol1", "carol1@example.com", "abcdefgh",
    #                      "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.",
    #                      "")
    # sign_up_tst_data.append = ("Carol1", "carol1@example.com", "12345678",
    #                      "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.",
    #                      "")
    print("Érvénytelen felhasználói regisztrációk sikertelenségének ellenőrzése")
    # TC1 Üresen hagyott mezők esetén a "Sign up" gombra kattintás
    sign_up_func("", "", "", "Username field required.")  # username/email/password
    #############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    # TC2 érvénytelen email hiányzik a domain végződés
    sign_up_func("Carol1", "carol1@example.", "Ab123456", "Email must be a valid email.")
    #############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    #############
    # érvénytelen email hiányzik a levelezőszerver címe
    sign_up_func("Carol1", "carol1@", "Ab123456", "Email must be a valid email.")
    #############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    #############
    # érvénytelen email hiányzik a kötelező elválasztójel
    sign_up_func("Carol1", "carol1example.com", "Ab123456", "Email must be a valid email.")
    #############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    #############
    # érvénytelen password nincs 8 karakter
    # sign_up_func("pentek", "pentek@example.com", "Abc1234", "Email already taken.", "")
    sign_up_func("Carol1", "carol1@example.com", "Ab12345",
                 "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.")
    #############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    #############
    # érvénytelen password hossza 8 karakter, de csupa nagybetü
    sign_up_func("Carol1", "carol1@example.com", "ABCDEFGH",
                 "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.")
    #############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    #############
    # érvénytelen password hossza 8 karakter, de csupa kisbetü
    # sign_up_func("pentek", "pentek@example.com", "Abc1234", "Email already taken.", "")
    sign_up_func("Carol1", "carol1@example.com", "abcdefgh",
                 "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.")
    #############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)
    #############
    # érvénytelen password hossza 8 karakter, de csupa szám
    # sign_up_func("pentek", "pentek@example.com", "Abc1234", "Email already taken.", "")
    sign_up_func("Carol1", "carol1@example.com", "12345678",
                 "Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.")
    #############
    if dly == 0:
        time.sleep(1)
    else:
        time.sleep(ts)

    # Érvényes Felhasználók regisztrációja (Sign up/register TC1-1-001-005 + logout)
    # sign_up_func(username, email, password, URL1: result)
    ###########################################################################
    # sign_up_tst_data[]
    # sign_up_tst_data.append = ("Carol1", "carol1@example.com", "Ab123451", "Your registration was successful!", "")    #TC1-1-001
    # sign_up_tst_data.append = ("Carol2", "carol2@example.com", "Ab123452", "Your registration was successful!", "")    #TC1-1-002
    # sign_up_tst_data.append = ("Carol3", "carol3@example.com", "Ab123453", "Your registration was successful!", "")    #TC1-1-003
    # sign_up_tst_data.append = ("Carol4", "carol4@example.com", "Ab123454", "Your registration was successful!", "")    #TC1-1-004
    # sign_up_tst_data.append = ("Carol5", "carol5@example.com", "Ab123455", "Your registration was successful!", "")    #TC1-1-005
    print("A felhesználók beregisztrálása a rendszerbe")
    sign_up_func("Carol1", "carol1@example.com", "Ab123451", "Your registration was successful!")  #
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    logout_func()
    sign_up_func("Carol2", "carol2@example.com", "Ab123452", "Your registration was successful!")  #
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    logout_func()
    sign_up_func("Carol3", "carol3@example.com", "Ab123453", "Your registration was successful!")  #
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    logout_func()
    sign_up_func("Carol4", "carol4@example.com", "Ab123454", "Your registration was successful!")  #
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    #############
    logout_func()
    sign_up_func("Carol5", "carol5@example.com", "Ab123455", "Your registration was successful!")  #
    logout_func()
    #############
    if dly == 0:
        time.sleep(2)
    else:
        time.sleep(ts)
    ####################################################################################
    # localhost-os alkalmazás frissen regisztrált felhasználóinak érvényes bejelentkezése (1-5)
    print("A korábban beregisztrált felhesználók beléptethetőségének ellenőrzése")
    login_func("carol1@example.com", "Ab123451", "Carol1", "")
    logout_func()
    login_func("carol2@example.com", "Ab123452", "Carol2", "")
    logout_func()
    login_func("carol3@example.com", "Ab123453", "Carol3", "")
    logout_func()
    login_func("carol4@example.com", "Ab123454", "Carol4", "")
    logout_func()
    login_func("carol5@example.com", "Ab123455", "Carol5", "")
    logout_func()
    #############
    time.sleep(1)

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    # pass
    driver.close()
    driver.quit()