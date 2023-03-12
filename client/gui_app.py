import tkinter as tk
from tkinter import ttk, messagebox
from model.registro_dao import crear_tabla, borrar_tabla
from model.registro_dao import Registro, guardar, listar, editar, eliminar

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=600)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear Registro', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    barra_menu.add_cascade(label='Configuracion')
    barra_menu.add_cascade(label='Ayuda')

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=600, height=320)
        self.root = root
        self.pack()
        self.config(bg='#CCEBEF')
        self.campos_pasientes()
        self.desabilitar_campos()
        self.tabla_registro()
        self.id_registro = None
        


    def campos_pasientes(self): 
        self.label_nombre = tk.Label(self, text='Nombre Mascota: ')   
        self.label_nombre.config(font=('Arial', 12, 'bold'), bg='#CCEBEF')   
        self.label_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.label_genero = tk.Label(self, text='Sexo: ')   
        self.label_genero.config(font=('Arial', 12, 'bold'), bg='#CCEBEF')   
        self.label_genero.grid(row=1, column=1, padx=10, pady=10)

        self.label_raza = tk.Label(self, text='Raza: ')   
        self.label_raza.config(font=('Arial', 12, 'bold'), bg='#CCEBEF')   
        self.label_raza.grid(row=2, column=1, padx=10, pady=10)

        self.label_propietario = tk.Label(self, text='Propietario: ')   
        self.label_propietario.config(font=('Arial', 12, 'bold'), bg='#CCEBEF')   
        self.label_propietario.grid(row=3, column=1, padx=10, pady=10)

        self.label_telefono = tk.Label(self, text='Telefono: ')   
        self.label_telefono.config(font=('Arial', 12, 'bold'), bg='#CCEBEF')   
        self.label_telefono.grid(row=4, column=1, padx=10, pady=10)
        # Entry de cada campo

        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width=40, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=2, padx=10, pady=10)

        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable= self.mi_genero)
        self.entry_genero.config(width=40, font=('Arial', 12))
        self.entry_genero.grid(row=1, column=2, padx=10, pady=10)

        self.mi_raza = tk.StringVar()
        self.entry_raza = tk.Entry(self, textvariable=self.mi_raza)
        self.entry_raza.config(width=40, font=('Arial', 12))
        self.entry_raza.grid(row=2, column=2, padx=10, pady=10)

        self.mi_propietario = tk.StringVar()
        self.entry_propietario = tk.Entry(self, textvariable=self.mi_propietario)
        self.entry_propietario.config(width=40, font=('Arial', 12))
        self.entry_propietario.grid(row=3, column=2, padx=5, pady=5)

        self.mi_telefono = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable=self.mi_telefono)
        self.entry_telefono.config(width=40, font=('Arial', 12))
        self.entry_telefono.grid(row=4, column=2, padx=10, pady=10)

        #Botones

        self.boton_nuevo = tk.Button(self, text="Nuevo", command=self.habilitar_campos)
        self.boton_nuevo.config(width=20,  font=('Arial', 12, 'bold'), fg='#2836EB', bg='#33E9FF', cursor='hand2', activebackground='#3D68B7')
        self.boton_nuevo.grid(row=5, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command=self.guardar_datos )
        self.boton_guardar.config(width=20,  font=('Arial', 12, 'bold'), fg='#2836EB', bg='#33E9FF', cursor='hand2', activebackground='#3D68B7')
        self.boton_guardar.grid(row=5, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command=self.desabilitar_campos)
        self.boton_cancelar.config(width=20,  font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#ED0B0B', cursor='hand2', activebackground='#D13E3E')
        self.boton_cancelar.grid(row=5, column=2, padx=10, pady=10)


    def habilitar_campos(self):
                
        self.entry_nombre.config(state='normal')
        self.entry_genero.config(state='normal')    
        self.entry_raza.config(state='normal') 
        self.entry_propietario.config(state='normal')    
        self.entry_telefono.config(state='normal')    


        self.boton_guardar.config(state='normal')    
        self.boton_cancelar.config(state='normal')  
        
    def desabilitar_campos(self):
        self.id_registro = None
        self.mi_nombre.set('')
        self.mi_genero.set('')
        self.mi_raza.set('')
        self.mi_propietario.set('')
        self.mi_telefono.set('')
        

        self.entry_nombre.config(state='disabled')
        self.entry_genero.config(state='disabled')    
        self.entry_raza.config(state='disabled') 
        self.entry_propietario.config(state='disabled')    
        self.entry_telefono.config(state='disabled')    


        self.boton_guardar.config(state='disabled')    
        self.boton_cancelar.config(state='disabled')    
        
    def guardar_datos(self):

        registro = Registro(

            self.mi_nombre.get(),
            self.mi_genero.get(),
            self.mi_raza.get(),
            self.mi_propietario.get(),
            self.mi_telefono.get(),
        )

        if self.id_registro == None:
            guardar(registro)
        else:
            editar(registro, self.id_registro)          

        self.tabla_registro()

        self.desabilitar_campos()

    def tabla_registro(self):

        self.lista_registros = listar()
        self.lista_registros.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Sexo', 'Raza', 'Propietario', 'Telefono'))  

        self.tabla.grid(row=6,   column=0, columnspan=4)

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=6, sticky='nse')
        #self.scroll.config(bg='green')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='GENERO')
        self.tabla.heading('#3', text='RAZA')
        self.tabla.heading('#4', text='PROPIETARIO')
        self.tabla.heading('#5', text='TELEFONO')

        #interar lista de registros

       

        for p in self.lista_registros:

          self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3], p[4], p[5]))


       

         #BOTONES DE EDITAR Y ELIMINAR

        self.boton_editar = tk.Button(self, text="EDITAR", command=self.editar_datos)
        self.boton_editar.config(width=20,  font=('Arial', 12, 'bold'), fg='#2836EB', bg='#33E9FF', cursor='hand2', activebackground='#3D68B7')
        self.boton_editar.grid(row=7, column=2, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text="ELIMINAR", command=self.eliminar_datos)
        self.boton_eliminar.config(width=20,  font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#ED0B0B', cursor='hand2', activebackground='#D13E3E')
        self.boton_eliminar.grid(row=7, column=3, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_registro = self.tabla.item(self.tabla.selection())['text']
            self.nombre_registro = self.tabla.item(
                self.tabla.selection())['values'][0]
            
            self.genero_registro = self.tabla.item(
                self.tabla.selection())['values'][1]
            
            self.raza_registro = self.tabla.item(
                self.tabla.selection())['values'][2]
            
            self.propietario_registro = self.tabla.item(
                self.tabla.selection())['values'][3]
            
            self.telefono_registro = self.tabla.item(
                self.tabla.selection())['values'][4]
            
            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_registro)
            self.entry_genero.insert(0, self.genero_registro)
            self.entry_raza.insert(0, self.raza_registro)
            self.entry_propietario.insert(0, self.propietario_registro)
            self.entry_telefono.insert(0, self.telefono_registro)

         
        except:    

            titulo = 'Edicion de datos'

            mensaje = 'No ha seleccionado ningun registro'

            messagebox.showerror(titulo, mensaje)


    def eliminar_datos(self):
        try:
            self.id_registro = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_registro)
            self.tabla_registro()
            self.id_registro = None
        except:

            titulo = 'Eliminar un registro'
            mensaje = 'No se pudo eliminar el registro'
            messagebox.showerror(titulo, mensaje)
                   