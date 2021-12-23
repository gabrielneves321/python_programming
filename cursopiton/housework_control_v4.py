from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self, ):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao] [0]
    
    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'



class Tarefa: 
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
           status.append('(concluida)')
        elif self.vencimento:
           if datetime.now() > self.vencimento:
               status.append('(vencida)')
           else:
               dias = (self.vencimento - datetime.now()).days
               status.append(f'(vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)

def main():
    casa = Projeto('tarefas domesticas')
    casa.add('limpar o piso', datetime.now())
    casa.add('lavar pratos', datetime.now())
    print(casa)

    casa.procurar('lavar pratos').concluir()
    for tarefa in casa:
        print(f'-{tarefa}')
    print(casa)

    mercado = Projeto('Compras no mercado')
    mercado.add('carne')
    mercado.add('frutas secas')
    mercado.add('tomate', datetime.now() + timedelta(days=3, minutes=12))
    print(mercado)

   
    comprar_carne = mercado.procurar('carne')
    comprar_carne.concluir()
    for tarefa in mercado:
        print(f'- {tarefa}')
    print(mercado)

        
if __name__ == '__main__':
    main()

