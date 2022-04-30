def game():
    


    return 501 

score=game()
with open('highscore.txt') as f:
    highscore=f.read()

if highscore=='':
    with open('highscore.txt','w') as f:
        f.write(str(score))

elif int(highscore)<score:
    with open("highscore.txt",'w') as f:
        f.write(str(score))