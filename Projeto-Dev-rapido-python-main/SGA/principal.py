from data.context.postgre_sql_context import Postgre_Sql_Context

#verificar se opção é valida
def verifica_opcao_selecionada(opcao_selecionada):
    try:
        e_numero = int(opcao_selecionada)

        if (e_numero >= 1 and e_numero <=3):
            return e_numero
        else:
            return 0
    except Exception as e:
        print("A opção informada não é valida. ")
        return 0

def alunos():
    print("1 - consultar")
    print("2 - Atualizar")
    print("3 - adicionar")

    opcao_selecionada = verifica_opcao_selecionada(input("informe a opção de desejo: "))
    
    if (opcao_selecionada == 0):
        alunos()
    else:
        db_pg_context = Postgre_Sql_Context()
        db_pg_context.conectar()

    #funcao para consultar
    if (opcao_selecionada == 1):
        alunos = db_pg_context.executar_query_sql("SELECT * FROM public.alunos")

        for aluno in alunos:
            print(f"ID: {aluno[0]}, NOME: {aluno[1]}, NOTA:{aluno[2]}")

    #funcao para atualizar dados
    elif (opcao_selecionada == 2):
        id_aluno = input("Informe o ID do aluno: ")
        novo_nome = input("Informe o NOME do aluno")
        nova_nota = input("Informe a NOTA do aluno: ")

        query = f"UPDATE public.alunos SET nome='{novo_nome}', nota={nova_nota}  WHERE id = {id_aluno}"

        db_pg_context.executar_update_sql(query)
    
    #funcao para adicionar novo aluno
    elif (opcao_selecionada == 3):
        nome = input("informe o NOME do aluno: ")
        nota = input("Informe a NOTA do aluno: ")
        
        query = f"INSERT INTO public.alunos (nome, nota) VALUES ('{nome}', {nota})"
        
        db_pg_context.executar_update_sql(query)

    #fecha a conexao com o banco de dados
    db_pg_context.desconectar()
    
alunos()






