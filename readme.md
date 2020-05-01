## Source Code Pybott Kerry Parcel Tracking API
แจกจ่ายเพื่อการเรียนรู้วิธีการสร้าง Web API ร่วมกับ Web Scraping ด้วย Selenium และ Beutiful Soup
เหมาะสำหรับในกรณีเว็บที่มีการผสมผสานการทำงาน Javascript ไม่สามารถ request แบบธรรมดาได้
สามารถนำไปใส่งานกับ Web track พัสดุทั่วๆไปได้ เช่น scg express / dhl express / lazada express และอื่นๆ

ทดลอง https://kerryapi.herokuapp.com/api/kerry/?tracking_number=<เลขพัสดุ>

![alt text](https://i.ibb.co/YBB8xTk/4.png)

## วิธีการใช้งาน
1. cmd > git clone https://github.com/Puttipong1234/Pybottkerrytrackingapi.git
2. สร้าง virtual env 
```
python -m venv venv (use python 3.6.8 - 3.6.10)
```
3. activate virtual evironment 
```
(window : venv\Scripts\activate / mac : source venv\bin\activate)
```
3. pip install -r requirements.txt
4. python app.py (รันแอพ)
5. deploy to heroku พร้อมตั้งค่า config local variable ง่ายๆ ให้ดูจากบทความนี้นะครับ https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/

## หลักการ
 - ที่ไฟล์ Kerry.py จะเป็นวิธีการ scrap ข้อมูลจากเว็บไซต์ ตรวจพัสดุ โดยใช้ selenium + bs4
 - app.py จะเป็นการสร้าง WEB API ง่ายๆด้วย Flask 
 - การ Deploy ให้ดูจากบทความนี้นะครับ https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/ โดยเป็น Deploy ขึ้นไปบน heroku

#### ฝากติดตาม กดไลค์ กดแชร์ คอนเทน เพื่อเป็นกำลังใจแก่ทีมงานด้วยนะครับขอบพระคุณอย่างสูง
