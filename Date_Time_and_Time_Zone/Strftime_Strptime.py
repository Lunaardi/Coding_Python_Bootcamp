from datetime import datetime

data_hora_atual = datetime.now()        # Imprime em formato americano
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %H:%M %a"         # adicionamos dia da semana que é a letra a
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual)
print(data_hora_atual.strftime(mascara_ptbr))         # O strftime é um mascará para a data atual que seja passada como uma variavel

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(data_convertida.strftime("%Y"))

print(type(data_convertida))