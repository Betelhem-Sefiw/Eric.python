# def get():
#     students= []
#     while True:
#         name= input("name: ")
#         if name=='q':
#             break
#         scores= []
#         total= 0
#         forgit push -u origin main --force i in range(3):
#             score= int(input(f"score {i+1} : "))
#             scores.append(score)
#             total+= score
#         average= total/3
#         students.append({
#             "name": name,
#             "score" : scores,
#             "average": average
#         })
#     return students
# def display(name, score):
#     print("name\tscore1\tscore2\tscore3\taverage\n")
#     for s in students:
#         print(f"{s['name']}\t{s['score'][0]}\t{s['score'][1]}\t{s['score'][2]}\t{s['average']}")
# get(name, score)
# display(name, score)
def get(names, scores, averages):
    student= []
    while True:
        name= input("name: ")
        if name=='q':
            break
        temp_score= []
        total= 0
        
        for n in range(3):
           score= int(input("score "+ str(n+1) + ": "))
           temp_score.append(score)
           total+= score
            
        average= total/3
        names.append(name)
        scores.append(temp_score)
        averages.append(average)

def display(names, scores, averages):
    print("name\tscore1\tscore2\tscore3\taverage\n")
    for i in range(len(names)):
        print(f"{names[i]}\t{scores[i][0]}\t{scores[i][1]}\t{scores[i][2]}\t{averages[i]}")
names=[]
scores= []
averages= []
get(names, scores, averages)
display(names, scores, averages)
