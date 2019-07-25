# #functions
# def addtwonumbers():
#     sum=10+20
#     return sum
# # print(addtwonumbers())
#
# #functions with parameters
# def addnumbers(a,b):#wih parameters
#     sum=a+b
#     return sum
# # print(addnumbers(10,20))#with arguements
#
# #print grade
# def findgrade(a,b,c,d,e):
#     total=a+b+c+d+e
#     avg=total/5
#     if avg<50:
#         return "pass", total, avg
#     else:
#         return "pass", total, avg

# separate the functions
def findtotal(a,b,c,d,e):
    total=a+b+c+d+e
    return total

def findavg(total):
    return total/5

def findgrade(avg):
    if avg<50:
        return "pass"
    else:
        return "pass"

total=(findtotal(45,67,34,78,65))
average=findavg(total)
grade=findgrade(average)

