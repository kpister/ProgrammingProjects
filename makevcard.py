
#format of contacts file
#firstName,lastName,primaryNumber,secondaryNumber (optional)

ex = open("contacts.txt").read()
loadcont = ex.split("\n")

newFile = open("newContacts.txt", 'w')

for contact in loadcont:
    info = contact.split(",")
    newFile.write("BEGIN:VCARD\nVERSION:4.0\nN:%s;%s;;;\nFN:%s\n" %(info[0],info[1], (info[0]+info[1])))
    newFile.write("TEL;TYPE=work,voice;VALUE=uri:%s\n" %(info[2]))

    if info[3].isalnum():
        newFile.write("TEL;TYPE=work,voice;VALUE=uri:%s\n" %(info[3]))
    newFile.write("END:VCARD\n")

