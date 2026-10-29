import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

###
# Taxa de Evasão do Sistema do Ensino Superior
###
def dropout_rate_per_year():
    years = ['2014-2015', '2015-2016', '2016-2017', '2017-2018', '2018-2019',
             '2019-2020', '2020-2021', '2021-2022', '2022-2023', '2023-2024']
    rates = [11.8, 13.4, 12.2, 13.6, 14.1,
             12.9, 13.5, 15.8, 16.0, 17.5]

    fig, axis = plt.subplots(figsize=(10, 5), dpi=300) # 3000x1500 px

    # Destaca a barra com a maior taxa de evasão
    colors = ['#CE1446' if rate == max(rates) else '#E17572' for rate in rates]

    bars = axis.bar(years, rates, color=colors, width=2/3)

    axis.set_ylabel('Taxa de Evasão (%)')

    # Remove os rótulos do eixo vertical
    axis.set_yticks([])

    # Remove as linhas de borda do gráfico
    for spine in ['top', 'left', 'right']:
        axis.spines[spine].set_visible(False)

    # Insere rótulos de dados sobre as barras
    axis.bar_label(
        bars, 
        fmt=lambda x: f'{x:.1f}%'.replace('.', ','),
        padding=2, 
        fontsize=8, 
        fontweight='bold'
    )

    # Aumenta o limite vertical em 10% para dar espaço aos rótulos de dados
    axis.set_ylim(0, max(rates) * 1.1)

    # Rotaciona os rótulos do eixo horizontal em 30º
    plt.xticks(rotation=30)

    return fig
###
  #
###



###
# Taxa de Evasão Acumulativa a Nível de Curso
###
def cumulative_dropout_rate():
    years = np.arange(2015, 2025) # Período 2015-2024

    dropout    = np.array([13, 29, 40, 48, 54,
                           57, 58, 59, 60, 60])
    conclusion = np.array([1 , 3 , 8 , 17, 28, 
                           34, 37, 38, 38, 39])
    retention  = np.array([86, 68, 52, 35, 18,
                           9 , 5 , 3 , 2 , 1 ])

    fig, axis = plt.subplots(figsize=(10, 5), dpi=300)

    # Cria listas de cores dinâmicas (destaque vs. cor padrão)
    # Valores máximos recebem uma cor mais escura/saturada
    colors_dropout    = ['#CE1446' if value == max(dropout) else '#E17572' for value in dropout]
    colors_conclusion = ['#3CB870' if value == max(conclusion) else '#73BC91' for value in conclusion]
    colors_retention  = ['#FFC271' if value == max(retention) else '#FFDEB3' for value in retention]

    # Barras empilhadas
    x = np.arange(len(years)) # position in x
    w = 2/3                   # width

    axis.bar(
        x, dropout,
        width = w,
        color = colors_dropout
    )

    axis.bar(
        x, conclusion,
        width  = w,
        bottom = dropout,
        color  = colors_conclusion
    )

    axis.bar(
        x, retention,
        width  = w,
        bottom = dropout + conclusion,
        color  = colors_retention
    )

    # Rótulos de valores
    for i in range(len(years)):
        values = [
            (dropout[i]   , 0                         ),
            (conclusion[i], dropout[i]                ),
            (retention[i] , dropout[i] + conclusion[i])
        ]

        for value, bottom in values:
            if value >= 4:
                axis.text(
                    x[i],
                    bottom + value / 2,
                    f'{value}%',
                    ha         = 'center',
                    va         = 'center',
                    fontsize   = 8,
                    fontweight = 'bold'
                )
            else:
                # Exibe o rótulo acima da respectiva barra para valores pequenos (< 4%)
                axis.text(
                    x[i],
                    bottom + value + 1.1,
                    f'{value}%',
                    ha         = 'center',
                    va         = 'bottom',
                    fontsize   = 8,
                    fontweight = 'bold'
                )

    axis.set_xticks(x, years)
    axis.set_yticks([])

    for spine in ['top', 'left', 'right']:
        axis.spines[spine].set_visible(False)

    # Legenda
    legend = [
        Patch(
            facecolor = '#E17572',
            label     = 'Taxa de Desistência'
        ),
        Patch(
            facecolor = '#73BC91',
            label     = 'Taxa de Conclusão'
        ),
        Patch(
            facecolor = '#FFDEB3',
            label     = 'Taxa de Permanência'
        )
    ]

    axis.legend(
        handles=legend,
        loc='upper center',
        bbox_to_anchor=(0.5, -0.1),
        ncol=3,
        frameon=False,
    )

    return fig
###
  #
###



###
# Taxa de Evasão por Idade
###
def dropout_rate_per_age():
    years = ['2021-2022', '2022-2023', '2023-2024']

    age_group = [
        'Até 19 anos',
        '20 a 22 anos',
        '23 a 24 anos',
        '25 a 29 anos',
        '30 a 39 anos',
        '40 a 49 anos',
        '50 anos ou mais'
    ]

    rates = np.array([
        [9.3, 10.7, 14.1, 18.4, 20.1, 19.9, 20.7],
        [9.3, 10.7, 14.4, 18.8, 20.3, 19.8, 20.3],
        [9.4, 11.0, 15.3, 20.3, 22.5, 22.3, 23.4]
    ])

    colors = [
        '#ED9DA1',
        '#E88692',
        '#E36F83',
        '#DE5974',
        '#D84264',
        '#D32B55',
        '#CE1446'
    ]

    fig, axis = plt.subplots(figsize=(10, 5), dpi=300)

    # Barras agrupadas
    x = np.arange(len(years)) * 2.5 # position in x (+2.5 spacing)
    w = 0.25                        # width
    s = 0.05                        # spacing
    for i in range(len(age_group)):
        pos = (
            x
            + (i - 3) * (w + s)
        )

        bars = axis.bar(
            pos,
            rates[:, i],
            width = w,
            color = colors[i],
        )

        # Rótulos sobre as barras
        for bar, rate in zip(bars, rates[:, i]):
            axis.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height() + 0.25,
                f'{rate:.1f}'.replace('.', ','),
                ha         = 'center',
                va         = 'bottom',
                fontsize   = 8,
                fontweight = 'bold',
            )

    axis.set_ylabel('Taxa de Evasão (%)')

    # Configuração dos eixos
    axis.set_xticks(x)
    axis.set_xticklabels(years)
    axis.set_yticks([])

    for spine in ['top', 'left', 'right']:
        axis.spines[spine].set_visible(False)

    # Legenda inferior
    legend = [
        Patch(
            facecolor = colors[i],
            label     = age_group[i]
        )
        for i in range(len(age_group))
    ]

    axis.legend(
        handles        = legend,
        loc            = 'upper center',
        bbox_to_anchor = (0.5, -0.1),
        ncol           = 4,
        frameon        = False,
    )

    return fig
###
  #
###



###
# Taxa de Evasão por Ambiente de Ensino
###
def dropout_rate_per_env():
    years          = ['2021-2022', '2022-2023', '2023-2024'] # Últimos 3 anos
    dropout        = [10.6, 10.4, 9.5]
    online_dropout = [22.0, 21.4, 24.1]

    x = np.arange(len(years)) # position in x
    w = 0.25                  # width
    s = 0.05                  # spacing

    fig, axis = plt.subplots(figsize=(10, 5), dpi=300)

    for spine in ['top', 'left', 'right']:
        axis.spines[spine].set_visible(False)

    # Destaca a barra com maior valor
    default_color       = '#E17572'
    default_light_color = '#ED9DA1'
    highlight_color     = '#CE1446'

    colors = [highlight_color if val == max(online_dropout) else default_color for val in online_dropout]

    Lrects = axis.bar(x - (w / 2 + s), dropout, w, label='Presencial', color=default_light_color)
    Rrects = axis.bar(x + (w / 2 + s), online_dropout, w, label='EaD', color=colors)

    axis.set_ylabel('Taxa de Evasão (%)')
    axis.set_xticks(x)
    axis.set_xticklabels(years)
    axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), frameon=False, ncol=2)
    axis.set_yticks([])

    # Rótulos de dados sobre as barras
    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            axis.annotate(f'{height}%'.replace('.',','),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3), # Deslocamento vertical de 3 pontos
                        textcoords='offset points',
                        ha='center', va='bottom',
                        fontsize=8, fontweight='bold'), 

    autolabel(Lrects)
    autolabel(Rrects)

    return fig
###
  #
###



###
# Taxa de Evasão por Tipo de Financiamento
###
def dropout_rate_per_financing():
    years          = ['2021-2022', '2022-2023', '2023-2024']
    refundable     = [16.1, 15.1, 15.5]
    non_refundable = [19.2, 19.5, 19.7]

    x = np.arange(len(years))
    w = 0.25
    s = 0.05

    fig, axis = plt.subplots(figsize=(10, 5), dpi=300)

    for spine in ['top', 'left', 'right']:
        axis.spines[spine].set_visible(False)

    default_color       = '#E17572'
    default_light_color = '#ED9DA1'
    highlight_color     = '#CE1446'
    
    colors = [highlight_color if val == max(non_refundable) else default_color for val in non_refundable]

    Lrects = axis.bar(x - (w/2 + s), refundable, w, label='Reembolsável', color=default_light_color)
    Rrects = axis.bar(x + (w/2 + s), non_refundable, w, label='Não Reembolsável', color=colors)

    axis.set_ylabel('Taxa de Evasão (%)')
    axis.set_xticks(x)
    axis.set_xticklabels(years)
    axis.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), frameon=False, ncol=2)
    axis.set_yticks([])

    def autolabel(rects):
        for rect in rects:
            height = rect.get_height()
            axis.annotate(f'{height}%'.replace('.',','),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords='offset points',
                        ha='center', va='bottom',
                        fontsize=8, fontweight='bold'), 

    autolabel(Lrects)
    autolabel(Rrects)

    return fig
###
  #
###



plt.rcParams.update({'font.size': 12})
# Define a fonte padrão para 12.