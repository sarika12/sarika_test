from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from unittest import TestCase
#
# driver=webdriver.Chrome()
# driver.get("https://letskodeit.teachable.com/p/practice")
# try:
#     element=WebDriverWait(driver,10).until(expected_conditions.title_is((By.TAG_NAME,"Practice Page")))
# finally:
#     driver.quit()

# import unittest
# from selenium import webdriver
# import page
# class PythonOrgSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver=webdriver.Chrome()
#         self.driver.get("http://www.python.org")
#
#     def test_search_in_python_org(self):
#         main_page=page.MainPage(self.driver)
#         assert main_page.is_tite_matches()

print("action chain")
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://letskodeit.teachable.com/p/practice")
#
# menu = driver.find_element_by_css_selector("#show-textbox")
# print (menu)
# hidden_submenu = driver.find_element_by_css_selector("#hide-textbox")
#
# actions = ActionChains(driver)
# actions.move_to_element(menu).send_keys(Keys.F5)
#
#
# actions.click(hidden_submenu)
# actions.perform()
# driver.close()
print ("CSS and maximum windows ")
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://letskodeit.teachable.com/p/practice")
#
# get_text = driver.find_element_by_css_selector("#displayed-text").send_keys("elements")
# print (get_text)
#
# test_1=TestCase.assertEqual(get_text,"elements","if not equal")
# print (test_1)

print("something")
# for i in range(2,2):
#     print (i)


# 1^1+ 2^2+ 3^3+ ... + 10^10=10405071317

sum = 0
for i in range(1, 13):
    sum = sum + pow(i, i)
print (sum)
n = sum
a = []
b = []
i = 0
while i < 10:
    rem = n % 10
    rem=int(rem)
    a.append(rem)
    n = n / 10
    i = i + 1
#print(a)# print the list of elements
i = 9
# reversed the list
while i >= 0:
    b.append(a[i])
    i = i - 1
#print b # print the reveresd elemets
for i in b:
    print (i ,end='')



