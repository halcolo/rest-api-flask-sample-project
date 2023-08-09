from data_contracts import user_contract

user_record_from_db = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}

# Use Pydantic to validate and parse the record
user = user_contract.UserContract(**user_record_from_db)
