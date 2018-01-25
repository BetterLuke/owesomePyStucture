#encoing: utf-8

def init_code(filename, init_code):
    '''create and write init code in a  file'''
    with open(filename, 'w+') as f:
        f.write(init_code)