from time import sleep
import os

try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By 
except:
    print("Requirment not Satisfied")
    choice=input("Do you want to install selenium(y/n): ")
    if(choice.lower()=="y"):
        os.system("pip install selenium")
    else:
        print("Download necessary files, using command ( pip install selenium )")
    sleep(5)
    quit()
try:
    driver=webdriver.Chrome()
    driver.maximize_window()
except:
    print('Download ChromeDriver, of same version as of Chrome and place the chromedriver.exe file in Same directory as of this file')
    print('download from here: https://chromedriver.chromium.org/downloads')
    sleep(10)
    quit()

def getdata():
    page="following"  #choose "following" or "followers"
    account="shirley.setia"     #enter username of person whose following you want
    driver.get("https://www.instagram.com/accounts/login/?next=/")
    sleep(3)
    driver.find_element_by_xpath('//*[@name="username"]').send_keys("")  #Enter your username
    driver.find_element_by_xpath('//*[@name="password"]').send_keys("")  #Enter your password
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    element=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')))
    element.click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    sleep(1)

    driver.get('https://www.instagram.com/%s' % account)
    sleep(2)
    driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
    txt=driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).text
    count=int(txt.split()[0])
    print(page," : ",count)
    sleep(2)
    list_h=[]

    path="F:\\" + account + ".txt"  #Enter path where you want to save txt file

    file=open(r"%s"%path,"w")
    for i in range(1,count+1):
        src=driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[%s]'% i)
        driver.execute_script("arguments[0].scrollIntoView();", src)
        if page=="following":
            if(i%10==0):
                sleep(1)
        else:
            if(i%20==0):
                sleep(1)
        txt=src.text
        name=txt.split()[0]
        file.write(str(i)+"    "+name+"\n")
        list_h.append(name)
    file.close()
    driver.quit()
    print (list_h)


getdata()
