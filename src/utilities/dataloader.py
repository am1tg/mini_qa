# author : Amit_g


def load_data(fname):
    f = open(fname, 'r')
    doc = f.read()
    f.close()
    return doc