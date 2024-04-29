#Sistema de Gerenciamento de Funcionários

#1. Single Responsibility Principle 
#Neste princípio afirma que uma classe deve ter apenas uma razão para mudar. 
#Aplicando em uma classe Employee que representa um funcionário.


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.1

#Neste exemplo, a classe Employee tem a responsabilidade de armazenar informações sobre 
#um funcionário e calcular o bônus com base no salário. Está seguindo o SRP porque só tem 
#uma razão para mudar: se a forma de calcular o bônus mudar.


#2. Open-Closed Principle
#Este princípio afirma que as entidades de software (classes, módulos, funções, etc.) devem estar 
#abertas para extensão, mas fechadas para modificação. Aplicando e criando uma classe BonusCalculator que 
#pode calcular bônus para diferentes tipos de funcionários sem modificar a classe Employee.

class BonusCalculator:
    def calculate_bonus(self, employee):
        if isinstance(employee, Manager):
            return employee.salary * 0.2
        elif isinstance(employee, Developer):
            return employee.salary * 0.15
        else:
            return employee.salary * 0.1

#Dessa forma, caso se precise adicionar novos tipos de funcionários no futuro, podesse simplesmente estender essa classe
#adicionando novas condições sem modificar o código.


#3. Dependency Inversion Principle
#Neste exemplo, o princípio afirma que os módulos de alto nível não devem depender de módulos de baixo nível, ambos devem depender 
#de abstrações. Aplicando em uma interface EmployeeRepository que será usada para acessar os dados dos funcionários.

from abc import ABC, abstractmethod
class EmployeeRepository(ABC):
    @abstractmethod
    def get_employee(self, employee_id):
        pass

    @abstractmethod
    def save_employee(self, employee):
        pass

class DatabaseEmployeeRepository(EmployeeRepository):
    def get_employee(self, employee_id):
        # Acessa um funcionário do banco de dados
        pass

    def save_employee(self, employee):
        # Salva o funcionário no banco de dados
        pass

#Dessa forma, o módulo de alto nível (por exemplo, a lógica de negócios que usa os funcionários) pode depender da interface 
#EmployeeRepository, enquanto os detalhes de implementação (por exemplo, o acesso ao banco de dados) são encapsulados na classe 
#DatabaseEmployeeRepository.


#4. Prefira Composição a Herança
#Este princípio sugere que a composição de objetos é geralmente preferível à herança de classes. Aplicando em um cenário onde 
#se precisa modelar diferentes tipos de funcionários com habilidades específicas.

class Skill:
    def __init__(self, name):
        self.name = name

class Employee:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

class Developer(Employee):
    def __init__(self, name, skills):
        super().__init__(name, skills)
        self.role = "Developer"

class Manager(Employee):
    def __init__(self, name, skills):
        super().__init__(name, skills)
        self.role = "Manager"

#Neste exemplo, Developer e Manager são tipos de funcionários que compartilham características comuns com a classe Employee, 
#mas também têm características específicas (role). Em vez de usar herança para isso, usasse a composição incluindo uma lista de 
#habilidades (Skill) em cada funcionário.
