'''
Created on 20 paź 2017

@author: Edu
'''

from model.User import User
from db.db import connect_to_db

try:
    cnx = connect_to_db("warsztat_2_messages")
    cur = cnx.cursor(prepared=True)
    
    user_from_db = User.load_by_id(4, cur)
    print(user_from_db.id,user_from_db.username,user_from_db.email)
    
    # new_user = User("ala@mail.com", "ala", "ala")
    # new_user.save(cur)
    # new_user.email = "alusia@mail.com"
    # new_user.save(cur)
except Exception as e:
    print(e)
finally:
    cur.close()
    cnx.close()