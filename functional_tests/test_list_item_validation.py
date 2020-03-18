from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
    
        # The browser intercepts the request, and does not load the
        # list page
        self.wait_for(
            lambda: self.browser.find_element_by_css_selector(
                '#id_text:invalid' 
        ))
<<<<<<< HEAD
        
        # She starts typing some text for the new item and the error disappears
        self.get_item_input_box().send_keys('Buy milk')    
        self.wait_for(
            lambda: self.browser.find_element_by_css_selector(
                '#id_text:valid' 
        ))
         
        # And she can submit it successfully
        self.get_item_input_box().send_keys(Keys.ENTER)   
=======

        # She tries again with some text for the item, which now work
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')    
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)    
>>>>>>> parent of fb533f7... rename all item input ids and names. still broken"
        self.wait_for_row_in_list_table('1: Buy milk')

        
        # Perversely, she now decides to submit a second blank list item    
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        # Again, the browser will not comply 
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for(
            lambda: self.browser.find_element_by_css_selector(
            '#id_text:invalid'
        ))

        
        # And she can correct it by filling some text in    
<<<<<<< HEAD
        self.get_item_input_box().send_keys('Make tea')   
        self.wait_for(
            lambda: self.browser.find_element_by_css_selector(
                '#id_text:valid' 
        ))
        self.get_item_input_box().send_keys(Keys.ENTER)    
=======
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea')    
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)    
>>>>>>> parent of fb533f7... rename all item input ids and names. still broken"
        self.wait_for_row_in_list_table('1: Buy milk')    
        self.wait_for_row_in_list_table('2: Make tea')