# inventory = [
# {"title" : "pencil", "price" : 20},
# {"title" : "pen", "price" : 20},
# {"title" : "book", "price" : 20},
# {"title" : "eraser", "price" : 20},
# {"title" : "sharpner", "price" : 20},
# {"title" : "ball", "price" : 20},
# {"title" : "bat", "price" : 20},
# {"title" : "box", "price" : 20},
# ]


# pd_title = input("Enter product title: ")

# for pd in inventory:
#     if pd["title"] == pd_title:
#         print(pd)




inventory = [
{"title" : "pencil", "price" : 20},
{"title" : "pen", "price" : 20},
{"title" : "book", "price" : 20},
{"title" : "eraser", "price" : 20},
{"title" : "sharpner", "price" : 20},
{"title" : "ball", "price" : 20},
{"title" : "bat", "price" : 20},
{"title" : "box", "price" : 20},
]

total = 0
while True:
    pd_title = input("Enter Product Title: ")
    if pd_title == "":
        break 
    
    for pd in inventory:
        if pd["title"] == pd_title:
            total += pd["price"]
        

print(total)