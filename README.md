### Routes
* ` POST /new_patient`

  ```python
  {"name": str, "id": int, "blood_type": str}
  ```
  where blood type is one of O+, O-, A+, A-, B+, B-, AB+, AB-.

* `POST /add_test`

  ```python
  {"id": int, "test_name": str, "test_result": int}
  ``` 

* `GET /get_results/<patient_id>`

* `GET /compatible/<donor>/<recipient>`
    
    where `<donor>` is the donor id and `<recipient>` is the recipient id.  It
    returns a string of "Compatible" if the donor can safely give blood to the
    recipient.  It returns a string of "Not Compatible" if the donor cannot
    give blood safely to the recipient.
    
    