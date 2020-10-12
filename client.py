import requests

print("Add new patient with good inputs")
new_patient = {"name": "Everett", "id": 102, "blood_type": "AB-"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=new_patient)
print(r.status_code)
print(r.text)

print("Try to add patient with missing key")
new_patient = {"name": "Frank", "id": 103, "blood_types": "O+"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=new_patient)
print(r.status_code)
print(r.text)

print("Try to add patient with wrong data type")
new_patient = {"name": "Frank", "id": "103", "blood_type": "O+"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=new_patient)
print(r.status_code)
print(r.text)

print("Try to add patient with incorrect blood type")
new_patient = {"name": "Frank", "id": "103", "blood_type": "X+"}
r = requests.post("http://127.0.0.1:5000/new_patient", json=new_patient)
print(r.status_code)
print(r.text)

print("Add test result")
new_test = {"id": 100, "test_name": "HDL", "test_results": 80}
r = requests.post("http://127.0.0.1:5000/add_test", json=new_test)
print(r.status_code)
print(r.text)

print("Add second test result")
new_test = {"id": 100, "test_name": "LDL", "test_results": 60}
r = requests.post("http://127.0.0.1:5000/add_test", json=new_test)
print(r.status_code)
print(r.text)

print("Try to add test result to id that doesn't exist")
new_test = {"id": 200, "test_name": "LDL", "test_results": 60}
r = requests.post("http://127.0.0.1:5000/add_test", json=new_test)
print(r.status_code)
print(r.text)

print("Try to add test with bad key")
new_test = {"id": 100, "testname": "LDL", "test_results": 11}
r = requests.post("http://127.0.0.1:5000/add_test", json=new_test)
print(r.status_code)
print(r.text)

print("Try to add test with bad data type")
new_test = {"id": 100, "testname": "LDL", "test_results": "LDL=22"}
r = requests.post("http://127.0.0.1:5000/add_test", json=new_test)
print(r.status_code)
print(r.text)
