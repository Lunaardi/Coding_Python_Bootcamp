# Example
# Unlike Direct Access where I pass the coordinate and it brings me the object, in index I pass the object and it brings me the coordinate.
# It is limited to bringing only the first occurrence in which the object appears

linguagens = ["python", "js", "c", "java", "csharp"]
					
print(linguagens.index("java"))
#>>> 3
					
print(linguagens.index("python"))
#>>> 0