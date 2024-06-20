# AND = para ser true tudo tem que ser True
# OR = para ser True apenas um tem que ser True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

# Case 1

#Operador E
saldo = 100
saque = 200
limite = 100

exp_1 = saldo >= saque and saque <= limite
print(exp_1)


#Operador OU
saldo = 1000
saque = 200
limite = 100

exp_2 = saldo >= saque or saque <= limite
print(exp_2)

# Case 2
saldo = 1000
saque = 250
limite = 200
conta_especial = True

conta_normal_com_saldo_sufuciente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_sufuciente or conta_especial_com_saldo_suficiente
print(exp_3)
