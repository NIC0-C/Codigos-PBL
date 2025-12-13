import tkinter as tk
from tkinter import messagebox, PhotoImage
import random
import json

# ====== CARREGAR PERGUNTAS ======
with open("quiz.json", "r", encoding="utf-8") as arquivo:
    perguntas = json.load(arquivo)

perguntas = random.sample(perguntas, min(20, len(perguntas)))

# ====== VARIÁVEIS ======
indice = 0
pontuacao = 0
usou_dica = False
usou_50_flag = False  # nome diferente para evitar conflito
opcoes_ativas = []

# ====== INTERFACE PRINCIPAL ======
janela = tk.Tk()
janela.title("🌱 Quiz de Biologia")
janela.geometry("850x600")
janela.resizable(False, False)

# ====== IMAGEM DE FUNDO ======
try:
    fundo_img = PhotoImage(file="fundo_bio.png")
    fundo_label = tk.Label(janela, image=fundo_img)
    fundo_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception:
    janela.configure(bg="#e6f2e6")

# ====== FRAMES ======
frame_inicio = tk.Frame(janela, bg="#e6f2e6")
frame_quiz = tk.Frame(janela, bg="#e6f2e6")
frame_fim = tk.Frame(janela, bg="#e6f2e6")

# ====== TELA INICIAL ======
titulo_inicio = tk.Label(
    frame_inicio,
    text="🌿 QUIZ DE BIOLOGIA 🌿",
    font=("Georgia", 30, "bold"),
    bg="#e6f2e6",
    fg="#2f4f2f",
)
titulo_inicio.pack(pady=60)

texto_inicio = tk.Label(
    frame_inicio,
    text="Descubra quanto você sabe sobre o incrível mundo da biologia!\nClique abaixo para começar.",
    font=("Arial", 14),
    bg="#e6f2e6",
    fg="#3d3d3d",
)
texto_inicio.pack(pady=20)


def iniciar_quiz():
    frame_inicio.pack_forget()
    frame_quiz.pack(fill="both", expand=True)
    mostrar_questao()


botao_comecar = tk.Button(
    frame_inicio,
    text="🌱 Começar Quiz",
    font=("Arial", 16, "bold"),
    bg="#9acd32",
    fg="white",
    width=18,
    height=2,
    command=iniciar_quiz,
)
botao_comecar.pack(pady=40)

frame_inicio.pack(fill="both", expand=True)

# ====== TELA DO QUIZ ======
categoria_label = tk.Label(frame_quiz, text="", font=(
    "Arial", 13, "italic"), bg="#e6f2e6", fg="#3d3d3d")
categoria_label.pack(pady=10)

texto_pergunta = tk.Label(frame_quiz, text="", wraplength=780, font=("Arial", 15, "bold"),
                          bg="#e6f2e6", fg="#2e4e1d", justify="left")
texto_pergunta.pack(pady=10)

frame_opcoes = tk.Frame(frame_quiz, bg="#e6f2e6")
frame_opcoes.pack()

botoes_opcao = []


def escolher_resposta(opcao):
    global pontuacao, indice
    questao = perguntas[indice]
    correta = questao["answer"]

    if opcao == correta:
        pontuacao += 10
        messagebox.showinfo("Resultado", "✅ Resposta correta!")
    else:
        messagebox.showerror(
            "Errado!", f"❌ Resposta incorreta!\nExplicação: {questao['explanation']}")

    pontuacao_label.config(text=f"Pontuação: {pontuacao}")
    proxima_questao()


for i in range(5):
    botao = tk.Button(
        frame_opcoes,
        text="",
        width=70,
        bg="#b5dcb5",
        font=("Arial", 12),
        command=lambda i=i: escolher_resposta(opcoes_ativas[i]),
    )
    botao.pack(pady=5)
    botoes_opcao.append(botao)


# ====== FUNÇÕES AUXILIARES ======
def mostrar_questao():
    global opcoes_ativas, usou_dica, usou_50_flag
    questao = perguntas[indice]
    usou_dica = False
    usou_50_flag = False
    opcoes_ativas = [
        questao["option1"],
        questao["option2"],
        questao["option3"],
        questao["option4"],
        questao["option5"],
    ]

    categoria_label.config(
        text=f"Categoria: {questao['category']} (Valor: {questao['value']})")
    texto_pergunta.config(text=f"{indice+1}. {questao['perguntasgeral']}")

    for i, botao in enumerate(botoes_opcao):
        botao.config(text=opcoes_ativas[i], state="normal", bg="#b5dcb5")


def usar_dica():
    global usou_dica
    if usou_dica:
        messagebox.showwarning("Atenção", "Você já usou a dica nesta questão!")
    else:
        dica = perguntas[indice]["hint"]
        messagebox.showinfo("Dica 🌿", dica)
        usou_dica = True


def usar_50_recurso():
    global usou_50_flag, opcoes_ativas
    if usou_50_flag:
        messagebox.showwarning(
            "Atenção", "Você já usou o 50/50 nesta questão!")
    else:
        correta = perguntas[indice]["answer"]
        erradas = [op for op in opcoes_ativas if op != correta]
        remover = random.sample(erradas, 2)
        for i, botao in enumerate(botoes_opcao):
            if botao["text"] in remover:
                botao.config(state="disabled", bg="#d0d0d0")
        usou_50_flag = True


def pular():
    messagebox.showinfo("Pular", "Questão pulada!")
    proxima_questao()


def proxima_questao():
    global indice
    indice += 1
    if indice < len(perguntas):
        mostrar_questao()
    else:
        finalizar_quiz()


def finalizar_quiz():
    frame_quiz.pack_forget()
    frame_fim.pack(fill="both", expand=True)
    texto_fim.config(text=f"Sua pontuação final foi: {pontuacao} 🌿")


# ====== BOTÕES DE AÇÃO ======
frame_acoes = tk.Frame(frame_quiz, bg="#e6f2e6", pady=20)
frame_acoes.pack()

botao_dica = tk.Button(frame_acoes, text="💡 Dica",
                       bg="#9acd32", fg="white", width=10, command=usar_dica)
botao_dica.grid(row=0, column=0, padx=10)

botao_pular = tk.Button(frame_acoes, text="➡ Pular",
                        bg="#8fbc8f", fg="white", width=10, command=pular)
botao_pular.grid(row=0, column=1, padx=10)

botao_50 = tk.Button(frame_acoes, text="⚖ 50/50", bg="#6b8e23",
                     fg="white", width=10, command=usar_50_recurso)
botao_50.grid(row=0, column=2, padx=10)

pontuacao_label = tk.Label(frame_quiz, text=f"Pontuação: {pontuacao}", font=("Arial", 12, "bold"),
                           bg="#e6f2e6", fg="#2e4e1d")
pontuacao_label.pack(pady=10)

# ====== TELA FINAL ======
texto_fim = tk.Label(frame_fim, text="", font=(
    "Georgia", 20, "bold"), bg="#e6f2e6", fg="#2f4f2f")
texto_fim.pack(pady=100)

botao_sair = tk.Button(frame_fim, text="Sair", font=("Arial", 14, "bold"),
                       bg="#9acd32", fg="white", width=12, command=janela.destroy)
botao_sair.pack(pady=30)

janela.mainloop()
