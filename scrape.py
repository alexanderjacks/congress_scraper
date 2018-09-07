from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome('./chromedriver')

# surf Incognito to scrape better
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# launch Chrome
browser = webdriver.Chrome(executable_path='./chromedriver', chrome_options=option)
# surf to this URL; use one of these at a time for now
# browser.get("https://www.congress.gov/members?q={%22congress%22:%22115%22}&pageSize=250")
# browser.get("https://www.congress.gov/members?q=%7B%22congress%22%3A%22115%22%7D&pageSize=250&page=2")
browser.get("https://www.congress.gov/members?q=%7B%22congress%22%3A%22115%22%7D&pageSize=250&page=3")

###############################
### timeout, error handling ###
timeout = 30
try:
	# checking for element in nav to load
	WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//a[@accesskey='5']")))
except TimeoutException:
	print("Page takes too long to load-- try again")
	browser.quit()
##############################

# grabbing last names from .gov
# want the <a> element after span class 'result-heading'
congress_names_page1 = browser.find_elements_by_xpath("//a/ancestor::span[@class='result-heading']")
# parsing returned objects into desired items ('list comprehension')
congressppl = [x.text for x in congress_names_page1]

# grabbing party affiliation from .gov
# element immediately after 'Party' key field
congress_partys_page1 = browser.find_elements_by_xpath("//strong[text()='Party:']/following-sibling::span")
# parsing returned objects into desired items ('list comprehension')
partys = [x.text for x in congress_partys_page1]

### ought to make factory function for above, cuz here's a 3rd copy

# grabbing img src from .gov
# src prop of img element; ancestor div class = "member-image" 
congress_imgs_page1 = browser.find_elements_by_xpath("//img")
# parsing returned objects into desired items ('list comprehension')
imgs = [x.get_attribute('src') for x in congress_imgs_page1]


# display congresspersons in terminal
print('Congress members w/ party from Current 115th House/Senate:')
# print(congressppl)
# print(partys)

# # combine and match array elements
for person, party, img in zip(congressppl, partys, imgs):
	print(person + ": " + party + ": " + img)



