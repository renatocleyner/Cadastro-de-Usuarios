from model.usuario import Usuario

listaUsuarios = list()



def Menu():
    
    opcao = int(input('''\n
    ##############  Sistema de Login ###############
    ##############  Sejam bem-vindos! ############## 
    #    O que deseja fazer?
    #    1 - Login;
    #    2 - Cadastrar Usuário;
    #    3 - Listar Usuários;
    #    4 - Deletar usuários;
    #    5 - Sair
    ############## ################## ############## 
    Sua escolha: '''))

    if opcao == 5:
        TelaSair()
    elif opcao == 1:
        TelaLogin()
    elif opcao == 2:
        TelaCadastro()
    elif opcao == 3:
        TelaListandoUsuarios()
    elif opcao == 4:
        deletandoUsuarios()
    else:
        print('digite opção valida')
        Menu()

def TelaSair():
    print('''Obrigado por acessar o sistema''')
    exit()

def TelaCadastro():
    print("\n++++++++ Cadastro de Usuario ++++++++")
    novoUsuario = str(input("Digite o nome do novo usuario: "))
    novaSenha = str(input("Digite a nova senha: "))
    usuarioCadastrado = Usuario(novoUsuario, novaSenha)
    dicio = dict({'usuario': usuarioCadastrado.usuario , 'senha': usuarioCadastrado.senha })

    print("\n++++++++ Salvando ++++++++")
    descisao = int(input(
        '''
        Deseja salvar esse usuario?
        1- Sim;
        2- Nao;
        '''))
    if descisao == 2:
        return
    else:
        listaUsuarios.append(dicio.copy())
        print(f'Usuario {usuarioCadastrado.usuario} salvo com sucesso')

    Menu()

def consultandoUsuario(usuarioPassado, senhaPassada):
    usuarioConsultado = usuarioPassado
    senhaConsultada = senhaPassada
    
    for usuario in listaUsuarios:
        user, senha = usuario.values()
        if(usuarioConsultado == user) and (senhaConsultada == senha):
            return print(f'Seja bem-vindo(a) {user} !')
        elif(usuarioConsultado == user) and (senhaConsultada != senha):
            print("Senha Invalida")
        elif(usuarioConsultado != user) and (senhaConsultada == senha):
            print('Usuario não encontrado')
        else:
            print("Usuario e senha não conferem")
    return Menu()        


def TelaLogin():
    print("\n++++++++ Acesso ao Sistema ++++++++")
    usuarioLogado = str(input("Digite um usuario: "))
    senhaLogado = str(input("Digite a senha: "))

    consultandoUsuario(usuarioLogado, senhaLogado)

def listandoUsuarios():
    print('#'*30)
    print('++++++++ Listando Usuarios ++++++++')
    for usuario in listaUsuarios:
        print(usuario)
        
    Menu()

def deletandoUsuarios():
    usuarioDeletado = str(input('Digite o nome do usuario a ser deletado: '))

    for usuario in range(len(listaUsuarios)):
        if listaUsuarios[usuario]['usuario'] == usuarioDeletado:
            del listaUsuarios[usuario]
            break            
            

    # usuarioParaDeletar = next((u for u in listaUsuarios if u['usuario']== usuarioDeletado), None)    
    # print(usuarioParaDeletar)
    # del usuarioParaDeletar 

    
    # for usuario in listaUsuarios:
    #     if usuario == usuarioDeletado:
    #         listaUsuarios.remove['usuario'](usuarioDeletado)
 
    print(f"O usuario {usuarioDeletado} deletado com sucesso")       
    listandoUsuarios()
    Menu()
    

def TelaListandoUsuarios():
    listandoUsuarios()
    Menu()

Menu()
