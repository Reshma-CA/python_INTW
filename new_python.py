


class Calculator:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def Addition(self):
        addition = self.num1+self.num2
        print(f"Addition :{addition}")

    def Subtraction(self):
        subtract = self.num1-self.num2
        print(f"Subtraction :{subtract}")
obj = Calculator(12,3)
obj.Addition()

###############################################################

new_data = {
  "name": "John Doe",
  "age": 28,
  "email": "john.doe@example.com",
  "isActive": True,
  "interests": [
    "coding",
    "reading",
    "music"
  ]
}

print(new_data.get("name"))
print(new_data.get("email"))
#####################################################################
new_data = {
  "companyName": "Tech Solutions",
  "departments": [{
      "name": "Engineering",
      "employees": [
          {
          "employeeId": 101,
          "fullName": "Alice Johnson",
          "role": "Software Engineer"
        },{
          "employeeId": 102,
          "fullName": "Bob Smith",
          "role": "QA Engineer"
        }
        ]

    },

    {
      "name": "Sales",
      "employees": [
        {
          "employeeId": 201,
          "fullName": "Carol Brown",
          "role": "Sales Executive"
        },
        {
          "employeeId": 202,
          "fullName": "Dave Wilson",
          "role": "Sales Associate"
        }
      ]
    }
  ]
}

print(new_data["departments"][0]["name"])
print(new_data["departments"][0]["employees"][1]["role"])

print(new_data["departments"][1]["employees"][1]["role"])
print(new_data["departments"][1]["employees"][0]["role"])



















