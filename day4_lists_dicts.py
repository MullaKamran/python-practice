def add_and_remove(items, to_add, to_remove):
    items.append(to_add)
    items.remove(to_remove)
    return items

print(add_and_remove([1, 2, 3], 4, 2))

def get_value(data, key):
    if key in data:
        return data[key]
    else:
        return "Not found"

person = {"name": "Kamran", "age": 22}
print(get_value(person, "name"))
print(get_value(person, "email"))
