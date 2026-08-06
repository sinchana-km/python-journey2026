dict={"this":"a keyword in c++",
      "youtube":"a vidio sharing platform",
      "instagram":"a picture sharing platform",
      "mylist":[1, 3, 4]
    
}
key = input("Enter the key:\n")
if(dict.get(key)==None):
    print("Value not found")
else:
    print("the value for your corresponding key is :", dict.get(key))