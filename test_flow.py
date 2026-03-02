from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.flow_page import FlowPage
import random


def test_flow():

    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://erptest.prog-biz.com")

    wait = WebDriverWait(driver, 40)

    try:
        wait.until(EC.visibility_of_element_located((By.ID, "companycode")))

        page = FlowPage(driver)

        # LOGIN
        page.login("globrootstest", "Sadiqh", "123")
        print("Dashboard loaded")

        # NAVIGATION
        page.open_crm_menu()
        page.click_create_enquiry_sidebar()

        wait.until(EC.visibility_of_element_located((By.ID, "branch")))
        print("Enquiry form loaded")

        # Dynamic phone
        phone = "90765" + str(random.randint(10000, 99999))
        print("Creating enquiry with phone:", phone)

        # FILL FORM
        page.select_branch("1039")
        page.enter_customer_phone(phone)
        page.enter_customer_name("Raghav")
        page.select_assign_to("33518")
        page.set_next_followup_auto()
        page.add_enquired_item("Dubai")

        # SAVE
        page.click_save()

        wait.until(EC.url_contains("enquiry"))
        print("Enquiry flow completed successfully")

    finally:
        driver.quit()