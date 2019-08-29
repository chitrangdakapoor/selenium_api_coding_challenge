import time

from selenium.webdriver import ActionChains


class Order():

    def __init__(self, driver):
        self.driver = driver
        self.women_category_xpath = '//*[@title="Women"]'
        self.add_to_cart_xpath = "//span[text()='Add to cart']"
        self.continue_shopping_xpath = '//*[@title="Continue shopping"]'
        self.proceed_to_checkout_title_xpath = '//*[@title="Proceed to checkout"]'
        self.proceed_to_checkout_span_xpath = "//span[text()='Proceed to checkout']"
        self.accept_order_id = "cgv"
        self.process_order_name = "processCarrier"
        self.product_list_frame_xpath = '//*[@id="center_column"]/ul'
        self.item_list_tagname  = "li"

    def click_women_subcategory(self):
        self.driver.find_element_by_xpath(self.women_category_xpath).click()

    def get_list_of_items(self):
        element = self.driver.find_element_by_xpath(self.product_list_frame_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        html_list = self.driver.find_element_by_xpath(self.product_list_frame_xpath)
        items = html_list.find_elements_by_tag_name(self.item_list_tagname)
        return items

    def select_items(self, product_items, number_of_items):
        for index in range(number_of_items):
            product_items[index].click()
            self.driver.find_element_by_xpath(self.add_to_cart_xpath).click()
            if index <= number_of_items -2: self.driver.find_element_by_xpath(self.continue_shopping_xpath).click()
            time.sleep(1)

        self.driver.find_element_by_xpath(self.proceed_to_checkout_title_xpath).click()
        time.sleep(1)
        for count in range(2):
                self.driver.execute_script("window.scrollTo(0, 2000)")
                self.driver.find_element_by_xpath(self.proceed_to_checkout_span_xpath).click()

        self.driver.execute_script("window.scrollTo(0, 2000)")
        self.driver.find_element_by_id(self.accept_order_id).click()
        self.driver.find_element_by_name(self.process_order_name).click()
