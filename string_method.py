

str1 = "UPPU"
print(str1.isupper()) # check string is upper case
str2 = "lower"
print(str2.islower()) # check string is lower case
str3 = "Hai Myname Is Reshma" 
print(str3.istitle()) # check string is title case
str4 = "12546665" 
print(str4.isdigit()) # check string is digit
str5 = "Reshma658955"
print(str5.isalnum()) # check string includes alphabet and numbers
str6 = "GshgfshRTYUYIUIKJ"
print(str6.isalpha()) # check string include both upper case and lower case letters
str7 = " "
print(str7.isspace())

remove_space = " Reshma   "
print("My name is ",remove_space.strip())

str22 = "Hai world"
new_str = str22.replace("Hai","Hello")
print(new_str)

new_strr = "Hello my name is Reshma"
after_split = new_strr.split(" ")
print(after_split)

new_strrr = ("Hello","Python","world")
after_joint = " ".join(new_strrr)
print(after_joint)

name = "Hi How are you"
new_name = name.startswith("Hi")
print(new_name)

name2 = "Hello world python"
new_name2 = name2.endswith("python")
print(new_name2)

