from selenium import webdriver
from selenium.webdriver.common.by import By
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_name = "file_example.txt"  
file_path = os.path.join(current_dir, 'file.txt')           
element.send_keys(file_path)


# запускается из файла, туда надо положить этот код, прописать путь к директории и положить туда файл