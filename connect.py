import pyrebase
import json
config = {
  "apiKey": "AIzaSyCdIiIcdxk3XtJ6RZWhjzQ9yh3jMxA3RQg",
  "authDomain": "student-data-jump.firebaseapp.com",
  "databaseURL": "https://student-data-jump.firebaseio.com",
  "storageBucket": "student-data-jump.appspot.com",
  "serviceAccount": "/home/nick/work/mitmproxy/student-data-jump-firebase-adminsdk-zzb0l-cfaf56906d.json"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("wnickb26@gmail.com","thisismypassword")
user = auth.refresh(user['refreshToken'])
user['idToken']
db = firebase.database()


def sendDataToFire(from_d, data):
  try:
    if from_d == "YouTube":
      db.child(from_d).child("y").push(data)
    elif from_d == "Google":
      db.child(from_d).child("g").push(data)
    elif from_d == "Web":
      db.child(from_d).child("w").push(data)
  except:
    raise Exception