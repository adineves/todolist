# Criar Layout
import PySimpleGUI as sg

def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    Layout = [
         [sg.Frame('Tarefas', layout=linha, key='container')],
         [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Lista de Tarefas', layout=Layout, finalize=True)
#Criar Janela
janela = criar_janela_inicial()

#Criar regras da janela
while True:
    event, value = janela.read()
    if event ==  sg.WIN_CLOSED:
            break
    elif event == 'Nova Tarefa':
         janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Resetar':
         janela.close()
         janela = criar_janela_inicial()