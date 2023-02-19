import customtkinter as tk
import openai

janela = tk.CTk()
janela.geometry("421x505+396+74")

#config grid
janela.grid_columnconfigure(0, weight=0)
janela.grid_columnconfigure(1, weight=0)
janela.grid_rowconfigure(0, weight=0)
janela.grid_rowconfigure(1, weight=0)

openai.api_key = "Your API"

model_engine = "text-davinci-003"

def buscar():
    response = openai.Completion.create(
    engine=model_engine,
    prompt= prompt.get(),
    max_tokens=1024,
    temperature=0.6
    )
    res = response['choices'][0]['text']
    output.insert('0.0', res)

frame = tk.CTkFrame(janela)
frame.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

titulo = tk.CTkLabel(frame, text='Chat with GPT-3', font=("", 25))
titulo.grid(row=0, column=0, padx=10, pady=10)

output = tk.CTkTextbox(frame, width=400, height=400)
output.grid(row=1, column=0)
output.configure(state='disabled')

prompt = tk.CTkEntry(janela, placeholder_text="Type a message", width=250)
prompt.grid(row=1, column=0)

enviar = tk.CTkButton(janela, text="Send", command=buscar)
enviar.grid(row=1, column=1)

janela.mainloop()
