
class InvalidTransaction(Exception):
    def message(self):
        return "Transaction Error: {} exceded".format(self.excesso())


class InsufficientFunds(InvalidTransaction):

    def __init__(self, saldo_atual, quantidade):
        super().__init__("sua conta nao tem R${}".format(quantidade))

        self.quantidade = quantidade
        self.saldo_atual = saldo_atual

    def excesso(self):
        return self.quantidade - self.saldo_atual
try:
    raise InsufficientFunds(10, 20)
except InsufficientFunds as e:
    print("$$$$ {}".format(e.message()))
