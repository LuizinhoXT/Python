import textwrap
import cliente

class sistema():
    # Essa calsse direciona o fluxo das acoes do usuario do usuario
    # Idealmente parece bem semlhante com o conttrole que criei no código antigo
    lista_de_clientes = cliente.cliente()
    
    def realizar_login():
        
        pass
        
    
    def menu_usuario():
        var = """\n
            ================ MENU ================
            [d]\tDepositar
            [s]\tSacar
            [e]\tExtrato
            [nc]\tNova conta
            [lc]\tListar contas
            [nu]\tNovo usuário
            [q]\tSair
            [c]\tInformações da conta
            
            => """
        return input(textwrap.dedent(var))

    def menu_inicial():
        
        cpf = """\n
        
        ================ Bem Vindo ao Sistema Bancário ================
        
        >>> Gigite seu CPF para entrar no sistema: \n

        
        => """
        return input(textwrap.dedent(cpf))


def main():
    
    acesso = sistema()
    
    sistema.menu_inicial()
    
    # while True:

    #     sel = acesso.menu_usuario()
    
    #     if sel == "s": # sacar
    #         pass
    #     elif sel == "e": # exibir extrato
    #         pass
    #     elif sel == "d": # depositar
    #         pass
    #     elif sel == "c": # informações da conta
    #         pass 
    #     elif sel == "nu": # cadastrar usuário
    #         pass
    #     elif sel == "lu": # lista de usuarios
    #         pass
    #     elif sel == "nc": # criar conta
    #         pass
    #     elif sel == "q":
    #         break

main()