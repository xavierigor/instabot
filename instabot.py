from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from secrets import username, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class InstaBot:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.login()
        following = self.get_following()
        followers = self.get_followers()

        not_following_you_back = [user for user in following if user not in followers]
        not_following_them_back = [user for user in followers if user not in following]

        print("==========================================")
        print("Quem você segue e não te segue de volta:")
        print(len(not_following_you_back), not_following_you_back)
        print("==========================================")
        print("Quem te segue e você não segue de volta:")
        print(len(not_following_them_back), not_following_them_back)
        print("==========================================")

    def login(self):
        self.driver.get("https://instagram.com")
        sleep(2)

        email_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/"
                                                        "div[2]/div/label/input")
        password_input = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/"
                                                           "form/div[3]/div/label/input")
        submit_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/"
                                                          "form/div[4]/button")

        email_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

        sleep(4)

        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
            sleep(2)
            # modal_ativar_notificacoes = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))).click()
            # ActionChains(self.driver).move_to_element(modal_ativar_notificacoes).click().perform()

            # modal_ativar_notificacoes = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
            # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, modal_ativar_notificacoes))).click()
            # # modal_ativar_notificacoes = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
            # modal_ativar_notificacoes.click()
        except NoSuchElementException:
            pass

    def get_following(self):
        account_link = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/"
                                                         "div[2]/div[1]/a")
        account_link.click()
        sleep(2)

        following_link = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/"
                                                           "a")
        following_link.click()

        # scrollbox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
        scrollbox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            sleep(1)
            height = self.driver.execute_script("""
                                                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                                return arguments[0].scrollHeight;
                                                """, scrollbox)

        links = scrollbox.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != ""]

        # close modal
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()

        return names

    def get_followers(self):
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        scrollbox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        sleep(1)

        last_height, height = 0, 1
        while last_height != height:
            last_height = height
            sleep(1)
            height = self.driver.execute_script("""
                                                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                                return arguments[0].scrollHeight;
                                                """, scrollbox)

        ul = scrollbox.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul")
        links = ul.find_elements_by_tag_name("a")
        names = [name.text for name in links if name.text != ""]

        return names


bot = InstaBot()
