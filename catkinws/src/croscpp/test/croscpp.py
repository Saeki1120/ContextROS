import sys
from textx.metamodel import metamodel_from_str
from jinja2 import Environment, FileSystemLoader


layersm = metamodel_from_str("P:'@layers' '=' '[' layers*=ID[','] ']';")
# it cannot deal with pointers as a ret val.
methodm = metamodel_from_str("P:'@base' ret=ID name=ID args=/[^;]+/';';")
classm = metamodel_from_str("P:'class' name=ID;")


def read_hl(lines):
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


def gen_body(layers, decls, file):
    env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
    tmpl = env.get_template('ccpp_gen.tmpl')
    return tmpl.render(layers=layers, methods=decls, file=file)


def gen_header(lines, layers, decls):
    def find_decl(klass, method):
        for d in decls:
            if d.current_class == klass and d.name == method:
                return d
        return False

    gen = []
    current_class = ''

    for line in lines:
        if '@layers' in line:
            pass
        elif 'class' in line:
            gen.append(line)
            m = classm.model_from_str(line)
            current_class = m.name
        elif '@base' in line:
            m = methodm.model_from_str(line)
            d = find_decl(current_class, m.name)

            gen.append(d.ret + ' ' + d.name + d.args + ';\n')
            for l in layers:
                gen.append(d.ret + ' ' + d.name + '_' + l + d.args + ';\n')
        else:
            gen.append(line)
    return gen


# arg check
if len(sys.argv) != 2:
    print('Usage: python %s file' % sys.argv[0])
    quit()

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    layers, decls = read_hl(lines)

with open(sys.argv[1][:-3] + '_gen.cpp', 'w') as f:
    f.write(gen_body(layers, decls, sys.argv[1][:-1]))

with open(sys.argv[1][:-3] + '.h', 'w') as f:
    lines = gen_header(lines, layers, decls)
    for l in lines:
        f.write(l)
