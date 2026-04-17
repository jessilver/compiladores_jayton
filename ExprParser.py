# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,2,1,
        2,1,2,5,2,30,8,2,10,2,12,2,33,9,2,1,3,1,3,1,3,5,3,38,8,3,10,3,12,
        3,41,9,3,1,4,1,4,1,4,3,4,46,8,4,1,5,1,5,1,5,3,5,51,8,5,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,59,8,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,1,0,3,4,1,
        0,5,6,60,0,14,1,0,0,0,2,24,1,0,0,0,4,26,1,0,0,0,6,34,1,0,0,0,8,42,
        1,0,0,0,10,50,1,0,0,0,12,58,1,0,0,0,14,19,3,2,1,0,15,16,5,1,0,0,
        16,18,3,2,1,0,17,15,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,
        0,0,0,20,22,1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,
        25,3,4,2,0,25,3,1,0,0,0,26,31,3,6,3,0,27,28,7,0,0,0,28,30,3,6,3,
        0,29,27,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,5,1,
        0,0,0,33,31,1,0,0,0,34,39,3,8,4,0,35,36,7,1,0,0,36,38,3,8,4,0,37,
        35,1,0,0,0,38,41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,7,1,0,0,
        0,41,39,1,0,0,0,42,45,3,10,5,0,43,44,5,2,0,0,44,46,3,8,4,0,45,43,
        1,0,0,0,45,46,1,0,0,0,46,9,1,0,0,0,47,48,7,0,0,0,48,51,3,10,5,0,
        49,51,3,12,6,0,50,47,1,0,0,0,50,49,1,0,0,0,51,11,1,0,0,0,52,59,5,
        9,0,0,53,59,5,10,0,0,54,55,5,7,0,0,55,56,3,2,1,0,56,57,5,8,0,0,57,
        59,1,0,0,0,58,52,1,0,0,0,58,53,1,0,0,0,58,54,1,0,0,0,59,13,1,0,0,
        0,6,19,31,39,45,50,58
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'**'", "'+'", "'-'", "'*'", "'/'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SEMI", "POW", "PLUS", "MINUS", "STAR", 
                      "SLASH", "LPAREN", "RPAREN", "INT", "ID", "WS" ]

    RULE_start_ = 0
    RULE_expr = 1
    RULE_additive = 2
    RULE_multiplicative = 3
    RULE_exponential = 4
    RULE_unary = 5
    RULE_primary = 6

    ruleNames =  [ "start_", "expr", "additive", "multiplicative", "exponential", 
                   "unary", "primary" ]

    EOF = Token.EOF
    SEMI=1
    POW=2
    PLUS=3
    MINUS=4
    STAR=5
    SLASH=6
    LPAREN=7
    RPAREN=8
    INT=9
    ID=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Start_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMI)
            else:
                return self.getToken(ExprParser.SEMI, i)

        def getRuleIndex(self):
            return ExprParser.RULE_start_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart_" ):
                listener.enterStart_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart_" ):
                listener.exitStart_(self)




    def start_(self):

        localctx = ExprParser.Start_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expr()
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 15
                self.match(ExprParser.SEMI)
                self.state = 16
                self.expr()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self):
            return self.getTypedRuleContext(ExprParser.AdditiveContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.additive()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(ExprParser.MultiplicativeContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.PLUS)
            else:
                return self.getToken(ExprParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MINUS)
            else:
                return self.getToken(ExprParser.MINUS, i)

        def getRuleIndex(self):
            return ExprParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)




    def additive(self):

        localctx = ExprParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.multiplicative()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 27
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 28
                self.multiplicative()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exponential(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExponentialContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExponentialContext,i)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.STAR)
            else:
                return self.getToken(ExprParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SLASH)
            else:
                return self.getToken(ExprParser.SLASH, i)

        def getRuleIndex(self):
            return ExprParser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)




    def multiplicative(self):

        localctx = ExprParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.exponential()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5 or _la==6:
                self.state = 35
                _la = self._input.LA(1)
                if not(_la==5 or _la==6):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 36
                self.exponential()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def POW(self):
            return self.getToken(ExprParser.POW, 0)

        def exponential(self):
            return self.getTypedRuleContext(ExprParser.ExponentialContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_exponential

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponential" ):
                listener.enterExponential(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponential" ):
                listener.exitExponential(self)




    def exponential(self):

        localctx = ExprParser.ExponentialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exponential)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.unary()
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 43
                self.match(ExprParser.POW)
                self.state = 44
                self.exponential()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def primary(self):
            return self.getTypedRuleContext(ExprParser.PrimaryContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)




    def unary(self):

        localctx = ExprParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self.unary()
                pass
            elif token in [7, 9, 10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.primary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = ExprParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_primary)
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.match(ExprParser.INT)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(ExprParser.ID)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.match(ExprParser.LPAREN)
                self.state = 55
                self.expr()
                self.state = 56
                self.match(ExprParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





