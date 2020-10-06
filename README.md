### Routes
` POST /new_patient`

```python
{"name": str, "id": int, "blood_type": str}
```
where blood type is one of O+, O-, A+, A-, B+, B-, AB+, AB-.


`POST /add_test`

```python
{"id": int, "test_name": str, "test_result": int}
``` 

`GET /get_results/<patient_id>`
