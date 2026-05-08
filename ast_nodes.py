# ast_nodes.py atualizado com anotações

class ASTNode:
    def __init__(self):
        self.eval_type = None # Aqui fica a anotação de tipo

class Number(ASTNode):
    def __init__(self, value):
        super().__init__()
        self.value = float(value)
        self.eval_type = 'FLOAT' # Anotação

class Identifier(ASTNode):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.eval_type = 'FLOAT' # Em uma linguagem maior, buscaríamos isso na tabela

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        super().__init__()
        self.left = left
        self.op = op
        self.right = right
        self.eval_type = 'FLOAT' # A operação entre floats resulta em float

class Assign(ASTNode):
    def __init__(self, name, expr):
        super().__init__()
        self.name = name
        self.expr = expr
        self.eval_type = 'VOID' # Atribuições geralmente não retornam valor