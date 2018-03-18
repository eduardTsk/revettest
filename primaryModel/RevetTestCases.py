import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from unittest import *

class TestPages(unittest.TestCase):

    def setUp(self):
        self.signin_email = "reuser15@grr.la"
        self.signin_password = "1q2w3e4R@"

        self.signup_fname = "fopot"
        self.signup_lname = "serotin"
        self.signup_email = "reuser39@grr.la"
        self.signup_password = "1q2w3e4R@"

        # self.driver = webdriver.Chrome("C:/Selenium/chromedriver.exe")
        self.driver = webdriver.Firefox()
        self.driver.get('https://dev2.revetinc.com/')

    def test_signup_sector(self):

        #  go to the registration form
        #
        join_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Join now')))
        join_link.click()

        address_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'or join using your Email Address')))
        address_link.click()

        # fill in the required fields for registration
        #
        fname_item = self.driver.find_element_by_xpath("//input[@name='FirstName']")
        fname_item.send_keys(self.signup_fname)
        lname_item = self.driver.find_element_by_xpath("//input[@name='LastName']")
        lname_item.send_keys(self.signup_lname)
        uname_item = self.driver.find_element_by_xpath("//input[@name='UserName']")
        uname_item.send_keys(self.signup_email)
        password_item = self.driver.find_element_by_xpath("//input[@name='Password']")
        password_item.send_keys(self.signup_password)

        submit_item = self.driver.find_element_by_class_name("form-group")
        submit_button = submit_item.find_element_by_xpath("//button[@type='submit']")

        submit_button.click()

        # fill out the zip code in the new profile
        #
        zipcode_item = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='zipCode']")))
        zipcode_item.send_keys("11209")

        continue_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        continue_button.click()

        # at the moment we will not fill out a new profile
        #
        skip_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-link margin-top-25']")))
        skip_link.click()

        skip_link = self.driver.find_element_by_xpath("//button[@class='btn btn-link margin-top-25']")
        skip_link.click()
        skip_link = self.driver.find_element_by_xpath("//button[@class='btn btn-link margin-top-25']")
        skip_link.click()
        skip_link = self.driver.find_element_by_xpath("//button[@class='btn btn-link margin-top-25']")
        skip_link.click()
        skip_link = self.driver.find_element_by_xpath("//button[@class='btn btn-link margin-top-25']")
        skip_link.click()

        # go to a new profile
        #
        profile_link = self.driver.find_element_by_partial_link_text("or go to your profile")
        profile_link.click()

        #  make sure that the first name and the second name in the new profile are true
        #
        profile_name = self.driver.find_element_by_xpath("//h1[1]")
        self.assertEqual(profile_name.text, "fopot serotin")


    def test_signin(self):
        email_box = self.driver.find_element_by_xpath("//input[@name='emailAddress']")
        email_box.send_keys(self.signin_email)
        password_box = self.driver.find_element_by_xpath("//input[@name='password']")
        password_box.send_keys(self.signin_password)
        signin_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        signin_button.click()

    def tearDown(self):
        # self.driver.close()
        None

if __name__ == "__main__":
    unittest.main()