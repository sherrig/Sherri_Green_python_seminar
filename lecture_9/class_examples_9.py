readText = open('haiku.txt', 'r')
haiku = readText.read(15)

writeText = open('/Users/joegriffin/Documents/' +
                 'Work/ES.S70/python_seminar/group_lectures/' +
                 'lecture_9/poetry.txt', 'w')
writeText.write(haiku)
writeText.close()

appendText = open('poetry.txt', 'a')
appendText.write(haiku)

appendText.close()
readText.close()

readText = open('haiku.txt', 'r')
readText.read() # Read full file
readText.seek(2) # Decide reading start point
readText.read(5) # Num chars to read
readText.tell() # Remind read start point location
readText.close() # Clean up after yourself

with open('poetry.txt', 'r') as readText: # This is for lazy people
    readText.read() # Auto-closes readText for you
