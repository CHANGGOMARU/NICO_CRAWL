from selenium import webdriver
from datetime import datetime
import os.path

#scriptpath = os.path.dirname(__file__)


#file_name = datetime.today().strftime("%Y/%m/%d")+" 니코링크.txt"

#links = open(datetime.today().strftime("%Y/%m/%d")+" 니코링크.txt", "w")
links = open("니코링크.txt", "w+",encoding='UTF-8')
#filename = os.path.join(scriptpath, file_name)

#links = open(filename , "w+",encoding='UTF-8')

#print(datetime.today().strftime("%Y/%m/%d"))

c = 9
driver = webdriver.Chrome(r'C:\Users\dnsxo\Downloads\chromedriver_file\chromedriver.exe')


address = input("링크 입력")
driver.get(address)


d = ('body > div > div:nth-child(2)')
a = driver.find_elements_by_css_selector(d)
for b in a:
        i = int(b.text.replace("Shared: ","").replace(" tabs","")) - 1




driver.implicitly_wait(10)

while i != 0:
    e = str(c)
    d = ('body > div > div:nth-child('+e+') > a')
    #body > div > div:nth-child(76) > a

    a = driver.find_elements_by_css_selector(d)


    for b in a:
        #b_text = b.text.replace("- ニコニコ動画","")
        #links.write(b_text)
        #links.write("\n")
        links.write(b.get_attribute('href'))
        links.write("\n")
        #links.write("\n \n")

    c = c+1
    i = i-1

driver.quit()
links.close()
