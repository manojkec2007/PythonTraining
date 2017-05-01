"""
9. Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 FAIL
Enter score: 0.95
A
Enter score: 11.5
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75
C
Enter score: 0.5
FAIL
"""
def score():
    score = float(input("Enter Score:"))
    if score >= 0.9 and score < 1.0:
        print "A"
    elif score >=0.8 and score < 0.9:
        print "B"
    elif score >=0.7 and score < 0.8:
        print "C"
    elif score >=0.6 and score < 0.7:
        print "D"
    elif score < 0.6:
        print "FAIL"
    else:
        print "Bad Score"
score()
score()
score()
score()
score()

