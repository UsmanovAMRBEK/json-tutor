l = [44,44,10,10,1,1,2,2,3,3,3,4,5,5]
print(set(l))
new_arr = []
for i in l:
    if i not in new_arr:
        new_arr.append(i)

print(new_arr)