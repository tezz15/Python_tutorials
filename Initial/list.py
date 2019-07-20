#a = [1,2,3,"hello",1.2,1+2j]
#print(a[5])

#Taking input from the list 
games = input("Enter the game separated by a space and coma: ")

games_list = games.split(", ")

for game in games_list:
    print(game)
