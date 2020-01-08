import random
highScores = [1000,950,850,700,675,550,443,414,395,380]
prices =[9.99,10.25,19.99,100.0]
dogBreeds = ["Poodle","Collie","Beagle"]
logicalResults = [True, True, False,True]
myCollection = [1000, 3.14159, "Carrots",False]
top_games = ["StarWars",
             "Minecraft",
             "Mario Kart",
             "Star Wars Force Unleashed",
             "Destiny 1",
             "Skyrim",
             "Ocarina of time",
             "HaloReach",
             "Wii Sports",
             "Roblox",
             "Halo 3 ODST",
             "Rainbow Six Siege",
             "Mario",
             "Rocket League",
             "Battlefield 4",
             "Dark Souls",
             "Castle Crashers",
             "ForHonor",
             "Shrek The Game",
             "Doom",]
if "Fortnite" in top_games:
    print("Fail")
elif top_games[0] != "StarWars":
    print("Fail")
else:
    print("Pass")
print(len(top_games))
for i in range (0,4): #for i in range (0, len(top_games)):
    print(top_games[i])
randomnum = random.randint(0,len(top_games))
print(top_games[randomnum])
top_games[0] = "Rainbow Six Siege"
if "Fortnite" in top_games:
    print("Fail")
elif top_games[0] != "Rainbow Six Siege":
    print("Fail")
else:
    print("Pass")
worstGames = ["Fortnite",
              "Anthem",
              "Apex Legends",
              "Evolve",
              "World of Warcraft",
              "Modern Warfare",
              "Halo5",
              "Rabbids",
              "Avengers the game",]
print(worstGames[0:3])
