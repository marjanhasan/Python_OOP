# .csv comman separated value
# .txt text file

# with open("message.txt", "w") as file:
#     file.write("Hello from python!!!")

# with open("message.txt", "a") as file:
#     file.write("Hola from python!!!")

with open("message.txt", "r") as file:
    text = file.read()
    print(text)
