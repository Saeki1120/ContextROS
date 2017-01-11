from pyparsing import \
   Literal, Word, ZeroOrMore, Group, Dict, Optional, \
   printables, ParseException, restOfLine, alphas, Keyword, \
   SkipTo

import copy

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
function_name = ZeroOrMore(pattern)
# function function_name(){ codes }
##function =  Group(function_name + lpar + SkipTo('}') + rbrace)

# argument (pattern...)
argument = lpar + SkipTo(')') + rpar

# code {...}
code = lbrace + SkipTo('}') + rbrace

function =  Group(Group(function_name) + argument + code)

# Layer pattern [ codes ]
Layer = Group(kLayer + pattern + lbrack + Group(ZeroOrMore(function)) + rbrack)

##Layer = kLayer + pattern + lbrack + Group(ZeroOrMore(function)) + SkipTo(']') + rbrack

# match ( variable ) { Layer... }
amatch = ZeroOrMore(Layer)

##amatch = Layer

##################################
# Test
##result = pat.parseString('long int cal()')
##print(result)




# Gen
def get_func_name(func_ast):
	return func_ast[0]

def set_name(ast, layer_name):
	ast[-1] = ast[-1] + "_" + layer_name

def bind_space(ast):
	moji = ""
	for kast in ast:
		moji += kast + " "
	return moji



def gen_func(ast, layer_name):
	l = []
	for i, kase in enumerate(ast):
		before_func_name = bind_space(kase[0])
		set_name(kase[0], layer_name)
		#function_name = get_name(ast[0])
		#print function_name
		line1 = bind_space(kase[0])
		line2 = '(' +  kase[1] + ')'
		line3 = '{' +  kase[2] + '}'
		print line1
		print line2
		print line3
		l.append([line1, line2])

	return l


def gen_if_sentence(ast, function_name):
	for i, kase in enumerate(ast):
		if kase[0] == 'Layer':
			variable = kase[1]
			#print variable
			before_func_name = bind_space(kase[2][0])
			l.append(layers(kase[2], variable))
		else:
			print("error")

	print l
	print before_func_name
	print ast


def gen(ast):
	l = []
	for i, kase in enumerate(ast):
		if kase[0] == 'Layer':
			variable = kase[1]
			#print variable
			#print kase_copy
			l.append(gen_func(kase[2], variable))
		else:
			print("error")
	print l
	#print function_name.parseString(before_func_name)


if __name__ == '__main__':
	import sys
	with open(sys.argv[1], 'r') as fp:
		txt = fp.read()
		result = amatch.parseString(txt)
		print result

		print ("-----------------------------")

		gen(result)








