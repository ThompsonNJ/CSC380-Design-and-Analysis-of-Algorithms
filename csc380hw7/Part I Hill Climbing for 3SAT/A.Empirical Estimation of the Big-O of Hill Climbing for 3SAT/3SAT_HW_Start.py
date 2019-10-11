import random, time

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


# let's play
num_experi = 100
for n in range(3, 76):
    num_guesses = 0
    for i in range(num_experi):
        assignments = n*[True]
        randomAssignment(assignments)
        
        m = n * 10
        allClauses = []
        for i in range(m):
            allClauses.append(Clause.randomClauseThatIsSatisfiable(n, assignments))

        # BRUTE BRUTE BRUTE
        # now can we find that set of assignments if we don't know it
        # brute force, try all assignments
##        for decimal in range(0, 2**n):
##            # convert to strings
##            binString = format(decimal, '0' + str(n) + 'b')
##            possibleAssignment = [True if ch == '1' else False for ch in binString]
##            if Clause.allClausesTrue(allClauses, possibleAssignment):
##                break

        # HILL W/RESTART HILL W/RESTART HILL W/RESTART
        randomRestart = True
        restartCount = 1
        while randomRestart:
            randomGuess = [True if random.randint(1,2) == 1 else False for _ in range(n)]
            x = 0
            theGuess = randomGuess
            while theGuess != False and Clause.countTrue(allClauses, theGuess) != len(allClauses):
                x += 1
                num_guesses += 1
                theGuess = hillClimb(allClauses, theGuess)
                if theGuess != False:
                    pass


            if theGuess == False:
                restartCount += 1
            else:
                randomRestart = False
                            
    num_guesses /= num_experi
    print(n, "\t", num_guesses)
