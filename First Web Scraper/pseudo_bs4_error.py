try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found!")
else:
    if badContent == None:
        print("Tag was not found!")
    else:
        print(badContent)