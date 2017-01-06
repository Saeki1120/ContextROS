from pyparsing import \
   Literal, Word, ZeroOrMore, Group, Dict, Optional, \
   printables, ParseException, restOfLine, alphas, Keyword, \
   SkipTo

# import pypatt # requires python 2, but did not use

##################################
# Literals
lbrack = Literal("[").suppress()
rbrack = Literal("]").suppress()
lpar = Literal("(").suppress()
rpar = Literal(")").suppress()
lbrace = Literal("{").suppress()
rbrace = Literal("}").suppress()

##################################
# Keywords
kLayer = Keyword('Layer')
##kmatch = Keyword('match')

##################################
# Syntax Rules

# variable (not implemented)
variable = Word(alphas)
# pattern (not implemented)
pattern = variable
# function_name pattern...
function_name = Group(ZeroOrMore(pattern))
# function function_name(){ codes }
function =  Group(function_name+ lpar + SkipTo('}') + rbrace)
# Layer pattern [ codes ]
Layer = Group(kLayer + pattern + lbrack + ZeroOrMore(function) + SkipTo(']') + rbrack)
# match ( variable ) { Layer... }
amatch = ZeroOrMore(Layer)

##################################
# Test
##result = pat.parseString('long int cal()')
##print(result)

if __name__ == '__main__':
	import sys
	with open(sys.argv[1], 'r') as fp:
		txt = fp.read()
		print amatch.parseString(txt)

		



