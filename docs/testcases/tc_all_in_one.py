# Bazsalya András Vizsgaremek Feladatok egyben
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

a = 1
i = 0
Y = "Headless"

if Y == "Headless":
    #A
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver.get("http://localhost:1667")
    #B
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
    pass
    # opt.headless = False
    # # In order for ChromeDriverManager to work you must pip install it in your own environment.
    # driver = webdriver.Chrome(ChromeDriverManager().install())

class MyRND():
    print("MyRND: Start")
    chars = string.ascii_lowercase
    charsf = string.ascii_letters + ' '
    charsv = string.ascii_uppercase + string.ascii_lowercase
    pchars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

    @classmethod
    def field_usrn(cls):
        #return "".join([random.choice(cls.chars) for _ in range(8)])
        return "".join([random.choice(cls.chars) for _ in range(8)])

    @classmethod
    def field_pwd(cls):
        return "".join([random.choice(cls.chars) for _ in range(8)])

    @classmethod
    def field_20(cls):
        return "".join([random.choice(cls.charsf) for _ in range(20)])

    @classmethod
    def field_50(cls):
        return "".join([random.choice(cls.charsf) for _ in range(50)])

    @classmethod
    def field_300(cls):
        return "".join([random.choice(cls.charsf) for _ in range(300)])

    @classmethod
    def email(cls):
        # 1. generalom a random kukac elotti reszt
        # @
        # 2. generalom a kukac utanni reszt
        # .
        # fixen "com"
        pass

# class TestData(darabszam):
#     def __init__(self):
#         self.data = []
#         for i in range(darabszam):
#             d = {}
#             d["username"] = MyRND.uname()
#             d["password"] = MyRND.ppass()
#             self.data.append(d)

# 4 beviteli mezőt tartalmaz: Email, Password, a kijelzett login ellenőrzéséhez, az elvárt üzenet assertnél
def login_func(email, pwd, logged_in, e_result):
    print("Login_func: Start")
    # Home: http://localhost:1667/#/
    if a == 1:
        sign_in_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="#/login"]')
    else:
        sign_in_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="/login"]')

    # sign_in_button = driver.find_element_by_class_name("nav-link")
    # sign_in_button_p1_x = driver.find_element_by_xpath('/html/body/div/nav/div/ul/li[2]/a') #URL1
    # sign_in_button_p1_x = driver.find_element_by_xpath('/html/body/div/div/nav/div/ul/li[2]/a')   # URL2
    # sign_in_button_p1_x = driver.find_element_by_xpath('//div/nav/div/ul/li[2]/a')  # URL1,2
    sign_in_button_p1_x.click()
    time.sleep(1)
    # Login: http://localhost:1667/#/login
    # email_input_field = driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/fieldset[1]/input')   # URL1
    # email_input_field = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[1]/input')  # URL2
    # email_input_field = driver.find_element_by_xpath('/fieldset/fieldset[1]/input')   # URL1,2
    email_input_field = driver.find_element_by_xpath(
        '//fieldset/input[@class="form-control form-control-lg"][@placeholder="Email"]')  # URL1,2
    # pwd_input_field = driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/fieldset[2]/input') # URL1
    # pwd_input_field = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[2]/input')    # URL2
    # pwd_input_field = driver.find_element_by_xpath('//input[@class="form-control form-control-lg"]')  # URL1,2
    pwd_input_field = driver.find_element_by_xpath(
        '//fieldset/input[@class="form-control form-control-lg"][@placeholder="Password"]')  # URL1,2
    # sign_in_button_p2_x = driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/button')
    sign_in_button_p2_x = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    # email input field clear + set email param
    email_input_field.clear()
    email_input_field.send_keys(email)
    time.sleep(1)
    # pwd input field clear + set pwd param
    pwd_input_field.clear()
    pwd_input_field.send_keys(pwd)
    time.sleep(1)
    # sign_in email & pwd data
    sign_in_button_p2_x.click()
    time.sleep(2)
    # nincs logged_in esetén
    if a == 1:
        user_logged_in_text_x = driver.find_elements_by_xpath('/html/body/div[1]/nav/div/ul/li[4]/a')
        if len(user_logged_in_text_x) == 0:
            # megnezi van-e figyelmeztető hiba ablak
            login_failed_window_p3_x = driver.find_elements_by_xpath('/html/body/div[2]/div/div[2]')
            # ha van figyelmeztető hiba ablak összehasonlítja az e_resoult paraméter értékével
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
    else:
        pass
        # //login
        # error_text_email_p2_x = driver.find_element_by_xpath()
        # error_text_pwd_p2_x = driver.find_element_by_xpath('//div[@class='alert alert-danger']').text
    time.sleep(2)


def logout_func():
    print("Logout_func: Start")
    log_out_button_p1_x = driver.find_elements_by_xpath('/html/body/div[1]/nav/div/ul/li[5]/a')
    if len(log_out_button_p1_x) != 0:
        log_out_button_p1_x = driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul/li[5]/a')
        log_out_button_p1_x.click()


# 3 beviteli mezőt tartalmaz: Username, Email, Password
def sign_up_func(usern, email, pwd, result1, result2):
    # Register (sign up): http://localhost:1667/#/register
    # sign_up_button = driver.find_element_by_class_name("nav-link")
    # sign_up_button_p1_x = driver.find_element_by_xpath('/html/body/div/nav/div/ul/li[3]/a')   #URL1
    # sign_up_button_p1_x = driver.find_element_by_xpath('/html/body/div/div/nav/div/ul/li[3]/a')   #URL2
    # sign_up_button_p1_x = driver.find_element_by_xpath('//ul/li[3]/a')  # URL1,2
    print("Sign_up_func: Start")
    time.sleep(1)
    if a == 1:
        sign_up_button_p1_x = driver.find_element_by_xpath('//li/a[@href="#/register"]')
    else:
        sign_up_button_p1_x = driver.find_element_by_xpath('//li/a[@href="/register"]')

    sign_up_button_p1_x.click()
    # signup_text_usern_p2_x = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[1]/input')
    # signup_text_usern_p2_x = driver.find_element_by_xpath('//div/form/fieldset/fieldset[1]/input')
    signup_text_usern_p2_x = driver.find_element_by_xpath(
        '//fieldset[@class="form-group"]/input[@placeholder="Username"]')
    signup_text_usern_p2_x.send_keys(usern)
    # signup_text_email_p2_x = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[2]/input')
    signup_text_email_p2_x = driver.find_element_by_xpath('//fieldset[@class="form-group"]/input[@placeholder="Email"]')
    signup_text_email_p2_x.send_keys(email)
    # signup_text_pwd_p2_x = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/fieldset[3]/input')
    signup_text_pwd_p2_x = driver.find_element_by_xpath(
        '//fieldset[@class="form-group"]/input[@placeholder="Password"]')
    signup_text_pwd_p2_x.send_keys(pwd)
    # signup_subm_btn_p2_x = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/fieldset/button')
    signup_subm_btn_p2_x = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    signup_subm_btn_p2_x.click()
    time.sleep(4)
    if a == 1:
        # reg_failed_window_x = driver.find_element_by_xpath('/html/body/div[2]/div')
        welcome_reg_failed_window_x = driver.find_elements_by_xpath('//div[@class="swal-modal"]')
        # print("reg_result=", driver.find_element_by_xpath('//html/body/div[2]/div/div[3]').text)
        print("Reg_result: ", driver.find_element_by_xpath('//div[@class="swal-text"]').text)
        assert driver.find_element_by_xpath('//div[@class="swal-text"]').text == result1
        # ha fan felugró Reg Failed ablak
        if len(welcome_reg_failed_window_x) != 0:
            # reg_failed_ok_btn_x = driver.find_element_by_xpath('//div/div/div/div/button[@class="swal-button swal-button--confirm"]')
            reg_failed_ok_btn_x = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
            reg_failed_ok_btn_x.click()
    else:
        alert_dander_window = driver.find_element_by_xpath('//div[@class="alert alert-danger"]').text
        print("Alert danger ablak: ", alert_dander_window)
        # assert alert_dander_window == result2
        # This email address is already registered.


#def new_article():
def new_article_func(uzenetszam):
    print("New_article_func: Start")
    # /home

    #a1 = "agkjsgjdfs"
    # a2 = "agkjsgjdfs"
    # a3 = "agkjsgjdfs"
    # a4 = "agkjsgjdfs"
    a2 = MyRND.field_50()
    a3 = MyRND.field_300()
    a4 = MyRND.field_20()

    time.sleep(2)
    # New Article
    if a == 1:
        new_article_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="#/editor"]')
        new_article_button_p1_x.click()

    # New post button click
    else:
        new_article_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="/editor"]')
        new_article_button_p1_x.click()

    time.sleep(2)
    # p_new_article = "http://localhost:1667/#/editor"
    # p_home = driver.window_handles[0]
    # driver.switch_to.frame(p_new_article)

    # article_title_field_x = driver.find_element_by_xpath('//div/div/div/div/form/fieldset/fieldset[1]/input')
    # /editor
    article_title_field_x = driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
    article_about_field_x = driver.find_element_by_xpath('//input[@class="form-control"]')
    write_article_field_x = driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
    enter_tag_field_x = driver.find_element_by_xpath('//input[@placeholder="Enter tags"]')
    pub_article_button_x = driver.find_element_by_xpath(
        '//button[@class="btn btn-lg pull-xs-right btn-primary"]')
    # enter_tag_field_x = driver.find_element_by_xpath('//fieldset[@class="form-group"]/input[@placeholder="Enter tags"]')
    # a1 = MyRND.field_20()
    # a2 = MyRND.field_50()
    # a3 = MyRND.field_300()
    # a4 = MyRND.chars
    # print(MyRND.field_20())
    # print(MyRND.field_50())
    # print(MyRND.field_300())
    # print(MyRND.chars())
    time.sleep(2)
    article_title_field_x.clear()
    article_about_field_x.clear()
    write_article_field_x.clear()
    enter_tag_field_x.clear()
    article_title_field_x.send_keys("NEW ARTICLE", str(uzenetszam))
    # article_about_field_x.send_keys(MyRND.field_20())
    # write_article_field_x.send_keys(MyRND.field_50())
    # enter_tag_field_x.send_keys(MyRND.field_300())
    #article_title_field_x.send_keys(a1)
    article_about_field_x.send_keys(a2)
    write_article_field_x.send_keys(a3)
    enter_tag_field_x.send_keys(a4)
    time.sleep(2)
    pub_article_button_x.click()
    print("Pub article button: Clicked")
    # if a == 1:
    #     # reg_failed_window_x = driver.find_element_by_xpath('/html/body/div[2]/div')
    #     welcome_reg_failed_window_x = driver.find_elements_by_xpath('//div[@class="swal-modal"]')
    #     # print("reg_result=", driver.find_element_by_xpath('//html/body/div[2]/div/div[3]').text)
    #     print("reg_result=", driver.find_element_by_xpath('//div[@class="swal-text"]').text)
    #     assert driver.find_element_by_xpath('//div[@class="swal-text"]').text == result1
    #     # ha fan felugró Reg Failed ablak
    #     if len(welcome_reg_failed_window_x) != 0:
    #         # reg_failed_ok_btn_x = driver.find_element_by_xpath('//div/div/div/div/button[@class="swal-button swal-button--confirm"]')
    #         reg_failed_ok_btn_x = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    #         reg_failed_ok_btn_x.click()
    # else:

    # Articicles: http://localhost:1667/#/articles/adafdsfs


def your_settings_func():
    print("Your_settings_func: Start")
    # Your settings

    b1 = "https://static.productionready.io/images/smiley-cyrus.jpg"
    b2 = "Carol1"
    b3 = "Barmi erdekes rolam ..."
    b4 = "carol1@example.com"
    b5 = "Ab1234567"


    if a == 1:
        your_settings_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="#/settings"]')
        your_settings_button_p1_x.click()

    # New post button click
    else:
        your_settings_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="/settings"]')
        your_settings_button_p1_x.click()

    time.sleep(3)
    ##############
    pict_url_field_x = driver.find_element_by_xpath('//input[@placeholder="URL of profile picture"]')
    user_name_field_x = driver.find_element_by_xpath('//input[@placeholder="Your username"]')
    short_about_you_field_x = driver.find_element_by_xpath('//textarea[@placeholder="Short bio about you"]')
    email_field_x = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    pwd_field_x = driver.find_element_by_xpath(
        '//input[@class="form-control form-control-lg"][@placeholder="Password"]')
    # pwd_field_x = driver.find_element_by_xpath('//fieldset[@class="form-group"]/input[@placeholder="Article title"]')
    ###############

    time.sleep(3)

    pict_url_field_x.clear()
    pict_url_field_x.send_keys(b1)
    user_name_field_x.clear()
    user_name_field_x.send_keys(b2)
    short_about_you_field_x.clear()
    short_about_you_field_x.send_keys(b3)
    email_field_x.clear()
    email_field_x.send_keys(b4)
    pwd_field_x.clear()
    pwd_field_x.send_keys(b5)
    time.sleep(5)
    ###############
    updt_sett_button_x = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    print("Gomb: ",driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').text)
    updt_sett_button_x.click()
    time.sleep(3)
    #update_pop_up_window_x = driver.find_elements_by_xpath('//div[@class="swal-modal"]/div[@class="swal-title"]')
    update_pop_up_window_x = driver.find_elements_by_xpath('//div[@class="swal-modal"][@role="dialog"]')
    print("Dialog window: ", len(update_pop_up_window_x))
    if a == 1:
        if len(update_pop_up_window_x) != 0:
            x = driver.find_element_by_xpath('//div[@class="swal-modal"]/div[@class="swal-title"]').text
            print("Window message: ", x)
            assert x == "Update successful!"
            update2_pop_up_button_x = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
            update2_pop_up_button_x.click()
            print("Pop-up button: Clicked")
    else:
        if len(update_pop_up_window_x) != 0:
            x = driver.find_element_by_xpath('//div/div[@class="swal-title"]').text
            print("Window message: ", x)
            assert x == "Update successful!"
            update2_pop_up_button_x = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
            update2_pop_up_button_x.click()
            print("Pop-up button: Clicked")
try:
    URL1 = "http://localhost:1667/#/"
    #URL1 = "http://localhost:1667"
    URL2 = "https://react-layr-realworld-example-app.layrjs.com/all"
    if a == 1:
        driver.get(URL1)
    else:
        driver.get(URL2)

    p_home = "http://localhost:1667/#/"
    p_login = "http://localhost:1667/#/login"
    p_new_article = "http://localhost:1667/#/editor"

    # p_home = driver.window_handles[0]

    # conduit_home = driver.find_element_by_class_name('home-page')
    # conduit_login = driver.find_element_by_class_name('home-page')
    time.sleep(5)
    # Felhasználók regisztrációja
    sign_up_func("Carol1", "carol1@example.com", "Ab1234567", "Your registration was successful!", "")
    time.sleep(2)
    logout_func()
    sign_up_func("Carol2", "carol2@example.com", "Ab1234567", "Your registration was successful!", "")
    time.sleep(2)
    logout_func()
    sign_up_func("Carol3", "carol3@example.com", "Ab1234567", "Your registration was successful!", "")
    time.sleep(2)
    logout_func()
    sign_up_func("Carol4", "carol4@example.com", "Ab1234567", "Your registration was successful!", "")
    time.sleep(2)
    logout_func()
    sign_up_func("Carol5", "carol5@example.com", "Ab1234567", "Your registration was successful!", "")
    logout_func()
    # 1db kiválasztott x felhasználó bejelentkezése
    login_func("carol1@example.com", "Ab1234567", "Carol1", "")
    # login_func("testuser1@example.com", "Abcd123$", "testuser1", "")
    # web applikacioban
    # login_func("testuser1@example.com", "Abcd123$", "testuser1", "")
    # login_func("testuser2@example.com", "Abcd123$", "testuser2", "")
    # login_func("testuser3@example.com", "Abcd123$", "testuser3", "")
    # login_func("testuser4@example.com", "Abcd123$", "testuser4", "")
    # login_func("testuser5@example.com", "Abcd123$", "testuser2", "")

    time.sleep(2)
    # x felhasználó adatainak módosítása
    # b1 = "https://static.productionready.io/images/smiley-cyrus.jpg"
    # b2 = "Carol1"
    # b3 = "Barmi erdekes rolam ..."
    # b4 = "carol1@example.com"
    # b5 = "Ab1234567"
    your_settings_func()
    time.sleep(2)
    # # x felhasználó új postokat hoz létre
    for i in range(20):
        new_article_func(i)
        print("New Article", i)

    # TC0
    # signup(username, email, password, URL1: result, URL2: result)
    # érvénytelen minden
    # "This email address is already registered."
    # "This username is already taken."
    # Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 lowercase letter.

    # sign_up_func("", "", "","Username field required.", "") # username/email/password
    # time.sleep(1)
    # #érvénytelen password nincs 8 karakter
    # sign_up_func("pentek", "pentek@example.com", "Abc1234", "Email already taken.", "")
    # time.sleep(1)
    # # érvénytelen password csak szám
    # sign_up_func("pentek", "pentek@example.com", "12345678", "Email already taken.", "")
    # time.sleep(1)
    # # érvénytelen password csak kisbetű
    # sign_up_func("pentek", "pentek@example.com", "12345678", "Email already taken.", "")
    # time.sleep(1)
    # # érvénytelen password csak nagybetű
    # sign_up_func("pentek", "pentek@example.com", "12345678", "Email already taken.", "")
    # time.sleep(1)
    # # érvényes és mégis hibaüzenet jön
    # sign_up_func("pentek", "pentek@example.com", "Ab123456", "Email already taken.", "")
    # time.sleep(1)
    # # érvényes
    # sign_up_func("pentek", "pentek@example.com", "Ab1234567", "Email already taken.", "")
    # time.sleep(1)
    #
    # # TC1: kitöltetlen adatokkal
    # login_func("", "", "", "Login failed!")
    # logout_func()
    # # TC2: hiányos domainű email cím
    # login_func("testuser1@example", "Abcd123$", "", "Login failed!")
    # logout_func()
    # # TC3: érvénytelen email cím
    # login_func("testuser1", "Abcd123$", "", "Login failed!")
    # logout_func()
    # # TC5 Érvénytelen password
    # login_func("testuser1@example.com", "Abcd", "testuser1", "Login failed!")
    # logout_func()
    # # TC6 Érvényes teszt adat1
    # login_func("testuser1@example.com", "Abcd123$", "testuser1", "")
    # logout_func()
    # # TC7 Érvényes teszt adat2
    # login_func("testuser2@example.com", "Abcd123$", "testuser2", "")
    # logout_func()
    # # TC8 Érvényes teszt adat3
    # login_func("testuser3@example.com", "Abcd123$", "testuser3", "")
    # logout_func()
    # # TC9 Érvényes teszt adat4
    # login_func("testuser4@example.com", "Abcd123$", "testuser4", "")
    # logout_func()
    # # TC10 Érvénytelen teszt adat 5 login email és password nem össze tartozó
    # login_func("testuser5@example.com", "Abcd123$", "testuser5", "Login failed!")
    # logout_func()

    time.sleep(1)

except NoSuchElementException as exc:
    print("Hiba történt: ", exc)

finally:
    # pass
    driver.close()
    driver.quit()
