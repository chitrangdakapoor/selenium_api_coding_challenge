class Login():

    def __init__(self, driver):
        self.driver = driver
        self.signin_button_class = "login"
        self.username_textbox_id = "email"
        self.password_textbox_id = "passwd"
        self.submit_button_id = "SubmitLogin"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_signin_button(self):
        self.driver.find_element_by_class_name(self.signin_button_class).click()

    def click_on_submit(self):
        self.driver.find_element_by_id(self.submit_button_id).click()
