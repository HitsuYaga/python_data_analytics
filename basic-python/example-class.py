import json

class Users(object):
    def __init__(self, firstName, lastName, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
    
    @staticmethod
    def printClientInfo(self):
        print self.json()
        # print {
        #     'firstname': self.firstName,
        #     'lastname': self.lastName,
        #     'email': self.email,
        #     'password': self.password
        # };
    
    @classmethod
    def printInfoDetail(cls, firstName, lastName, email, password):
        user = cls(firstName, lastName, email, password);
        print user.json()

    def json(self):
        return {
            "firstname": self.firstName,
            "lastname": self.lastName,
            "email": self.email,
            "password": self.password
        }

client = Users("Hitsu", "Yaga", "test01@gmail.com", "123456");
client.printClientInfo(client);
client.printInfoDetail("Yuki", "Matsu", "test02@gmail.com", "123456");
