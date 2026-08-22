class ContactManager:
    def __init__(self):
        self.contacts=[]
    def add_contacts(self,name,phone):
        contact={"name":name,"phone":phone}
        self.contacts.append(contact)
    def list_contacts(self):
        return self.contacts
    def contact_update(self, name, phone):
       for contact in self.contacts:
         if contact["name"] == name:
            contact["phone"] = phone
            return "Contact updated"
       return "Contact not found"   
    def contact_delete(self,name,phone):
        for contact in self.contacts:
            if contact["name"]==name and contact["phone"]==phone:
                self.contacts.remove(contact)
                return self.contacts
        return "Contact not deleted"    
manager = ContactManager()
manager.add_contacts("kamran", "123456789")
manager.add_contacts("Asha", "987654321")
print("Before update:", manager.list_contacts())
manager.contact_update("kamran", "4753456789")
manager.contact_update("Sami", "987654321")
print("After update:", manager.list_contacts())         
result1 = manager.contact_update("kamran", "111111111")
result2 = manager.contact_update("Sami", "999999999")
print(result1)
print(result2)               
                
def get_phone(contact):
    try:
        return contact["phone"]
    except KeyError:
        return "Phone number not available"

contact = {"name": "kamran", "phone": "123456789"}
print(get_phone(contact))            