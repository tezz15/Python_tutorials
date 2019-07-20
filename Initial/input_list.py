games = input("Enter integers seperated by a coma and a space: ")

games_list = games.split(", ")
print("\nPrinting all the games you know:")
print(games_list)
#for game in games_list:
#    print(game.capitalize())
#print(int(games_list[0])+int(games_list[1]))
b = 0
for a in games_list:
    b+=int(a)
print(b)