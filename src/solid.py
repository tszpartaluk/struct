import elements


class SolidModule(object):

    def __init__(self, E, nu):
        self.E = E
        self.nu = nu
        self.asmMap = {"Triangle": self.assembleStiffnessTriangle}


    def assembleStiffnessMatrix(self, grid):
        for el in grid.Elements:
            self.asmMap[el.name](el)

    def assembleStiffnessTriangle(self, ob):

        print("Triangle Assemblation")
        pass


if __name__ == "__main__":
    
    
    from mesh import Mesh
    import elements as elem
    import numpy as np

    a = Mesh()

    a.dim = 2

    tris = elem.Triangle(order=1)
    a.Elements.append(tris)

    a.Points = np.array([[0,0],[1,0],[1,1]])

    tris.elementArray = np.array([[0,1,2]],dtype=int,ndmin=2)

    m = SolidModule(2e5,0.3)
    m.assembleStiffnessMatrix(a)

