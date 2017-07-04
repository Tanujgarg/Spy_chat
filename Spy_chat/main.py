from details import admin,Spy,friends,password,user_friends,chat_messages
from stegano import lsb
import colors
from termcolor import colored

print(colors.green("------Wellcome to spychat app-----\n"))
print(colors.green("--------Let's Gets Started--------\n"))

status_messages = ['Online','Offline','Busy']
special = ['SOS','sos','HELP','help']
verification = 'yes'
user = []
'''
There are 4 fuctions (name,salutation,age,rating)
which takes inputs from user and check inputs on some
conditions.
After filter the inputs each fuction return a perticular information
'''

def name():
    spy_name = str(input("What is your name?\n"))
    if len(spy_name) == 0:
        print(colors.red("You must enter a name!"))
        print("")
    else:
        if spy_name.isalpha():
            return spy_name
        else:
            print(colors.red("Name must be a string not a number"))
    return name()

def salutation():
    spy_gender = input("Enter your gender either male or female\n")
    if spy_gender.isnumeric():
        print(colors.red("Name must be a string not a number"))
    else:
        if spy_gender.upper() == 'MALE':
            return 'Mr.'
        elif spy_gender.upper() == 'FEMALE':
            married = input("Are you married (yes/no)?\n")
            if married.upper() == 'YES':
                return 'Mrs.'
            else:
                if married.upper() == 'NO':
                    return 'Miss.'
                else:
                    print(colors.red("Wrong Entry!"))
        else:
            print(colors.red("Wrong Entry!"))
            print(" ")
            print("Let's try again")
    return salutation()



def age():
    spy_age = input("What is your age?\n")
    if spy_age.isdigit():
        spy_age = int(spy_age)
        if spy_age > 12 and spy_age < 50:
            spy_age = int(spy_age)
            return spy_age

        else:
            print(colors.red("Age must be in between 12 and 50"))
            print(" ")
            print("Let's try again")
    else:
        print(colors.red("Age must be in between 12 and 50"))
    return age()


def rating():
    spy_rating = input("What is your spy rating (Rating between 1 and 10)?\n")
    if len(spy_rating) == 0:
        print(colors.red("You must provide some rating"))
    else:
        if spy_rating.isalpha():
            print(colors.red("Rating must be float or integer"))
        else:
            try:
                spy_rating = float(spy_rating)
            except ValueError:
                print(colors.red("Rating must be float or integer"))
                return rating()
            if spy_rating >= 0.0 and spy_rating <= 3.0:
                print("Your rating is poor")
                return spy_rating
            elif spy_rating > 3.0 and spy_rating <= 7.0:
                print("Your rating is good")
                return spy_rating
            elif spy_rating > 7.0 and spy_rating <= 10.0:
                print("Your rating is excelent")
                return spy_rating
            else:
                print(colors.red("please provide rating between 0 to 10"))
    return rating()


# add_status used for update the current status of spy


def add_status(current_status):
    updated_status = None

    if current_status != None:
        print("your current status message is  ",current_status)
    else:
        print("You don't have any current status")

    status_choice = input("Do you want to select your status from older status list (yes/no)?\n")
    if status_choice.upper() == 'YES':
        status_position = 1
        for message_list in status_messages:
            print(status_position,message_list)
            status_position += 1
        try:
            status_select = int(input("Select a status from given list\n"))
        except ValueError:
            print(colors.red("invalid entry"))
            return add_status(current_status)
        if len(status_messages) >= status_select:
            updated_status = colored(status_messages[status_select - 1],'green')
            print("Your status is updated")
            print("Now your current status is ",updated_status)
        else:
            print(colors.red("Your choice is wrong"))
            print("")
            menu()
    elif status_choice.upper() == 'NO':
        new_status = input("Enter your new status message which you want to update.\n")
        if len(new_status) == 0:
            print("You don't have any status update")
            menu()
        else:
            status_messages.append(new_status)
            updated_status = colored(new_status,'green')
            print(colors.cyan("Your status is updated"))
            print("your updated status is ",updated_status)
    else:
        print(colors.red("you choice is invalid or wrong!"))
        menu()
    return updated_status

# add_friend used for adding some new friends in list

def add_friend():
    print("Enter details of new friend")
    new_friend = Spy('','',0,0.0)
    new_friend.name = name()
    new_friend.salutation = salutation()
    new_friend.age = age()
    new_friend.rating = rating()
    if user_name == 'yes':
        friends.append(new_friend)
        return len(friends)
    else:
        user_friends.append(new_friend)
        return len(user_friends)

# select_friend used for finding the index of friend

def select_friend():
    print("Select a friend")
    position = 1
    if user_name == 'yes':
        for friend in friends:
            print(position,friend.name)
            position += 1
    else:
        if len(user_friends) == 0:
            print(colors.red("You don't have any friend in your list\nPlease add atleast 1 friend"))
            menu()
        else:
            for friend in user_friends:
                print(position,friend.name)
                position += 1
    friend_position = input("Your choice ")
    if len(friend_position) == 0:
        print(colors.red("Please select"))
        select_friend()
    elif friend_position.isdigit():
        friend_position = int(friend_position)
        friend_position = friend_position - 1
        return friend_position
    else:
        print(colors.red("Wrong entry"))
        select_friend()

'''
send_message encode the message in a image using stegano library
after encoding message will be saved in friend chatbox
'''

def send_message():
    friend_position = select_friend()
    original_image = input("Enter name of image followed by extension\n")
    text = input("Enter message which you want to encode\n ")
    output_image = input("Enter name of output image without extension\n")
    output_image = "./"+output_image+".png"
    try:
        secret = lsb.hide(original_image,text)
        secret.save(output_image)
    except FileNotFoundError:
        print(colors.red("No image found with this name"))
        menu()
    temp = text.split(' ')
    for index in special:
        if index in temp:
            temp[temp.index(index)]='Please help me'
    text = str.join(' ',temp)
    new_chat = chat_messages(text, True)
    if user_name == 'yes':
        friends[friend_position].chats.append(new_chat)
    else:
        user_friends[friend_position].chats.append(new_chat)
    print(colors.cyan("Your secret message is ready"))
    print("")

'''
read_chat works in two ways
1. it decodes the image
2. shows the message from friend's chatbox
'''

def read_message():
    choice = input("1.Read message from image\n2.Read friend chat history\n")
    if choice == '1':
        print("Select a friend")
        friend_position = select_friend()
        output_image = input("Enter tha name of image without extension\n")
        output_image = output_image+'.png'
        try:
            secret = lsb.reveal(output_image)
            secret = str(secret)

            #secret = colored(secret,'cyan')
        except FileNotFoundError:
            print(colors.red("No image found with this name"))
            menu()
        if secret == 'None':
            print(colors.red("No secret message in given image"))
        else:
            temp = secret.split(' ')
            for index in special:
                if index in temp:
                    temp[temp.index(index)] = 'Please help me'
            if len(temp) > 100:
                print(colored("Your friend talk more then 100 words",'red'))
                delete = input("Do you want to delete this friend(yes/no)?\n")
                if delete == 'yes':
                    if verification == 'yes':
                        del friends[friend_position]
                        print(colored("Friend deleted",'cyan'))
                        menu()
                    else:
                        del user_friends[friend_position]
                        print(colored("Friend deleted", 'cyan'))
                        menu()
                else:
                    pass
            secret = str.join(' ', temp)

            new_chat = chat_messages(secret, False)
            if user_name == 'yes':
                friends[friend_position].chats.append(new_chat)
            else:
                user_friends[friend_position].chats.append(new_chat)
            secret = colored(secret,'yellow')
            print("Secret message is",secret)
    elif choice == '2':
        friend_position = select_friend()
        if user_name == 'yes':
            if len(friends[friend_position].chats) == 0:
                print(colors.red("Chat is empty"))
            else:
                for chat in friends[friend_position].chats:
                    if chat.sent_by_me:
                        print("At ", chat.time, "You said ", chat.message)
                    else:
                        print("At ", chat.time, "Your friend said ", chat.message)

        else:
            if len(user_friends[friend_position].chats) == 0:
                print(colors.red("Chat is empty"))
            else:
                for chat in user_friends[friend_position].chats:
                    print("At ",chat.time,"message ",chat.message)
    else:
        print(colors.red("wrong entry"))
        read_message()


def show_profile():
    if user_name == 'yes':
        print("Name : ",admin.salutation.upper(),admin.name.upper())
        print("Age : ",admin.age)
        print("Rating : ",admin.rating)
        print("No. of friends : ",len(friends))
    else:
        for i in user:
            print("Name : ", i.salutation.upper(), i.name.upper())
            print("Age : ", i.age)
            print("Rating : ", i.rating)
            print("No. of friends : ", len(user_friends))


'''
menu function is like a menu card 
by which user can select option which he/she want to do
'''



def menu():
    current_status = None
    while(1):
        print(colors.yellow("Enter your choice"))
        print(colors.blue("(For example,\n if you want to add\n new friends then,\n type 2)"))
        print("1.Status update.\n2.Add a new friend\n3.Read chat\n4.Send message\n5.View Profile\n6.Exit")
        choice = input("Your choice is ")
        if len(choice) == 0:
            print(colors.red("Please choose a option"))
            menu()
        else:
            if choice == '1':
                print("You choose for status update")
                current_status = add_status(current_status)
            elif choice == '2':
                print("You choose for Add a new friend")
                total_friends = add_friend()
                print("you have",total_friends,"friend/friends in your list")
            elif choice == '3':
                print("You choose For read a chat")
                read_message()
            elif choice == '4':
                print("You choose to send a message")
                send_message()
            elif choice == '5':
                print("You choose for view profile")
                show_profile()
            elif choice == '6':
                exit()
            else:
                print("please enter a valid choice")
                menu()




def main():
    new_user = Spy('','',0,0.0)
    new_user.name = name()
    if admin.name.upper() == new_user.name.upper():
        print("Are you spy admin?")
        verify = input("Please enter your password\n")
        if len(verify) == 0:
            print(colors.red("You are not admin"))
            new_user.salutation = salutation()
            new_user.age = age()
            new_user.rating = rating()
            user.append(new_user)
            print("Wellcome " + new_user.salutation + " " + new_user.name + " in spy chat")
        else:
            if password == verify:
                print(colors.cyan("Verification successful"))
                print("Wellcome " + admin.salutation + " " + admin.name)
                return 'yes'
            else:
                print(colors.red("You are not admin"))
                new_user.salutation = salutation()
                new_user.age = age()
                new_user.rating = rating()
                user.append(new_user)
                print("Wellcome " + new_user.salutation + " " + new_user.name + " in spy chat")
    else:

        new_user.salutation = salutation()
        new_user.age = age()
        new_user.rating = rating()
        user.append(new_user)
        print("Wellcome " + new_user.salutation + " " + new_user.name + " in spy chat")
    return 'no'

user_name = main()
menu()