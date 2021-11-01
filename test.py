import sqlite3
import datetime

def inputting(values, tags, codeids):
  results = {} #store stuff in a dictionary
  for i in range (0, len(values)):
    results.update({codeids[i] : str(input("What is your " + values[i] + ", " + ("required" if tags[i] == 0 else "optional") + ": "))}) # type in a number
  return results

def confluence(table, id2, confluenceid, value):
  conn.execute("INSERT INTO " + table + " values (" + id2 + ","+ confluenceid + ",\"" + value + "\")")

def confluencecheck(table, id2, confluenceid, value):
  if value != "":
    confluence(str(table), str(id2), str(confluenceid), str(value))

def main():
  conn = sqlite3.connect("store.db");
  conn.execute("PRAGMA foreign_keys = 1")
  conn.commit()
  startchoice = int(input("Input 1 for creating membership, 2 for adding or removing items from the cart, 3 for viewing your cart, 4 for traditional purchasing, 5 for checking out your cart."))
  if startchoice == 1: 
    createmembership()
  elif startchoice == 2:
    addrem()
  elif startchoice == 3:
    viewcart()
  elif startchoice == 4:
    classicalbuy()
  elif startchoice == 5:
    buycart()
    
      

def createmembership():
  codeids = ["name", "age", "id", "card", "cphone", "wphone", "hphone", "haddress", "waddress", "gaddress"]
  values = ["name", "age", "wanted id", "card number", "cell phone number", "work phone number", "home phone number",  "home address" , "work address", "grandma's address"]
  tags = [0, 0, 0, 0, 0, 1, 1, 0, 1, 1] #1 is optional
  info = inputting(values, tags, codeids)
  conn.execute("INSERT INTO customer values (" + info.get("id") + ",\"" + info.get("name") + "\"," + info.get("age") + ",\"" + info.get("card") + "\")")
  conn.commit()

  print("membership created!")
  
  # confluence("c_number", info.get("id"), "2", info.get("cphone"))
  # confluence("c_address", info.get("id"), "0", info.get("haddress"))

  confluencecheck("c_number", info.get("id"), "2", info.get("cphone"))
  confluencecheck("c_address", info.get("id"), "0", info.get("haddress"))


  confluencecheck("c_number", info.get("id"), "1", info.get("wphone"))
  confluencecheck("c_number", info.get("id"), "0", info.get("hphone"))
  confluencecheck("c_address", info.get("id"), "1", info.get("waddress"))
  confluencecheck("c_address", info.get("id"), "2", info.get("gaddress"))

  conn.commit()
  conn.close()
  print ("phone numbers and addresses inserted!")    
  
def addrem():
  values = ["wanted item (0 for apple, 1 for orange, 2 for bananas, 3 for watermelon, 4 for strawberries)", "wanted amound of that item"]
  codeids = ["item", "amount"]
  tags = [0, 0]
  cart = []
  cartamounts = []
  user_id = input("What is your id? ")
  amountofUsers = conn.execute("SELECT COUNT (cid) FROM customer WHERE cid = " + str(user_id))

  b = True
  for i in amountofUsers: # error catching if the id is invalid
    num = i[0] # yay it works
    if (num == 0):
      print("invalid")
      b = False
    else:
      continue

  if(b):
    addrem  = int(input("Do you want to add or remove items?(1 for add, 2 for remove) "))
    while True:
      cartinputs = inputting(values, tags, codeids) #get inputs for the cart
      if addrem == 1:
        if int(cartinputs.get("amount")) > 0:
          if cartinputs.get("item") in cart: #if item is found (existing)
            cartamounts[cart.index(cartinputs.get("item"))] = str(int(cartinputs.get("amount"))+ int(cartamounts[cart.index(cartinputs.get("item"))]))
            #adding original amount to the new amount just entered
          else: #if item is not in the cart
            cart.append(cartinputs.get("item"))
            cartamounts.append(cartinputs.get("amount"))
        else:
          print("Invalid value, please input a positive value")
      if addrem == 2:
        print("addrem 2")
        if int(cartinputs.get("amount")) > 0:
          amountarray = conn.execute("SELECT amount FROM cart WHERE item_id = " + cartinputs.get("item"))
          for amountlist in amountarray:
            amount = amountlist[0]
          insidecart = cartinputs.get("item") in cart
          if insidecart:
            cartindex = int(cartamounts[cart.index(cartinputs.get("item"))])
          print("test " + str(int(cartinputs.get("amount")) + (cartindex if insidecart else 0) <= int(amount)))
          if int(cartinputs.get("amount")) + (cartindex if insidecart else 0)<= int(amount):
            print(insidecart)
            if insidecart: #if item is found (existing)
              print(str(int(cartinputs.get("amount")) - cartindex))
              cartamounts[cart.index(cartinputs.get("item"))] = str(int(cartinputs.get("amount")) - cartindex)
              #adding original amount to the new amount just entered
            else: #if item is not in the cart
              print("signal")
              cart.append(cartinputs.get("item"))
              cartamounts.append(-1*int(cartinputs.get("amount")))
          else:
            print("You don't have that amount of items in your cart, please retry.")
        else:
          print("Invalid value, please input a positive value")
      if input("wanna stop? (y or n) ") == "y":
        break
      else:
        continue
    print(cart)
    print(cartamounts)
    for i in range (0, len(cart)):
      print("weitbgwiog " + cart[i])
      count_array = conn.execute("SELECT COUNT (amount) FROM cart WHERE item_id = " + str(cart[i])) 
      for count_thing in count_array:
        count = count_thing[0]
      print("count: " + str(count))
      if count == 0:
        conn.execute("INSERT INTO cart values (" + str(user_id) + "," + str(cart[i]) + "," + str(cartamounts[i]) + ")")
        conn.commit()
      else:
        amount_array_sqlite = conn.execute("SELECT amount FROM cart where cid = " + str(user_id) + " and item_id = " + cartinputs.get("item")) 
        print("warning") 
        for smth in amount_array_sqlite:
          item_amount = smth[0] 
          print("hi " + str(item_amount))
        # print("aaaaaaaaaaaaaaa " + str(int(item_amount) + int(cartinputs.get("amount"))))
        conn.execute("UPDATE cart SET amount = " + str(int(item_amount) + int(cartamounts[i])) + " WHERE cid = " + str(user_id) + " and item_id = " + str(cart[i]))
        print("-1 equal itme amount: " + str(-1*int(cartamounts[i]) == int(item_amount)))
        if -1*int(cartamounts[i]) == int(item_amount):
          conn.execute("DELETE FROM cart WHERE cid = " + str(user_id) + " and item_id = " + str(cart[i]))
        conn.commit()
    conn.close()
  else:
    print("bad, make a membership")
def viewcart():
  person_id = input("What is your id? ")
  cart = conn.execute("SELECT * FROM cart WHERE cid = " + str(person_id)) 
  for i in cart: 
    itemname = conn.execute("SELECT item_name FROM item WHERE item_id = " + str(i[1]))
    for j in itemname:
      print(str(j[0]) + ": " + str(i[2]))


def classicalbuy(): #deprecated
  values = ["id", "wanted item (0 for apple, 1 for orange, 2 for bananas, 3 for watermelon, 4 for strawberries)", "wanted amound of that item"]
  codeids = ["id", "item", "amount"]
  tags = [0, 0, 0]
  truevalues = inputting(values, tags, codeids)
  price = conn.execute("SELECT item_price FROM item i WHERE i.item_id = " + truevalues.get("item"))
  for x in price: 
    total_price = x[0]*float(truevalues.get("amount"))
  timestamp = str(datetime.datetime.now())
  conn.execute("INSERT INTO customer_item values (" + truevalues.get("id") + "," + truevalues.get("item") + "," + truevalues.get("amount") + ",\"" + timestamp + "\")")
  conn.commit()
  print("item bought!") 
  conn.close()  
  #time to grind life
  
def buycart():
  person_id = input("What is your id? ")
  timestamp = str(datetime.datetime.now())
  total_price = 0 
  insertlist = []
  cart = conn.execute("SELECT * FROM cart WHERE cid = " + str(person_id)) 
  for i in cart: 
    #i[1] is item_id
    #i[2] is amount
    pricearray = conn.execute("SELECT item_price from item WHERE item_id = " + str(i[1]))
    for pricething in pricearray:
      price = pricething[0]
      total_price += float(price)
    insertlist.append("INSERT INTO customer_item values(" + str(person_id) + ", " + str(i[1]) + ", " + str(i[2]) + ", \"" + timestamp + "\")")


  conn.execute("INSERT INTO corder values(" + str(person_id) + ", \"" + str(timestamp) + "\", " + str(total_price) + ")")
  conn.commit()
  for i in insertlist:
    conn.execute(i)
  conn.commit()
  conn.execute("DELETE FROM cart WHERE cid = " + str(person_id))
  conn.commit()
  conn.close()
    


"""
conn = sqlite3.connect("store.db");
e = conn.execute("SELECT * FROM customer")
for i in e:
  print(i);
f = conn.execute("SELECT * FROM c_number")
for i in f:
  print(i);
g = conn.execute("SELECT * FROM c_address")
for i in g:
  print(i);
conn.close()
"""



    