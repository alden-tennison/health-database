from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

db = list()


def init_db():
    logging.basicConfig(filename="health_db.log", filemode='w',
                        level=logging.DEBUG)
    add_patient_to_database("Ann Ables", 100, "A+")
    add_patient_to_database("Bob Boyles", 101, "B-")


def add_patient_to_database(name, id, blood_type):
    new_patient = {"name": name,
                   "id": id,
                   "blood_type": blood_type,
                   "tests": list()}
    db.append(new_patient)
    logging.info("Added patient {}".format(name))
    print(db)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Receive request data
    in_data = request.get_json()
    # Call functions
    answer, server_status = process_new_patient(in_data)
    # return results
    return answer, server_status


def process_new_patient(in_data):
    expected_key = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    validate_input = validate_post_input(in_data, expected_key, expected_types)
    if validate_input is not True:
        return validate_input, 400
    valid_blood_type = validate_blood_type(in_data)
    if valid_blood_type is not True:
        return valid_blood_type, 400
    add_patient_to_database(in_data["name"], in_data["id"],
                            in_data["blood_type"])
    return "Patient successfully added", 200


def validate_post_input(in_data, expected_key, expected_types):
    for key, v_type in zip(expected_key, expected_types):
        if key not in in_data.keys():
            return "{} key not found in input".format(key)
        if type(in_data[key]) != v_type:
            return "{} key value has the wrong variable type".format(key)
    return True


def validate_blood_type(in_data):
    blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    if in_data["blood_type"] not in blood_types:
        return "{} is not a valid blood type".format(in_data["blood_type"])
    return True


@app.route("/add_test", methods=["POST"])
def post_add_test():
    in_data = request.get_json()
    answer, status_code = process_add_test(in_data)
    return answer, status_code


def process_add_test(in_data):
    expected_key = ["id", "test_name", "test_results"]
    expected_types = [int, str, int]
    valid_data = validate_post_input(in_data, expected_key, expected_types)
    if valid_data is not True:
        return valid_data, 400
    patient = find_correct_patient(in_data["id"])
    if patient is False:
        return "Could not find patient in database", 400
    data_to_add = (in_data["test_name"], in_data["test_results"])
    patient["tests"].append(data_to_add)
    logging.info("Added test to patient {}".format(patient["name"]))
    print(db)
    return "Test successfully added", 200


def find_correct_patient(patient_id):
    for patient in db:
        if patient["id"] == patient_id:
            return patient
    return False


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results(patient_id):
    patient_id = int(patient_id)
    patient = find_correct_patient(patient_id)
    if patient == False:
        tests = 0000
    else:
        tests = patient["tests"]
    return "patient results are {}".format(tests)


if __name__ == '__main__':
    init_db()
    app.run()
