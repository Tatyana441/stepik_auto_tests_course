from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("document.title='Название страницы';alert('Robots at work');")