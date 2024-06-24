# Example
# It returns a list equal to the one passed but in a different instance, this has no impact on the original list it is changed.

list = [1, "Python", [40, 30, 20], "Bitcoin"]

otherlist= list.copy()

print(list)
print(otherlist)
