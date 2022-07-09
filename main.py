#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Reading invited names from invited_names.txt and then storing in a list
file = open("C:/Users/DELL/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt",
            mode="r")
#Relative File Path for the above Absolute path
#file = open("./Input/Names/invited_names.txt", mode="r")
names = file.readlines()
for name_ind in range(0, len(names)):
    names[name_ind] = names[name_ind].strip("\n")
file.close()

#Modifying the starting letter and then creating new file
file = open("C:/Users/DELL/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/"
            "starting_letter.txt", mode="r")
#Relative File Path for the above Absolute path
#file = open("./Input/Letters/starting_letter.txt", mode="r")

#Note:- Do not try to read content from  the file more than once because after getting content from the file first time
#The second time we don't have content as the file is already being read. That's why I read the content of the file once
#and that to out-side of the loop.
txt = file.read()
for name in names:
    new_letter = txt.replace("[name]", name)
    send_letter = open(f"C:/Users/DELL/Downloads/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/"
                       f"{name}.txt", mode="w")
    send_letter.write(new_letter)
    send_letter.close()
