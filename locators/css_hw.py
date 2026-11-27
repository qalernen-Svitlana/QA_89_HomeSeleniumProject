from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # open site на страничке логин
    driver.get("https://telranedu.pages.dev/login") # открывает браузер каждый раз новую страницу
    # input("Press Enter to close the browser...") # необязательно, просто для проверки
    # links = driver.find_element(By.TAG_NAME, "a") # найди элемент по его названию

    # by tag name поиск элементов по тегу <teg
    html = driver.find_element(By.TAG_NAME, "html")
    link = driver.find_element(By.TAG_NAME, "link")

    # by Name
    name_input_1 = driver.find_element(By.NAME, "email") # 0

    a_list = driver.find_elements(By.TAG_NAME, "a") # собирает все элементы
    # print(len(a_list)) # 3
    # h1_list = driver.find_elements(By.TAG_NAME, "h1")
    # print(len(h1_list)) # 1

    # by class ".element" для Selenium
    active = driver.find_element(By.CLASS_NAME, "active") # .active > .product для динамических ID

    # by id "#element" для Selenium
    root = driver.find_element(By.ID, "root")

    # by id list - s на конце метода
    # root_2 = driver.find_elements(By.ID, "root")

    # by tag name поиск элементов по тегу
    html_1 = driver.find_element(By.CSS_SELECTOR, "html")
    link_1 = driver.find_element(By.CSS_SELECTOR, "link")
    a_1 = driver.find_elements(By.CSS_SELECTOR, "a")

    # by class ".element" для Selenium
    active_1 = driver.find_element(By.CSS_SELECTOR, ".active")

    # by id "#element" для Selenium
    root_1 = driver.find_element(By.CSS_SELECTOR, "#root")

    # by id list - s на конце метода
    # root_3 = driver.find_elements(By.CSS_SELECTOR, "#root")

    # by attribute - все, что не определено как класс или айди [placeholder='Email']
    name_input = driver.find_element(By.CSS_SELECTOR, "[placeholder='Email']")

    # по тегу* и атрибуту
    home = driver.find_element(By.CSS_SELECTOR, "[href='/home']")
    name_input_2 = driver.find_element(By.CSS_SELECTOR, "input[name='email']")

    # для driver.get("https://icarro-v1.netlify.app/login")
    # start -> ^
    # starts = driver.find_elements(By.CSS_SELECTOR, ".[class^='login']") # найди элемент по началу имени атрибута
    # end -> $
    # end = driver.find_element(By.CSS_SELECTOR, "[class$='auth-page']") # найди элемент по концу имени атрибута
    # contains -> *
    # contains = driver.find_element(By.CSS_SELECTOR, "[class*='container']") # найди элемент по содержит в имени атрибута
finally:
    driver.quit() # закрывает браузер



# driver.close()
# div>div>form>input - CSS от родителя вниз, с пробелом в конце - до любого уровня