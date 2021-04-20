from abc import ABC, abstractmethod

class Funcionario (ABC):
    def __init__ (self, nome, cpf, data_nasc, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nasc = data_nasc
        self.__salario = salario
    
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_dia_nasc(self):
        return self.__data_nasc [0] + self.__data_nasc [1]
    
    def get_mes_nasc(self):
        return self.__data_nasc [3] + self.__data_nasc [4]
    
    def get_ano_nasc(self):
        return self.__data_nasc [6] + self.__data_nasc [7] + self.__data_nasc [8] + self.__data_nasc [9]
    
    def get_salario(self):
        return self.__salario

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf
    
    def set_data_nasc(self, nova_data_nasc):
        self.__data_nasc = nova_data_nasc
    
    def set_salario(self, novo_salario):
        self.__salario = novo_salario
    
    @abstractmethod
    def calcular_salario_final(): 
        pass
    
    @abstractmethod
    def converter_para_string():
        pass

class Vendedor (Funcionario):
    def __init__ (self, nome, cpf, data_nasc, salario, quantidade_vendas):
        super().__init__(nome, cpf, data_nasc, salario)
        self.__quantidade_vendas = quantidade_vendas
    
    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        self.__salario = novo_salario

    def get_quantidade_vendas(self):
        return self.__quantidade_vendas
    
    def set_quantidade_vendas(self, nova_quantidade_vendas):
        self.__quantidade_vendas = nova_quantidade_vendas
    
    def calcular_salario_final(self):
        x = self.get_salario
        self.salario = self.get_salario + (x * 0.005) *  self.get_quantidade_vendas
        return self.salario
    
    def converter_para_string(self):
        return self.__nome+";"+self.__cpf+";"+self.__data_nasc [6] + self.__data_nasc [7] + self.__data_nasc [8] + self.__data_nasc [9]+"-"+self.__data_nasc [3] + self.__data_nasc [4]+ "-" +self.__data_nasc [0] + self.__data_nasc [1] + ";" + f'{self.get_salario:.2f}' + ";" + self.__quantidade_vendas

class Gerente (Funcionario):
    def __init__ (self, nome, cpf, data_nasc, salario, vendedores):
        super().__init__(nome, cpf, data_nasc, salario)
        self.__vendedores = vendedores

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        self.__salario = novo_salario

    def get_cpf(self):
        return self.__cpf

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def get_vendedores(self):
        return self.__vendedores
    
    def set_vendedores(self, vendedores):
        self.__vendedores = vendedores

    def adicionar_vendedor(vendedores, novo_vendedor):
        vendedores = vendedores + novo_vendedor
    
    def calcular_salario_final(self, salario):
        salario = salario + (salario * 0.001) *  self.get_quantidade_vendas
        return salario
    
    def converter_para_string(self, listacpf):
        listacpf = []
        listacpf = listacpf + self.get_cpf
        return self.__nome+";"+self.__cpf+";"+self.__data_nasc [6] + self.__data_nasc [7] + self.__data_nasc [8] + self.__data_nasc [9]+"-"+self.__data_nasc [3] + self.__data_nasc [4]+ "-" +self.__data_nasc [0] + self.__data_nasc [1] + ";" + f'{self.get_salario:.2f}' + ";" + listacpf
