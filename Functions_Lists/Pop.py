# Imagine it as a stack of dishes, where the first dish added to the table is below the others.
# The last dish would be on top of all, when we were to select we would pick up (remove) this last object from the list, or last element added to the list.
# Simply put, it removes the last object added to the list.

linguagens = ["python", "js", "c", "java", "csharp"]
					
print(linguagens.pop())	
# >>> csharp
print(linguagens.pop())	
#>>> java
print(linguagens.pop())	
#>>> c
print(linguagens.pop(0))	
#>>> python
