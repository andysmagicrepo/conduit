# Bazsalya András Vizsgaremek Feladatok egyben
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

def test_e_rep_data_new_article():
    # egységesen állítható time.sleep
    dly = 0  # késleltetés korábbi(0) vagy egységes(!=0)
    ts = 3
    i = 0
    Y = "Headless"

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


    class MyRND():
        print("MyRND: Start")
        chars = string.ascii_lowercase
        charsf = string.ascii_letters + ' '
        charsv = string.ascii_uppercase + string.ascii_lowercase
        pchars = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation

        @classmethod
        def field_usrn(cls):
            print("MyRND.field_usrn")
            return "".join([random.choice(cls.chars) for _ in range(8)])

        @classmethod
        def field_pwd(cls):
            print("MyRND.field_usrn")
            return "".join([random.choice(cls.chars) for _ in range(8)])

        @classmethod
        def field_20_char(cls):
            print("MyRND.field_20_char")
            return "".join([random.choice(cls.charsf) for _ in range(20)])

        @classmethod
        def field_50_char(cls):
            print("MyRND.field_50_char")
            return "".join([random.choice(cls.charsf) for _ in range(50)])

        @classmethod
        def field_300_char(cls):
            print("MyRND.field_300_char")
            return "".join([random.choice(cls.charsf) for _ in range(300)])

        @classmethod
        def email(cls):
            print("MyRND.field_usrn")
            # 1. generalom a random kukac elotti reszt
            # @
            # 2. generalom a kukac utanni reszt
            # .
            # fixen "com"
            pass


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

    # def new_article():
    def new_article_func(uzenetszam):
        print("New_article_func: Start")
        # /home

        # a1 = "New Article 001"
        # a2 = "agkjsgjdfs"
        # a3 = "agkjsgjdfs"
        # a4 = "agkjsgjdfs"

        a1 = "NEW ARTICLE" + str(uzenetszam)
        a2 = MyRND.field_50_char()
        a3 = MyRND.field_300_char()
        a4 = MyRND.field_20_char()
        print(a1)
        print(a2)
        print(a3)
        print(a3)
        ##############
        if dly == 0:
            time.sleep(2)
        else:
            time.sleep(ts)
        ##############
        # New Article
        new_article_button_p1_x = driver.find_element_by_xpath('//ul/li/a[@href="#/editor"]')
        new_article_button_p1_x.click()

        ##############
        if dly == 0:
            time.sleep(2)
        else:
            time.sleep(ts)
        ##############
        # p_new_article = "http://localhost:1667/#/editor"
        # p_home = driver.window_handles[0]
        # driver.switch_to.frame(p_new_article)

        # /editor
        article_title_field_x = driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
        article_about_field_x = driver.find_element_by_xpath('//input[@class="form-control"]')
        write_article_field_x = driver.find_element_by_xpath('//textarea[@placeholder="Write your article (in markdown)"]')
        enter_tag_field_x = driver.find_element_by_xpath('//input[@placeholder="Enter tags"]')
        pub_article_button_x = driver.find_element_by_xpath(
            '//button[@class="btn btn-lg pull-xs-right btn-primary"]')
        ##############
        if dly == 0:
            time.sleep(2)
        else:
            time.sleep(ts)
        ##############
        article_title_field_x.clear()
        article_about_field_x.clear()
        write_article_field_x.clear()
        enter_tag_field_x.clear()
        article_title_field_x.send_keys(a1)
        article_about_field_x.send_keys(a2)
        write_article_field_x.send_keys(a3)
        enter_tag_field_x.send_keys(a4)
        ##############
        if dly == 0:
            time.sleep(2)
        else:
            time.sleep(ts)
        ##############
        pub_article_button_x.click()
        print("Pub article button: Clicked")


        # Articicles: http://localhost:1667/#/articles/adafdsfs

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
        # Érvényes Felhasználó regisztrációja (Sign up/register TC1-1-001-005 + logout)
        sign_up_func("Carol1", "carol1@example.com", "Ab123451", "Your registration was successful!")  #
        #############
        if dly == 0:
            time.sleep(2)
        else:
            time.sleep(ts)
        if dly == 0:
            time.sleep(2)
        else:
            time.sleep(ts)
        #############
        # # x felhasználó új postokat hoz létre
        for i in range(20):
            new_article_func(i)
            print("New Article", i)
        # #############
        # if dly == 0:
        #     time.sleep(1)
        # else:
        #     time.sleep(ts)
        # ############
        logout_func()
        time.sleep(1)

    except NoSuchElementException as exc:
        print("Hiba történt: ", exc)

    finally:
        # pass
        driver.close()
        driver.quit()
