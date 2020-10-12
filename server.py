from flask import Flask, jsonify, request

app = Flask(__name__)

db = list()


def add_patient_to_database(name, id, blood_type):
    new_patient = {"name": name,
                   "id": id,
                   "blood_type": blood_type,
                   "tests": list()}
    db.append(new_patient)
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
    validate_input, server_status = validate_new_patient_data(in_data)
    if validate_input is not True:
        return validate_input, server_status
    add_patient_to_database(in_data["name"], in_data["id"],
                            in_data["blood_type"])
    return "Patient successfully added", 200


def validate_new_patient_data(in_data):
    expected_key = ["name", "id", "blood_type"]
    for key in expected_key:
        if key not in in_data.keys():
            return "{} key not found in input".format(key), 400
    return True, 200


if __name__ == '__main__':
    app.run()
