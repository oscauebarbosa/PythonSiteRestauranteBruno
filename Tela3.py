
from Modulos import *

def Contatos():
    print("Função Contatos chamada.")

TelaReserva = CriarJanela("Reserva", "400x500+650+150", 1)
TelaReserva.configure(fg_color= "#171717")
Abas = CriarAbas(TelaReserva, 3, 6, 350, 450, "Reservas", "Revisar pedido", "Contato")
Abas.configure(state="normal")

def EnviarDados():
    Lb_EnviarContatos.configure(text="Dados enviados!")

def ConfirmarReserva():
    Lb_ConfirmarReserva.configure(text="Reserva confirmada!")

def MudarpRevisar():
    Abas.set("Revisar pedido")

def MudarpContato():
    Abas.set("Contato")

def VoltarpReservas():
    Abas.set("Reservas")

def Finalizar():
    pass

def VoltarpRevisar():
    Abas.set("Revisar pedido")




################## HEADER  ##################
imgHeader = CriarImagem(TelaReserva, "Imagens/DELíCIA.png", 1, 6, 50, 230)




###########   Tela de Reservas   ###########

#Data
Lb_Data = CriarLabel(Abas.tab("Reservas"), "Data:", 1,0)
Lb_Data.grid(columnspan=6)
Lb_Data2 = CriarLabel(Abas.tab("Reservas"), "Data", 1, 6)
Lb_Data2.grid(columnspan=6)

# #Hora
Lb_Hora = CriarLabel(Abas.tab("Reservas"), "Hora:", 3, 0)
Lb_Hora.grid(columnspan=6)
Lb_Hora2 = CriarLabel(Abas.tab("Reservas"), "Hora", 3, 6)
Lb_Hora2.grid(columnspan=6)


#Número de Pessoas
Lb_Pessoas = CriarLabel(Abas.tab("Reservas"), "Número de pessoas:", 5, 0)
Lb_Pessoas.grid(columnspan=6)
Lb_Pessoas2 = CriarLabel(Abas.tab("Reservas"), "Pessoas", 5, 6)
Lb_Pessoas2.grid(columnspan=6)


#Mesa Reservada
Lb_Mesa = CriarLabel(Abas.tab("Reservas"), "Mesa reservada:", 7, 0)
Lb_Mesa.grid(columnspan=6)
Lb_Mesa2 = CriarLabel(Abas.tab("Reservas"), "Mesa", 7, 6)
Lb_Mesa2.grid(columnspan=6)


#Politicas de cancelamento
Lb_polCancelamento = CriarLabel(Abas.tab("Reservas"), "Políticas de cancelamento de reservas:", 9, 0)
Lb_polCancelamento.grid(columnspan=13)
Lb_polCancelamento2 = CriarLabel(Abas.tab("Reservas"), "Ao desmarcar de última hora, você prejudica"
                                                       "\n a chance de outras pessoas desfrutarem"
                                                       "\n da experiência.", 10, 0)
Lb_polCancelamento2.grid(columnspan=13)


#Botao
Lb_ConfirmarReserva = CriarLabel(Abas.tab("Reservas"), "", 11, 6)
btnConfirmarReserva = CriarBotão(Abas.tab("Reservas"), "Confirmar reserva!", ConfirmarReserva, 12, 3, 30, 30)
#
btnMudarpRevisar = CriarBotão(Abas.tab("Reservas"), "Avançar ->", MudarpRevisar, 12, 12, 30, 30)




###########   Revisar pedido   ###########

#Botao
btnVoltarpRevisar = CriarBotão(Abas.tab("Revisar pedido"), "<- Voltar", VoltarpReservas, 12, 2, 30, 30)
#
btnMudarpRevisar = CriarBotão(Abas.tab("Revisar pedido"), "Avançar ->", MudarpContato, 12, 10, 30, 30)





###########   Tela de Contato   ###########

#Nome
Lb_Cad_Nome = CriarLabel(Abas.tab("Contato"), "Nome:", 1, 5)
Lb_Cad_Nome.grid(sticky="S")
Cx_Cad_Nome = CriarCaixaDeTexto(Abas.tab("Contato"), 150, 30, 1, 6, "Insira seu nome")
Cx_Cad_Nome.grid(sticky="S")

#Telefone
Lb_Cad_Tel = CriarLabel(Abas.tab("Contato"), "Telefone:", 2, 5)
Lb_Cad_Tel.grid(sticky="S")
Cx_Cad_Tel = CriarCaixaDeTexto(Abas.tab("Contato"), 150, 30, 2, 6, "Insira seu telefone")
Cx_Cad_Tel.grid(sticky="S")

#Email
Lb_Cad_Email = CriarLabel(Abas.tab("Contato"), "Email:", 3, 5)
Lb_Cad_Email.grid(sticky="S")
Cx_Cad_Email = CriarCaixaDeTexto(Abas.tab("Contato"), 150, 30, 3, 6, "Insira seu email")
Cx_Cad_Email.grid(sticky="S")

#Botao
btnVoltarpRevisar = CriarBotão(Abas.tab("Contato"), "<- Voltar", VoltarpRevisar, 12, 2, 30, 30)
#
Lb_EnviarContatos = CriarLabel(Abas.tab("Contato"), "", 11, 6)
btnEnviarContatos = CriarBotão(Abas.tab("Contato"), "Enviar", EnviarDados, 12, 10, 30, 30)
























TelaReserva.mainloop()