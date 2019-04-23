import numpy as np
import elements as elem
import matplotlib.pyplot as plt


class Mesh(object):
    
    def __init__(self):
        self.dim = 0
        self.nodes = np.array([], dtype=int)

        self.Points = []
        self.Elements = []
        pass

    def importGmsh(self, filename):

        pass
    
    def display(self):
        pass

    def plot(self):

        for el in self.Elements:
            el.plot(coords=self.Points,ax=plt.gca())

        plt.draw()
        pass


if __name__ == "__main__":
    pass

    a = Mesh()

    a.dim = 2

    #a.Elements.append(ElementOwner2D(type='Hex'))

    tris = elem.Triangle(order=1)
    a.Elements.append(tris)

    a.Points = np.array([[0,0],[1,0],[1,1]])

    tris.elementArray = np.array([[0,1,2]],dtype=int,ndmin=2)

    a.plot()
