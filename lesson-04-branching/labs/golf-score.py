# accept two integers from input for strokes and par
strokes = int(input())  # test inputs: 3, 2
par = int(input())  # test inputs: 4, 1

# eagle number of strokes is two less than par
Eagle = strokes == par - 2
# birdie number of strokes is one less than par
Birdie = strokes == par - 1
# par number of strokes is equal to par
Par = strokes == par
# bogey number of strokes is one more than par
Bogey = strokes == par + 1

if par not in (3, 4, 5):  # only allows 3, 4, 5 as valid par values
    score = "Error"  # print error if par is not 3, 4, or 5
elif Eagle is True:
    score = "Eagle"
elif Birdie is True:
    score = "Birdie"
elif Par is True:
    score = "Par"
elif Bogey is True:
    score = "Bogey"
else:  # print error at the end of output if score is not eagle, birdie, par, or bogey
    score = "Error"

print(f'Par {par} in {strokes} strokes is {score}')
