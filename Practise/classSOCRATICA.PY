'''1'''
class User:
    pass

user1 = User()
user1.fn = "Dave"
user1.ln = "Bowman"
user1.age = 20

user2 = User()
user2.fn = "Ave"
user2.ln = "Ram"
user2.fb = "2002: Money in the bank"

print(user1.fn, user2.fn)

fn = "Arthur"
ln = "Clarke"

print(fn, ln)



"""2"""
import datetime

class User:
    """Hello i am friendface"""
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday

        #extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
        
    def age(self):
        """return age of user in year"""
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)
    
user1 = User("Sushil", "20020304")
print(user1.age())
# help(User)