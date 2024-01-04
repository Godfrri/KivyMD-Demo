#! Youtube Video
# https://youtu.be/f_3YFEEovCc?si=RA8e3ZM1RtRe1jn3

import pyrebase
from getpass import getpass


firebaseConfig = {
    "apiKey": "AIzaSyB1M-p6zClTO5cN4IrX7TzkATbbD1uGEPY",
    "authDomain": "agro-farm-bea51.firebaseapp.com",
    "databaseURL": "https://agro-farm-bea51-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "agro-farm-bea51",
    "storageBucket": "agro-farm-bea51.appspot.com",
    "messagingSenderId": "709059373191",
    "appId": "1:709059373191:web:ba4c65f113fb34f19b7022",
    "measurementId": "G-0Y5HDBNWZ0"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
email = 'nixongodfrricroos@gmail.com'
password = 'ocnOIJ028021@ww'

#? Create User
# user = auth.create_user_with_email_and_password(email, password)

#? Login to user
# login = auth.sign_in_with_email_and_password(email, password)

#! for this, dont type the password, we can aprove by email for login
#? Send Email verification
# auth.send_email_verification(login['idToken'])

#? Reset Password
# auth.send_password_reset_email(email)

print('Sucess....')

# -----------------------------------------To Catch Errors Output---------------------------------------------------

try:
    login = auth.sign_in_with_email_and_password(email, password)
    print(str(login) + '\n\n')
    print(login['email'])

except Exception as e:
    Er = e.args[0]
    print(str(Er) + '\n\n')

    Er_2 = e.args[1]
    print(str(Er_2) + '\n\n')


    # Save it as a json andthen get the specific error message
    jsonEr = json.loads(Er_2)

    # print(jsonEr)
    print(jsonEr['error']['code'])
    print(jsonEr['error']['message'])



