# 1️⃣ Import required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from selenium.webdriver.support import expected_conditions as EC
import time


# 2️⃣ Test data (credentials)
URL = "https://erptest.prog-biz.com"
COMPANY_CODE = "globrootstest"
USERNAME = "Sadiqh"
PASSWORD = "123"


def test_login():
    # 3️⃣ Chrome browser options
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("detach", True)

    prefs = {
        "profile.default_content_setting_values.notifications": 1
    }
    options.add_experimental_option("prefs", prefs)

    # 4️⃣ Open Chrome browser
    driver = webdriver.Chrome(options=options)

    try:
        # 5️⃣ Open ERP website
        driver.get(URL)

        # 6️⃣ Wait until Company Code field is visible
        wait = WebDriverWait(driver, 20)

        # 7️⃣ Enter Company Code
        company_code_field = wait.until(
            EC.visibility_of_element_located((By.ID, "companycode"))
        )
        company_code_field.send_keys(COMPANY_CODE)

        # 8️⃣ Enter Username
        username_field = driver.find_element(By.ID, "signin-username")
        username_field.send_keys(USERNAME)

        # 9️⃣ Enter Password
        password_field = driver.find_element(By.ID, "signin-password")
        password_field.send_keys(PASSWORD)

        # 🔟 Click Login button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # 1️⃣1️⃣ Wait to see result
        time.sleep(6)

        print("✅ Login test executed successfully")

        #Click on createbutton
        wait = WebDriverWait(driver, 15)

        create_new_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Create New')]"))
        )
        create_new_btn.click()
        time.sleep(2)

        enquiry_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='enquiry']"))
        )
        enquiry_option.click()
        wait.until(EC.url_contains("enquiry"))
        time.sleep(5)
                    # Branch(2nd option or first)
    # ===============================
    branch_dropdown = Select(
        wait.until(EC.element_to_be_clickable((By.ID, "branch")))
    )

    if len(branch_dropdown.options) > 1:
        branch_dropdown.select_by_index(1)
    else:
        branch_dropdown.select_by_index(0)

    # ===============================
    # Phone Number
    # ===============================
    phone_input = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Enter phone number and search']")
        )
    )
    phone_input.send_keys("9856232001")

    # ===============================
    # Customer Name
    # ===============================
    customer_name = driver.find_element(
        By.XPATH, "//input[@placeholder='Customer Name']"
    )
    customer_name.send_keys("Amstard")

    # ===============================
    # Assign To (2nd person)
    # ===============================
    assign_to = Select(
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'form-select')]"))
        )
    )

    if len(assign_to.options) > 1:
        assign_to.select_by_index(1)

    # ===============================
    # Next Follow-up Date (Today + 2 days)
    # ===============================
    future_date = (datetime.today() + timedelta(days=2)).strftime("%d-%m-%Y %I:%M %p")

    followup_date = driver.find_element(
        By.XPATH, "//input[contains(@placeholder,'Date')]"
    )
    followup_date.clear()
    followup_date.send_keys(future_date)

    # ===============================
    # Lead Quality (7th → 70%)
    # ===============================
    lead_quality = Select(
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'form-select')]"))
        )
    )

    if len(lead_quality.options) >= 7:
        lead_quality.select_by_index(6)

    # ===============================
    # Lead Source → Facebook
    # ===============================
    lead_source = Select(
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'form-select')]"))
        )
    )
    lead_source.select_by_visible_text("Facebook")

    # ===============================
    # Custom Field Test → Yes (2nd option)
    # ===============================
    custom_field = Select(
        wait.until(
            EC.element_to_be_clickable((By.XPATH, "//select[contains(@class,'form-select')]"))
        )
    )

    if len(custom_field.options) > 1:
        custom_field.select_by_index(1)

    # ===============================
    # Enquiry Search → Austria (3rd option)
    # ===============================
    enquiry_search = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@placeholder='Search Item Name']")
        )
    )
    enquiry_search.send_keys("Austria")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(text(),'Austria')]")
        )
    ).click()

    # ===============================
    # Save Button
    # ===============================
    save_button = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(),'Save')]")
        )
    )
    save_button.click()

    finally:

        pass
############################################################################################################################
