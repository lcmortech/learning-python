# Problem Statement
# Output - Say something: it's good weather today
# Output - how is the weather there
# Say something: /end
# "It's good weather today. How is the weather there? There's only some clouds here."

# APPROACH
# Program asks for user input repeatedly
# Receives strings
# If the user returns \end, the program recognizes it and returns the output.
# The program is capitalizing the strings and is adding a period or question mark (conditional)
# First, think of how to get a raw string and convert it into a sentence.
# The best way to do it, is by using a function

def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("who","what","when","where","why","how","do","does","did")
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}."format(capitalized)

#print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        result.append(sentence_maker(user_input))

print(" ".join(results))

# Use Join Method to concatenate
