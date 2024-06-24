# Example: 
# Interatable order, basically the same as "sort", the difference is that it is a function.		

linguagens = ["python", "js", "c", "java", "csharp"]
					

print(sorted(linguagens, key=lambda x: len(x)))
# >>> ["c", "js", "java", "python", "csharp"]
					

print(sorted(linguagens, key=lambda x: len(x), reverse=True))
# >>> ["python", "csharp", "java", "js", "c"]