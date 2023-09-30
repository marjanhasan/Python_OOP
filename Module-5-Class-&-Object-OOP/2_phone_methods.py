class Phone:
    brand = "Samsung"
    price = 18000
    color = "Blue"

    def call(self, phone, msg):
        txt = f"Calling {phone} and sending {msg}"
        return txt


my_text = Phone()
res = my_text.call(4189327489, "Hello World!!!")
print(res)  # Calling 4189327489 and sending Hello World!!!
