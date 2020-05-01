from selenium import webdriver
import os
from bs4 import BeautifulSoup

def Get_data_by_tracking(tracking_number,driver):
    driver.get("https://th.kerryexpress.com/th/track/")
    res = {}
    try:
        import time
        inputElement = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/input')
        inputElement.send_keys(tracking_number)
        button = driver.find_element_by_id('btnSubmit').click()
        time.sleep(1)
        try:
            data = driver.find_element_by_xpath('/html/body/div[3]/div')
            คาดว่าจะถึงวันที่ = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div[2]')
            ผู้ส่ง = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div[4]')
            ผู้รับ = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div[5]')
            
            soup = BeautifulSoup(data.get_attribute('innerHTML'),features="lxml")
            date = soup.findAll("div", {"class": "date"})
            description = soup.findAll("div", {"class": "d1"})
            location = soup.findAll("div", {"class": "d2"})
            
            res['คาดว่าจะถึงวันที่'] = คาดว่าจะถึงวันที่.text.replace("คาดว่าจะถึงวันที่: ","")
            res['ผู้ส่ง'] = ผู้ส่ง.text.replace("ผู้ส่ง: ","")
            res['ผู้รับ'] = ผู้รับ.text.replace("ผู้รับ: ","")
            
            date_clean = []
            time_clean = []
            for i in date:
                r = i.text.replace("\n","").split("Time")
                date_clean.append(r[0])
                time_clean.append(r[1])
                
            description_clean = [i.text.split("\n")[1].strip() for i in description]
            location_clean = [i.text for i in location]
            info = []
            for date,time,des,location in zip(date_clean,time_clean,description_clean,location_clean):
                r = { "date" : date ,
                    "time":time ,
                    "description" : des ,
                    "location" : location}
                
                info.append(r)
            
            res["info"] = info
            return res
        except :
            return "Shipment Not Found!"
        
    finally:
        driver.quit()
        

#TEST

# if __name__ == '__main__':

#     driver = webdriver.Chrome('C:/Users/SAMPLE/Downloads/chromedriver_win32/chromedriver.exe')
#     r = Get_data_by_tracking(tracking_number="KERPU071401717",driver=driver)
#     print(r)
