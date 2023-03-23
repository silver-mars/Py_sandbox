#https://webscraping.pro/extract-browsers-local-storage-with-python/
from selenium import webdriver
driver = webdriver.GoogleChrom()
url='http://is.monitor-utm.ru/'
driver.get(url)
scriptArray="""localStorage.setItem("key1", 'new item');
               localStorage.setItem("key2", 'second item');
				return Array.apply(0, new Array(localStorage.length)).map(function (o, i) { return localStorage.getItem(localStorage.key(i)); }
				)"""
               #localStorage.getItem("
result = driver.execute_script(scriptArray)
print(result)
