# -*- coding: utf-8 -*-
"""
    pygments.lexers.cellscript
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for Cell Script.

"""

import re

from pygments.lexer import Lexer, RegexLexer, include, bygroups, using, \
    default, words, combined, do_insertions
from pygments.util import get_bool_opt, shebang_matches
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation, Generic, Other, Error
from pygments import unistring as uni

__all__ = ['CellScriptLexer']

line_re = re.compile('.*?\n')


class CellScriptLexer(RegexLexer):
    """
    For `OpenCOR <http://www.opencor.ws>`_ CellML script code.
    """

    name = 'CellScript'
    aliases = ['cell']
    filenames = ['*.cell']

    tokens = {
        'root': [
            (r'\n', Text),
        #    (r'^(\s*)([rRuU]{,2}"""(?:.|\n)*?""")', bygroups(Text, String.Doc)),
        #    (r"^(\s*)([rRuU]{,2}'''(?:.|\n)*?''')", bygroups(Text, String.Doc)),
            (r'[^\S\n]+', Text),
            (r'//.*$', Comment.Single),
            (r'[]{}:(),;[]', Punctuation),
            (r'(pref|expo|init|pub|priv)', Name.Function),
            (r'\\\n', Text),
            (r'\\', Text),
            (r'(dimensionless)\b', Operator.Word),
            (r'!=|==|<<|>>|[-~+/*%=<>&^|.]', Operator),
            (r'L?"', String, 'string'),
            include('keywords'),
            include('builtins'),
            include('name'),
            include('numbers'),
        ],
        'keywords': [
            (words((
                'ode', 'def', 'enddef', 'model', 'comp', 'var', 'import', 'using', 'map', 'group', 
                'incl', 'between', 'vars',
                'unit', 'as',  'endcomp', 'sel', 'case', 'otherwise', 'endsel', 'and', 'or', 'for'
                ), suffix=r'\b'),
             Keyword),
        ],
        'builtins': [
            (words((
                'sqr', 'sqrt', 'ln', 'log', 'exp', 'pow',
                'sin', 'cos', 'tan', 'csc', 'sec', 'cot',
                'asin', 'acos', 'atan', 'acsc', 'asec', 'acot',
                'sinh', 'cosh', 'tanh', 'csch', 'sech', 'coth',
                'asinh', 'acosh', 'atanh', 'acsch', 'asech', 'acoth'),
                prefix=r'(?<!\.)', suffix=r'\b'),
             Name.Builtin),
            (words((
                'dimensionless'), prefix=r'(?<!\.)', suffix=r'\b'),
             Name.Exception),
        ],
        'numbers': [
            (r'([+-]{0,1}\d+\.\d*|\d*\.\d+)([eE][+-]?[0-9]+)?j?', Number.Float),
            (r'[+-]{0,1}\d+[eE][+-]?[0-9]+j?', Number.Float),
            (r'0[0-7]+j?', Number.Oct),
            (r'0[bB][01]+', Number.Bin),
            (r'0[xX][a-fA-F0-9]+', Number.Hex),
            (r'[+-]{0,1}\d+L', Number.Integer.Long),
            (r'[+-]?\d+j?', Number.Integer)
        ],
        'name': [
            (r'@[\w.]+', Name.Decorator),
            ('[a-zA-Z_]\w*', Name),
        ],
        'funcname': [
            ('[a-zA-Z_]\w*', Name.Function, '#pop')
        ],
        'classname': [
            ('[a-zA-Z_]\w*', Name.Class, '#pop')
        ],
        'string': [
            (r'"', String, '#pop'),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|'
             r'u[a-fA-F0-9]{4}|U[a-fA-F0-9]{8}|[0-7]{1,3})', String.Escape),
            (r'[^\\"\n]+', String),  # all other characters
            (r'\\\n', String),  # line continuation
            (r'\\', String),  # stray backslash
        ],
    }

