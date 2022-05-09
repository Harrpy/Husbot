import random

#de beginnin
user_input = input("Hey, how are u feelin'? :) <3\n" )
#LIST en here .. hehehhee
good_list = ["Good, hbu?", "Good u?", "good, hbu?", "good hbu?", "good hbu","Good, u?","Good, u", "good u","good u?", "Good, and you?", "Good, wbu?","good wbu?"]

ok_list = ["okay", "OK", "oki", "okay", "meh", "Meh"]

bad_list = ["bad", "bad, hbu?"]

k_list = ["K", "k", "Good", "good","Gud","gud", "Pretty good", "pretty good"]

dodge_list = ["I don't wanna talk about it, i don't wanna talk about it", "i dont wanna talk about it", "I don't feel like talking about it", "i don't feel like talking about it", "i dont feel like talking about"]

#de answers

if user_input in good_list:
  sayings = ["That is nice to hear, I feel amazing angel!","amazing now that you are home my angel,"niceuuuu <3 uwu\nme too, did I already tell you how much I love you????","pog, me too","poggers babe, so do I"]
  print(random.choice(list(sayings)))

if user_input in bad_list:
  briish = ["ight m8", "kekw", "kekW", "u wanna get shanked m8?", "feelsbad", "feelsbadman", "rip", "rip" "lol", "F", "f", "f in chat", "sucks to be you"]
  print(random.choice(list(briish)))

if user_input in ok_list:
  print("whoooo wants a mercy pockeeet?")

if user_input in dodge_list:
  print("I respecc dah")

if user_input in ["'Murica","Murica","'murica","murica" "kkona brother"]:
  print("god bless america")

if user_input in ["China", "china"]:
    print("https://tenor.com/view/trump-trump-face-gif-12025846")

  #MISC#s
