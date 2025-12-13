import time
import random
import os


def pergunta_quiz():
    perguntas = [
        {
            "category": "Historia",
            "value": 10,
            "questiontext": "Quem decretou o Bloqueio Continental, impedindo o acesso a portos, em 21 de novembro de 1806?",
            "1": "D. João VI",
            "2": "Napoleão Bonaparte",
            "3": "D. Pedro I",
            "4": "D. Pedro II",
            "5": "Alexandre I da Rússia",
            "correta": "2",
            "explanation": "O Bloqueio Continental foi um decreto assinado pelo imperador francês Napoleão Bonaparte em 1806. Essa resolução proibia países europeus de comercializarem produtos ingleses. Napoleão Bonaparte foi imperador da França e decretou o Bloqueio Continental para arruinar a economia da Inglaterra",
            "hint": "um líder que estava buscando expandir seu poder na europa"
        }
    ]

    # Escreve as perguntas no arquivo quiz.txt
    with open("quiz.txt", "w") as arquivo:
        for pergunta in perguntas:
            for chave, valor in pergunta.items():
                arquivo.write(f"{chave}: {valor}\n")
            arquivo.write("\n")

    # Lê o arquivo e imprime as perguntas no terminal
    score = 0
    for questoes in perguntas:
        categoria = questoes["category"]
        valor = questoes["value"]
        quiz_texto = questoes["questiontext"]
        opcoes = [questoes["1"], questoes["2"],
                  questoes["3"], questoes["4"], questoes["5"]]
        resposta_correta = questoes["correta"]
        explicacao = questoes["explanation"]
        dica = questoes["hint"]

        print(f"Categoria: {categoria} (Valor: {valor})")
        print(f"Pergunta: {quiz_texto}")
        print("Opções:")

        for i, opcao in enumerate(opcoes, 1):
            print(f"  {i}: {opcao}")

        print(f"Dica: {dica}")
        resposta = input("Digite sua resposta (número da opção): ").strip()

        if resposta == resposta_correta:
            print("Você acertou!!!")
            score += valor
        else:
            print("Você errou!!!")
            print(f"Explicação: {explicacao}")
        print("\n")

    print(f"Pontuação final: {score}")


# Executa a função para exibir o quiz
pergunta_quiz()
