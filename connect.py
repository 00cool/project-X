import pyrebase
import json
config = {
  "apiKey": "AIzaSyCdIiIcdxk3XtJ6RZWhjzQ9yh3jMxA3RQg",
  "authDomain": "student-data-jump.firebaseapp.com",
  "databaseURL": "https://student-data-jump.firebaseio.com",
  "storageBucket": "student-data-jump.appspot.com",
<<<<<<< HEAD
  "serviceAccount": "/home/nick/work/project-X/student-data-jump-firebase-adminsdk-zzb0l-cfaf56906d.json"
=======
  "serviceAccount": "/home/project-X/student-data-jump-firebase-adminsdk-zzb0l-cfaf56906d.json"
>>>>>>> 0174e969983653d2dd7cb33790adc50558464606
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
      for y in data:
        db.child(from_d).child(str(y[0][7:]).replace("."," ")).push(y[1])
    elif from_d == "Google":
      for g in data:
<<<<<<< HEAD
        db.child(from_d).child(str(g[0]).replace("."," ")).push(g[1])
=======
        db.child(from_d).child(str(g[0][7:]).replace("."," ")).push(g[1])
>>>>>>> 0174e969983653d2dd7cb33790adc50558464606
    elif from_d == "Web":
      for w in data:
        db.child(from_d).child(str(w[0][7:]).replace("."," ")).push(w[1])
  except:
    raise Exception
