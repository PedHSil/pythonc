from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    
if __name__ == '__main__':
    p1 = Pessoa('luis', 30)