class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        
    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        if valor > self.saldo or valor <= 0:
            return False
        else:
            self.saldo -= valor
            return True
        
    def extrato(self):
        print('Cliente: {} {}'.format(self.titular.nome, self.titular.sobrenome))
        print('CPF: {}'.format(self.titular.cpf))
        print('Saldo: R$ {}'.format(self.saldo))
        
    def transfere_para(self, conta_destino, valor):
        if valor <= self.saldo:
            self.saca(valor)
            conta_destino.deposita(valor)
            return True
        else:
            return False
    
    def atualiza(self, taxa_percentual):
        pass
    

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
  
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Historico:
    def __init__(self):
        self.historico = []
            
class ContaCorrente:
    pass
        


d1 = Data(11, 4, 2002)
d2 = Data(30, 11, 2100)
cl1 = Cliente('Maria', 'Nascimento', '12830439635')
ct1 = Conta(11111, cl1, 0, 5000, d1)
cl2 = Cliente('Joao', 'Irinelson', '12830439636')
ct2 = Conta(11112, cl2, 0, 5000, d2)
