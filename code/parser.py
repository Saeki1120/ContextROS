from pyparsing import \
   Literal, Word, ZeroOrMore, Group, Dict, Optional, \
   printables, ParseException, restOfLine, alphas, alphanums, Keyword, \
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
variable = Word(alphas, alphanums+'_')
# pattern (not implemented)
pattern = variable
# function_name pattern...

function_name = ZeroOrMore(pattern)
# function function_name(){ codes }
##function =  Group(function_name + lpar + SkipTo('}') + rbrace)

#argument_list
argument_list = function_name + ZeroOrMore(',' + function_name)

# argument (pattern...)
argument = lpar + argument_list + rpar

# code {...}
code = lbrace + SkipTo('}') + rbrace

function =  Group(Group(function_name) + Group(argument) + code)

# Layer pattern [ codes ]
Layer = Group(kLayer + pattern + lbrack + Group(ZeroOrMore(function)) + rbrack)

##Layer = kLayer + pattern + lbrack + Group(ZeroOrMore(function)) + SkipTo(']') + rbrack

# match ( variable ) { Layer... }
amatch = SkipTo(kLayer) + ZeroOrMore(Layer)

##amatch = Layer

##################################
# Test
##result = pat.parseString('long int cal()')
##print(result)




# Gen
def get_func_name(func_ast):
	l = []
	for i, kase in enumerate(func_ast):
		if kase == ',':
			l.append(func_ast[i-1])

	l.append(func_ast[-1])
	return l

def set_name(ast, layer_name):
	ast[-1] = ast[-1] + "_" + layer_name

def bind_space(ast):
	moji = ""
	for i, kast in enumerate(ast):
		if i == 0:
			moji += kast
		else:
			moji += ' ' + kast
	return moji

def bind_comma(ast):
	moji = ""
	for i, kast in enumerate(ast):
		if i == 0:
			moji += kast
		else:
			moji += ',' + kast
	return moji


def gen_func(ast, layer_name, f):
	l = []
	for i, kase in enumerate(ast):
		before_func_name = bind_space(kase[0])
		func_name_list = get_func_name(kase[1])
		set_name(kase[0], layer_name)
		#function_name = get_name(ast[0])
		#print function_name
		line1 = bind_space(kase[0])
		line2 = '(' +  bind_space(kase[1]) + ')'
		line3 = '{\n ' +  kase[2] + '}\n'

		print line1
		print line2
		print line3

		##
		f.write(line1)
		f.write(line2)
		f.write(line3)
		##

		l.append([before_func_name, bind_space(kase[1]), kase[0][-1], func_name_list, line1 + line2])

	return l


def gen_func_def(ast):
	mojiretu = ast[0] + '(' + ast[1] + ',' + "int layer_name" + ')'
	return mojiretu

def gen_if(ast):
	l = []
	for i, kase in enumerate(ast):
		#print kase
		line1 = gen_func_def(kase)
		line2 = "if (layer_name == 0) {return " + kase[2] + '(' + bind_comma(kase[3]) + ");}\n"
		#print line1
		#print line2
		l.append([kase[0], line1, line2])
	#print l
	return l


def gen_elif(ast, katamari, num):
	for i, kase in enumerate(ast):
		#print kase
		if kase[0] == katamari[i][0]:
			sen = "else if (layer_name == " + str(num) + "){return " \
				+ kase[2] + '(' + bind_comma(kase[3]) + ");}\n"
			#print sen
			katamari[i].append(sen)
		else:
			print("error")
		pass

def gen_if_sentence(ast, f):
	for kase in ast:
		print kase[1]
		print '{'

		##
		f.write(kase[1])
		f.write('{\n')
		##
		for kase2 in kase[2:]:
			print kase2
			f.write(kase2)
		print '}'
		f.write('}\n')


def gen(ast):
	l = []
	f = open("layer.cpp", "w")
	fh = open("layer.h", "w")

	f.write(' #include "layer.h"\n ')

	for i, kase in enumerate(ast[1:]):
		if kase[0] == 'Layer':
			variable = kase[1]
			#print variable
			#print kase_copy
			l.append(gen_func(kase[2], variable, f))
		else:
			print("error")
	#print l

	for i, kase in enumerate(l):
		if i == 0:
			katamari = gen_if(kase)
		else:
			gen_elif(kase, katamari, i)
	
	gen_if_sentence(katamari, f)

	print ("-----------------------------")

	## include
	fh.write("#ifndef _chapter03_layer_H_\n#define _chapter03_layer_H_\n")
	fh.write(ast[0])

	for lay in l:
		for func_l in lay:
			print func_l[-1] + ';'
			fh.write(func_l[-1] + ';\n')
	for if_sen in katamari:
		print if_sen[1] + ';'
		fh.write(if_sen[1] + ';\n')
	print ("-----------------------------")

	fh.write("#endif")	



if __name__ == '__main__':
	import sys
	with open(sys.argv[1], 'r') as fp:
		txt = fp.read()
		result = amatch.parseString(txt)
		print result

		print ("-----------------------------")

		gen(result)










