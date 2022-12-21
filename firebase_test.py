import pyrebase

config = {
  "apiKey": "AIzaSyDGmL7-6nLhILnEHHR04-ZfR72nyX9G8vA",
  "authDomain": "bawang-80997.firebaseapp.com",
  "databaseURL": "https://bawang-80997-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "bawang-80997.appspot.com"
}

firebase = pyrebase.initialize_app(config)


storage = firebase.storage()
database = firebase.database()

database.child("bawang").update({"temp": 102})
