from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from secrets import username, password


class InstaBot:

    def __init__(self):
        self.driver = webdriver.Firefox()

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
            modal_ativar_notificacoes = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")
            modal_ativar_notificacoes.click()
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

        scrollbox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div[2]")
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
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()

        # print(len(names), names)
        return names

    def get_followers(self):
        # TODO: implement
        # not_following_back = [user for user in following if user not in followers]
        pass


bot = InstaBot()
bot.login()
bot.get_following()
