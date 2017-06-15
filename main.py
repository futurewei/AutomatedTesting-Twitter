import TwitterPosting

user = input("Enter your Twitter Account: ")
print ("you entered " + user) 

password = input("Enter your Twitter password: ")
twitter = TwitterPosting.Twitter(user, password)
twitter.typing()