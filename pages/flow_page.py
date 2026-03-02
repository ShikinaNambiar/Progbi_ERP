from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta


class FlowPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # ---------- LOCATORS ----------

    # Login
    company_code_input = (By.ID, "companycode")
    username_input = (By.ID, "signin-username")
    password_input = (By.ID, "signin-password")
    sign_in_button = (By.XPATH, "//button[@type='submit']")
    dashboard_anchor = (By.ID, "nav-home")

    # Sidebar
    crm_menu = (By.ID, "nav-crm")
    create_enquiry_sidebar = (By.ID, "nav-crm-create-enquiry")

    # Form Fields
    branch_dropdown = (By.ID, "branch")
    customer_phone_input = (By.ID, "customer-phone")
    customer_name_input = (By.ID, "TxtCustomer")
    assign_to_dropdown = (By.ID, "assignto")
    next_followup_input = (By.ID, "next-followup-date")

    enquired_for_input = (By.ID, "item-search-input")
    add_item_button = (By.ID, "btn-add-item")
    save_button = (By.ID, "btn-save-enquiry")

    # ---------- WAITS ----------

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    # ---------- LOGIN ----------

    def login(self, company, username, password):
        self.wait_visible(self.company_code_input).send_keys(company)
        self.wait_visible(self.username_input).send_keys(username)
        self.wait_visible(self.password_input).send_keys(password)
        self.wait_clickable(self.sign_in_button).click()
        self.wait_visible(self.dashboard_anchor)

    # ---------- NAVIGATION ----------

    def open_crm_menu(self):
        crm = self.wait_clickable(self.crm_menu)
        self.driver.execute_script("arguments[0].click();", crm)
        self.wait.until(
            EC.visibility_of_element_located(self.create_enquiry_sidebar)
        )

    def click_create_enquiry_sidebar(self):
        enquiry = self.wait_clickable(self.create_enquiry_sidebar)
        self.driver.execute_script("arguments[0].click();", enquiry)

    # ---------- FORM ----------

    def select_branch(self, value):
        Select(self.wait_visible(self.branch_dropdown)).select_by_value(value)

    def enter_customer_phone(self, value):
        field = self.wait_visible(self.customer_phone_input)
        field.clear()
        field.send_keys(value)

    def enter_customer_name(self, value):
        field = self.wait_visible(self.customer_name_input)
        field.clear()
        field.send_keys(value)

    def select_assign_to(self, value):
        Select(self.wait_visible(self.assign_to_dropdown)).select_by_value(value)

    def set_next_followup_auto(self):
        field = self.wait_visible(self.next_followup_input)

        future_time = datetime.now() + timedelta(minutes=2)
        value_to_set = future_time.strftime("%Y-%m-%dT%H:%M")

        self.driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, field, value_to_set)

    def add_enquired_item(self, value):
        field = self.wait_visible(self.enquired_for_input)
        field.clear()
        field.send_keys(value)

        add_button = self.wait_clickable(self.add_item_button)
        self.driver.execute_script("arguments[0].click();", add_button)

    def click_save(self):
        button = self.wait_clickable(self.save_button)
        self.driver.execute_script("arguments[0].click();", button)