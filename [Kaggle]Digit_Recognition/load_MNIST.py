import numpy
import csv

def load_MNIST(filename_train='train.csv', filename_test='test.csv'):
    """ Load all of MNIST dataset. MNIST dataset is composed of 60,000 examples
        and a test set of 10,000 examples. The original black and white bilavel
        images from NIST were size normalized to fit in a 20x20 pixel box while
        preserving their aspect ratio. The resulting images contain grey levels
        as a result of the anti-aliasing technique used by the normolization
        algorithm. The images were centerd in a 28x28 by computing center of
        mass of the pixels, and translating so as to position this point at the
        center of the 28x28 field.
    """
    # Load training data
    reader = csv.reader(open(filename_train,"rb"), delimiter=',')
    reader.next()
    x = list(reader)

    xs = []
    ys = []
    for i in xrange(len(x)):
        ys.append([x[i][0]])
        xs.append(x[i][1:])
    Xtr = numpy.array(xs)
    Ytr = numpy.array(ys)

    # Load test data
    reader = csv.reader(open(filename,test,"rb"), delimiter=',')
    reader.next()
    x = list(reader)
    xs = []
    ys = []
    for i in xrange(len(x)):
        ys.append([x[i][0]])
        xs.append(x[i][1:])
    Xte = numpy.array(xs)
    Yte = numpy.array(ys)

    return Xtr,Ytr,Xte,Yte

if __name__ == '__main__':
    Xtr, Ytr, Xte, Yte = load_MNIST()
