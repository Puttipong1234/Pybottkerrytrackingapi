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

@app.route("/api/kerry/") # /api/kerry?tracking_number="KERPU071401717"
def kerry():
    tracking_number = request.args.get('tracking_number')
    r = Get_data_by_tracking(tracking_number=tracking_number,driver=driver)
    return jsonify(r)

# if __name__ == "__main__":
#     app.run(port=8000,debug=True)
