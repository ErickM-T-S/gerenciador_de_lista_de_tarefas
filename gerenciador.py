def adicionar_tarefas(tarefas, nome_tarefa):

    tarefa = {"nome": nome_tarefa, "completada":False}
    tarefas.append(tarefa)
    print('a tarefa {} foi adicionada'.format(nome_tarefa))
    return

def ver_tarefas(tarefas): 
    print('\n Lista de tarefas')
    for indice, tarefa in enumerate(tarefas, start=1):
        status = '✓' if tarefa["completada"] else ''
        nome_tarefa = tarefa["nome"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    
def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    if indice_tarefa_ajustado >= 0 and  indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["nome"] = novo_nome_tarefa
        print(f'Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}')
    else: 
        print('Indice de tarefas invalido.')
    return

def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    tarefas[indice_tarefa_ajustado]["completada"] =True
    print(f'Tarefa {indice_tarefa} marcada como completo.')
    return

def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"] == True:
            tarefas.remove(tarefa)
    print('Tarefas completadas foram deletadas.')
    return

tarefas = []
while True:
    print('\n Menu do gerenciador de lista de tarefas:')
    print('1. adicionar tarefa')
    print('2. ver tarefas')
    print('3 .atualizar tarefas')
    print('4. completar tarefa')
    print('5. deletar tarefas completadas')
    print('6. Sair')

    escolha = int(input('digite a sua escolha: '))
    
    if escolha== 1:
        nome_tarefa =input('digite o nome da tarefa que deseja adicionar: ')
        adicionar_tarefas(tarefas, nome_tarefa) 

    elif escolha ==2:
        ver_tarefas(tarefas)
    
    elif escolha ==3:
        ver_tarefas(tarefas)
        indice_tarefa = input('Digite o número da tarefa que deseja atualizar: ')
        novo_nome = input('Digite o novo nome da tarefa: ')
        atualizar_tarefa(tarefas, indice_tarefa, novo_nome)
    
    elif escolha ==4:
        ver_tarefas(tarefas)
        indice_tarefa = input('Digite o número da tarefa que deseja completar: ')
        completar_tarefa(tarefas,indice_tarefa)

    elif escolha ==5:
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == 6:
        break

print('Programa finalizado')