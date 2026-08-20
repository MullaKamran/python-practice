class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return f"{self.name} says Woof!"
dog1 = Dog("Tommy", "Labrador")
dog2 = Dog("Rex", "German Shepherd")

print(dog1.bark())
print(dog2.bark())        


class ContactManager:
    def __init__(self):
        self.contacts = []  # starts empty

    def add_contact(self, name, phone):
        contact={"name":name,"phone":phone}
        self.contacts.append(contact)

    def list_contacts(self):
        return self.contacts
manager = ContactManager()          # Step 1: create an actual object from the blueprint
manager.add_contact("kamran", "123456789")
manager.add_contact("Asha", "987654321")# Step 2: call the method ON that object
print(manager.list_contacts())      # Step 3: call another method on the same object        