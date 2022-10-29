import wikipedia

x = 'y'

while x == "y":
    wikPage = input('What wiki page would you like info from?')
    print(wikipedia.summary(wikPage))
    x = input('Would you like to check another article?')