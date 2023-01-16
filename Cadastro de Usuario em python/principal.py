from operator import index
from model.usuarioModel import Usuario

listaUsuario = []

def telaInicial():
    opcao = int(input(
    '''\n
    Sejam bem-vindos!
    O que deseja fazer?
        1 - Login;
        2 - Cadastrar Usuário;
        3 - Listar Usuários;
        4 - Deletar usuários;
        5 - Sair
     Sua escolha: '''))
    
    if opcao == 5:
        return
    elif opcao == 1:
        telaLogin()
    elif opcao == 2:
        telaNovoUsuario()
    elif opcao == 3:
        telaListarUsuario()
    elif opcao == 4:
        telaDeletarUsuario()
    else:
        print('Digite uma opção válida: ')
        telaInicial()      
    
def mostrarListaUsuario():
    print('#' * 30)
    for usuario in listaUsuario:
        #nome, nUsuario, senha = usuario.values()
        #print(f'{nome} | {nUsuario} | {senha}')
        print(usuario)
    
    print('#' * 30)

def telaListarUsuario():
    
    mostrarListaUsuario()

    telaInicial()

def getLoginUsuario(usuarioPassado, senhaPassada):
    usuarioProcurado = usuarioPassado
    senhaProcurada = senhaPassada
    
    for usuario in listaUsuario:
        nome, nUsuario, senha = usuario.values()

        if ( usuarioProcurado == nUsuario) and (senhaProcurada == senha):
            return print(f'Seja bem-vindo(a) {nUsuario} !')
        elif(usuarioProcurado == nUsuario) and (senhaProcurada != senha):
            print('Senha inválida.')
        elif(usuarioProcurado != nUsuario) and (senhaProcurada == senha):
            print('Usuário não encontrado.')
        else:
            print('Usuário e senha não conferem.')
    return telaInicial()
    

def telaDeletarUsuario():

    mostrarListaUsuario()


    print("\n++++++++ Deletando Usuario ++++++++")
    loginUsuario = str(input('Qual usuario deseja excluir: '))
    
    for user in listaUsuario:
        if user['usuario'] == loginUsuario:
            listaUsuario = listaUsuario['usuario'].pop(user)
            
    
    mostrarListaUsuario()
    
        
   

def telaLogin():
    print("\n++++++++ Acesso ao Sistema ++++++++")
    loginUsuario = str(input('Digite um usuario: '))
    loginSenha = str(input('Digite a senha: '))
    
    getLoginUsuario(loginUsuario, loginSenha)
    

def telaNovoUsuario():
    
    print("\n++++++++ Novo Usuário ++++++++")
    nome = str(input('Digite o nome completo do usuário: '))
    usuario = str(input('Digite o Usuário: '))
    senha = str(input('Digite a senha: '))
    novoUsuario = Usuario(nome, usuario, senha)
    dicio = {'nome': novoUsuario.nome, 'usuario': novoUsuario.usuario, 'senha': novoUsuario.senha}
    
    print("\n++++++++ Salvando ++++++++")
    decisao = int(input(
        '''Deseja salvar esse usuario?
           1 - Sim;
           2 - Não;
        '''))

    if decisao == 1:
        listaUsuario.append(dicio.copy())
        print("\n++++++++  ++++++++")
        print(f'Usuário {usuario} salvo com sucesso')
       
    
    return telaInicial()


telaInicial()