# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:27]

category1 = categories.split(",")[0].strip() 
category2 = categories.split(",")[1].strip()

bubblegum_price = 1.50
chocolate_price = 2.00
pasta_price = 5.40

message_we_have = "We have "
message_for = " for $"
message_in_the = " in the "

print(message_we_have + candy1 + message_for + "{:.2f}".format(bubblegum_price) + message_in_the + category1)
print(message_we_have + candy2 + message_for + "{:.2f}".format(chocolate_price) + message_in_the + category1)
print(message_we_have + dry_goods + message_for + "{:.2f}".format(pasta_price) + message_in_the + category2)