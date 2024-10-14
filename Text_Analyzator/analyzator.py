import task_template as tt

print("""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Samuel Wlaschinsky

email: wlaschinsky.samuel@gmail.com
email_2: samuel.wlaschinsky@daktela.com

discord: samuel_qa

""")

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username: ")
password = input("password: ")

# veryfiing user after password input
if username in users and users[username] == password:
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    exit()

# selecting text from imported source
texts = tt.texts

# selecting text
num_text = input("Enter a number btw. 1 and 3 to select: ")

# checking if input is valid
if not num_text.isdigit() or int(num_text) not in range(1, 4):
    print("Invalid input, terminating the program..")
    exit()

selected_text = texts[int(num_text) - 1]

# get words from text and lenght
words = selected_text.split()
words_count = len(words)

title_words = 0
upper_words = 0
lower_words = 0
numeric_strings = []

# function to check if word is title, upper, lower or numeric
for word in words:
    if word.istitle():
        title_words += 1
    if word.isupper() and word.isalpha():
        upper_words += 1
    if word.islower():
        lower_words += 1
    if word.isdigit():
        numeric_strings.append(int(word))

#  sum of all numeric strings
sum_numbers = sum(numeric_strings)
# print(numeric_strings)

# print results
print(f"There are {words_count} words in the selected text.")
print(f"There are {title_words} titlecase words.")
print(f"There are {upper_words} uppercase words.")
print(f"There are {lower_words} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}")


# Icnicialization of empty dictionary for word lenght and its count
word_len_dic = {}

for word in words:
    # Clear word from interpunction and count its length
    length = len(word.strip(".,!?"))
    
    if length in word_len_dic:
       # If length is already in dictionary, increase its count, using length as key
        word_len_dic[length] += 1
        
    else:
        # If length is not in dictionary, add it with count 1
        word_len_dic[length] = 1
    
# Graph of word lenghts and its count
print("----------------------------------------")
print("LEN|  OCCURRENCES  |NR.")
print("----------------------------------------")

# Sort dictionary by length (key)
for length in sorted(word_len_dic):
    
    # Get count per current key - length
    count = word_len_dic[length]
    
    # Create graph through f-string - new way with formatting
    print(f"{length:>3}|{'*' * count:<20}|{count}")
    
    
