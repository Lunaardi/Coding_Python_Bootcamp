# Example
# Will sort our list
# Note1: remembering that lambda is an anonymous function.
# Note2: len(x) takes (checks, reads, looks) the size of a string, that is, how many characters it has.			
				
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)
# >>> [["c", "csharp", "java", "js", "python"]]
					
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)
# >>> [["python", "js", "java", "csharp", "c"]]
					
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) #ordenando por tamanho de palavras ou seja do menor para o maior ()
print(linguagens)
# >>> [["c", "js", "java", "python", "csharp"]]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) #ordenando por tamanho de palavras ou seja do maior para o menor
print(linguagens)
#>>> [["python", "csharp", "java", "js", "c"]]
