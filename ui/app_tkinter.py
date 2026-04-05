import tkinter as tk
from tkinter import ttk
from servicios.tarea_servicio import TareaServicio

class AppTkinter:
    def __init__(self, root):
        self.servicio = TareaServicio()
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")
        self.root.resizable(True, True)

        # Configure grid weights
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        # Label for entry
        self.label_entry = ttk.Label(root, text="Nueva tarea:")
        self.label_entry.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

        # Entry for new task
        self.entry = ttk.Entry(root, width=50)
        self.entry.grid(row=0, column=1, columnspan=2, sticky=tk.EW, padx=10, pady=5)
        self.entry.bind('<Return>', self.agregar_tarea)
        self.entry.focus()

        # Button to add
        self.btn_agregar = ttk.Button(root, text="Agregar Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=1, column=0, columnspan=3, pady=5)

        # Frame for listbox and scrollbar
        frame_list = ttk.Frame(root)
        frame_list.grid(row=2, column=0, columnspan=3, sticky=tk.NSEW, padx=10, pady=5)
        frame_list.columnconfigure(0, weight=1)
        frame_list.rowconfigure(0, weight=1)

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(frame_list)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # Listbox for tasks
        self.listbox = tk.Listbox(frame_list, height=10, selectmode=tk.SINGLE, yscrollcommand=self.scrollbar.set)
        self.listbox.grid(row=0, column=0, sticky=tk.NSEW)
        self.scrollbar.config(command=self.listbox.yview)

        # Buttons frame
        frame_btn = ttk.Frame(root)
        frame_btn.grid(row=3, column=0, columnspan=3, pady=5)
        self.btn_completar = ttk.Button(frame_btn, text="Marcar Completada", command=self.marcar_completada)
        self.btn_completar.pack(side=tk.LEFT, padx=5)
        self.btn_eliminar = ttk.Button(frame_btn, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Instructions label
        self.label_instr = ttk.Label(root, text="Atajos: Enter (agregar), C (completar), D/Delete (eliminar), Escape (salir)")
        self.label_instr.grid(row=4, column=0, columnspan=3, pady=10)

        # Bind keys
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
        for i, tarea in enumerate(self.tareas):
            self.listbox.insert(tk.END, tarea.descripcion)
            if tarea.completada:
                self.listbox.itemconfig(i, fg='gray')
            else:
                self.listbox.itemconfig(i, fg='black')