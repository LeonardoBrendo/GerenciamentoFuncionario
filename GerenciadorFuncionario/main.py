import tkinter as tk
from model.usuario_model import UsuarioModel
from view.usuario_view import UsuarioView
from controller.usuario_controller import UsuarioController

if __name__ == "__main__":
    root = tk.Tk()
    model = UsuarioModel()
    view = UsuarioView(root)
    controller = UsuarioController(model, view)
    root.mainloop()
