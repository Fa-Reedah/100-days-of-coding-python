#TODO: Create a letter using starting_letter.txt
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as file:
    names= file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()

# for each name in invited_names.txt
for i in range(len(names)):
    # Replace the [name] placeholder with the actual name.
    n_letter = "".join(letter).replace(PLACEHOLDER, names[i].strip())

    # Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{names[i].strip()}.txt","w") as file:
       file.write(n_letter)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp