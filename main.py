from replit import clear
import art
print(art.logo)

bidd_dict = {}
maior_dic = {}
other = True
maior = 0
winner =""

while other == True:
  name = input ("What is your name?: ")
  bid = int(input ("What's your bid?: $"))
  other = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if bid > maior:
    maior=bid
    winner = name
    maior_dic = {name: bid}

  bidd_dict[name]= (bid)
  if other == "no":
    other = False
    clear()
  else:
    other = True
    clear()

print (f"The winner is:{winner} with the bid of ${maior}")
    


