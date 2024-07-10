
import joblib 
import numpy as np;
import pandas as pd;
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
gmail_list=[]
password_list=[]
gmail_list1=[]
password_list1=[]
import numpy as np;
import pandas as pd;
import matplotlib.pyplot  as plt;
from sklearn.model_selection  import train_test_split
from sklearn.linear_model  import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
import pickle
from flask import Flask, request, render_template, redirect, url_for,send_file
import joblib
import csv
import os
import cv2
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

import refresh_code
import hashlib
import qrcode

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import binascii
import random
#from email_sender import otp_sender
from block1 import protect_data

# Function to load keys from files
def load_keys():
    with open("private_key.pem", "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
            backend=default_backend()
        )

    with open("public_key.pem", "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
            backend=default_backend()
        )

    return private_key, public_key








def check_hash_code_in_csv(hash_code):
    # Open the data.csv file and check if the hash code is present in the "hash_code" column
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['hash_code'] == hash_code:
                return True
    return False
#from recamandation_code import recondation_fn
#from recamandation_code_fh import recondation_fn_fh

app = Flask(__name__)


@app.route('/')
def home(): 
    return render_template('index-demo-2.html') 



@app.route('/nextpage')
def nextpage():

    return render_template('login23.html')

@app.route('/nextpage2')
def nextpage2():
    print("nothing")
    # Name of the file to modify
    file_name = 'refresh_code.py'

    # Import statement to add
    import_statement = 'import numpy as np\n'

    # Read the existing content of the file
    with open(file_name, 'r') as file:
        content = file.read()

    # Add the import statement at the beginning of the content
    modified_content = import_statement + content

    # Write the modified content back to the file
    with open(file_name, 'w') as file:
        file.write(modified_content)

    print(f"Added 'import numpy as np' to {file_name}")



    return render_template('buyer.html')




@app.route('/logedin',methods=['POST'])
def logedin():
    
    int_features3 = [str(x) for x in request.form.values()]
    print(int_features3)
    logu=int_features3[0]
    passw=int_features3[1]
   # if int_features2[0]==12345 and int_features2[1]==12345:

    return render_template('product_details.html')    

@app.route('/crop')
def crop():
     return render_template('index23.html') 


@app.route('/crop2')
def crop2():
    return render_template('buyer.html')                     



@app.route('/download')
def download_file():
    path = "output.png"
    return send_file(path, as_attachment=True)





@app.route('/crop/predict1',methods=['POST'])




def predict1():
    '''
    For rendering results on HTML GUI
    '''
    int_features1 = [str(x) for x in request.form.values()]

    # Combine all details into a single string
    brand = int_features1[0]
    product_id = int_features1[1]
    date_of_manufacture = int_features1[2]
    batch = int_features1[3]
    price = int_features1[4]
    product_type = int_features1[5]

    product_details = f"{brand}{product_id}{date_of_manufacture}{batch}{price}{product_type}"

    # Generate a hash code using SHA-256
    hash_code = hashlib.sha256(product_details.encode()).hexdigest()

    #print(hashed_password)

    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization, hashes
    import binascii

    # Load keys from files
    hashed_password=hash_code
    loaded_private_key, loaded_public_key = load_keys()
    #message =hashed_password
    message =hashed_password.encode()  # Convert string to bytes

    # Encrypt using loaded public key
    ciphertext = loaded_public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Decrypt using loaded private key
    plaintext = loaded_private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("Original message:", message.decode())
    print("first block encrypted  message:", ciphertext)


    result=protect_data(ciphertext)
    #print("Decrypted message:", plaintext.decode())

    print("encrpted and hashed output after all blocks",result)




    

    # Check if the data.csv file exists, create it if not
    if not os.path.exists('data.csv'):
        with open('data.csv', mode='w', newline='') as file:
            fieldnames = ['brand', 'product_id', 'date_of_manufacture', 'batch', 'price', 'product_type', 'hash_code']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    # Check if the product with the same hash code is already present in the CSV file
    with open('data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['hash_code'] == hash_code:
                return render_template('product_details.html', alert_text="Product is already added to the database")

    # If the product is not present, add it to the CSV file
    with open('data.csv', mode='a', newline='') as file:
        fieldnames = ['brand', 'product_id', 'date_of_manufacture', 'batch', 'price', 'product_type', 'hash_code']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write a new row with the product details and hash code
        writer.writerow({
            'brand': brand,
            'product_id': product_id,
            'date_of_manufacture': date_of_manufacture,
            'batch': batch,
            'price': price,
            'product_type': product_type,
            'hash_code': hash_code
        })

    # Generate a QR code and save it as you were doing before
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(hash_code)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(str(product_id)+".png")
    img.save("output.png")


    return render_template('qr_download.html')

    

   # return render_template('otp_verification.html')


@app.route('/crop1/predict23',methods=['POST'])
def predict23():
    '''
    For rendering results on HTML GUI
    '''

    # Initialize the webcam
    cap = cv2.VideoCapture(0)  # 0 for the default camera

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Detect and decode the QR code in the frame
        detector = cv2.QRCodeDetector()
        decoded_info, points, straight_qrcode = detector.detectAndDecode(frame)

        # If a QR code is detected, check the CSV file for the hash code
        if decoded_info:

            
            print("Decoded QR Code Data:")
            print(decoded_info)

            # Read data from the CSV file
            with open('data.csv', 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    if row['hash_code'] == decoded_info:
                        # Return product details from the CSV file
                        #print("Buyer data is safe")  
                        #break
                        return render_template('verified_data.html', alert_text1="Product is Verified-- Details", product_details=row)

            # If the hash code is not found in the CSV file
            return render_template('verified_data1.html', alert_text1="Product is Fake")

        # Display the frame with detected QR code (optional)
        cv2.imshow("QR Code Scanner", frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close OpenCV windows 
    print("Buyer data is safe")
    cap.release()
    cv2.destroyAllWindows()

    #print("Buyer data is safe") 


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.cache = {}
    app.run(debug=True)
