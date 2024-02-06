import time
import re
from MainPage import Helper

def test_page(browser):
    main_page = Helper(browser)
    main_page.go_to_site()
    pattern_for_email_validate = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    first_name = "Aleksandr"
    last_name = "Bogdashkin"
    email = "bogdash999@gmail.com"

    assert bool(re.match(pattern_for_email_validate, email))==True, 'Тест не пройден, т.к. вы ввели невалидную почту '

    gender = "Male"
    mobile = "9608299999"

    assert len(mobile)==10, 'Тест не пройден. В номере должно быть строго 10 цифр'

    year_birth = 1999
    month_birth = 10
    day_birth = 13
    subjects = ("Maths", "Computer Science", "English")
    hobbies = ("Sports", "Music")
    picture = "D:\PycharmProjects\SDET_test_task\photo_2022-12-24_14-31-23.jpg"
    current_address = "Samara, Lenina str, 1-2"
    state = "Haryana"
    city = "Karnal"

    main_page.enter_first_name(first_name)
    main_page.enter_last_name(last_name)
    main_page.enter_email(email)
    main_page.enter_gender(gender)
    main_page.enter_mobile_phone(mobile)
    main_page.enter_date_of_birth(year_birth, month_birth, day_birth)
    main_page.enter_subjects(subjects)
    main_page.enter_hobbies(hobbies)
    #time.sleep(20)
    main_page.upload_picture(picture)
    main_page.enter_current_address(current_address)
    main_page.enter_state_and_city(state, city)
    main_page.click_submit()
    time.sleep(1)
    assert main_page.check_result_test() == True, "Тест не пройден корректно"
