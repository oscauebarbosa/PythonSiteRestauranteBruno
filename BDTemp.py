#-----------------------------------------Reservas-----------------------------

class Reserva:
    def __init__(self, Data, Hora, Pessoa, Mesa):
        self.Data = Data
        self.Hora = Hora
        self.Pessoa = Pessoa
        self.Mesa = Mesa


ListaReserva = []


def CadastrarBD(Data, Hora, Pessoa, Mesa):
    print(Data, Hora, Pessoa, Mesa)
    Obj = Reserva (Data, Hora, Pessoa, Mesa)
    ListaReserva.append(Obj)


def AutenticarBD(Data, Hora, Pessoa, Mesa):
    if not ListaPessoa:
        return "Vazia"
    else:
        for User in ListaPessoa:
            if User.Nome == Nome and User.Telefone == Telefone and User.Email == Email:
                return "Certo"

        return "Errado"


# ----------------------------------------Contato------------------------------
class Pessoa:
    def __init__(self, Nome, Telefone, Email):
        self.Nome = Nome
        self.Telefone = Telefone
        self.Email = Email


ListaPessoa = []


def CadastrarBD(Nome, Telefone, Email):
    print(Nome, Telefone, Email)
    Obj = Pessoa(Nome, Telefone, Email)
    ListaPessoa.append(Obj)


def AutenticarBD(Nome, Telefone, Email):
    if not ListaPessoa:
        return "Vazia"
    else:
        for User in ListaPessoa:
            if User.Nome == Nome and User.Telefone == Telefone and User.Email == Email:
                return "Certo"

        return "Errado"

