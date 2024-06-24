# Example:
# It is used to join 2 lists, but it does not remove duplicate objects. (It inserts the objects from the desired list into the original list).
				
linguagens = ["python", "js", "c"]
					
print(linguagens) 
#>>> ["python", "js" "c"]
					
linguagens.extend(["java", "csharp"])
					
print(linguagens)
#>>> ["python", "js", "c", "java", "csharp"]