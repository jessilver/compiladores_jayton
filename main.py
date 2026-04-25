# main.py
import sys
from antlr4 import *
from generated.ExprLexer import ExprLexer
from generated.ExprParser import ExprParser
from ast_builder import ASTBuilder
from evaluator import Evaluator
from visualizer import draw_ast, print_ast
from ast_nodes import Assign

def main():
    # 1. Verificação de argumentos de linha de comando
    if len(sys.argv) < 2:
        print('Uso correto: python main.py <arquivo_de_entrada.txt>')
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    print(f"Lendo e interpretando o arquivo: {arquivo_entrada}")
    print("=" * 50)

    # 2. Configuração do ANTLR para leitura de arquivo
    try:
        input_stream = FileStream(arquivo_entrada, encoding='utf-8')
    except FileNotFoundError:
        print(f"Erro crítico: O arquivo '{arquivo_entrada}' não foi encontrado.")
        sys.exit(1)
        
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    
    # Gera a Árvore de Derivação (Parse Tree) inicial
    tree = parser.start_() 
    
    # 3. Inicialização dos nossos componentes
    builder = ASTBuilder()
    evaluator = Evaluator()
    
    # 4. Iteração sobre cada instrução (statement) do arquivo
    instrucao_count = 0
    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        
        # Ignora o marcador de fim de arquivo
        if child.getText() == "<EOF>":
            break
            
        # Constrói o nó da AST para a linha atual
        ast_node = builder.visit(child)
        
        if ast_node:
            instrucao_count += 1
            print(f"\n[Linha {instrucao_count}] Processando...")
            
            # --- VISUALIZAÇÃO ---
            # Imprime no terminal (árvore de texto)
            print_ast(ast_node) 
            
            # Gera imagem PNG única para esta linha
            # Nomeia como ast_linha_1, ast_linha_2, etc.
            nome_img = f"ast_linha_{instrucao_count}"
            draw_ast(ast_node, nome_img)
            
            # --- EXECUÇÃO ---
            try:
                resultado = evaluator.evaluate(ast_node)
                
                # Se for uma expressão pura (sem ser atribuição), mostramos o resultado
                if resultado is not None and not isinstance(ast_node, Assign):
                    print(f"   >>> Resultado: {resultado}")
            except Exception as e:
                print(f"   >>> Erro Semântico: {e}")
                
    print("-" * 50)
    print("Tabela de Símbolos Final (Memória):")
    if not evaluator.symbols:
        print("  (Vazia)")
    else:
        for var, val in evaluator.symbols.items():
            print(f"  {var} = {val}")
    print("=" * 50)
    print(f"Sucesso! {instrucao_count} imagens de árvores foram geradas.")

if __name__ == '__main__':
    main()
    