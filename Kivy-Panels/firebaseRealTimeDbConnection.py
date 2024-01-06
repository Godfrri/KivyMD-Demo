#! Youtube Video
# https://youtu.be/DCaH4bQ4DxA?si=Lhtsh_z5oL_yjB4X

import pyrebase


Config = {
    "apiKey": "AIzaSyB1M-p6zClTO5cN4IrX7TzkATbbD1uGEPY",
    "authDomain": "agro-farm-bea51.firebaseapp.com",
    "databaseURL": "https://agro-farm-bea51-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "agro-farm-bea51",
    "storageBucket": "agro-farm-bea51.appspot.com",
    "messagingSenderId": "709059373191",
    "appId": "1:709059373191:web:ba4c65f113fb34f19b7022",
    "measurementId": "G-0Y5HDBNWZ0",
    "databaseURL": "https://agro-farm-bea51-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

#! Add the databaseURL for the above

firebase = pyrebase.initialize_app(Config)
db = firebase.database()

data= {"Age": 23, "Name": "Godfrri", "Email": "godfric@gmail.com"}


#----------------------------------------------------------------
#! Create Data
# #? This will just add the data to the database
# db.push(data)

# #? This will create subfolders and add data to the database
# db.child('Users').child('Godfrri').set(data)


#----------------------------------------------------------------
#! Read Data
# data = db.child('Users').child('Godfrri').get()

# #? print all data
# print(data.val())

# #? print specific data
# print(data.val()['Age'])



#----------------------------------------------------------------
#! Update Data
# db.child('Users').child('Godfrri').update({'Age':23})


#----------------------------------------------------------------
#! Remove Data
db.child('Users').child('Godfrri').child('Age').remove()
