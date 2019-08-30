from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import json
import time
import unittest
from Pages.Login import Login
from Pages.Order import Order

class OrderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        CONFIG_PATH = os.path.join(ROOT_DIR, 'Config//login.json')
        with open(CONFIG_PATH) as config_file:
            config = json.load(config_file)
        cls.username = config["username"]
        cls.password = config["password"]

        cls.driver = webdriver.Chrome(executable_path="Drivers//chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get("http://automationpractice.com/index.php")
        loginObj = Login(self.driver)
        loginObj.click_signin_button()
        loginObj.enter_username(self.username)
        loginObj.enter_password(self.password)
        loginObj.click_on_submit()

    def test_ShouldBeAbleToPlaceOrderWithTwoItemsInTheCart(self):
        orderObj = Order(self.driver)
        orderObj.click_women_subcategory()
        items = orderObj.get_list_of_items()
        orderObj.select_items(items, 2)
        self.assertIsNotNone("Test for Order 2 items")


    def tearDown(self):
        self.driver.find_element_by_class_name("logout").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
