

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __repr__(self):
        return "{}/{}/{}".format(self.dia, self.mes, self.ano)

    @classmethod
    def de_string(cls, data_string):    #10-10-2016
        '''
        Receive the class as parameter
        classmethod creates new instances of class
        Can be heritence
        '''
        kwargs = {}
        kwargs['dia'], kwargs['mes'], kwargs['ano'] = map(int, data_string.split('-'))
        return cls(**kwargs)

    @staticmethod
    def is_date_valid(data_string):
        '''
        Not has class and instance
        Can't be heritence
        '''
        dia, mes, ano = map(int, data_string.split('-'))
        return dia <= 31 and mes <= 12 and ano <= 2018


print(Data.de_string('12-06-2017'))
print(Data.is_date_valid('12-13-2014'))
print(Data.is_date_valid('12-12-2014'))
