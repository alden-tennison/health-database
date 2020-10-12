import requests

new_patient = {"name": "Everett", "id": 102, "blood_type": "A-"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=new_patient)
print(r.status_code)
print(r.text)
