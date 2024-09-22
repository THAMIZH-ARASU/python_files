txt=['cardio','renal','neuro','peds','cancer','colon']
new=[x for x in txt if x != 'peds']
len=[0,1,2,3,4,5,6,8,9,4,7]
l=[i for i in len if i<5]


print(new)
print(l)