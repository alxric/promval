# Generated from PromQLParser.g4 by ANTLR 4.10
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
        4,1,43,308,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,79,8,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,111,8,1,10,
        1,12,1,114,9,1,1,2,1,2,1,3,1,3,3,3,120,8,3,1,4,1,4,3,4,124,8,4,1,
        5,1,5,3,5,128,8,5,1,6,1,6,3,6,132,8,6,1,6,3,6,135,8,6,1,7,1,7,3,
        7,139,8,7,1,8,1,8,3,8,143,8,8,1,9,1,9,3,9,147,8,9,1,10,1,10,3,10,
        151,8,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,
        163,8,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,3,14,172,8,14,1,14,3,
        14,175,8,14,1,14,1,14,1,14,1,14,3,14,181,8,14,1,15,1,15,1,15,1,15,
        1,16,1,16,1,17,1,17,1,17,5,17,192,8,17,10,17,12,17,195,9,17,1,18,
        1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,208,8,19,
        1,20,1,20,1,20,1,20,1,20,5,20,215,8,20,10,20,12,20,218,9,20,3,20,
        220,8,20,1,20,1,20,1,21,1,21,3,21,226,8,21,1,22,1,22,1,22,1,22,5,
        22,232,8,22,10,22,12,22,235,9,22,3,22,237,8,22,1,22,1,22,1,23,1,
        23,1,23,1,23,1,23,3,23,246,8,23,1,23,1,23,1,23,1,23,1,23,1,23,3,
        23,254,8,23,3,23,256,8,23,1,24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,
        3,26,266,8,26,1,26,1,26,3,26,270,8,26,1,27,1,27,1,27,1,28,1,28,1,
        28,1,29,1,29,3,29,280,8,29,1,30,1,30,3,30,284,8,30,1,31,1,31,1,31,
        3,31,289,8,31,1,32,1,32,1,32,1,32,5,32,295,8,32,10,32,12,32,298,
        9,32,3,32,300,8,32,1,32,1,32,1,33,1,33,1,34,1,34,1,34,0,1,2,35,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,62,64,66,68,0,8,1,0,3,4,1,0,5,7,1,0,13,18,2,
        0,9,9,11,11,2,0,11,11,23,23,3,0,12,12,14,14,19,20,2,0,9,11,21,30,
        1,0,1,2,319,0,70,1,0,0,0,2,78,1,0,0,0,4,115,1,0,0,0,6,117,1,0,0,
        0,8,121,1,0,0,0,10,125,1,0,0,0,12,129,1,0,0,0,14,136,1,0,0,0,16,
        140,1,0,0,0,18,144,1,0,0,0,20,148,1,0,0,0,22,152,1,0,0,0,24,162,
        1,0,0,0,26,164,1,0,0,0,28,180,1,0,0,0,30,182,1,0,0,0,32,186,1,0,
        0,0,34,188,1,0,0,0,36,196,1,0,0,0,38,207,1,0,0,0,40,209,1,0,0,0,
        42,225,1,0,0,0,44,227,1,0,0,0,46,255,1,0,0,0,48,257,1,0,0,0,50,260,
        1,0,0,0,52,265,1,0,0,0,54,271,1,0,0,0,56,274,1,0,0,0,58,277,1,0,
        0,0,60,281,1,0,0,0,62,288,1,0,0,0,64,290,1,0,0,0,66,303,1,0,0,0,
        68,305,1,0,0,0,70,71,3,2,1,0,71,72,5,0,0,1,72,1,1,0,0,0,73,74,6,
        1,-1,0,74,75,3,4,2,0,75,76,3,2,1,8,76,79,1,0,0,0,77,79,3,24,12,0,
        78,73,1,0,0,0,78,77,1,0,0,0,79,112,1,0,0,0,80,81,10,10,0,0,81,82,
        3,6,3,0,82,83,3,2,1,10,83,111,1,0,0,0,84,85,10,7,0,0,85,86,3,8,4,
        0,86,87,3,2,1,8,87,111,1,0,0,0,88,89,10,6,0,0,89,90,3,10,5,0,90,
        91,3,2,1,7,91,111,1,0,0,0,92,93,10,5,0,0,93,94,3,12,6,0,94,95,3,
        2,1,6,95,111,1,0,0,0,96,97,10,4,0,0,97,98,3,14,7,0,98,99,3,2,1,5,
        99,111,1,0,0,0,100,101,10,3,0,0,101,102,3,16,8,0,102,103,3,2,1,4,
        103,111,1,0,0,0,104,105,10,2,0,0,105,106,3,18,9,0,106,107,3,2,1,
        3,107,111,1,0,0,0,108,109,10,9,0,0,109,111,3,20,10,0,110,80,1,0,
        0,0,110,84,1,0,0,0,110,88,1,0,0,0,110,92,1,0,0,0,110,96,1,0,0,0,
        110,100,1,0,0,0,110,104,1,0,0,0,110,108,1,0,0,0,111,114,1,0,0,0,
        112,110,1,0,0,0,112,113,1,0,0,0,113,3,1,0,0,0,114,112,1,0,0,0,115,
        116,7,0,0,0,116,5,1,0,0,0,117,119,5,8,0,0,118,120,3,52,26,0,119,
        118,1,0,0,0,119,120,1,0,0,0,120,7,1,0,0,0,121,123,7,1,0,0,122,124,
        3,52,26,0,123,122,1,0,0,0,123,124,1,0,0,0,124,9,1,0,0,0,125,127,
        7,0,0,0,126,128,3,52,26,0,127,126,1,0,0,0,127,128,1,0,0,0,128,11,
        1,0,0,0,129,131,7,2,0,0,130,132,5,28,0,0,131,130,1,0,0,0,131,132,
        1,0,0,0,132,134,1,0,0,0,133,135,3,52,26,0,134,133,1,0,0,0,134,135,
        1,0,0,0,135,13,1,0,0,0,136,138,7,3,0,0,137,139,3,52,26,0,138,137,
        1,0,0,0,138,139,1,0,0,0,139,15,1,0,0,0,140,142,5,10,0,0,141,143,
        3,52,26,0,142,141,1,0,0,0,142,143,1,0,0,0,143,17,1,0,0,0,144,146,
        7,4,0,0,145,147,3,52,26,0,146,145,1,0,0,0,146,147,1,0,0,0,147,19,
        1,0,0,0,148,150,5,38,0,0,149,151,3,22,11,0,150,149,1,0,0,0,150,151,
        1,0,0,0,151,21,1,0,0,0,152,153,5,27,0,0,153,154,5,40,0,0,154,23,
        1,0,0,0,155,163,3,40,20,0,156,163,3,46,23,0,157,163,3,28,14,0,158,
        163,3,36,18,0,159,163,3,38,19,0,160,163,3,68,34,0,161,163,3,26,13,
        0,162,155,1,0,0,0,162,156,1,0,0,0,162,157,1,0,0,0,162,158,1,0,0,
        0,162,159,1,0,0,0,162,160,1,0,0,0,162,161,1,0,0,0,163,25,1,0,0,0,
        164,165,5,33,0,0,165,166,3,2,1,0,166,167,5,34,0,0,167,27,1,0,0,0,
        168,174,5,41,0,0,169,171,5,31,0,0,170,172,3,34,17,0,171,170,1,0,
        0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,175,5,32,0,0,174,169,1,0,
        0,0,174,175,1,0,0,0,175,181,1,0,0,0,176,177,5,31,0,0,177,178,3,34,
        17,0,178,179,5,32,0,0,179,181,1,0,0,0,180,168,1,0,0,0,180,176,1,
        0,0,0,181,29,1,0,0,0,182,183,3,62,31,0,183,184,3,32,16,0,184,185,
        5,2,0,0,185,31,1,0,0,0,186,187,7,5,0,0,187,33,1,0,0,0,188,193,3,
        30,15,0,189,190,5,37,0,0,190,192,3,30,15,0,191,189,1,0,0,0,192,195,
        1,0,0,0,193,191,1,0,0,0,193,194,1,0,0,0,194,35,1,0,0,0,195,193,1,
        0,0,0,196,197,3,28,14,0,197,198,5,39,0,0,198,37,1,0,0,0,199,200,
        3,28,14,0,200,201,5,27,0,0,201,202,5,40,0,0,202,208,1,0,0,0,203,
        204,3,36,18,0,204,205,5,27,0,0,205,206,5,40,0,0,206,208,1,0,0,0,
        207,199,1,0,0,0,207,203,1,0,0,0,208,39,1,0,0,0,209,210,5,30,0,0,
        210,219,5,33,0,0,211,216,3,42,21,0,212,213,5,37,0,0,213,215,3,42,
        21,0,214,212,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,
        0,0,217,220,1,0,0,0,218,216,1,0,0,0,219,211,1,0,0,0,219,220,1,0,
        0,0,220,221,1,0,0,0,221,222,5,34,0,0,222,41,1,0,0,0,223,226,3,68,
        34,0,224,226,3,2,1,0,225,223,1,0,0,0,225,224,1,0,0,0,226,43,1,0,
        0,0,227,236,5,33,0,0,228,233,3,42,21,0,229,230,5,37,0,0,230,232,
        3,42,21,0,231,229,1,0,0,0,232,235,1,0,0,0,233,231,1,0,0,0,233,234,
        1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,236,228,1,0,0,0,236,237,
        1,0,0,0,237,238,1,0,0,0,238,239,5,34,0,0,239,45,1,0,0,0,240,241,
        5,29,0,0,241,256,3,44,22,0,242,245,5,29,0,0,243,246,3,48,24,0,244,
        246,3,50,25,0,245,243,1,0,0,0,245,244,1,0,0,0,246,247,1,0,0,0,247,
        248,3,44,22,0,248,256,1,0,0,0,249,250,5,29,0,0,250,253,3,44,22,0,
        251,254,3,48,24,0,252,254,3,50,25,0,253,251,1,0,0,0,253,252,1,0,
        0,0,254,256,1,0,0,0,255,240,1,0,0,0,255,242,1,0,0,0,255,249,1,0,
        0,0,256,47,1,0,0,0,257,258,5,21,0,0,258,259,3,64,32,0,259,49,1,0,
        0,0,260,261,5,22,0,0,261,262,3,64,32,0,262,51,1,0,0,0,263,266,3,
        54,27,0,264,266,3,56,28,0,265,263,1,0,0,0,265,264,1,0,0,0,266,269,
        1,0,0,0,267,270,3,58,29,0,268,270,3,60,30,0,269,267,1,0,0,0,269,
        268,1,0,0,0,269,270,1,0,0,0,270,53,1,0,0,0,271,272,5,23,0,0,272,
        273,3,64,32,0,273,55,1,0,0,0,274,275,5,24,0,0,275,276,3,64,32,0,
        276,57,1,0,0,0,277,279,5,25,0,0,278,280,3,64,32,0,279,278,1,0,0,
        0,279,280,1,0,0,0,280,59,1,0,0,0,281,283,5,26,0,0,282,284,3,64,32,
        0,283,282,1,0,0,0,283,284,1,0,0,0,284,61,1,0,0,0,285,289,3,66,33,
        0,286,289,5,41,0,0,287,289,5,42,0,0,288,285,1,0,0,0,288,286,1,0,
        0,0,288,287,1,0,0,0,289,63,1,0,0,0,290,299,5,33,0,0,291,296,3,62,
        31,0,292,293,5,37,0,0,293,295,3,62,31,0,294,292,1,0,0,0,295,298,
        1,0,0,0,296,294,1,0,0,0,296,297,1,0,0,0,297,300,1,0,0,0,298,296,
        1,0,0,0,299,291,1,0,0,0,299,300,1,0,0,0,300,301,1,0,0,0,301,302,
        5,34,0,0,302,65,1,0,0,0,303,304,7,6,0,0,304,67,1,0,0,0,305,306,7,
        7,0,0,306,69,1,0,0,0,33,78,110,112,119,123,127,131,134,138,142,146,
        150,162,171,174,180,193,207,216,219,225,233,236,245,253,255,265,
        269,279,283,288,296,299
    ]

class PromQLParser ( Parser ):

    grammarFileName = "PromQLParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'^'", "'and'", "'or'", "'unless'", 
                     "'='", "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'=~'", "'!~'", "'by'", "'without'", "'on'", "'ignoring'", 
                     "'group_left'", "'group_right'", "'offset'", "'bool'", 
                     "<INVALID>", "<INVALID>", "'{'", "'}'", "'('", "')'", 
                     "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "NUMBER", "STRING", "ADD", "SUB", "MULT", 
                      "DIV", "MOD", "POW", "AND", "OR", "UNLESS", "EQ", 
                      "DEQ", "NE", "GT", "LT", "GE", "LE", "RE", "NRE", 
                      "BY", "WITHOUT", "ON", "IGNORING", "GROUP_LEFT", "GROUP_RIGHT", 
                      "OFFSET", "BOOL", "AGGREGATION_OPERATOR", "FUNCTION", 
                      "LEFT_BRACE", "RIGHT_BRACE", "LEFT_PAREN", "RIGHT_PAREN", 
                      "LEFT_BRACKET", "RIGHT_BRACKET", "COMMA", "SUBQUERY_RANGE", 
                      "TIME_RANGE", "DURATION", "METRIC_NAME", "LABEL_NAME", 
                      "WS" ]

    RULE_expression = 0
    RULE_vectorOperation = 1
    RULE_unaryOp = 2
    RULE_powOp = 3
    RULE_multOp = 4
    RULE_addOp = 5
    RULE_compareOp = 6
    RULE_andUnlessOp = 7
    RULE_orOp = 8
    RULE_vectorMatchOp = 9
    RULE_subqueryOp = 10
    RULE_offsetOp = 11
    RULE_vector = 12
    RULE_parens = 13
    RULE_instantSelector = 14
    RULE_labelMatcher = 15
    RULE_labelMatcherOperator = 16
    RULE_labelMatcherList = 17
    RULE_matrixSelector = 18
    RULE_offset = 19
    RULE_function_ = 20
    RULE_parameter = 21
    RULE_parameterList = 22
    RULE_aggregation = 23
    RULE_by = 24
    RULE_without = 25
    RULE_grouping = 26
    RULE_on_ = 27
    RULE_ignoring = 28
    RULE_groupLeft = 29
    RULE_groupRight = 30
    RULE_labelName = 31
    RULE_labelNameList = 32
    RULE_keyword = 33
    RULE_literal = 34

    ruleNames =  [ "expression", "vectorOperation", "unaryOp", "powOp", 
                   "multOp", "addOp", "compareOp", "andUnlessOp", "orOp", 
                   "vectorMatchOp", "subqueryOp", "offsetOp", "vector", 
                   "parens", "instantSelector", "labelMatcher", "labelMatcherOperator", 
                   "labelMatcherList", "matrixSelector", "offset", "function_", 
                   "parameter", "parameterList", "aggregation", "by", "without", 
                   "grouping", "on_", "ignoring", "groupLeft", "groupRight", 
                   "labelName", "labelNameList", "keyword", "literal" ]

    EOF = Token.EOF
    NUMBER=1
    STRING=2
    ADD=3
    SUB=4
    MULT=5
    DIV=6
    MOD=7
    POW=8
    AND=9
    OR=10
    UNLESS=11
    EQ=12
    DEQ=13
    NE=14
    GT=15
    LT=16
    GE=17
    LE=18
    RE=19
    NRE=20
    BY=21
    WITHOUT=22
    ON=23
    IGNORING=24
    GROUP_LEFT=25
    GROUP_RIGHT=26
    OFFSET=27
    BOOL=28
    AGGREGATION_OPERATOR=29
    FUNCTION=30
    LEFT_BRACE=31
    RIGHT_BRACE=32
    LEFT_PAREN=33
    RIGHT_PAREN=34
    LEFT_BRACKET=35
    RIGHT_BRACKET=36
    COMMA=37
    SUBQUERY_RANGE=38
    TIME_RANGE=39
    DURATION=40
    METRIC_NAME=41
    LABEL_NAME=42
    WS=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vectorOperation(self):
            return self.getTypedRuleContext(PromQLParser.VectorOperationContext,0)


        def EOF(self):
            return self.getToken(PromQLParser.EOF, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = PromQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.vectorOperation(0)
            self.state = 71
            self.match(PromQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOp(self):
            return self.getTypedRuleContext(PromQLParser.UnaryOpContext,0)


        def vectorOperation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.VectorOperationContext)
            else:
                return self.getTypedRuleContext(PromQLParser.VectorOperationContext,i)


        def vector(self):
            return self.getTypedRuleContext(PromQLParser.VectorContext,0)


        def powOp(self):
            return self.getTypedRuleContext(PromQLParser.PowOpContext,0)


        def multOp(self):
            return self.getTypedRuleContext(PromQLParser.MultOpContext,0)


        def addOp(self):
            return self.getTypedRuleContext(PromQLParser.AddOpContext,0)


        def compareOp(self):
            return self.getTypedRuleContext(PromQLParser.CompareOpContext,0)


        def andUnlessOp(self):
            return self.getTypedRuleContext(PromQLParser.AndUnlessOpContext,0)


        def orOp(self):
            return self.getTypedRuleContext(PromQLParser.OrOpContext,0)


        def vectorMatchOp(self):
            return self.getTypedRuleContext(PromQLParser.VectorMatchOpContext,0)


        def subqueryOp(self):
            return self.getTypedRuleContext(PromQLParser.SubqueryOpContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_vectorOperation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVectorOperation" ):
                listener.enterVectorOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVectorOperation" ):
                listener.exitVectorOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorOperation" ):
                return visitor.visitVectorOperation(self)
            else:
                return visitor.visitChildren(self)



    def vectorOperation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PromQLParser.VectorOperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_vectorOperation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.ADD, PromQLParser.SUB]:
                self.state = 74
                self.unaryOp()
                self.state = 75
                self.vectorOperation(8)
                pass
            elif token in [PromQLParser.NUMBER, PromQLParser.STRING, PromQLParser.AGGREGATION_OPERATOR, PromQLParser.FUNCTION, PromQLParser.LEFT_BRACE, PromQLParser.LEFT_PAREN, PromQLParser.METRIC_NAME]:
                self.state = 77
                self.vector()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 110
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = PromQLParser.VectorOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vectorOperation)
                        self.state = 80
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 81
                        self.powOp()
                        self.state = 82
                        self.vectorOperation(10)
                        pass

                    elif la_ == 2:
                        localctx = PromQLParser.VectorOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vectorOperation)
                        self.state = 84
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 85
                        self.multOp()
                        self.state = 86
                        self.vectorOperation(8)
                        pass

                    elif la_ == 3:
                        localctx = PromQLParser.VectorOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vectorOperation)
                        self.state = 88
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 89
                        self.addOp()
                        self.state = 90
                        self.vectorOperation(7)
                        pass

                    elif la_ == 4:
                        localctx = PromQLParser.VectorOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vectorOperation)
                        self.state = 92
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 93
                        self.compareOp()
                        self.state = 94
                        self.vectorOperation(6)
                        pass

                    elif la_ == 5:
                        localctx = PromQLParser.VectorOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vectorOperation)
                        self.state = 96
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 97
                        self.andUnlessOp()
                        self.state = 98
                        self.vectorOperation(5)
                        pass

                    elif la_ == 6:
                        localctx = PromQLParser.VectorOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vectorOperation)
                        self.state = 100
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 101
                        self.orOp()
                        self.state = 102
                        self.vectorOperation(4)
                        pass

                    elif la_ == 7:
                        localctx = PromQLParser.VectorOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vectorOperation)
                        self.state = 104
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 105
                        self.vectorMatchOp()
                        self.state = 106
                        self.vectorOperation(3)
                        pass

                    elif la_ == 8:
                        localctx = PromQLParser.VectorOperationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_vectorOperation)
                        self.state = 108
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 109
                        self.subqueryOp()
                        pass

             
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(PromQLParser.ADD, 0)

        def SUB(self):
            return self.getToken(PromQLParser.SUB, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_unaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)




    def unaryOp(self):

        localctx = PromQLParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not(_la==PromQLParser.ADD or _la==PromQLParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POW(self):
            return self.getToken(PromQLParser.POW, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_powOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowOp" ):
                listener.enterPowOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowOp" ):
                listener.exitPowOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowOp" ):
                return visitor.visitPowOp(self)
            else:
                return visitor.visitChildren(self)




    def powOp(self):

        localctx = PromQLParser.PowOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_powOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(PromQLParser.POW)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PromQLParser.ON or _la==PromQLParser.IGNORING:
                self.state = 118
                self.grouping()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULT(self):
            return self.getToken(PromQLParser.MULT, 0)

        def DIV(self):
            return self.getToken(PromQLParser.DIV, 0)

        def MOD(self):
            return self.getToken(PromQLParser.MOD, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_multOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultOp" ):
                listener.enterMultOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultOp" ):
                listener.exitMultOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultOp" ):
                return visitor.visitMultOp(self)
            else:
                return visitor.visitChildren(self)




    def multOp(self):

        localctx = PromQLParser.MultOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PromQLParser.MULT) | (1 << PromQLParser.DIV) | (1 << PromQLParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PromQLParser.ON or _la==PromQLParser.IGNORING:
                self.state = 122
                self.grouping()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(PromQLParser.ADD, 0)

        def SUB(self):
            return self.getToken(PromQLParser.SUB, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_addOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = PromQLParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            _la = self._input.LA(1)
            if not(_la==PromQLParser.ADD or _la==PromQLParser.SUB):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PromQLParser.ON or _la==PromQLParser.IGNORING:
                self.state = 126
                self.grouping()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEQ(self):
            return self.getToken(PromQLParser.DEQ, 0)

        def NE(self):
            return self.getToken(PromQLParser.NE, 0)

        def GT(self):
            return self.getToken(PromQLParser.GT, 0)

        def LT(self):
            return self.getToken(PromQLParser.LT, 0)

        def GE(self):
            return self.getToken(PromQLParser.GE, 0)

        def LE(self):
            return self.getToken(PromQLParser.LE, 0)

        def BOOL(self):
            return self.getToken(PromQLParser.BOOL, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_compareOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareOp" ):
                listener.enterCompareOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareOp" ):
                listener.exitCompareOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompareOp" ):
                return visitor.visitCompareOp(self)
            else:
                return visitor.visitChildren(self)




    def compareOp(self):

        localctx = PromQLParser.CompareOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_compareOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PromQLParser.DEQ) | (1 << PromQLParser.NE) | (1 << PromQLParser.GT) | (1 << PromQLParser.LT) | (1 << PromQLParser.GE) | (1 << PromQLParser.LE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PromQLParser.BOOL:
                self.state = 130
                self.match(PromQLParser.BOOL)


            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PromQLParser.ON or _la==PromQLParser.IGNORING:
                self.state = 133
                self.grouping()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndUnlessOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(PromQLParser.AND, 0)

        def UNLESS(self):
            return self.getToken(PromQLParser.UNLESS, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_andUnlessOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndUnlessOp" ):
                listener.enterAndUnlessOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndUnlessOp" ):
                listener.exitAndUnlessOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndUnlessOp" ):
                return visitor.visitAndUnlessOp(self)
            else:
                return visitor.visitChildren(self)




    def andUnlessOp(self):

        localctx = PromQLParser.AndUnlessOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_andUnlessOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            _la = self._input.LA(1)
            if not(_la==PromQLParser.AND or _la==PromQLParser.UNLESS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PromQLParser.ON or _la==PromQLParser.IGNORING:
                self.state = 137
                self.grouping()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self):
            return self.getToken(PromQLParser.OR, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_orOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrOp" ):
                listener.enterOrOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrOp" ):
                listener.exitOrOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrOp" ):
                return visitor.visitOrOp(self)
            else:
                return visitor.visitChildren(self)




    def orOp(self):

        localctx = PromQLParser.OrOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_orOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(PromQLParser.OR)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PromQLParser.ON or _la==PromQLParser.IGNORING:
                self.state = 141
                self.grouping()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorMatchOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(PromQLParser.ON, 0)

        def UNLESS(self):
            return self.getToken(PromQLParser.UNLESS, 0)

        def grouping(self):
            return self.getTypedRuleContext(PromQLParser.GroupingContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_vectorMatchOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVectorMatchOp" ):
                listener.enterVectorMatchOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVectorMatchOp" ):
                listener.exitVectorMatchOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVectorMatchOp" ):
                return visitor.visitVectorMatchOp(self)
            else:
                return visitor.visitChildren(self)




    def vectorMatchOp(self):

        localctx = PromQLParser.VectorMatchOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vectorMatchOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            _la = self._input.LA(1)
            if not(_la==PromQLParser.UNLESS or _la==PromQLParser.ON):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==PromQLParser.ON or _la==PromQLParser.IGNORING:
                self.state = 145
                self.grouping()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubqueryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBQUERY_RANGE(self):
            return self.getToken(PromQLParser.SUBQUERY_RANGE, 0)

        def offsetOp(self):
            return self.getTypedRuleContext(PromQLParser.OffsetOpContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_subqueryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubqueryOp" ):
                listener.enterSubqueryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubqueryOp" ):
                listener.exitSubqueryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubqueryOp" ):
                return visitor.visitSubqueryOp(self)
            else:
                return visitor.visitChildren(self)




    def subqueryOp(self):

        localctx = PromQLParser.SubqueryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_subqueryOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(PromQLParser.SUBQUERY_RANGE)
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 149
                self.offsetOp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OffsetOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OFFSET(self):
            return self.getToken(PromQLParser.OFFSET, 0)

        def DURATION(self):
            return self.getToken(PromQLParser.DURATION, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_offsetOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOffsetOp" ):
                listener.enterOffsetOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOffsetOp" ):
                listener.exitOffsetOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOffsetOp" ):
                return visitor.visitOffsetOp(self)
            else:
                return visitor.visitChildren(self)




    def offsetOp(self):

        localctx = PromQLParser.OffsetOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_offsetOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(PromQLParser.OFFSET)
            self.state = 153
            self.match(PromQLParser.DURATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_(self):
            return self.getTypedRuleContext(PromQLParser.Function_Context,0)


        def aggregation(self):
            return self.getTypedRuleContext(PromQLParser.AggregationContext,0)


        def instantSelector(self):
            return self.getTypedRuleContext(PromQLParser.InstantSelectorContext,0)


        def matrixSelector(self):
            return self.getTypedRuleContext(PromQLParser.MatrixSelectorContext,0)


        def offset(self):
            return self.getTypedRuleContext(PromQLParser.OffsetContext,0)


        def literal(self):
            return self.getTypedRuleContext(PromQLParser.LiteralContext,0)


        def parens(self):
            return self.getTypedRuleContext(PromQLParser.ParensContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_vector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVector" ):
                listener.enterVector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVector" ):
                listener.exitVector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVector" ):
                return visitor.visitVector(self)
            else:
                return visitor.visitChildren(self)




    def vector(self):

        localctx = PromQLParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_vector)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.function_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.aggregation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.instantSelector()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.matrixSelector()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.offset()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 160
                self.literal()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 161
                self.parens()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(PromQLParser.LEFT_PAREN, 0)

        def vectorOperation(self):
            return self.getTypedRuleContext(PromQLParser.VectorOperationContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(PromQLParser.RIGHT_PAREN, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_parens

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)




    def parens(self):

        localctx = PromQLParser.ParensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parens)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(PromQLParser.LEFT_PAREN)
            self.state = 165
            self.vectorOperation(0)
            self.state = 166
            self.match(PromQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstantSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METRIC_NAME(self):
            return self.getToken(PromQLParser.METRIC_NAME, 0)

        def LEFT_BRACE(self):
            return self.getToken(PromQLParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(PromQLParser.RIGHT_BRACE, 0)

        def labelMatcherList(self):
            return self.getTypedRuleContext(PromQLParser.LabelMatcherListContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_instantSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstantSelector" ):
                listener.enterInstantSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstantSelector" ):
                listener.exitInstantSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstantSelector" ):
                return visitor.visitInstantSelector(self)
            else:
                return visitor.visitChildren(self)




    def instantSelector(self):

        localctx = PromQLParser.InstantSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_instantSelector)
        self._la = 0 # Token type
        try:
            self.state = 180
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.METRIC_NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.match(PromQLParser.METRIC_NAME)
                self.state = 174
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 169
                    self.match(PromQLParser.LEFT_BRACE)
                    self.state = 171
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PromQLParser.AND) | (1 << PromQLParser.OR) | (1 << PromQLParser.UNLESS) | (1 << PromQLParser.BY) | (1 << PromQLParser.WITHOUT) | (1 << PromQLParser.ON) | (1 << PromQLParser.IGNORING) | (1 << PromQLParser.GROUP_LEFT) | (1 << PromQLParser.GROUP_RIGHT) | (1 << PromQLParser.OFFSET) | (1 << PromQLParser.BOOL) | (1 << PromQLParser.AGGREGATION_OPERATOR) | (1 << PromQLParser.FUNCTION) | (1 << PromQLParser.METRIC_NAME) | (1 << PromQLParser.LABEL_NAME))) != 0):
                        self.state = 170
                        self.labelMatcherList()


                    self.state = 173
                    self.match(PromQLParser.RIGHT_BRACE)


                pass
            elif token in [PromQLParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(PromQLParser.LEFT_BRACE)
                self.state = 177
                self.labelMatcherList()
                self.state = 178
                self.match(PromQLParser.RIGHT_BRACE)
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


    class LabelMatcherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelName(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameContext,0)


        def labelMatcherOperator(self):
            return self.getTypedRuleContext(PromQLParser.LabelMatcherOperatorContext,0)


        def STRING(self):
            return self.getToken(PromQLParser.STRING, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelMatcher

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelMatcher" ):
                listener.enterLabelMatcher(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelMatcher" ):
                listener.exitLabelMatcher(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelMatcher" ):
                return visitor.visitLabelMatcher(self)
            else:
                return visitor.visitChildren(self)




    def labelMatcher(self):

        localctx = PromQLParser.LabelMatcherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_labelMatcher)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.labelName()
            self.state = 183
            self.labelMatcherOperator()
            self.state = 184
            self.match(PromQLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelMatcherOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(PromQLParser.EQ, 0)

        def NE(self):
            return self.getToken(PromQLParser.NE, 0)

        def RE(self):
            return self.getToken(PromQLParser.RE, 0)

        def NRE(self):
            return self.getToken(PromQLParser.NRE, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelMatcherOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelMatcherOperator" ):
                listener.enterLabelMatcherOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelMatcherOperator" ):
                listener.exitLabelMatcherOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelMatcherOperator" ):
                return visitor.visitLabelMatcherOperator(self)
            else:
                return visitor.visitChildren(self)




    def labelMatcherOperator(self):

        localctx = PromQLParser.LabelMatcherOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_labelMatcherOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PromQLParser.EQ) | (1 << PromQLParser.NE) | (1 << PromQLParser.RE) | (1 << PromQLParser.NRE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelMatcherListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labelMatcher(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.LabelMatcherContext)
            else:
                return self.getTypedRuleContext(PromQLParser.LabelMatcherContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PromQLParser.COMMA)
            else:
                return self.getToken(PromQLParser.COMMA, i)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelMatcherList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelMatcherList" ):
                listener.enterLabelMatcherList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelMatcherList" ):
                listener.exitLabelMatcherList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelMatcherList" ):
                return visitor.visitLabelMatcherList(self)
            else:
                return visitor.visitChildren(self)




    def labelMatcherList(self):

        localctx = PromQLParser.LabelMatcherListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_labelMatcherList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.labelMatcher()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PromQLParser.COMMA:
                self.state = 189
                self.match(PromQLParser.COMMA)
                self.state = 190
                self.labelMatcher()
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixSelectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instantSelector(self):
            return self.getTypedRuleContext(PromQLParser.InstantSelectorContext,0)


        def TIME_RANGE(self):
            return self.getToken(PromQLParser.TIME_RANGE, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_matrixSelector

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixSelector" ):
                listener.enterMatrixSelector(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixSelector" ):
                listener.exitMatrixSelector(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixSelector" ):
                return visitor.visitMatrixSelector(self)
            else:
                return visitor.visitChildren(self)




    def matrixSelector(self):

        localctx = PromQLParser.MatrixSelectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_matrixSelector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.instantSelector()
            self.state = 197
            self.match(PromQLParser.TIME_RANGE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OffsetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instantSelector(self):
            return self.getTypedRuleContext(PromQLParser.InstantSelectorContext,0)


        def OFFSET(self):
            return self.getToken(PromQLParser.OFFSET, 0)

        def DURATION(self):
            return self.getToken(PromQLParser.DURATION, 0)

        def matrixSelector(self):
            return self.getTypedRuleContext(PromQLParser.MatrixSelectorContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_offset

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOffset" ):
                listener.enterOffset(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOffset" ):
                listener.exitOffset(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOffset" ):
                return visitor.visitOffset(self)
            else:
                return visitor.visitChildren(self)




    def offset(self):

        localctx = PromQLParser.OffsetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_offset)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 199
                self.instantSelector()
                self.state = 200
                self.match(PromQLParser.OFFSET)
                self.state = 201
                self.match(PromQLParser.DURATION)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.matrixSelector()
                self.state = 204
                self.match(PromQLParser.OFFSET)
                self.state = 205
                self.match(PromQLParser.DURATION)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(PromQLParser.FUNCTION, 0)

        def LEFT_PAREN(self):
            return self.getToken(PromQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PromQLParser.RIGHT_PAREN, 0)

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PromQLParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PromQLParser.COMMA)
            else:
                return self.getToken(PromQLParser.COMMA, i)

        def getRuleIndex(self):
            return PromQLParser.RULE_function_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_" ):
                listener.enterFunction_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_" ):
                listener.exitFunction_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_" ):
                return visitor.visitFunction_(self)
            else:
                return visitor.visitChildren(self)




    def function_(self):

        localctx = PromQLParser.Function_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_function_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(PromQLParser.FUNCTION)
            self.state = 210
            self.match(PromQLParser.LEFT_PAREN)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PromQLParser.NUMBER) | (1 << PromQLParser.STRING) | (1 << PromQLParser.ADD) | (1 << PromQLParser.SUB) | (1 << PromQLParser.AGGREGATION_OPERATOR) | (1 << PromQLParser.FUNCTION) | (1 << PromQLParser.LEFT_BRACE) | (1 << PromQLParser.LEFT_PAREN) | (1 << PromQLParser.METRIC_NAME))) != 0):
                self.state = 211
                self.parameter()
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PromQLParser.COMMA:
                    self.state = 212
                    self.match(PromQLParser.COMMA)
                    self.state = 213
                    self.parameter()
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 221
            self.match(PromQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(PromQLParser.LiteralContext,0)


        def vectorOperation(self):
            return self.getTypedRuleContext(PromQLParser.VectorOperationContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = PromQLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_parameter)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.vectorOperation(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(PromQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PromQLParser.RIGHT_PAREN, 0)

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.ParameterContext)
            else:
                return self.getTypedRuleContext(PromQLParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PromQLParser.COMMA)
            else:
                return self.getToken(PromQLParser.COMMA, i)

        def getRuleIndex(self):
            return PromQLParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = PromQLParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(PromQLParser.LEFT_PAREN)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PromQLParser.NUMBER) | (1 << PromQLParser.STRING) | (1 << PromQLParser.ADD) | (1 << PromQLParser.SUB) | (1 << PromQLParser.AGGREGATION_OPERATOR) | (1 << PromQLParser.FUNCTION) | (1 << PromQLParser.LEFT_BRACE) | (1 << PromQLParser.LEFT_PAREN) | (1 << PromQLParser.METRIC_NAME))) != 0):
                self.state = 228
                self.parameter()
                self.state = 233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PromQLParser.COMMA:
                    self.state = 229
                    self.match(PromQLParser.COMMA)
                    self.state = 230
                    self.parameter()
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 238
            self.match(PromQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATION_OPERATOR(self):
            return self.getToken(PromQLParser.AGGREGATION_OPERATOR, 0)

        def parameterList(self):
            return self.getTypedRuleContext(PromQLParser.ParameterListContext,0)


        def by(self):
            return self.getTypedRuleContext(PromQLParser.ByContext,0)


        def without(self):
            return self.getTypedRuleContext(PromQLParser.WithoutContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_aggregation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregation" ):
                listener.enterAggregation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregation" ):
                listener.exitAggregation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregation" ):
                return visitor.visitAggregation(self)
            else:
                return visitor.visitChildren(self)




    def aggregation(self):

        localctx = PromQLParser.AggregationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_aggregation)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(PromQLParser.AGGREGATION_OPERATOR)
                self.state = 241
                self.parameterList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(PromQLParser.AGGREGATION_OPERATOR)
                self.state = 245
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PromQLParser.BY]:
                    self.state = 243
                    self.by()
                    pass
                elif token in [PromQLParser.WITHOUT]:
                    self.state = 244
                    self.without()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 247
                self.parameterList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 249
                self.match(PromQLParser.AGGREGATION_OPERATOR)
                self.state = 250
                self.parameterList()
                self.state = 253
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [PromQLParser.BY]:
                    self.state = 251
                    self.by()
                    pass
                elif token in [PromQLParser.WITHOUT]:
                    self.state = 252
                    self.without()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ByContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(PromQLParser.BY, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_by

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBy" ):
                listener.enterBy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBy" ):
                listener.exitBy(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBy" ):
                return visitor.visitBy(self)
            else:
                return visitor.visitChildren(self)




    def by(self):

        localctx = PromQLParser.ByContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_by)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(PromQLParser.BY)
            self.state = 258
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WithoutContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITHOUT(self):
            return self.getToken(PromQLParser.WITHOUT, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_without

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithout" ):
                listener.enterWithout(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithout" ):
                listener.exitWithout(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWithout" ):
                return visitor.visitWithout(self)
            else:
                return visitor.visitChildren(self)




    def without(self):

        localctx = PromQLParser.WithoutContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_without)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(PromQLParser.WITHOUT)
            self.state = 261
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def on_(self):
            return self.getTypedRuleContext(PromQLParser.On_Context,0)


        def ignoring(self):
            return self.getTypedRuleContext(PromQLParser.IgnoringContext,0)


        def groupLeft(self):
            return self.getTypedRuleContext(PromQLParser.GroupLeftContext,0)


        def groupRight(self):
            return self.getTypedRuleContext(PromQLParser.GroupRightContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_grouping

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrouping" ):
                listener.enterGrouping(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrouping" ):
                listener.exitGrouping(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrouping" ):
                return visitor.visitGrouping(self)
            else:
                return visitor.visitChildren(self)




    def grouping(self):

        localctx = PromQLParser.GroupingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_grouping)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.ON]:
                self.state = 263
                self.on_()
                pass
            elif token in [PromQLParser.IGNORING]:
                self.state = 264
                self.ignoring()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.GROUP_LEFT]:
                self.state = 267
                self.groupLeft()
                pass
            elif token in [PromQLParser.GROUP_RIGHT]:
                self.state = 268
                self.groupRight()
                pass
            elif token in [PromQLParser.NUMBER, PromQLParser.STRING, PromQLParser.ADD, PromQLParser.SUB, PromQLParser.AGGREGATION_OPERATOR, PromQLParser.FUNCTION, PromQLParser.LEFT_BRACE, PromQLParser.LEFT_PAREN, PromQLParser.METRIC_NAME]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class On_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON(self):
            return self.getToken(PromQLParser.ON, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_on_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn_" ):
                listener.enterOn_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn_" ):
                listener.exitOn_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOn_" ):
                return visitor.visitOn_(self)
            else:
                return visitor.visitChildren(self)




    def on_(self):

        localctx = PromQLParser.On_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_on_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(PromQLParser.ON)
            self.state = 272
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGNORING(self):
            return self.getToken(PromQLParser.IGNORING, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_ignoring

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnoring" ):
                listener.enterIgnoring(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnoring" ):
                listener.exitIgnoring(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnoring" ):
                return visitor.visitIgnoring(self)
            else:
                return visitor.visitChildren(self)




    def ignoring(self):

        localctx = PromQLParser.IgnoringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ignoring)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(PromQLParser.IGNORING)
            self.state = 275
            self.labelNameList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupLeftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP_LEFT(self):
            return self.getToken(PromQLParser.GROUP_LEFT, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_groupLeft

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupLeft" ):
                listener.enterGroupLeft(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupLeft" ):
                listener.exitGroupLeft(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupLeft" ):
                return visitor.visitGroupLeft(self)
            else:
                return visitor.visitChildren(self)




    def groupLeft(self):

        localctx = PromQLParser.GroupLeftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_groupLeft)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(PromQLParser.GROUP_LEFT)
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 278
                self.labelNameList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupRightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP_RIGHT(self):
            return self.getToken(PromQLParser.GROUP_RIGHT, 0)

        def labelNameList(self):
            return self.getTypedRuleContext(PromQLParser.LabelNameListContext,0)


        def getRuleIndex(self):
            return PromQLParser.RULE_groupRight

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroupRight" ):
                listener.enterGroupRight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroupRight" ):
                listener.exitGroupRight(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupRight" ):
                return visitor.visitGroupRight(self)
            else:
                return visitor.visitChildren(self)




    def groupRight(self):

        localctx = PromQLParser.GroupRightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_groupRight)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(PromQLParser.GROUP_RIGHT)
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 282
                self.labelNameList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyword(self):
            return self.getTypedRuleContext(PromQLParser.KeywordContext,0)


        def METRIC_NAME(self):
            return self.getToken(PromQLParser.METRIC_NAME, 0)

        def LABEL_NAME(self):
            return self.getToken(PromQLParser.LABEL_NAME, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelName" ):
                listener.enterLabelName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelName" ):
                listener.exitLabelName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelName" ):
                return visitor.visitLabelName(self)
            else:
                return visitor.visitChildren(self)




    def labelName(self):

        localctx = PromQLParser.LabelNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_labelName)
        try:
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PromQLParser.AND, PromQLParser.OR, PromQLParser.UNLESS, PromQLParser.BY, PromQLParser.WITHOUT, PromQLParser.ON, PromQLParser.IGNORING, PromQLParser.GROUP_LEFT, PromQLParser.GROUP_RIGHT, PromQLParser.OFFSET, PromQLParser.BOOL, PromQLParser.AGGREGATION_OPERATOR, PromQLParser.FUNCTION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.keyword()
                pass
            elif token in [PromQLParser.METRIC_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.match(PromQLParser.METRIC_NAME)
                pass
            elif token in [PromQLParser.LABEL_NAME]:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.match(PromQLParser.LABEL_NAME)
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


    class LabelNameListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_PAREN(self):
            return self.getToken(PromQLParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PromQLParser.RIGHT_PAREN, 0)

        def labelName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PromQLParser.LabelNameContext)
            else:
                return self.getTypedRuleContext(PromQLParser.LabelNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PromQLParser.COMMA)
            else:
                return self.getToken(PromQLParser.COMMA, i)

        def getRuleIndex(self):
            return PromQLParser.RULE_labelNameList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelNameList" ):
                listener.enterLabelNameList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelNameList" ):
                listener.exitLabelNameList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelNameList" ):
                return visitor.visitLabelNameList(self)
            else:
                return visitor.visitChildren(self)




    def labelNameList(self):

        localctx = PromQLParser.LabelNameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_labelNameList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(PromQLParser.LEFT_PAREN)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PromQLParser.AND) | (1 << PromQLParser.OR) | (1 << PromQLParser.UNLESS) | (1 << PromQLParser.BY) | (1 << PromQLParser.WITHOUT) | (1 << PromQLParser.ON) | (1 << PromQLParser.IGNORING) | (1 << PromQLParser.GROUP_LEFT) | (1 << PromQLParser.GROUP_RIGHT) | (1 << PromQLParser.OFFSET) | (1 << PromQLParser.BOOL) | (1 << PromQLParser.AGGREGATION_OPERATOR) | (1 << PromQLParser.FUNCTION) | (1 << PromQLParser.METRIC_NAME) | (1 << PromQLParser.LABEL_NAME))) != 0):
                self.state = 291
                self.labelName()
                self.state = 296
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PromQLParser.COMMA:
                    self.state = 292
                    self.match(PromQLParser.COMMA)
                    self.state = 293
                    self.labelName()
                    self.state = 298
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 301
            self.match(PromQLParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(PromQLParser.AND, 0)

        def OR(self):
            return self.getToken(PromQLParser.OR, 0)

        def UNLESS(self):
            return self.getToken(PromQLParser.UNLESS, 0)

        def BY(self):
            return self.getToken(PromQLParser.BY, 0)

        def WITHOUT(self):
            return self.getToken(PromQLParser.WITHOUT, 0)

        def ON(self):
            return self.getToken(PromQLParser.ON, 0)

        def IGNORING(self):
            return self.getToken(PromQLParser.IGNORING, 0)

        def GROUP_LEFT(self):
            return self.getToken(PromQLParser.GROUP_LEFT, 0)

        def GROUP_RIGHT(self):
            return self.getToken(PromQLParser.GROUP_RIGHT, 0)

        def OFFSET(self):
            return self.getToken(PromQLParser.OFFSET, 0)

        def BOOL(self):
            return self.getToken(PromQLParser.BOOL, 0)

        def AGGREGATION_OPERATOR(self):
            return self.getToken(PromQLParser.AGGREGATION_OPERATOR, 0)

        def FUNCTION(self):
            return self.getToken(PromQLParser.FUNCTION, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_keyword

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeyword" ):
                listener.enterKeyword(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeyword" ):
                listener.exitKeyword(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyword" ):
                return visitor.visitKeyword(self)
            else:
                return visitor.visitChildren(self)




    def keyword(self):

        localctx = PromQLParser.KeywordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_keyword)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << PromQLParser.AND) | (1 << PromQLParser.OR) | (1 << PromQLParser.UNLESS) | (1 << PromQLParser.BY) | (1 << PromQLParser.WITHOUT) | (1 << PromQLParser.ON) | (1 << PromQLParser.IGNORING) | (1 << PromQLParser.GROUP_LEFT) | (1 << PromQLParser.GROUP_RIGHT) | (1 << PromQLParser.OFFSET) | (1 << PromQLParser.BOOL) | (1 << PromQLParser.AGGREGATION_OPERATOR) | (1 << PromQLParser.FUNCTION))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(PromQLParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(PromQLParser.STRING, 0)

        def getRuleIndex(self):
            return PromQLParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = PromQLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            _la = self._input.LA(1)
            if not(_la==PromQLParser.NUMBER or _la==PromQLParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.vectorOperation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def vectorOperation_sempred(self, localctx:VectorOperationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         




