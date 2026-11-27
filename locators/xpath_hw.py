from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # open site на страничке логин
    driver.get("https://telranedu.pages.dev/login") # открывает браузер каждый раз новую страницу

    # by tag name поиск элементов по тегу "//teg"
    html = driver.find_element(By.XPATH, "//html")
    div = driver.find_elements(By.XPATH, "//div") # list
    link = driver.find_element(By.XPATH,"//link")
    input_2 = driver.find_element(By.XPATH, "//input")

    a_2 = driver.find_elements(By.XPATH, "//a") # собирает все элементы
    # print(len(a_2)) # 3

    # by class "//a[@class='...']" / "//*[@class='...']"для Selenium
    active = driver.find_element(By.XPATH, "//a[@class='active']")
    form = driver.find_element(By.XPATH,"//*[@class='login_login__3EHKB']")

    # by id "//*[@id='element']" для Selenium
    root = driver.find_element(By.XPATH, "//*[@id='root']")

    # by attribute - все, что не определено как класс или айди "//*[@attribut='...']"
    name_input_4 = driver.find_element(By.XPATH, "//*[@placeholder='Email']")
    # name_input_7 = driver.find_element(By.XPATH, "//*[@name='Login']") # 0 !!!

    # по тегу* и атрибуту "//*[@attribut='/teg']"
    # home_1 = driver.find_element(By.XPATH, "//*[@href='/home']")
    about = driver.find_element(By.XPATH, "//*[@href='/about']")
    # name_input_3 = driver.find_element(By.XPATH, "//input[@name='email']")
    password = driver.find_element(By.XPATH, "//input[@name='password']")

    # by Name
    name_input_5 = driver.find_element(By.XPATH,"//*[text()='Registration']")
    name_input_6 = driver.find_element(By.XPATH, "//*[contains(text(),'Registration')]")

    # by text only xPath
    # login_button = driver.find_element(By.XPATH,"//*[text()='Login']")
    registration_button = driver.find_element(By.XPATH, "//*[text()='Registration']")

    # parent
    div_4 = driver.find_element(By.XPATH, "//h1/..")
    div_5 = driver.find_element(By.XPATH, "//h1/parent::div")
    div_6 = driver.find_element(By.XPATH, "//h1/parent::*")
    div_7 = driver.find_element(By.XPATH, "//h1/ancestor-or-self::*")  # нумерация

    ancestors = driver.find_elements(By.XPATH, "//h1/ancestor::*")
    for ancestor in ancestors:
        print(ancestor.tag_name)
    # html
    # body
    # div
    # div

    # ancestors = driver.find_elements(By.XPATH, "//h1/ancestor::*")
    # for ancestor in ancestors:
    #     print(ancestor.text)

    # ancestor предки на всех вышестоящих уровнях
    # div_9 = driver.find_element(By.XPATH, "//h1/ancestor::*") # всех покажет
    # div_10 = driver.find_element(By.XPATH, "//h1/ancestor::body")
    # div_8 = driver.find_element(By.XPATH, "//h1/ancestor::div[@id='root']")
    div_7 = driver.find_element(By.XPATH, "//a[@href='/login']/preceding-sibling::*")

finally:
    driver.quit() # закрывает браузер

# driver.close()

# //*[@id='root' and @class='container'] найди это и это
# //*[@id='root' or @class='container'] найди это или это

# //div/div/form/input - XPATH от родителя вниз
# //h1/.. - XPATH от ребенка вверх
# //h1/../h1/.. - XPATH от ребенка вверх на два уровня
# //h1/parrent::div -  XPATH от ребенка вверх на один уровень
# //h1/parrent::div/parrent::div -  XPATH от ребенка вверх на два уровня
# //h1/parent::* -  XPATH от ребенка вверх
# //h1/ancestor::div[@id='root'] - предки на всех вышестоящих уровнях
# //h1/following-sibling::* на том же уровне все соседи сверху вниз
# //a[@href='/login']/preceding-sibling::* на том же уровне все соседи снизу вверх
# //a[@href='/login']/preceding-sibling::a[2] на том же уровне все соседи снизу вверх - второй по счету