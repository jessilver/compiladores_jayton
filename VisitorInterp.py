#!/usr/bin/env python3
"""Visitor simples que avalia expressões geradas pela gramática Expr.
Requer que o parser seja gerado com a opção `-visitor`.
"""
import sys
from generated.ExprVisitor import ExprVisitor
from generated.ExprParser import ExprParser


class VisitorInterp(ExprVisitor):
    def __init__(self):
        super().__init__()
        self.env = {}

    # start_ : statement+ EOF ;
    def visitStart_(self, ctx:ExprParser.Start_Context):
        results = []
        for i in range(len(ctx.statement())):
            results.append(self.visit(ctx.statement(i)))
        return results

    def visitStatement(self, ctx:ExprParser.StatementContext):
        if ctx.declaration():
            return self.visit(ctx.declaration()) # NOVA LINHA
        if ctx.assignment():
            return self.visit(ctx.assignment())
        return self.visit(ctx.expr())
    
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        var_type = ctx.TYPE().getText()
        var_name = ctx.ID().getText()
        
        if var_name in self.env:
            raise NameError(f"Erro Semântico: Variável '{var_name}' já declarada.")
            
        # Verifica se o usuário colocou o sinal de '=' na declaração
        if ctx.ATTRIB():
            # Pega a expressão do lado direito e já resolve o valor
            value = self.visit(ctx.expr())
            self.env[var_name] = value
            return f"Declarada e inicializada: {var_type} {var_name} = {value}"
        else:
            # Se for só 'int a;', coloca o valor padrão zero
            self.env[var_name] = 0 if var_type == 'int' else 0.0
            return f"Variavel declarada: {var_type} {var_name}"

    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        name = ctx.ID().getText()
        if name not in self.env:
            raise NameError(f"Erro Semântico: Variável '{name}' não foi declarada antes do uso.")
        value = self.visit(ctx.expr())
        self.env[name] = value
        return value

    def visitAdditive(self, ctx:ExprParser.AdditiveContext):
        # children: multiplicative (op multiplicative)*
        n = ctx.getChildCount()
        res = self.visit(ctx.getChild(0)) # int 
        res = self._validate_number(res)
        i = 1
        while i < n:
            op = ctx.getChild(i).getText()
            rhs = self.visit(ctx.getChild(i+1))
            
            rhs = self._validate_number(rhs)
            
            if op == '+':
                res = res + rhs
            else:
                res = res - rhs
            i += 2
        return res

    def visitMultiplicative(self, ctx:ExprParser.MultiplicativeContext):
        n = ctx.getChildCount()
        res = self.visit(ctx.getChild(0))
        res = self._validate_number(res)
        i = 1
        while i < n:
            op = ctx.getChild(i).getText()
            rhs = self.visit(ctx.getChild(i+1))
            rhs = self._validate_number(rhs)
            if op == '*':
                res = res * rhs
            else:
                res = res / rhs
            i += 2
        return res

    def visitExponential(self, ctx:ExprParser.ExponentialContext):
        # unary (POW exponential)?
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unary())
        base = self.visit(ctx.unary())
        base = self._validate_number(base)
        exp = self.visit(ctx.exponential())
        exp = self._validate_number(exp)
        
        return base ** exp

    def visitUnary(self, ctx:ExprParser.UnaryContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())
        op = ctx.getChild(0).getText()
        val = self.visit(ctx.unary())
        val = self._validate_number(val)
        return +val if op == '+' else -val

    def visitPrimary(self, ctx:ExprParser.PrimaryContext):
        if ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        
        if ctx.INT():
            return int(ctx.INT().getText())
            
        if ctx.ID():
            name = ctx.ID().getText()
            if name not in self.env:
                raise NameError(f"Erro Semântico: Variavel '{name}' nao definida")
            return self.env[name]
            
        # '(' expr ')'
        return self.visit(ctx.expr())
    
    def _validate_number(self, value):
        """Valida se o valor é estritamente um int ou float."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"Erro Semântico: Operação matemática inválida com o tipo '{type(value).__name__}'")
        return value


if __name__ == '__main__':
    from antlr4 import FileStream, CommonTokenStream
    if len(sys.argv) < 2:
        print("Uso: python VisitorInterp.py <arquivo> (ou pipedir)")
        sys.exit(1)
    stream = FileStream(sys.argv[1])
    from generated.ExprLexer import ExprLexer
    from generated.ExprParser import ExprParser
    lexer = ExprLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)
    tree = parser.start_()
    v = VisitorInterp()
    print(v.visit(tree))
