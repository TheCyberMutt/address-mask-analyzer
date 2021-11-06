from collections import Counter

passwords_file = "/home/coderpad/data/passwords.txt"

sample_file = ['123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111', '1234567', 'dragon',
               '123123', 'baseball',
               'abc123', 'football', 'monkey', 'letmein', '696969', 'shadow2', 'master1', '666666']

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']

upper = [x.upper() for x in lower]

d = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Break down the password to individual characters
def split(word):
    return [char for char in word]


# Convert each character to corresponding mask value
def converter(password):
    broken_password = split(password)
    converted_splitword = []

    for i in range(0, len(password)):
        if broken_password[i] in lower:
            converted_splitword.append("l")

        elif broken_password[i] in upper:
            converted_splitword.append("u")

        elif broken_password[i] in d:
            converted_splitword.append("d")

        else:
            converted_splitword.append("s")

    return converted_splitword


# Add each word into a new wordlist with its mask values
def wordlistappender(wordfile):
    converted_wordlist = []
    for word in wordfile:
        new_word = converter(word)
        converted_wordlist.append(''.join(new_word))

    return converted_wordlist


# With Counter being imported, we find the top 3 string values on the list # and how frequently they show up
def topthree(wordlist):
    masterlist = wordlistappender(wordlist)
    c = Counter(masterlist)
    answer = c.most_common(3)

    print(answer)


 topthree(sample_file)    #To verify that it works on a smaller list

topthree(passwords_file)  # This literally takes the string ("/home/coderpad/data/passwords.txt") instead of the actual file. I am not sure how to get it to read directly from the file but I tested the code on multiple lists to verify its accuracy
