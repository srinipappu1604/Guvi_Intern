from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Datas import data
import pytest
import time

class Test_GUVI_Intern:
    url = "https://www.demoblaze.com/"
    
    @pytest.fixture
    def booting_function(self):
        try:
            self.driver = webdriver.Firefox()
            yield
            self.driver.close()
        except:
            print("ERROR IN THE FUCTION - booting_function")
            
    def test_demoblaz_website(self, booting_function):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            time.sleep(3)
            cookies = self.driver.get_cookies()
            cookie_home_page = cookies[0]['value']
            print('Initial Value of Cookie Before Login # ', cookie_home_page)
            
            
# Test Case #1 (Homepage Verification):
            try:
                self.driver.find_element(by = By.XPATH,value = data.Test_Case_1.website_logo).is_displayed
                self.driver.find_element(by = By.LINK_TEXT,value = data.Test_Case_1.navigation_Contact).is_displayed
                self.driver.find_element(by = By.LINK_TEXT,value = data.Test_Case_1.navigation_Monitors).is_displayed
                print("Successfull - Test Case #1 (Homepage Verification)")
            except:
                print("Not Successfull - Test Case #1 (Homepage Verification)")
                
# Test Case #2 (Registration with valid data):
            try:
                self.driver.find_element(by = By.ID,value = data.Test_Case_2.sign_up).click()
                self.driver.implicitly_wait(5)
                self.driver.find_element(by = By.ID, value = data.Test_Case_2.sign_in_username).send_keys(data.username_password.username)
                self.driver.find_element(by = By.ID, value = data.Test_Case_2.sign_in_password).send_keys(data.username_password.password)
                self.driver.implicitly_wait(5)
                self.driver.find_element(by = By.XPATH,value = data.Test_Case_2.sign_up_button).click()
                time.sleep(5)
                self.driver.switch_to.alert.accept()
                print("Successfull - Test Case #2 (Registration with valid data)")
            except:
                print("Not-Successfull - Test Case #2 (Registration with valid data)")
                
# Test Case #3 (User Login):
            try:
                self.driver.find_element(by = By.ID,value = data.Test_Case_3.navigation_login).click()
                self.driver.find_element(by = By.ID, value = data.Test_Case_3.login_username).send_keys(data.username_password.username)
                self.driver.find_element(by = By.ID, value = data.Test_Case_3.login_password).send_keys(data.username_password.password)
                self.driver.implicitly_wait(5)
                self.driver.find_element(by = By.XPATH,value = data.Test_Case_3.login_button).click()
                print("Successfull - Test Case #3 (User Login)")
            except:
                print("Not Successfull - Test Case #3 (User Login)")
                
# Test Case #4 (Product Selection and Cart Interaction):
            try:
                time.sleep(5)
                self.driver.find_element(by = By.ID,value = data.Test_Case_4.phones_button).click()
                time.sleep(5)
                self.driver.find_element(by = By.XPATH,value = data.Test_Case_4.Samsung_galaxy_s6).click()
                time.sleep(5)
                self.driver.find_element(by = By.XPATH,value = data.Test_Case_4.add_to_cart).click()
                time.sleep(5)
                self.driver.switch_to.alert.accept()
                print("Successfull - Test Case #4 (Product Selection and Cart Interaction)")
            except:
                print("Not Successfull - Test Case #4 (Product Selection and Cart Interaction)")
                
# Test Case #5(Placing an Order):
            try:
                time.sleep(5)
                self.driver.find_element(by = By.ID,value = data.Test_Case_5.navigation_Cart).click()
                time.sleep(5)
                self.driver.find_element(by = By.XPATH,value = data.Test_Case_5.place_order).click()
                time.sleep(5)
                self.driver.find_element(by = By.ID, value = data.Test_Case_5.name).send_keys(data.Test_Case_5.name_Send_keys)
                self.driver.find_element(by = By.ID, value = data.Test_Case_5.country).send_keys(data.Test_Case_5.country_Send_keys)
                self.driver.find_element(by = By.ID, value = data.Test_Case_5.city).send_keys(data.Test_Case_5.city_Send_keys)
                self.driver.find_element(by = By.ID, value = data.Test_Case_5.card).send_keys(data.Test_Case_5.card_Send_keys)
                self.driver.find_element(by = By.ID, value = data.Test_Case_5.month).send_keys(data.Test_Case_5.month_Send_keys)
                self.driver.find_element(by = By.ID, value = data.Test_Case_5.year).send_keys(data.Test_Case_5.year_Send_keys)
                time.sleep(5)
                self.driver.find_element(by = By.XPATH,value =data.Test_Case_5.purchase_button).click()
                time.sleep(5)
                self.driver.find_element(by = By.XPATH,value =data.Test_Case_5.Ok_button).click()
                print("Successfull - Test Case #5(Placing an Order)")
            except:
                print("Not Successfull - Test Case #5(Placing an Order)")
                
# Test Case #6 (Logout):
            try:
                time.sleep(5)
                self.driver.find_element(by = By.ID,value = data.Test_Case_6.logout_button).click()
                print("Successfull - Test Case #6 (Logout)")
            except:
                print("Not Successfull - Test Case #6 (Logout)")
                
            time.sleep(3)
            cookie_after_login = self.driver.get_cookies()
            cookie_after_login = cookie_after_login[0]['value']
            print("Cookie Value after Login # ", cookie_after_login)
            if(cookie_home_page != cookie_after_login):
                print("SUCCESS # Login Success. Previous Cookie ID before Login is {a} and after login Cookie ID is {b}".format(a=cookie_home_page, b=cookie_after_login))
        except:
            print("ERROR IN THE FUCTION - test_Homepage_Verification")
            