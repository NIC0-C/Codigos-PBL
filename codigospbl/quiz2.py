import json

# Abrindo o arquivo JSON com as perguntas
with open("quiz.json", "r", encoding="utf-8") as arquivo:
    Salvos = json.load(arquivo)

# Inicializando a pontuação total
pontuacao_total = 0

# Iterando pelas questões no arquivo JSON
for questao in Salvos:
    categoria = questao["category"]
    valor = questao["value"]
    quiz_texto = questao["questiontext"]
    opcoes = [questao["option1"], questao["option2"],
              questao["option3"], questao["option4"], questao["option5"]]
    resposta_correta = questao["answer"]
    explicacao = questao["explanation"]

    # Exibindo a pergunta e as opções
    print(f"\nCategoria: {categoria} (Valor: {valor} pontos)")
    print(f"Pergunta: {quiz_texto}")
    print("Opções:")
    for i, opcao in enumerate(opcoes, 1):
        print(f"  {i}: {opcao}")

    # Solicitando a resposta do jogador
    while True:
        resposta = input("Digite o número da sua resposta: ").strip()
        if resposta.isdigit() and 1 <= int(resposta) <= len(opcoes):
            resposta_escolhida = opcoes[int(resposta) - 1]
            break
        else:
            print(
                "Entrada inválida. Por favor, insira um número correspondente a uma das opções.")

    # Verificando se a resposta é correta
    if resposta_escolhida == resposta_correta:
        print("Você acertou!!!")
        pontuacao_total += valor
    else:
        print("Você errou!!!")
        print(f"Explicação: {explicacao}")

# Exibindo a pontuação final
print(f"\nSua pontuação final foi: {pontuacao_total} pontos")
