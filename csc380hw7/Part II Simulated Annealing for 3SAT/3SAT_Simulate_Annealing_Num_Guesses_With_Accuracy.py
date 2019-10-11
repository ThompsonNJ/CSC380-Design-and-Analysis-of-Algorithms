import random, time, math

from Term import *
from Clause import *


def randomAssignment(assignments):
    ''' Randomly assign True or False to each element in the list
    assignments.  '''
    for i in range(len(assignments)):
        if random.randint(1,2) == 1:
            assignments[i] = False
        else:
            assignments[i] = True

def hillClimb(clauses, guess):
    ''' Finds a new "guess" that is better than the input "guess".  Each possible
    "new guess" is made by flipping one variable in "guess" from True to False (or
    vice versa).
    Returns False if it can't find a better guess.  '''

    # assume the minimum is the current guess
    minValue = [(Clause.countTrue(clauses, guess), guess)]

    # if the current guess solves the problem, don't try any others
    if Clause.countTrue(clauses, guess) == len(clauses):
        return guess

    foundBetter = False
    for i in range(0, len(guess)):
        newGuess = guess.copy()

        # the next statement flips the True/False value at index i
        newGuess[i] = True if guess[i] == False else False
        count = Clause.countTrue(clauses, newGuess) # see how good the new guess is

        if count == len(clauses): # perfect.   No need to try anything else.
            return newGuess

        if count > minValue[0][0]: # better than the best so far
            minValue = [(count, newGuess)]
            foundBetter = True
        elif count == minValue[0][0] and foundBetter: # equal to the best so far
            minValue.append((count, newGuess))

    if not foundBetter:
        return False

    # pick one at random
    index = random.randint(0, len(minValue) - 1)
    return minValue[index][1]

def simulatedAnnealing(allClauses, currentGuess):
    temperature = 100
    numGuesses = 0
    coolingRate = 0.995
    while temperature > 0.00001:
        temperature *= coolingRate
        currentScore = Clause.countTrue(allClauses, currentGuess)
        
        i = random.randint(0, len(currentGuess) - 1)
        newGuess = currentGuess.copy()
        newGuess[i] = True if newGuess[i] == False else False
        newScore = Clause.countTrue(allClauses, newGuess)
        numGuesses += 1

        if Clause.countTrue(allClauses, newGuess) == len(allClauses):
            return [newGuess, numGuesses, max(newScore, currentScore), len(allClauses)]

        if newScore > currentScore:
            currentGuess = newGuess

        else:
            prob = math.e ** ((newScore - currentScore) / temperature)

            if random.random() < prob:
                currentGuess = newGuess

    return [currentGuess, numGuesses, max(newScore, currentScore), len(allClauses)]


# let's play
numExperi = 32
for n in range(3, 76):
    numGuesses = 0
    correctCount = 0
    totalClauses = 0
    for i in range(numExperi):
        assignments = n*[True]
        randomAssignment(assignments)
        m = n * 10
        allClauses = []
        for i in range(m):
            allClauses.append(Clause.randomClauseThatIsSatisfiable(n, assignments))

        # HILL W/O RESTART HILL W/O RESTART HILL W/O RESTART
        randomGuess = [True if random.randint(1,2) == 1 else False for _ in range(n)]
        theGuess = randomGuess       
        while theGuess != False and Clause.countTrue(allClauses, theGuess) != len(allClauses):
            temp = simulatedAnnealing(allClauses, theGuess)
            theGuess = temp[0]
            numGuesses += temp[1]
            correctCount += temp[2]
            totalClauses += temp[3]

    numGuesses /= numExperi
    accuracy = correctCount / totalClauses
    print(n, "\t", numGuesses, "\t", accuracy)
