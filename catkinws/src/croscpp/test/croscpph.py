import sys
from textx.metamodel import metamodel_from_str
from jinja2 import Environment, FileSystemLoader


def read_hl(lines):
    layersm = metamodel_from_str("P:'@layers' '=' '[' layers*=ID[','] ']';")
    # it cannot deal with pointers as a ret val.
    methodm = metamodel_from_str("P:'@base' ret=ID name=ID args=/[^;]+/';';")
    classm = metamodel_from_str("P:'class' name=ID;")

    layers = False
    decls = []
    current_class = ''

    for line in lines:
        if '@layers' in line:
            m = layersm.model_from_str(line)
            layers = m.layers

        if 'class' in line:
            m = classm.model_from_str(line)
            current_class = m.name

        if '@base' in line:
            m = methodm.model_from_str(line)
            m.current_class = current_class
            decls.append(m)

    return layers, decls


def gen(layers, decls, file):
    env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
    tmpl = env.get_template('ccpp_gen.tmpl')
    return tmpl.render(layers=layers, methods=decls, file=file)


# arg check
if len(sys.argv) != 2:
    print('Usage: python %s file' % sys.argv[0])
    quit()

with open(sys.argv[1], 'r') as f:
    layers, decls = read_hl(f.readlines())

with open(sys.argv[1][:-3] + '_gen.cpp', 'w') as f:
    f.write(gen(layers, decls, sys.argv[1][:-1]))
