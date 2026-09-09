#for else

success = True
for i in range(3):
    print("attempt")
    if success:
        print("Successfull")
        break
else:
    print("Tried 3 attempts and failed")

#attempt
#Successfull

success = False
for i in range(3):
    print("attempt")
    if success:
        print("Successfull")
        break
else:
    print("Tried 3 attempts and failed")

#attempt
#attempt
#attempt
#Tried 3 attempts and failed
