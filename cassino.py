```python
import tkinter as tk
import random

# Configurações
SIMBOLOS = ["🍌", "🍇", "🍉", "🍓", "🍊"]
SALDO_INICIAL = 20.0
CUSTO_GIRO = 2

saldo = SALDO_INICIAL

# Função de girar
def girar():
    global saldo

    if saldo < CUSTO_GIRO:
        resultado_label.config(text="Saldo insuficiente!", fg="red")
        return

    saldo -= CUSTO_GIRO

    resultado = [random.choice(SIMBOLOS) for _ in range(3)]

    # Atualiza os slots
    for i, slot in enumerate([slots1, slots2, slots3]):
        slot.config(text=resultado[i])

    # Verifica vitória
    if resultado[0] == resultado[1] == resultado[2]:
        premio = 20
        saldo += premio
        resultado_label.config(text=f"🎉 JACKPOT! +R$ {premio}", fg="green")
    elif len(set(resultado)) == 2:
        premio = 5
        saldo += premio
        resultado_label.config(text=f"✨ 2 iguais! +R$ {premio}", fg="blue")
    else:
        resultado_label.config(text="Tente novamente!", fg="black")

    saldo_label.config(text=f"Saldo: R$ {saldo:.2f}")

# Interface
janela = tk.Tk()
janela.title("🎰 Caça-Níquel")
janela.resizable(False, False)

# Slots
slots1 = tk.Label(janela, text="❔", font=("Arial", 40))
slots1.grid(row=0, column=0, padx=10, pady=10)

slots2 = tk.Label(janela, text="❔", font=("Arial", 40))
slots2.grid(row=0, column=1, padx=10, pady=10)

slots3 = tk.Label(janela, text="❔", font=("Arial", 40))
slots3.grid(row=0, column=2, padx=10, pady=10)

# Botão
botao = tk.Button(janela, text="Girar", font=("Arial", 14), command=girar)
botao.grid(row=1, column=0, columnspan=3, pady=10)

# Resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 12))
resultado_label.grid(row=2, column=0, columnspan=3)

# Saldo
saldo_label = tk.Label(janela, text=f"Saldo: R$ {saldo:.2f}", font=("Arial", 12))
saldo_label.grid(row=3, column=0, columnspan=3, pady=5)

janela.mainloop()
