questions = []
questions.append("Q1: Python was developed in ")
questions.append("Q2: c++ was developed in")
questions.append("Q3: HTML was developed in")
questions.append("Q4: which one is ont a keyword")
questions.append("Q5: full form of css ")
questions.append("Q5: full form of css ")
questions.pop()

options = [
    ("A: 1990" , "B: 1991" , "C: 1999" , "D: 2000"),
    ("A: 1990" , "B: 1991" , "C: 1979" , "D: 2000"),
    ("A: 1991" , "B: 1980" , "C: 1999" , "D: 2000"),
    ("A: true" , "B: true" , "C: false" , "D: none"),
    ("A: cascadile style sheet" , "B: cagshsj" , "C: hdbhjdb" , "D: cascadile style sheet"),
]

answer = ["B","C","A","A","D"]

ans=[]
points=0

print(questions[0])
print(options[0])
ans.append(input("select the correct opption").upper())
points= points + 1 if ans[0] ==answer[0] else points

print(questions[1])
print(options[1])
ans.append(input("select the correct opption").upper())
points= points + 1 if ans[1] ==answer[1] else points


print(questions[2])
print(options[2])
ans.append(input("select the correct opption").upper())
points= points + 1 if ans[2] ==answer[2] else points


print(questions[3])
print(options[3])
ans.append(input("select the correct opption").upper())
points= points + 1 if ans[3] ==answer[3] else points


print(questions[4])
print(options[4])
ans.append(input("select the correct opption").upper())
points= points + 1 if ans[4] ==answer[4] else points



print()
print(f"Total points are : {points}")
print(f"your selected options are {ans}")
print(f"your correct options are {answer}")
