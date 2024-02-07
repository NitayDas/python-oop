class Login:
    def __init__(self,username,password):
        self.usename = username
        self.password = password
        
    def set_new_pass(self,new_password):
        if(self.password != new_password):
            self.password = new_password
        else:
            print(f"Password shoudn't be same as older password !")
            
    def get_user_info(self):
        return f"Username: {self.usename}, Password: {self.password}\n"
    
user = Login("nitay","190129")
print(user.get_user_info())

user.set_new_pass("190129")
print(user.get_user_info())

user.set_new_pass("nitay_190129")
print(user.get_user_info())
        
        