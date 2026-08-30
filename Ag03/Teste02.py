import tkinter as tk

def converter_temperatura():
    texto_digitado = entrada_celsius.get()
    celsius = float(texto_digitado)
    fahrenheit = (celsius * 9/5) + 32
    label_resultado.config(text=f"Resultado: {fahrenheit:.2f} °F")

# Cria a janela principal
janela = tk.Tk()
janela.title("Conversor de Temperatura do SAM")
janela.geometry("300x200")

#Cria o texto
label_instrucao = tk.Label(janela, text = "Digite a temperatura em Celsius: ")
label_instrucao.pack(pady=10)

#Cria a caixa de texto para o usuário digitar
entrada_celsius = tk.Entry(janela)
entrada_celsius.pack()

#Cria o botão que vai dispara a função
botao_converter = tk.Button(janela, text="Converte", command=converter_temperatura)
botao_converter.pack(pady=10)

#Cria o texto do resultado
label_resultado = tk.Label(janela, text="Resultado: --")
label_resultado.pack(pady=10)

janela.mainloop()