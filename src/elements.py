from matplotlib import pyplot as plt


class ElementBase(object):
    def __init__(self, order=1):
        self.elementArray = []
        self.globalIndices = []
        pass

    def plot(self):
        raise NotImplementedError

    def name(self):
        return self.name


class Element2D(ElementBase):
    def __init__(self, order=1):
        super().__init__(order=order)
    pass

    def plot(self):
        raise NotImplementedError


class Element3D(ElementBase):
    def __init__(self, order=1):
        super().__init__(order=order)
    pass

    def plot(self):
        raise NotImplementedError


class Tetra(Element3D):
    def __init__(self, order=1):
        super().__init__(order=order)
        pass

    def plot(self, coords, axis=plt.gca()):
        #
        # draw draw draw
        
        pass


class Triangle(Element2D):
    def __init__(self, order=1):
        super().__init__(order=order)
        self.name = 'Triangle'
    pass

    def plot(self, coords, ax):

        #from matplotlib.patches import Circle, Wedge, Polygon
        #from mpl_toolkits.mplot3d.art3d import Poly3DCollection
        #from mpl_toolkits.mplot3d import Axes3D
        import numpy as np
        
        #pol = Polygon()

        tris = np.array([[[]]], ndimn=3)

        for el in np.nditer(self.elementArray, flags=['external_loop'], order='C'):

            verts = coords[el, :]
            ax.add_collection3d(Poly3DCollection(verts))
            print(verts)

        pass
