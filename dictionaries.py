customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

customer["name"] = "Jack Smith"
customer["birthday"] = "Jan 1 1986"
print(customer["name"])
print(customer.get("age"))
print(customer)