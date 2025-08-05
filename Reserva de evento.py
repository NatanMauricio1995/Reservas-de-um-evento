"""
Sistema de Reservas para Eventos
Exercício de Programação Orientada a Objetos em Python

Objetivo: Demonstrar uso de classes, métodos e validação de entrada
para criar um sistema funcional de reservas de eventos.

Funcionalidades:
- Criação de eventos com capacidade limitada
- Sistema de reservas com validação
- Cancelamento de reservas  
- Visualização de disponibilidade
- Interface interativa no terminal

Autor: [Seu Nome]
Data: [Data atual]  
Versão: 1.0
"""

class Evento:
    """
    Classe que representa um evento com capacidade limitada de lugares.
    
    Atributos:
        capacidade (int): Número total de lugares do evento
        reservado (int): Número de lugares já reservados
    """
    
    def __init__(self, capacidade, reservado=0):
        """
        Inicializa um evento com capacidade definida.
        
        Args:
            capacidade (int): Capacidade total do evento
            reservado (int): Número inicial de reservas (padrão: 0)
        """
        self.capacidade = capacidade
        self.reservado = reservado
        
    def reservar(self):
        """
        Realiza reserva de lugares no evento.
        Solicita quantidade e valida se há vagas suficientes.
        """
        # Verifica se há vagas disponíveis
        if self.capacidade - self.reservado <= 0:
            print("Não há mais vagas disponíveis para o evento!")
            print("-" * 100, "\n\n")
            return
            
        while True:
            try:
                reservas = int(input("Digite a quantidade de pessoas para reservar lugar: "))
                
                # Valida se a quantidade é positiva
                if reservas <= 0:
                    print("Quantidade deve ser maior que zero!")
                    continue
                
                # Verifica se há vagas suficientes para a reserva
                if self.capacidade - self.reservado - reservas >= 0:
                    self.reservado += reservas
                    print("Reserva efetuada com sucesso!")
                    print(f" - Reservado: {self.reservado}")
                    print(f" - Disponíveis: {self.capacidade - self.reservado}")
                    print("-" * 100, "\n\n")
                    break
                else:
                    vagas_disponiveis = self.capacidade - self.reservado
                    print(f"Quantidade solicitada ({reservas}) é maior que as vagas disponíveis ({vagas_disponiveis})!")
                    
            except ValueError:
                print("Por favor, insira um número válido!")
                    
    def cancelar(self):
        """
        Cancela reservas do evento.
        Valida se existem reservas suficientes para cancelar.
        """
        # Verifica se há reservas para cancelar
        if self.reservado == 0:
            print("Não há reservas para cancelar!")
            print("-" * 100, "\n\n")
            return
            
        while True:
            try:
                cancelamento = int(input("Digite a quantidade de pessoas que desejam cancelar: "))
                
                # Valida se a quantidade é positiva
                if cancelamento <= 0:
                    print("Quantidade deve ser maior que zero!")
                    continue
                
                # Verifica se há reservas suficientes para cancelar
                if self.reservado - cancelamento >= 0:
                    self.reservado -= cancelamento
                    print("Cancelamento realizado com sucesso!")
                    print(f" - Reservado: {self.reservado}")
                    print(f" - Disponíveis: {self.capacidade - self.reservado}")
                    print("-" * 100, "\n\n")
                    break
                else:
                    print(f"Quantidade solicitada ({cancelamento}) é maior que as reservas existentes ({self.reservado})!")
                    
            except ValueError:
                print("Por favor, insira um número válido!")
                    
    def lugares_disponiveis(self):
        """
        Exibe informações detalhadas sobre a disponibilidade do evento.
        """
        imprimir_titulo("Status do Evento")
        print(f"O evento possui {self.capacidade} lugares totais:")
        
        if self.reservado == 0:
            print("Nenhuma reserva registrada ainda!")
        else:
            print(f" - Reservados: {self.reservado}")
            print(f" - Disponíveis: {self.capacidade - self.reservado}")
            
        print("-" * 100, "\n\n")


def imprimir_titulo(titulo):
    """
    Imprime um título formatado com bordas decorativas.
    
    Args:
        titulo (str): O texto do título a ser exibido
    """
    titulo = titulo.upper()
    quantidade_tracos = 100
    tamanho_titulo = len(titulo)
    quantidade_espacos = (quantidade_tracos - tamanho_titulo) // 2
    
    print()
    print("-" * quantidade_tracos)
    print(" " * quantidade_espacos, titulo)
    print("-" * quantidade_tracos)
    print()


def menu():
    """
    Exibe o menu principal com todas as opções disponíveis.
    """
    imprimir_titulo("Menu Principal")   
    print("Opções disponíveis:")
    print("  1. Visualizar status do evento")
    print("  2. Realizar reserva")
    print("  3. Cancelar reserva")
    print("  4. Sair do sistema")
    print("-" * 100, "\n\n")


def definindo_lugares():
    """
    Solicita e valida a capacidade do evento.
    
    Returns:
        Evento: Nova instância de evento com capacidade definida
    """
    imprimir_titulo("Configuração do Evento")
    
    while True:
        try:
            lugares = int(input("Insira a capacidade total do evento: "))
            
            if lugares > 0:
                evento = Evento(lugares, 0)
                print(f"Evento criado com sucesso! Capacidade: {lugares} lugares")
                print("-" * 100, "\n\n")
                return evento
            else:
                print("A capacidade deve ser maior que zero!")
                
        except ValueError:
            print("Por favor, insira um número válido!")


def definindo_escolha():
    """
    Captura e valida a escolha do usuário do menu.
    
    Returns:
        int: Número da opção escolhida (1-4)
    """
    while True:
        try:
            escolha = int(input("Digite sua escolha (1-4): "))
            
            if 1 <= escolha <= 4:
                print("-" * 100, "\n\n")
                return escolha
            else:
                print("Opção inválida! Escolha entre 1 e 4.")
                
        except ValueError:
            print("Por favor, insira um número válido!")


def main():
    """
    Função principal que executa o sistema de reservas.
    Controla o fluxo principal do programa.
    """
    # Configuração inicial do evento
    evento = definindo_lugares()
    
    # Loop principal do sistema
    opcao = 0
    while opcao != 4:
        menu()
        opcao = definindo_escolha()
        
        # Executa a ação escolhida pelo usuário
        if opcao == 1:
            evento.lugares_disponiveis()
        elif opcao == 2:
            evento.reservar()
        elif opcao == 3:
            evento.cancelar()
        elif opcao == 4:
            imprimir_titulo("Sistema Finalizado")
            print("Obrigado por usar o Sistema de Reservas!")
            print("Até logo!")


# Ponto de entrada do programa
if __name__ == "__main__":
    main()