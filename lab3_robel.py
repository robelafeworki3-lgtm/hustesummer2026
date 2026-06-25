#robel|lab 3 |Intro to python 
#ticket 1
import profile


username = "rofiaf"
print(len(username)) #6


#ticket 2
print(username[0]) #R

print(username[len(username) - 1]) 
# R and F
#-1 is to target the end string

#ticket 3
print(f"welcome to loop,{username}")
#both line look identical on screen, f string is easier

#ticket 4
#username[0] = "x".           ISNT
#print(username.upper())      ISNT
# Traceback (most recent call last):
 # File "/Users/robelafeworki/Desktop/hustesummer2026/lab3_robel.py", line 19, in <module>
  #  username[0] = "x"
   # ~~~~~~~~^^^
#TypeError: 'str' object does not support item assignment 
# i thhink python will say typeError or crash
# one a string is creaated in python's memory you canot modify its individual charaacters

#ticket 5
feedlist = ["apple", "banana", "cherry"]
print(len(feedlist)) 
#3
# i used 0 to print index

#ticket 6
feedlist.append("orange")
print(len(feedlist))
#3
#the fourth post sit at index 3 because apple 0 banana 1 cherry 2 orange 3

#ticket 7
feedlist.pop(0)
#apple banana start at 0
#.pop() and .remove()

#ticket 8
profile = {
    "username": "rofiaf",
    "followers": 100,
    "verified": True
}
#100. my profile name
print(profile[0])
#cuz dictionaries are accessed by key

#ticket 9
profile["followers"]+=50
profile["bio"] = "life is a journey."
print(profile)
# it will print none

# ticket 10
print(f"@{profile['username']} has {profile['followers']} followers. Bio: {profile['bio']}")
# @rofiaf has 150 followers. Bio: life is a journey.
# list, dictionary , nested dictionary
