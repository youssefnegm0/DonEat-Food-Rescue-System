#1
import json

class Authentication:
 
 def load_users(self):
      try:
        with open("users.json", "r") as file:
            users = json.load(file)
        return users
      except FileNotFoundError:
        users = {}
        self.save_users(users)
        return users

 def save_users(self,users):
   with open("users.json","w")as file:
     json.dump(users,file,indent=4)

 def generate_id(self,users):
     if len(users)==0:
        return "10001"
     ids=[]
     for id in users:
         ids.append(int(id))
     new_id=max(ids)+1
     return str(new_id)

 def register(self):
     users=self.load_users()
     print("         ======REGISTER======")

     name = input("Enter your name : ")
     email = input("Enter your email : ")
     phone = input("Enter your phone : ")

     chars = "!|$%^&*#.><?-_+{}[])(@~"

     while True:
         password = input("Enter your password : ")

         if len(password) == 8:
             found = False
             for i in chars:
                 if i in password:
                     found = True
                     break
             if found:
                print("Successful password.")
                break
             else:
                print("Password must have special chars.")
                print("Please try again...")
         else:
             print("The password must consist of 8 characters..")
     new_user={
        "Name":name,
        "Email":email,
        "Phone":phone,
        "Password":password
}
     while True:
        print("What would you like to do?")
        print("1. Donate food")
        print("2. Receive food")
        print("3. Volunteer (as a delivery person.)")
        choice=int(input("Enter your choice : "))
        if choice == 1:
          role = "donor"
          org_name=input("Enter organization name :")
          org_address=input("Enter organization address :")
          new_user["Role"]=role
          new_user ["Organization name"]=org_name
          new_user["Organization address"]=org_address
          break
        elif choice == 2:
          role = "receiver"
          org_name=input("Enter organization name :")
          org_address=input("Enter organization address :")
          new_user["Role"]=role
          new_user ["Organization name"]=org_name
          new_user["Organization address"]=org_address
          break
        elif choice == 3:
          role = "volunteer"
          availability=input("Enter availability :")
          new_user["Role"]=role
          new_user["Availability"]=availability
          break
        else:
          print("Invalid choice , Try again..")
     user_id=self.generate_id(users)
     users[user_id]=new_user
     self.save_users(users)
     print("Register successful..")

 def login(self):
     users=self.load_users()
     print("         ======LOGIN======")
     while True:
        email=input("Enter your email :")
        for user_id in users:
            if users[user_id]["Email"]==email:
                while True:
                    password=input("Enter your password :")
                    if users[user_id]["Password"]==password:
                        print(" Login Successful!")
                        return users[user_id]
                    else:
                        print("Incorrect Password.")
                        print(" Please , Make sure you entered the correct password.")
            else :
                pass
        else:
            print("This Email is not registed. ")
            print(" Please , Make sure you entered the correct email.")
            choice=(int(input("Do you already have an account,or not? \n 1.Yes \t 2.No \n")))
            if choice==1:
                pass
            elif choice==2:
                self.register()
                return
            else:
                print("Invalid choice.")