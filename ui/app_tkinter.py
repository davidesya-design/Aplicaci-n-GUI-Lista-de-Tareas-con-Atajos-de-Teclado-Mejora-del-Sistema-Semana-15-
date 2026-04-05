import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root):
        self.servicio = TareaServicio()
        self.root = root
        self.root.title("Lista de Tareas Moderna")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        self.root.configure(bg='#fefefe')  # Blanco pastel muy suave

        # Estilo moderno para ttk
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', font=('Segoe UI', 9), background='#fefefe', foreground='#666666')
        style.configure('TEntry', font=('Segoe UI', 9))
        style.configure('TButton', font=('Segoe UI', 9), padding=3)
        style.configure('TFrame', background='#fefefe')

        # Configurar pesos de la cuadrícula
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        # Etiqueta del campo de entrada
        self.label_entry = ttk.Label(root, text="Nueva tarea:")
        self.label_entry.grid(row=0, column=0, sticky=tk.W, padx=12, pady=6)

        # Campo de texto para nueva tarea
        self.entry = ttk.Entry(root, width=50)
        self.entry.grid(row=0, column=1, columnspan=2, sticky=tk.EW, padx=12, pady=6)
        self.entry.bind('<Return>', self.agregar_tarea)
        self.entry.focus()

        # Botón para agregar tarea
        self.btn_agregar = tk.Button(root, text="Agregar Tarea", command=self.agregar_tarea, bg='#c8e6c9', fg='#2e7d32', font=('Segoe UI', 9), relief=tk.FLAT, padx=8, pady=4, bd=0, highlightthickness=0)
        self.btn_agregar.grid(row=1, column=0, columnspan=3, pady=8)

        # Marco para lista y barra de desplazamiento
        frame_list = ttk.Frame(root)
        frame_list.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW, padx=12, pady=6)
        frame_list.columnconfigure(0, weight=1)
        frame_list.rowconfigure(0, weight=1)

        # Barra de desplazamiento
        self.scrollbar = ttk.Scrollbar(frame_list)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Lista de tareas
        self.listbox = tk.Listbox(frame_list, height=12, selectmode=tk.SINGLE, yscrollcommand=self.scrollbar.set, bg='#fefefe', fg='#333333', selectbackground='#64b5f6', selectforeground='white', font=('Segoe UI', 9), relief=tk.FLAT, bd=0, highlightthickness=0)
        self.listbox.grid(row=0, column=0, sticky=tk.NSEW)
        self.scrollbar.config(command=self.listbox.yview)

        # Marco para botones de acción
        frame_btn = ttk.Frame(root)
        frame_btn.grid(row=3, column=0, columnspan=3, pady=6)
        self.btn_completar = tk.Button(frame_btn, text="Marcar Completada", command=self.marcar_completada, bg='#bbdefb', fg='#1565c0', font=('Segoe UI', 9), relief=tk.FLAT, padx=8, pady=4, bd=0, highlightthickness=0)
        self.btn_completar.pack(side=tk.LEFT, padx=8)
        self.btn_eliminar = tk.Button(frame_btn, text="Eliminar Tarea", command=self.eliminar_tarea, bg='#ffcdd2', fg='#c62828', font=('Segoe UI', 9), relief=tk.FLAT, padx=8, pady=4, bd=0, highlightthickness=0)
        self.btn_eliminar.pack(side=tk.LEFT, padx=10)

        # Etiqueta de instrucciones
        self.label_instr = ttk.Label(root, text="Atajos: Enter (agregar), C (completar), D/Delete (eliminar), Escape (salir)")
        self.label_instr.grid(row=4, column=0, columnspan=3, pady=6)

        # Barra de estado
        self.status_label = ttk.Label(root, text="Total: 0 | Pendientes: 0 | Completadas: 0", anchor=tk.W, font=('Segoe UI', 8))
        self.status_label.grid(row=5, column=0, columnspan=3, sticky=tk.EW, padx=12, pady=4)

        # Vincular teclas
        self.root.bind('<Key-c>', lambda e: self.marcar_completada())
        self.root.bind('<Key-d>', lambda e: self.eliminar_tarea())
        self.root.bind('<Delete>', lambda e: self.eliminar_tarea())
        self.root.bind('<Escape>', self.cerrar_app)

        self.actualizar_lista()

    def agregar_tarea(self, event=None):
        desc = self.entry.get().strip()
        if desc:
            self.servicio.agregar_tarea(desc)
            self.entry.delete(0, tk.END)
            self.actualizar_lista()

    def marcar_completada(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            tarea = self.tareas[idx]
            self.servicio.marcar_completada(tarea.id)
            self.actualizar_lista()

    def eliminar_tarea(self):
        sel = self.listbox.curselection()
        if sel:
            idx = sel[0]
            tarea = self.tareas[idx]
            self.servicio.eliminar_tarea(tarea.id)
            self.actualizar_lista()

    def cerrar_app(self, event=None):
        self.root.quit()

    def actualizar_lista(self):
        self.tareas = self.servicio.obtener_tareas()
        self.listbox.delete(0, tk.END)
        total = len(self.tareas)
        pendientes = sum(1 for t in self.tareas if not t.completada)
        completadas = total - pendientes
        self.status_label.config(text=f"📊 Total: {total} | ⏳ Pendientes: {pendientes} | ✅ Completadas: {completadas}")
        for i, tarea in enumerate(self.tareas):
            self.listbox.insert(tk.END, tarea.descripcion)
            if tarea.completada:
                self.listbox.itemconfig(i, fg='#81c784')  # Verde pastel
            else:
                self.listbox.itemconfig(i, fg='#333333')