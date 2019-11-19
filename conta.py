class Conta:
    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura

         
    def atualiza(self, taxa_percentual):
        self.saldo *= taxa_percentual        
         
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
    def __str__(self):
        return '''
Isso é uma Conta, meu jovi :v
'''
        
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
            
class ContaCorrente(Conta):    
    def atualiza(self, taxa_percentual):
        self.saldo *= 2*taxa_percentual
    def deposita(self, valor):
        self.saldo += valor - 0.1
        
class ContaPoupanca(Conta):    
    def atualiza(self, taxa_percentual):
        self.saldo *= 3*taxa_percentual

class AtualizadorDeContas:
    def __init__(self, taxa):
        self._taxa = taxa
        
    def roda(self, conta):
        print('\n')
        conta.extrato()
        conta.atualiza(self._taxa)
        print('==========')
        conta.extrato()
        print('\n')

class Banco:
    def __init__(self, contas=[]):
        self._contas = contas
    
    def adicionaConta(self, conta):
        self._contas.append(conta)
        
    def pegaConta(self, posicao):
        return self._contas[posicao]
    
    def pegaTotalDeContas(self):
        return len(self._contas)

d1 = Data(11, 4, 2002)
d2 = Data(30, 11, 2100)
cl1 = Cliente('Maria', 'Nascimento', '12830439635')
ct1 = Conta(11111, cl1, 0, 5000, d1)
cl2 = Cliente('Joao', 'Irinelson', '12830439636')
ct2 = Conta(11112, cl2, 0, 5000, d2)

cc = ContaCorrente(11113, cl2, 0, 5000, d2)
cc.deposita(10)

atualizador = AtualizadorDeContas(1.1)
atualizador.roda(cc)

bb = Banco()
bb.adicionaConta(ct1)
bb.adicionaConta(ct2)
bb.adicionaConta(cc)

qnt = bb.pegaTotalDeContas()
for i in range(qnt):
    atualizador.roda(bb.pegaConta(i))
