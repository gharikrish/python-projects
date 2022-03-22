complaints = [] 
feedbacks   = []
def cms():
    print("welcome to the xyz.company")
    print("complaints ---> enter 1")
    print("feedback   ---> enter 2")
    user = int(input("enter the option"))
    if user == 1:
        user_comp = []
        name = str(input('please enter your name'))
        user_comp.append(name)
        city = str(input('please enter the your city'))
        user_comp.append(city)
        contact = int(input('please enter the your mobile number'))
        user_comp.append(contact)
        complaint = str(input('please enter the your complaint'))
        user_comp.append(complaint)
        complaints.append(user_comp)
        print("We are analyse your complaint and clear quickly")
        print('Thank you')
        
    elif user == 2:
        user_feed = []
        name = str(input('please enter your name'))
        user_feed.append(name)
        city = str(input('please enter the your city'))
        user_feed.append(city)
        contact = int(input('please enter the your mobile number'))
        user_feed.append(contact)
        feedback = str(input('please enter the your feedback'))
        user_feed.append(feedback)
        feedbacks.append(user_feed)
        print('Thank you for your feed back')
    else:
        print("enter the corect option")
cms()