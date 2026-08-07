spamwords =['buy now', 'subscribe this','click this']
email = input("Enter your email:").lower()
spam = False

if('buy now' in email):
    spam = True
    
if('subscribe this' in email):
    spam = True
if('click this' in email):
    spam = True
print("spam is",spam)    
        