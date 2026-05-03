import argparse
from personalizador import estilo, painel, layout, progresso

def main():
    parser = argparse.ArgumentParser(description="Formatador de texto usando a biblioteca Rich.")
    
    parser.add_argument("entrada", help="O texto ou caminho do arquivo a ser impresso.")
    
    parser.add_argument("-a", "--arquivo", action="store_true", 
                        help="Define que a entrada deve ser tratada como um arquivo.")
    
    parser.add_argument("-m", "--modulo", type=str, required=True,
                        choices=["estilo", "painel", "layout", "progresso"],
                        help="Escolha o módulo: estilo, painel, layout, progresso")
    
    parser.add_argument("-f", "--funcao", type=int, required=True,
                        choices=[1, 2],
                        help="Escolha a função do módulo: 1 ou 2")

    args = parser.parse_args()

    # Mapeamento de funções para facilitar o acesso via ID
    mapa = {
        "estilo": [estilo.imprimir_negrito_azul, estilo.imprimir_sublinhado_alerta],
        "painel": [painel.painel_simples, painel.painel_shadow],
        "layout": [layout.layout_divido, layout.layout_lateral],
        "progresso": [progresso.progresso_leitura, progresso.progresso_batida]
    }

    # Seleciona a função baseada no módulo e índice (ID - 1)
    funcao_escolhida = mapa[args.modulo][args.funcao - 1]
    
    # Executa a função
    funcao_escolhida(args.entrada, args.arquivo)

if __name__ == "__main__":
    main()