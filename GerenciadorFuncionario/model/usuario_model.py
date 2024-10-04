class UsuarioModel:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self, nome, idade, profissao, cidade, genero, email, senha):
        usuario = {
            'nome': nome,
            'idade': idade,
            'profissao': profissao,
            'cidade': cidade,
            'genero': genero,
            'email': email,
            'senha': senha
        }
        self.usuarios.append(usuario)
        return usuario

    def autenticar_usuario(self, usuario, senha):
        for u in self.usuarios:
            if u['email'] == usuario and u['senha'] == senha:
                return True
        return False
