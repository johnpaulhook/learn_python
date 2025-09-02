import random


guesses = 0
# Put all words in a list (square brackets [])
words = [
    "apple","grape","pearl","stone","candy","brick","flame","chair","table","water",
    "light","plant","earth","music","dream","clock","grass","river","bread","sweet",
    "house","heart","mouth","beach","storm","green","black","white","brown","blue",
    "quiet","funny","happy","lucky","sharp","round","point","sword","arrow","spear",
    "crown","queen","joker","cards","coins","pouch","boots","socks","shirt","pants",
    "skirt","dress","cabin","field","woods","mount","hills","plaza","track","train",
    "plane","truck","bikes","camel","zebra","horse","sheep","goats","geese","ducks",
    "eagle","raven","swanx","fishy","whale","shark","crabs","frogs","snail","worms",
    "tiger","lions","bears","otter","panda","lemur","koala","mouse","snake","viper",
    "cobra","gecko","spide","insect","roses","tulip","daisy","lotus","poppy","wheat",
    "mango","peach","berry","melon","olive","lemon","chili","sauce","sugar","honey",
    "pizza","drink","juicy","shake","latte","cocoa","spoon","forks","knife","plate",
    "glass","books","story","novel","poems","voice","laugh","smile","teeth","brain",
    "blood","cells","bones","spine","robot","wheel","metal","gears","laser","games",
    "chess","dicey","sport","teams","goals","kickx","block","catch","throw","punch",
    "fight","magic","spell","curse","ghost","demon","angel","fairy","giant","troll",
    "elfin","dwarf","orcsy","dragon","flame","storm","cloud","rainy","sunny","moons",
    "stars","space","orbit","comet","earth","venus","pluto","alien","power","quick",
    "grand","minor","alpha","omega","sigma","delta","kitty","puppy","cubsx","foals",
    "orang","green","brown","clear","shiny","rough","solid","fluid","rocks","miner",
    "golds","stone","cryst","armor","plate","magic","altar","prayx","bless","faith",
    "devil","satan","ghoul","mummy","zomby","skull","grave","coffin","beard","faces",
    "mouth","tooth","heart","dream","craft","paint","color","novel","music","dance",
    "peace","truce","lovee","happy","funny","silly","crazy","quick","night","dawns",
    "dusky","hours","clock","watch","bells","alarm","sound","noise","blast","storm",
    "light","darkx","shine","spark","world","ocean","river","swamp","plains","mount",
    "rocks","cabin","house","gates","barns","shops","roads","track","train","plane",
    "boats","truck","wagon","sleds","snowy","cloud","storm","comet","orbit","space",
    "alien","witch","fairy","elves","angel","dragon"
]

# Pick a random word
word = random.choice(words)
letters = list(word)

while True:
    guess = input("Put a five letter word: ").lower()
    g_letters = list(guess)
    
    # check length
    if len(guess) != 5:
        print(" Please enter exactly 5 letters!")
        continue

    if guess == word:
        print(" You guessed it! The word was:", word)
        break
    elif guess != word:
        print(" Not correct, try again.")
        guesses += 1
    
    if guesses == 6:
        break
    
    if (g_letters[0] == letters[0]):
        print("the first letter is correct")
    elif g_letters[0] in letters[1:]:
        print ("the first letter of your guess is in the word")
    else:
        print("the first letter is not correct")
        
    if (g_letters[1] == letters[1]):
        print("the second letter is correct")
    elif g_letters[1] in letters[1:]:
        print ("the second letter of your guess is in the word")
    else:
        print("the second letter is not correct")
        
    if (g_letters[2] == letters[2]):
        print("the third letter is correct")
    elif g_letters[2] in letters[1:]:
        print ("the third letter of your guess is in the word")
    else:
        print("the third letter is not correct")
        
    if (g_letters[3] == letters[3]):
        print("the fourth letter is correct")
    elif g_letters[3] in letters[1:]:
        print ("the fourth letter of your guess is in the word")
    else:
        print("the fourth letter is not correct")
        
    if (g_letters[4] == letters[4]):
        print("the fith letter is correct")
    elif g_letters[4] in letters[1:]:
        print ("the fith letter of your guess is in the word")
    else:
        print("the fith letter is not correct")
        
    
        