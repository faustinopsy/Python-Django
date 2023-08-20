import tkinter as tk
import resposta as resp
import treine as tre
import historico as hist

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        
        self.mode_label = tk.Label(root, text="Escolha o modo:")
        self.mode_label.pack(padx=10, pady=5)
        
        self.mode_var = tk.StringVar(value="conversar")
        self.train_mode = tk.Radiobutton(root, text="Treinar", variable=self.mode_var, value="treinar")
        self.train_mode.pack(padx=10, pady=5)
        self.chat_mode = tk.Radiobutton(root, text="Conversar", variable=self.mode_var, value="conversar")
        self.chat_mode.pack(padx=10, pady=5)
        
        self.start_button = tk.Button(root, text="Começar", command=self.start_mode)
        self.start_button.pack(padx=10, pady=5)
        
    def start_mode(self):
        mode = self.mode_var.get()
        self.mode_label.pack_forget()
        self.train_mode.pack_forget()
        self.chat_mode.pack_forget()
        self.start_button.pack_forget()
        
        self.chatlog = tk.Text(self.root, bg="white", state=tk.DISABLED)
        self.chatlog.pack(padx=10, pady=10)
        
        self.entry_label = tk.Label(self.root, text="Pergunta:")
        self.entry_label.pack(padx=10, pady=5)
        self.entry = tk.Entry(self.root, bg="white", width=40)
        self.entry.insert(0, "Digite a pergunta aqui...")
        self.entry.bind("<FocusIn>", self.clear_placeholder)
        self.entry.pack(padx=10, pady=10)
        
        self.send_button = tk.Button(self.root, text="Enviar", command=self.send_message)
        self.send_button.pack(padx=10, pady=5)
        
        if mode == "treinar":
            self.response_label = tk.Label(self.root, text="Resposta:")
            self.response_label.pack(padx=10, pady=5)
            self.response_entry = tk.Entry(self.root, bg="white", width=40)
            self.response_entry.insert(0, "Digite a resposta aqui...")
            self.response_entry.bind("<FocusIn>", self.clear_placeholder)
            self.response_entry.pack(padx=10, pady=10)
            self.send_button.config(command=self.train_bot)
        
    def send_message(self, event=None):
        message = self.entry.get()
        self.entry.delete(0, tk.END)
        hist.registrar_historico(message)
        response = resp.buscar_resposta(message)
        self.display_message("Você: " + message)
        self.display_message("Chatbot: " + response)
        
    def train_bot(self, event=None):
        pergunta = self.entry.get()
        resposta = self.response_entry.get()
        self.entry.delete(0, tk.END)
        self.response_entry.delete(0, tk.END)
        tre.salvar_pergunta_resposta(pergunta, resposta)
        self.display_message(f"Pergunta treinada: {pergunta}, Resposta treinada: {resposta}")
        
    def display_message(self, message):
        self.chatlog.config(state=tk.NORMAL)
        self.chatlog.insert(tk.END, message + "\n")
        self.chatlog.config(state=tk.DISABLED)
        self.chatlog.see(tk.END)
        
    def clear_placeholder(self, event):
        if event.widget.get() == "Digite a pergunta aqui..." or event.widget.get() == "Digite a resposta aqui...":
            event.widget.delete(0, tk.END)
        
root = tk.Tk()
app = ChatbotApp(root)
root.mainloop()
