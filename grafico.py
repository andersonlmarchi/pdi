import matplotlib.pyplot as plt
import numpy as np

# Definir os dados
labels = ['Árvore B', 'Árvore Binária', 'Árvore AVL']

def ns_para_ms(dados_ns):
    return [valor / 1e6 for valor in dados_ns]

# Matrizes de resultados
insercao_ordenada_1 = [
    [35260503, 13711004, 38622813],  # Conjunto de 100000 dados ordenados
    [44628023, 16224129, 31222508],  # Conjunto de 100000 dados ordenados
    [41350819, 19487494, 62726375]   # Conjunto de 100000 dados ordenados
]

insercao_ordenada_2 = [
    [210798403, 88338642, 156683870],  # Conjunto de 1000000 dados ordenados
    [148971682, 97709207, 185957796],  # Conjunto de 1000000 dados ordenados
    [219042883, 94887862, 162249386]   # Conjunto de 1000000 dados ordenados
]

insercao_aleatoria_1 = [
    [34414610, 2774974, 39253547],   # Conjunto de 100000 dados aleatórios
    [41606203, 1865047, 38353590],   # Conjunto de 100000 dados aleatórios
    [28448748, 1549675, 37132125]    # Conjunto de 100000 dados aleatórios
]


insercao_aleatoria_2 = [
    [536635880, 61097821, 424641287],   # Conjunto de 1000000 dados aleatórios
    [528059689, 26231466, 464654080],   # Conjunto de 1000000 dados aleatórios
    [558472180, 19832500, 467643210]    # Conjunto de 1000000 dados aleatórios
]

busca_1 = [
    [2647380, 1035232, 16779],  # Conjunto de 100000 dados aleatórios
    [2954349, 2462082, 13436],  # Conjunto de 100000 dados aleatórios
    [2680719, 1820435, 13622]   # Conjunto de 100000 dados aleatórios
]

busca_2 = [
    [104034, 15565702, 13811],  # Conjunto de 1000000 dados aleatórios
    [99076, 8566056, 13811],  # Conjunto de 1000000 dados aleatórios
    [99164, 13853690, 27706]   # Conjunto de 1000000 dados aleatórios
]

# Função para criar gráfico
def criar_grafico(teste, dados, labels):
    x = np.arange(len(labels))
    width = 0.25
    fig, ax = plt.subplots()

    for i, conjunto in enumerate(dados):
        ax.bar(x + i*width, conjunto, width, label=f'Repetição {i+1}')

    ax.set_xlabel('Tipos de Árvore')
    ax.set_ylabel('Tempo (ns)')
    ax.set_title(teste)
    ax.set_xticks(x + width)
    ax.set_xticklabels(labels)
    ax.legend()

    return fig

# Criar gráficos
testes = [
    ('Inserção Ordenada - Conjunto 1', insercao_ordenada_1),
    ('Inserção Ordenada - Conjunto 2', insercao_ordenada_2),
    ('Inserção Aleatória - Conjunto 1', insercao_aleatoria_1),
    ('Inserção Aleatória - Conjunto 2', insercao_aleatoria_2),
    ('Busca - Conjunto 1', busca_1),
    ('Busca - Conjunto 2', busca_2)
]

for nome_teste, dados_teste in testes:
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(nome_teste)

    for i, dados_repeticao in enumerate(dados_teste):
        dados_ms = ns_para_ms(dados_repeticao)  # Converter para milissegundos
        axs[i].bar(labels, dados_ms)
        axs[i].set_title(f'Repetição {i+1}')
        axs[i].set_ylabel('Tempo (ms)')

    plt.show()
