from BaseApp import BasePage
from selenium.webdriver.common.by import By
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class MainLocators:
    LOCATOR_FIRST_NAME = (By.ID, "firstName")
    LOCATOR_LAST_NAME = (By.ID, "lastName")
    LOCATOR_EMAIL = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input")
    LOCATOR_GENDER_MALE = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[1]/label")
    LOCATOR_GENDER_FEMALE = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[2]/label")
    LOCATOR_GENDER_OTHER = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[3]/div[2]/div[3]/label")
    LOCATOR_MOBILE_NUMBER = (By.CSS_SELECTOR, "#userNumber")
    LOCATOR_DATE_OF_BIRTH = (By.ID, "dateOfBirthInput")
    LOCATOR_YEAR_OF_BIRTH = (By.XPATH,
                             '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/select')
    LOCATOR_MONTH_OF_BIRTH = (By.XPATH,
                              '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/select')
    LOCATOR_SUBJECTS = (By.ID, "subjectsInput")
    LOCATOR_SPORTS = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[1]/label")
    LOCATOR_READING = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[2]/label")
    LOCATOR_MUSIC = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[7]/div[2]/div[3]/label")
    LOCATOR_UPLOAD_PICTURE = (By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[8]/div[2]/div/input")
    LOCATOR_CURRENT_ADDRESS = (By.ID, "currentAddress")
    LOCATOR_STATE = (By.ID, "state")
    LOCATOR_CITY = (By.ID, "city")
    LOCATOR_SUBMIT = (By.ID, "submit")
    LOCATOR_GOOD_TEST = (By.ID, "example-modal-sizes-title-lg")

    @staticmethod
    def LOCATOR_DAY_OF_BIRTH(day_value):
        return (By.XPATH, f"//div[text()='{day_value}']")

    @staticmethod
    def LOCATOR_STATE_SELECTION(state_value):
        return (By.XPATH, f"//div[contains(text(), '{state_value}')]")

    @staticmethod
    def LOCATOR_CITY_SELECTION(city_value):
        return (By.XPATH, f"//div[contains(text(), '{city_value}')]")


class Helper(BasePage):
    def enter_first_name(self, word):
        first_name = self.find_element(MainLocators.LOCATOR_FIRST_NAME)
        first_name.send_keys(word)
        return first_name

    def enter_last_name(self, word):
        last_name = self.find_element(MainLocators.LOCATOR_LAST_NAME)
        last_name.send_keys(word)
        return last_name

    def enter_email(self, word):
        email = self.find_element(MainLocators.LOCATOR_EMAIL)
        email.send_keys(word)
        return email

    def enter_gender(self, word):
        if word.lower() == "male":
            gender = self.find_element(MainLocators.LOCATOR_GENDER_MALE)
        if word.lower() == "female":
            gender = self.find_element(MainLocators.LOCATOR_GENDER_FEMALE)
        if word.lower() == "other":
            gender = self.find_element(MainLocators.LOCATOR_GENDER_FEMALE)
        gender.click()
        return gender

    def enter_mobile_phone(self, word):
        number = self.find_element(MainLocators.LOCATOR_MOBILE_NUMBER)
        number.send_keys(word)
        return number

    def enter_date_of_birth(self, year, month, day):
        date_of_birth = self.find_element(MainLocators.LOCATOR_DATE_OF_BIRTH)
        date_of_birth.click()

        current_year = Select(self.find_element(MainLocators.LOCATOR_YEAR_OF_BIRTH))
        current_year.select_by_value(str(year))

        current_month = Select(self.find_element(MainLocators.LOCATOR_MONTH_OF_BIRTH))
        current_month.select_by_value(str(int(month) - 1))
        time.sleep(0.1)

        current_day = self.find_element(MainLocators.LOCATOR_DAY_OF_BIRTH(str(day)))
        current_day.click()
        return current_day

    def enter_subjects(self, list_subjects):
        for this_subject in list_subjects:
            subjects = self.find_element(MainLocators.LOCATOR_SUBJECTS)
            subjects.send_keys(this_subject)
            subjects.send_keys(Keys.ENTER)
            time.sleep(0.1)
        return subjects

    def enter_hobbies(self, list_hobbies):
        list_hobbies = [current_hobby.lower() for current_hobby in list_hobbies]
        list_hobbies = list(set(list_hobbies))

        for this_hobbies in list_hobbies:
            if this_hobbies == "sports":
                hobby = self.find_element(MainLocators.LOCATOR_SPORTS)
                hobby.click()
            if this_hobbies == "reading":
                hobby = self.find_element(MainLocators.LOCATOR_READING)
                hobby.click()
            if this_hobbies == "music":
                hobby = self.find_element(MainLocators.LOCATOR_MUSIC)
                hobby.click()
        return hobby

    def upload_picture(self, word):
        picture = self.find_element(MainLocators.LOCATOR_UPLOAD_PICTURE)
        picture.send_keys(word)
        return picture

    def enter_current_address(self, word):
        current_address = self.find_element(MainLocators.LOCATOR_CURRENT_ADDRESS)
        current_address.send_keys(word)
        return current_address

    def enter_state_and_city(self, state, city):
        current_state = self.find_element(MainLocators.LOCATOR_STATE)
        current_state.click()
        current_state = self.find_element(MainLocators.LOCATOR_STATE_SELECTION(state))
        current_state.click()

        current_city = self.find_element(MainLocators.LOCATOR_CITY)
        current_city.click()
        current_city = self.find_element(MainLocators.LOCATOR_CITY_SELECTION(city))
        current_city.click()

        return current_city

    def click_submit(self):
        self.driver.execute_script("document.body.style.transform='scale(0.5)'")
        submit = self.find_element(MainLocators.LOCATOR_SUBMIT)
        submit.click()
        return submit

    def check_result_test(self):
        result_test = self.find_element(MainLocators.LOCATOR_GOOD_TEST)
        if result_test.text == 'Thanks for submitting the form':
            return True
        else:
            return False
