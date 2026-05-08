# ast_builder.py
from generated.ExprVisitor import ExprVisitor
from ast_nodes import Number, Identifier, BinOp, Assign

class ASTBuilder(ExprVisitor):

    # 1. Corrigindo o bug do ponto e vírgula
    def visitStatement(self, ctx):
        # Forçamos o retorno apenas do filho 0 (que é a atribuição ou expressão)
        # Ignorando completamente o filho 1 (que é o SEMI ';')
        return self.visit(ctx.getChild(0))

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        expr_node = self.visit(ctx.expr())
        return Assign(name, expr_node)

    def visitExpr(self, ctx):
        # A regra expr só aponta para additive
        return self.visit(ctx.additive())

    def visitAdditive(self, ctx):
        # Pega o primeiro nó à esquerda
        node = self.visit(ctx.getChild(0))
        
        # Itera pulando de 2 em 2 para pegar os operadores (+ ou -) e os próximos nós
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            node = BinOp(node, op, right) # Agrupa nativamente à esquerda
            
        return node

    def visitMultiplicative(self, ctx):
        # Se for apenas um 'unary' (sem * ou /), ele desvia para cá
        if ctx.unary():
            return self.visit(ctx.unary())
        
        # Se tiver multiplicações/divisões, faz a mesma lógica do additive
        node = self.visit(ctx.getChild(0))
        for i in range(1, ctx.getChildCount(), 2):
            op = ctx.getChild(i).getText()
            right = self.visit(ctx.getChild(i+1))
            node = BinOp(node, op, right)
        return node

    def visitExponential(self, ctx):
        node = self.visit(ctx.unary())
        
        # Como potência é associativa à direita e opcional (?), olhamos se tem filhos
        if ctx.getChildCount() > 1:
            op = ctx.POW().getText()
            right = self.visit(ctx.exponential())
            node = BinOp(node, op, right)
        return node

    def visitUnary(self, ctx):
        # Se for um 'primary' comum
        if ctx.primary():
            return self.visit(ctx.primary())
        
        # Se for um operador unário (exemplo: -5)
        op = ctx.getChild(0).getText()
        node = self.visit(ctx.unary())
        
        # Truque rápido: como não criamos um nó 'UnaryOp', emulamos subtraindo de zero (0 - X)
        if op == '-':
            return BinOp(Number(0), '-', node) 
        return node

    def visitPrimary(self, ctx):
        if ctx.INT():
            return Number(ctx.INT().getText())
        elif ctx.ID():
            return Identifier(ctx.ID().getText())
        else:
            # É um parênteses: ( expr ). O 'expr' é o filho do meio (índice 1)
            return self.visit(ctx.expr())