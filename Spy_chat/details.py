from datetime import datetime
from termcolor import colored,cprint

password = '1234'

class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.age = age
        self.salutation = salutation
        self.rating = rating
        self.chats = []
        self.current_status_message = None
        self.spy_is_online = True

class chat_messages:
    def __init__(self,message,sent_by_me):
        self.message = colored(message,'green')
        self.time = colored(datetime.now(),'blue')
        self.sent_by_me = sent_by_me

admin = Spy("Tanuj","Mr.",20,9.9)

friend_1 = Spy("Pulkit","Mr.",19,9.5)
friend_2 = Spy("Abhimanyu","Mr.",20,9.7)
friend_3 = Spy("Yogesh","Mr.",20,9.6)
friend_4 = Spy("Parminder","Mr.",20,9.4)

friends = [friend_1,friend_2,friend_3,friend_4]
user_friends = []
