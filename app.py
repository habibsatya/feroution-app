import mysql.connector
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import torch
import cv2

app = Flask(__name__)

# app.secret_key = "caircocoders-ednalan"

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'db_feroution'
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
# mysql = MySQL(app) 

app.config['UPLOAD_FOLDER'] = 'static/img'

mydb = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7584011",
    password="2vVGSET8kh",
    database="sql7584011"
)


@app.route('/', methods=['GET', 'POST'])
def main():
    
    if request.method == 'GET':
        cursor = mydb.cursor()
        cursor.execute("SELECT DISTINCT label FROM mytable ORDER BY label ASC")
        mytable = cursor.fetchall()  
        print(mytable)
        return render_template('index.html', mytable=mytable)

    elif request.method == 'POST':
        model1 = torch.hub.load("yolo", 'custom', path="best.pt", source='local')
        model2 = joblib.load("stacking-model.pkl")

        a = request.form.get('optradio')
        a = int(a)

        b = request.form.get('umur')
        b = int(b)

        img = request.files['photo']
        img_path = app.config['UPLOAD_FOLDER']+img.filename
        img.save(img_path)

        img = cv2.imread(img_path)
        results = model1(img)
        classes = np.array(results.pandas().xyxy[0])
        classes = classes[0][5]
        if classes == 0:
            classes = 2
        elif classes == 1:
            classes = 0
        else:
            classes = 1

        features = [[a, b, classes]]
        result = model2.predict(features)
        label = {
            '0': 'normal-jerawat',
            '1': 'normal-komedo',
            '2': 'normal-bopeng',
            '3': 'berminyak-jerawat',
            '4': 'berminyak-komedo',
            '5': 'berminyak-bopeng',
            '6': 'kering-jerawat',
            '7': 'kering-komedo',
            '8': 'kering-bopeng',
            '9': 'kombinasi-jerawat',
            '10': 'kombinasi-komedo',
            '11': 'kombinasi-bopeng',
            '12': 'sensitif-jerawat',
            '13': 'sensitif-komedo',
            '14': 'sensitif-bopeng',
        }
        result = label[str(result[0])]

        if result == "normal-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'normal-jerawat' ")
            data = cursor.fetchall()
            kulit = "Normal"
            masalah = "jerawat"

        elif result == "normal-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'normal-poribesar' ")
            data = cursor.fetchall()
            kulit = "Normal"
            masalah = "Pori - pori besar"

        elif result == "normal-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'normal-komedo' ")
            data = cursor.fetchall()
            kulit = "Normal"
            masalah = "Komedo"

        elif result == "normal-bopeng":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'normal-bopeng' ")
            data = cursor.fetchall()
            kulit = "Normal"
            masalah = "Bopeng"

        elif result == "berminyak-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'berminyak-jerawat' ")
            data = cursor.fetchall()
            kulit = "Berminyak"
            masalah = "Jerawat"

        elif result == "berminyak-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'berminyak-poribesar' ")
            data = cursor.fetchall()
            kulit = "Berminyak"
            masalah = "Pori - pori besar"

        elif result == "berminyak-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'berminyak-komedo' ")
            data = cursor.fetchall()
            kulit = "Berminyak"
            masalah = "Komedo"

        elif result == "berminyak-bopeng":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'berminyak-bopeng' ")
            data = cursor.fetchall()
            kulit = "Berminyak"
            masalah = "Bopeng"

        elif result == "kering-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'kering-jerawat' ")
            data = cursor.fetchall()
            kulit = "Kering"
            masalah = "Jerawat"

        elif result == "kering-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'kering-poribesar' ")
            data = cursor.fetchall()
            kulit = "Kering"
            masalah = "Pori - pori besar"

        elif result == "kering-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'kering-komedo' ")
            data = cursor.fetchall()
            kulit = "Kering"
            masalah = "Komedo"

        elif result == "kering-bopeng":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'kering-bopeng' ")
            data = cursor.fetchall()
            kulit = "Kering"
            masalah = "Bopeng"

        elif result == "kombinasi-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'kombinasi-jerawat' ")
            data = cursor.fetchall()
            kulit = "Kombinasi"
            masalah = "Jerawat"

        elif result == "kombinasi-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'kombinasi-poribesar' ")
            data = cursor.fetchall()
            kulit = "Kombinasi"
            masalah = "Pori - pori besar"

        elif result == "kombinasi-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'kombinasi-komedo' ")
            data = cursor.fetchall()
            kulit = "Kombinasi"
            masalah = "Komedo"

        elif result == "kombinasi-bopeng":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'kombinasi-bopeng' ")
            data = cursor.fetchall()

        elif result == "sensitif-jerawat":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'sensitif-jerawat' ")
            data = cursor.fetchall()
            kulit = "Sensitif"
            masalah = "Jerawat"

        elif result == "sensitif-poribesar":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'sensitif-poribesar' ")
            data = cursor.fetchall()
            kulit = "Sensitif"
            masalah = "Pori - pori besar"

        elif result == "sensitif-komedo":
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'sensitif-komedo' ")
            data = cursor.fetchall()
            kulit = "Sensitif"
            masalah = "Komedo"

        else:
            cursor = mydb.cursor()
            cursor.execute(
                "SELECT product_name, brand, img_url, price, category FROM mytable WHERE label = 'sensitif-bopeng' ")
            data = cursor.fetchall()
            kulit = "Sensitif"
            masalah = "Bopeng"

        return render_template('index.html', data=data, result=result, kulit=kulit, masalah=masalah)

    # def fetchrecords():
    #     cursor = mydb.connection.cursor(MySQLdb.cursors.DictCursor)
    #         # cursor = mydb.cursor(MySQLdb.cursors.DictCursor)
    #     if request.method == 'POST':
    #         query = request.form['query']
    #         #print(query)
    #         if query == '':
    #             cursor.execute("SELECT * FROM mytable ORDER BY product_id DESC")
    #             employeelist = cursor.fetchall()
    #             print('all list')
    #         else:
    #             search_text = request.form['query']
    #             print(search_text)
    #             cursor.execute("SELECT * FROM mytable WHERE label IN (%s) ORDER BY product_id DESC", [search_text])
    #             employeelist = cursor.fetchall()  
    #     return jsonify({'htmlresponse': render_template('response.html', employeelist=employeelist)})
    

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
