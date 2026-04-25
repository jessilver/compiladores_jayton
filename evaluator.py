# evaluator.py
from ast_nodes import Number, Identifier, BinOp, Assign

class Evaluator:
    def __init__(self):
        # ESTA É A SUA TABELA DE SÍMBOLOS
        self.symbols = {}

    def evaluate(self, node):
        if isinstance(node, Number):
            return node.value

        elif isinstance(node, Identifier):
            # Busca na tabela de símbolos
            if node.name in self.symbols:
                return self.symbols[node.name]
            raise NameError(f"Erro: Variável '{node.name}' não declarada!")

        elif isinstance(node, Assign):
            # Avalia a expressão direita e salva na tabela de símbolos
            value = self.evaluate(node.expr)
            self.symbols[node.name] = value
            return value

        elif isinstance(node, BinOp):
            left = self.evaluate(node.left)
            right = self.evaluate(node.right)
            
            if node.op == '+': return left + right
            elif node.op == '-': return left - right
            elif node.op == '*': return left * right
            elif node.op == '/': return left / right
            elif node.op == '**': return left ** right