import os
from datetime import datetime
import random

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    if comando in ('olá', 'boa tarde', 'bom dia'):
        return 'Olá tudo bem!'
    if comando == 'como estás':
        return 'Estou bem, obrigado!'
    if comando == 'como te chamas?':
        return 'O meu nome é: Bot :)'
    if comando == 'tempo':
        return 'Está um dia de sol!'
    if comando in ('bye', 'adeus', 'tchau', 'xau'):
        return 'Gostei de falar contigo! Até breve...'
    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'
    if ('data' or 'dia') and 'é hoje' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'
    if 'ajuda' in comando or 'comandos' in comando:
        return ("Podes perguntar: olá, como estás, como te chamas, tempo, horas, data, piada, curiosidade, ajuda, "
                "ou dizer bye para sair.")
    if 'piada' in comando:
        piadas = [
            "Porque é que o computador foi ao médico? Porque tinha um vírus!",
            "Para que servem os óculos verdes? Para verde perto.",
            "Porque é que o livro de matemática se suicidou? Porque tinha muitos problemas."
            "O que é um vegetariano que come carne? Um ex-vegetariano!",
        ]
        return random.choice(piadas)
    if 'curiosidade' in comando:
        curiosidades = [
            "Sabias que o polvo tem três corações?",
            "Sabias que  mel nunca se estraga e que deve-se usar sempre uma colher de madeira?",
            "Sabias que o maior animal do mundo é a baleia-azul? Ela pode pesar até 200 toneladas!",
            "Sabias que o tempo que a luz leva para chegar do Sol à Terra é de aproximadamente 8 minutos e 20 segundos?",
        ]
        return random.choice(curiosidades)
    if 'previsão' in comando or 'metereologia' in comando:
        previsoes = [
            "A previsão do tempo para hoje é de sol com algumas nuvens.",
            "Hoje pode chover à tarde, não se esqueça do guarda-chuva!",
            "O dia será nublado, mas sem previsão de chuva.",
            "Prepare-se para um dia ensolarado e quente!",
        ]
        return random.choice(previsoes) 
    



    return f'Desculpa, não entendi a questão! {texto}'

    # respostas = {
    #     ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
    #     'como estás': 'Estou bem, obrigado!',
    #     ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...',
    # }

    # for chave, resposta in respostas.items():
    #     if isinstance(chave, tuple):
    #         if comando in chave:
    #             return resposta
    #     elif chave in comando:
    #         return resposta

    # return f'Desculpa, não entendi a questão! {texto}'


def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')
        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()