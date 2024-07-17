class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
 
    def verificar_saldo(self):
        return self.saldo
 
    def mensagem_personalizada(self):
        saldo = self.verificar_saldo()
        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
 
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
 
    def verificar_saldo(self):
        saldo_usuario = self.plano.verificar_saldo()
        mensagem_usuario = self.plano.mensagem_personalizada()
        return saldo_usuario, mensagem_usuario
 
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = UsuarioTelefone(nome_usuario, plano_usuario)
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
 
print(mensagem_usuario)