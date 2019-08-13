alphabet="abcdefghijklmnopqrstuvwxyz"
key=3
newmess=''
character=input("Enter the message")
for message in character:
    if message in alphabet:
	    position=alphabet.find(message)
	    new=(position+key)%26
	    newcha=alphabet[new]
	    newmess += newcha
    else:
	    newmess+=message
print(newmess)
