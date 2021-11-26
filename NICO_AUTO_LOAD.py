from selenium import webdriver
import time


driver = webdriver.Chrome(r'여기에 크롬 웹드라이버가 설치된 경로를 입력해주세요.')



links = open("니코링크.txt", "r",encoding='UTF-8')

fin_list = open("완료 리스트.txt","w+",encoding='UTF-8')

driver.implicitly_wait(10)

#z = 'https://www.nicovideo.jp/watch/sm39659560?ref=search_key_video&playlist=eyJ0eXBlIjoic2VhcmNoIiwiY29udGV4dCI6eyJrZXl3b3JkIjoiVm9jYWxvaWQiLCJzb3J0S2V5IjoicmVnaXN0ZXJlZEF0Iiwic29ydE9yZGVyIjoiZGVzYyIsInBhZ2UiOjYsInBhZ2VTaXplIjozMiwibWluUmVnaXN0ZXJlZEF0IjoiMjAyMS0xMS0yMVQwMDowMDowMCswOTowMCIsIm1heFJlZ2lzdGVyZWRBdCI6IjIwMjEtMTEtMjNUMjM6NTk6NTkrMDk6MDAiLCJnZW5yZXMiOiJtdXNpY19zb3VuZCJ9fQ&ss_pos=3&ss_id=32c2f1ff-df38-4042-8c94-3798dc2bb362'
#driver.get(z[0:41])

#a = driver.find_element_by_css_selector('#js-app > div > div.WatchAppContainer-main > div.HeaderContainer > div.HeaderContainer-topArea > div.HeaderContainer-topAreaLeft > h1')

while True:
    line = links.readline()
    
    if not line: break
    driver.get(line[0:41])

    
    try:
        driver.find_element_by_css_selector('body > div.BaseLayout-main > div.WatchExceptionPage > section.ErrorMessage.WatchExceptionPage-message > h1')
        continue
    except:
        pass

    a = driver.find_element_by_css_selector('#js-app > div > div.WatchAppContainer-main > div.HeaderContainer > div.HeaderContainer-topArea > div.HeaderContainer-topAreaLeft > h1')

    time.sleep(12)



    fin_list.write(a.text)
    fin_list.write("\n")
    fin_list.write(driver.current_url)
    fin_list.write("\n")
    fin_list.write("\n \n")


    
fin_list.close()
links.close()
driver.quit()





#print(a.text)

#print(driver.current_url)
