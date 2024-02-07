class Login:
    def __init__(self,username,password):
        self.usename = username
        self.password = password
        
    def set_new_pass(self,new_password):
        #if password is not same as older password
        if(self.password != new_password):
            self.password = new_password
        #if password is same as older password
        else:
            print(f"Password shoudn't be same as older password !")
            
    #return user info      
    def get_user_info(self):
        return f"Username: {self.usename}, Password: {self.password}\n"
    
#creating object   
user = Login("nitay","190129")
#get user info
print(user.get_user_info())

#set new pass
user.set_new_pass("190129")
print(user.get_user_info())

user.set_new_pass("nitay_190129")
print(user.get_user_info())
        
        