import PySimpleGUI as sg


def criar_menu():

    menu_def = [
        ['Curso de Programação', ['Como é esse curso de Programação?',
                                  'Quem é o professor de Programação?',]],
        ['CVTI', ['O que é o CVTI?']],
        ['MEI', ['O que é MEI?']],
        ['Imposto de Renda', ['O que é Imposto de Renda?']],
        ['Renda Bruta', ['O que é Renda Bruta?']],
        ['Despesas', ['O que são Despesas?']],
        ['Isenção', ['O que é Isenção?']],
        ['Renda Tributavel', ['O que é Renda Tributavel?',]],
    ]
    return menu_def

sg.theme('DarkGrey8')

def telaapresentacao():

    layout = [
        [sg.MenuBar(criar_menu())],
        [sg.Frame(" Projeto da Turma A de Programação ", font=('Tahoma', 18), layout=[
            [sg.Canvas(background_color=None, size=(110, 10)), sg.Frame("", layout=[
                [sg.Image('CVTILogo.png')]], relief=sg.RELIEF_RAISED, border_width=4)],
            [sg.Text('''
O projeto a seguir foi criado pela turma de Programação A sob a orientação do professor João para o evento do CVTI Innovation Day.
                     
O projeto foi idealizado sob a ajuda ao MEI, o Microempreendedor Individual.
Para auxiliá-lo a declarar ao Imposto de Renda caso ele tenha um ganho acima de R$: 28559.70.
        ''', font=('Tahoma', 16, 'italic',))],
            [sg.Button('Iniciar o Projeto', font=('Tahoma', 12), button_color='green',
                       pad=(15), border_width=4)]
        ], relief=sg.RELIEF_SUNKEN, border_width=3)]
    ]
    window = sg.Window('Apresentação do Projeto', layout)
    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        elif event in 'Como é esse curso de Programação?':
            sg.popup('O curso ensina os fundamentos da programação e ensina a criar programas em Python', no_titlebar=True, font=(
                'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in 'Quem é o professor de Programação?':
            sg.popup('O professor do curso de Programação é o professor João, que também é professor de Robótica', no_titlebar=True, font=(
                'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in 'O que é o CVTI?':
            sg.popup('''
Centro Vocacional de Tecnologia e Inovação
Um projeto da Prefeitura de Nova Iguaçu em parceria com o Governo Federal
                         ''', no_titlebar=True, font=(
                'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in 'O que é MEI?':
            sg.popup('''
O Microempreendedor Individual (MEI) é uma figura jurídica do Brasil. É a pessoa que trabalha por conta própria e que se legaliza como pequeno empresário para ser um microempreendedor individual. Poderá ter um faturamento anual de até R$ 81000.00 e não ter participação em outra empresa como sócio ou titular. 
O MEI também pode ter um empregado contratado que receba um salário mínimo ou o piso da categoria.
                        ''', no_titlebar=True, font=(
                'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in 'O que é Imposto de Renda?':
            sg.popup('''
O Imposto de Renda é um tributo cobrado anualmente pelo Governo Federal sobre os ganhos de pessoas e de empresas. Ele é pago conforme os rendimentos declarados, de forma que os cidadãos com renda maior pagam mais impostos. Pessoas físicas que ganham até R$28559.70 não precisam declarar e serão isentas do tributo.
                         ''', no_titlebar=True, font=(
                'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in 'O que é Renda Bruta?':
            sg.popup('''
Renda bruta é o total de ganhos ou receitas obtidas por uma pessoa, empresa ou organização  antes da dedução de qualquer imposto, tributo ou despesas.
                        ''', no_titlebar=True, font=(
                'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in 'O que são Despesas?':
            sg.popup('''
As despesas são recursos aplicados à estrutura gerencial de uma empresa com o objetivo de sustentar seu funcionamento
como um todo. Em outras palavras, podemos dizer que elas estão relacionadas à administração do negócio. Pode ser dividida em:

-Despesas Fixas
As despesas fixas correspondem a gastos mensais fixos, como o nome indica. 
Elas são constantes e, em muitos casos, previsíveis, pois não estão vinculadas às oscilações no volume de produção.
                     
-Despesas Variáveis
Já as variáveis são aquelas que estão relacionadas ao volume de produção e, por isso, os valores oscilam de um período para outro.

-Despesas Operacionais
As operacionais são aquelas despesas fundamentais para manter o funcionamento da empresa

-Despesas Não Operacionais
As não operacionais são aquelas que não estão ligadas diretamente ao funcionamento ou à realização da atividade principal da empresa.
Alguns exemplos são o pagamento de juros e dividendos.

-Despesas Pré-Operacionais
Já as pré-operacionais são essenciais para que a empresa tenha condições de realizar suas atividades e expandir seus processos.
Elas são pagas antes do início da produção e são inevitáveis para a implementação do negócio.
                        ''', no_titlebar=True, font=(
                'Helvetica', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in 'O que é Isenção?':
            sg.popup('''
Isenção de taxas é a dispensa do pagamento de valores cobrados sobre determinados serviços.
Essa isenção é uma prerrogativa que na maioria das vezes requer o cumprimento de algumas exigências, como no caso do MEI onde
ocorre pela ocupação que está habilitado. Que no caso são:

-Comércio, Indústria e Transporte de Carga que recebe 8 porcento de Isenção (8%)
                     
-Transporte de Passageiros que recebe 16 porcento de Isenção (16%)

-Serviços em Geral que recebe 32 porcento de Isenção (32%)
                        ''', no_titlebar=True, font=(
                'Helvetica', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in 'O que é Renda Tributavel?':
            sg.popup('Um rendimento tributável é aquele que está sujeito à cobrança de Imposto de Renda.', no_titlebar=True, font=(
                'Helvetica', 12, 'italic', 'bold'), text_color='white', background_color='#363636', button_color=('white', '#1C1C1C'))
        elif event in ('Iniciar o Projeto'):
            window.close()
            tema1 = sg.theme('DarkGrey15')
            tela1(tema1)
            break
    window.close()


def tela1(tema1):

    gifimagem1 = 'Dinheiro1.gif'

    layout = [
        [sg.Frame(" Tela de Declaração de Renda ", font=('Helvetica', 14), layout=[
            [sg.Frame("", layout=[
                [sg.Image('MEIReceitaLogo.png')]], relief=sg.RELIEF_RAISED, border_width=4, pad=(10))],
            [sg.Canvas(background_color=None, size=(115, 10)), sg.Text('Digite a renda bruta para ser testado: R$',
                                                                       font=('Helvetica', 16, 'italic', 'bold')), sg.InputText(size=(10, 45))],
            [sg.Canvas(background_color=None, size=(100, 10)), sg.Frame("", layout=[
                [sg.Image(gifimagem1, key='-IMAGE-', enable_events=True)]], relief=sg.RELIEF_RAISED, border_width=4, pad=(10))],
            [sg.Button('Prosseguir ➡', pad=(15), border_width=4)]
        ], relief=sg.RELIEF_SUNKEN, border_width=3)]
    ]

    window = sg.Window('Teste 1 de 4', layout, no_titlebar=True)

    while True:
        event, values = window.read(timeout=10)

        if event == sg.WIN_CLOSED:
            break
        try:
            if event in ('Prosseguir ➡'):
                if float(values[1]) <= 28559.70:
                    sg.popup('O valor inserido não deve ser declarado, pois o imposto de renda deve ser maior que 28559.70', no_titlebar=True, font=(
                        'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#1C1C1C', button_color=('white', '#2F4F4F'))
                elif float(values[1]) > 81000:
                    sg.popup('O valor inserido é superior ao limite em que o MEI pode ter(R$ 81000,00). Você deve migrar para a MicroEmpresa', no_titlebar=True, font=(
                        'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#1C1C1C', button_color=('white', '#2F4F4F'))
                elif float(values[1]) > 0:
                    RendaBruta = values[1]
                    window.close()
                    tema2 = sg.theme('DarkTanBlue')
                    tela2(tema2, RendaBruta)
                    break
        except ValueError:
            continue
        window['-IMAGE-'].update_animation(gifimagem1,
                                           time_between_frames=100)
    window.close()


def tela2(tema2, RendaBruta):

    gifimagem2 = 'Dinheiro4c.gif'

    layout = [
        [sg.Frame(" Tela de Declaração de Despesa ", font=('Helvetica', 14), layout=[
            [sg.Frame("", layout=[
                [sg.Image('MEIReceitaLogo.png')]], relief=sg.RELIEF_RAISED, border_width=4, pad=(5))],
            [sg.Canvas(background_color=None, size=(70, 10)), sg.Text('Digite o valor das despesas feitas pelo MEI: R$',
                                                                      font=('Helvetica', 16, 'italic', 'bold')), sg.InputText(size=(10, 45))],
            [sg.Canvas(background_color=None, size=(180, 10)), sg.Frame("", layout=[
                [sg.Image(gifimagem2, key='-IMAGE-', enable_events=True)]], relief=sg.RELIEF_RAISED, border_width=4, pad=(10))],
            [sg.Button('Prosseguir ➡', button_color=(
                '#1E90FF', '#363636'), pad=(5), border_width=4)]
        ], relief=sg.RELIEF_SUNKEN, border_width=3)]
    ]

    window = sg.Window('Tela 2 de 4', layout, no_titlebar=True)

    while True:
        event, values = window.read(timeout=10)

        if event == sg.WIN_CLOSED:
            break

        try:
            if event in ('Prosseguir ➡'):
                if float(values[1]) >= 0 and float(values[1]) <= (float(RendaBruta) * 0.8):
                    Despesa = float(values[1])
                    DespesaRenda = float(RendaBruta) - float(Despesa)
                    window.close()
                    tela3(RendaBruta, DespesaRenda)
                    break
                elif float(values[1]) > (float(RendaBruta) * 0.8):
                    sg.popup('O valor inserido é superior ao limite que o MEI pode ter(que é até 80 por cento da Renda Bruta). Você deve migrar para a MicroEmpresa', no_titlebar=True, font=(
                        'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#1C1C1C', button_color=('white', '#2F4F4F'))
                elif float(values[1]) < 0:
                    sg.popup('O valor inserido não pode ser Negativo', no_titlebar=True, font=(
                        'Verdana', 12, 'italic', 'bold'), text_color='white', background_color='#1C1C1C', button_color=('white', '#2F4F4F'))
                else:
                    sg.popup('A simulação não aceita valores que não sejam numerais', no_titlebar=True, font=(
                        'Verdana', 12), text_color='white', background_color='#1C1C1C', button_color=('white', '#2F4F4F'))

        except ValueError:
            continue
        window['-IMAGE-'].update_animation(gifimagem2,
                                           time_between_frames=100)
    window.close()


def tela3(RendaBruta, DespesaRenda):
    sg.theme('DarkGrey15')
    gifimagem3 = 'Dinheiro2.gif'
    layout = [
        [sg.Frame(" Tela de Declaração de Ocupação do MEI ", font=('Helvetica', 14), layout=[
            [sg.Canvas(background_color=None, size=(60, 10)), sg.Frame("", layout=[
                [sg.Image('MEIReceitaLogo.png')]], relief=sg.RELIEF_RAISED, border_width=4, pad=(10))],
            [sg.Text('Indique qual é a sua ocupação para receber isenção: ', font=(
                'Helvetica', 16, 'italic', 'bold')), sg.OptionMenu(['Comércio, Indústria e Transporte de Carga', 'Transporte de Passageiros', 'Serviços em Geral'], k='Escolha', default_value=('Selecione Aqui'))],
            [sg.Canvas(background_color=None, size=(210, 10)), sg.Frame("", layout=[
                [sg.Image(gifimagem3, key='-IMAGE-', enable_events=True)]], relief=sg.RELIEF_RAISED, border_width=4, pad=(10))],
            [sg.Button('Prosseguir ➡', pad=(15), border_width=4)]
        ], relief=sg.RELIEF_SUNKEN, border_width=3)]
    ]

    window = sg.Window('Tela 3 de 4', layout, no_titlebar=True)

    while True:
        event, values = window.read(timeout=20)

        if event == sg.WIN_CLOSED:
            break

        try:
            if event in ('Prosseguir ➡'):
                if values['Escolha'] in 'Comércio, Indústria e Transporte de Carga':
                    isencao = float(RendaBruta) * 0.08
                    RendaTributavel = float(DespesaRenda) - float(isencao)
                    window.close()
                    tela4(RendaTributavel, isencao)
                    break
                elif values['Escolha'] in 'Transporte de Passageiros':
                    isencao = float(RendaBruta) * 0.16
                    RendaTributavel = float(DespesaRenda) - float(isencao)
                    window.close()
                    tela4(RendaTributavel, isencao)
                    break
                elif values['Escolha'] in 'Serviços em Geral':
                    isencao = float(RendaBruta) * 0.32
                    RendaTributavel = float(DespesaRenda) - float(isencao)
                    window.close()
                    tela4(RendaTributavel, isencao)
                    break
        except ValueError:
            continue
        window['-IMAGE-'].update_animation(gifimagem3,
                                           time_between_frames=100)
    window.close()


def tela4(RendaTributavel, isencao):
    sg.theme('DarkTanBlue')
    gifimagem4 = 'Dinheiro3.gif'
    texto = '''
Você deve declarar esse valor, porém NÃO precisará 
pagar nada,já que é menor de R$: 28559.70
    ''' if RendaTributavel <= 28559.70 else '''
Você terá que pagar a Receita Federal, quando fizer 
a Declaração Escolha a Opção Alíquota Simples
'''
    layout = [
        [sg.Frame(" Tela de Demonstração da Renda Tributável ", font=('Helvetica', 14), layout=[
            [sg.Frame("", layout=[
                [sg.Image('CVTIFinal.png')]], border_width=4, pad=(10))],
            [sg.Text(f'Sua renda tributável é de R$: {RendaTributavel:2}', font=(
                'Helvetica', 16, 'italic'))],
            [sg.Text(texto, font=('Helvetica', 16, 'italic', 'bold'))],
            [sg.Text(f'Sua isenção é de R$: {isencao:2}', font=(
                'Helvetica', 16, 'italic'))],
            [sg.Canvas(background_color=None, size=(3, 10)), sg.Frame("", layout=[
                [sg.Image(gifimagem4, key='-IMAGE-', enable_events=True)]], border_width=4, pad=(15))],
            [sg.Button('Finalizar', size=(20, 1), pad=(20, (0, 20)),
                       border_width=4, button_color=('white', '#4682B4'))]
        ], relief=sg.RELIEF_SUNKEN, border_width=3)]
    ]
    window = sg.Window('Tela 4 de 4, Conclusão', layout,
                       no_titlebar=True, grab_anywhere=False)

    while True:
        event, values = window.read(timeout=10)

        if event == sg.WIN_CLOSED:
            break
        elif event == 'Finalizar':
            window.close()
            telaapresentacao()
            break
        window['-IMAGE-'].update_animation(gifimagem4,
                                           time_between_frames=60)
    window.close()


telaapresentacao()
