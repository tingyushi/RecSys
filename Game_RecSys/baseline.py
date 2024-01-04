import pandas as pd
from collections import defaultdict

"""
Time-played baseline: 
compute averages for each user, or return the global average if we've never seen the user before

prediction using validation set 
"""

# training
df = pd.read_csv('data/hoursTrain.csv')
trainUsers = list(df['userID'])
trainItems = list(df['itemID'])
trainHours = list(df['hours_transformed'])

allHours = []
userHours = defaultdict(list)

for user, game, hour in zip(trainUsers, trainItems, trainHours):
   allHours.append(hour)
   userHours[user].append(hour)

globalAverage = sum(allHours) / len(allHours)

userAverage = {}
for u in userHours:
    userAverage[u] = sum(userHours[u]) / len(userHours[u])


# make predictions
df = pd.read_csv('data/hoursValid.csv')
validUsers = list(df['userID'])
validItems = list(df['itemID'])
validHours = list(df['hours_transformed'])

prediction = []
for user in validUsers:
    if user in userAverage:
        prediction.append(userAverage[user])
    else:
        prediction.append(globalAverage)

temp = [(x-y)**2 for x, y in zip(prediction, validHours)]
mse = sum(temp) / len(temp)
print(f"hours prediction MSE on validation set = {mse}")


"""
Would-play baseline:
just rank which games are popular and which are not, 
and return '1' if a game is among the top-ranked

prediction using validation set
"""

# training
df = pd.read_csv('data/playedTrain.csv')
trainUsers = list(df['userID'])
trainItems = list(df['itemID'])
trainPlayed = list(df['played'])

gameCount = defaultdict(int)
totalPlayed = 0

for game in trainItems:
    gameCount[game] += 1
    totalPlayed += 1

mostPopular = [(gameCount[x], x) for x in gameCount]
mostPopular.sort()
mostPopular.reverse()

return1 = set()
count = 0
for ic, i in mostPopular:
    count += ic
    return1.add(i)
    if count > totalPlayed/2: break

# make predictions
df = pd.read_csv('data/playedValid.csv')
validUsers = list(df['userID'])
validItems = list(df['itemID'])
validPlayed = list(df['played'])

correct = 0

for item, played in zip(validItems, validPlayed):
    if item in return1:
        pred = 1
    else:
        pred = 0
    if pred == played:
        correct += 1

accu = correct / len(validItems)

print(f"played prediction accuracy on validation set = {accu}")
