import random
from unidecode import unidecode

nome_jogo = 'Palavras'
arquivo_palavras = 'palavras.txt'

def retorna_lista_palavras():
    # Inserindo as palavras do arquivo 'palavras.txt' na lista 'palavras'
    lista_palavras = []
    try:
        with open(arquivo_palavras, 'r', encoding='utf-8') as arquivo:
            for palavra in arquivo:
                # Append alterando as palavras para mínuscula e removendo espaços antes e depois da string
                lista_palavras.append(palavra.rstrip().lower())
    except Exception as e:
        print(f'Não foi possível realizar operação devido: {e}')

    palavra_aleatoria = random.choice(lista_palavras)
    palavra_aleatoria_filtro = unidecode(palavra_aleatoria)
    
    return palavra_aleatoria, palavra_aleatoria_filtro

def jogo(palavra_aleatoria, palavra_aleatoria_filtro):
    max_turnos = 5
    turno_atual = 0
    letras_posicao_errada = []
    letras_erradas = []

    print(f'Bem vindo ao jogo {nome_jogo}!')
    print(f'A palavra tem {len(palavra_aleatoria)} letras.')
    print('Você tem', max_turnos - turno_atual, 'turnos para adivinhar a palavra.')

    while max_turnos > turno_atual:
        chute = unidecode(input('Qual é a palavra? ').lower())
        
        if len(chute) != len(palavra_aleatoria):
            print('Digite uma palavra de 5 letras')
            continue
        elif not chute.isalpha():
            print('Digite uma palavra com caracteres válidos')
            continue

        index = 0
        for c in chute:
            if c == palavra_aleatoria_filtro[index]:
                print(c, end=' ')
                if c in letras_posicao_errada:
                    letras_posicao_errada.remove(c)
            elif c in palavra_aleatoria_filtro:
                if c not in letras_posicao_errada:
                    letras_posicao_errada.append(c)
                print('_', end=' ')
            else:
                if c not in letras_erradas:
                    letras_erradas.append(c)
                print('_', end=' ')
            index += 1

        print('\n')
        if len(letras_posicao_errada) == 1:
            print('A seguinte letra está na posição errada:', letras_posicao_errada)
        elif len(letras_posicao_errada) > 1:
            print('As seguintes letras estão na posição errada:', letras_posicao_errada)
        
        if len(letras_erradas) == 1:
            print('A seguinte letra não consta na palavra:', letras_erradas)
        elif len(letras_erradas) > 1:
            print('As seguintes letras não constam na palavra:', letras_erradas)
            
        turno_atual += 1
        
        if chute == palavra_aleatoria_filtro:
            print('\n')
            print('Você acertou a palavra: ', palavra_aleatoria)
            break
        elif max_turnos == turno_atual:
            print('\n')
            print('Acabou suas tentativas')
            print('A palavra era: ', palavra_aleatoria)
            break
        
        if (max_turnos - turno_atual) > 1:
            print('Você tem', max_turnos - turno_atual, 'turnos para adivinhar a palavra.')
        else:
            print('Você tem', max_turnos - turno_atual, 'turno para adivinhar a palavra.')

def main():
    while True:
        try:
            print('1 - Iniciar o jogo')
            print('2 - Terminar aplicação')
            selecao = int(input('Selecione uma das opções: '))
            
            if selecao == 1:
                palavra_aleatoria, palavra_aleatoria_filtro = retorna_lista_palavras()
                jogo(palavra_aleatoria, palavra_aleatoria_filtro)
            elif selecao == 2:    
                print('Aplicação finalizada')
                break
            else:
                print('Opção inválida! Digite 1 ou 2.')
        except ValueError:
            print('O valor inserido não é um número')
            print('Digite 1 ou 2')

if __name__ == '__main__':
    main()
