fruits=['banana','apple','plum']

# d={}

# for i in fruits:
#     d.update({i:len(i)})

# print(d)


d={i:len(i) for i in fruits}

print(d)