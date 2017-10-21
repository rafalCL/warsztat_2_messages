'''
Created on 20 paź 2017

@author: Edu
'''

class User:
    _TABLE_NAME = "user_data"

#     def __init__(self):
#         self._id = -1
#         self._email = None
#         self._username = None
#         self._hashed_password = None
        
    def __init__(self, email, username, password):
        self._id = -1
        self.email = email
        self.username = username
        self.hashed_password = password
   
    @property 
    def id(self):
        return self._id
       
    @property 
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
        
    @property 
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username
        
    @property 
    def hashed_password(self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, hashed_password):
        # TODO: Implement hashing password
        self._hashed_password = "*HASHED*" + hashed_password
        
    def save(self, cursor):
        if self._id == -1:  
            sql = "INSERT INTO {} VALUES(default, %s, %s, %s);".format(User._TABLE_NAME)
            cursor.execute(sql, (self.email, self.username, self.hashed_password))
            self._id = cursor.lastrowid
        else:
            sql = """
            UPDATE {} SET email=%s, username=%s, hashed_password=%s
            WHERE id=%s;
            """.format(User._TABLE_NAME)
            cursor.execute(sql, (self.email, self.username, self.hashed_password, self.id))
    
    @classmethod
    def load_by_id(cls, user_id, cursor):
        sql = "SELECT id, email, username, hashed_password FROM {} WHERE id=%s;".format(cls._TABLE_NAME)
        cursor.execute(sql, (user_id,))
        loaded_user = User("","","")
        for row in cursor:
            loaded_user._id = row[0]
            loaded_user._email = row[1]
            loaded_user._username = row[2]
            loaded_user._hashed_password = row[3]
            break
        
        return loaded_user