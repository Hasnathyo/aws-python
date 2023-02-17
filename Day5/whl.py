#while

#while <condition>:
#   <code>


message = ""
while message != "quit":
    message = input("prompt ")
    print(message)

if message == "quit":
    print("cya")