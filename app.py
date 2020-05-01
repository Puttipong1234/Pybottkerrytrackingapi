import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from selenium import webdriver

from Kerry import Get_data_by_tracking

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['JSON_AS_ASCII'] = False

@app.route("/api/kerry/")
def kerry():
    # step 1 ทำการรับ args เลขพัสดุ มาจาก url ที่ใช้เรียก เช่น /api/kerry?tracking_number="123456789"
    tracking_number = request.args.get('tracking_number')
    # step 2 ทำการนำค่าที่รับมาจาก url ใส่ลงใน function จากไฟล์ Kerry.py
    try:
        r = Get_data_by_tracking(tracking_number=tracking_number,driver=driver)
        return jsonify(r)
    except:
        return jsonify("ขออภัยคะ server กำลังปิดปรับปรุง")
    # step 3 ส่งค่าที่ได้จากการค้นหา เลขพัสดุ กลับไปแสดงที่ client side
    

# if __name__ == "__main__":
#     app.run(port=8000,debug=True)
