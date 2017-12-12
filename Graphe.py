class Sommet :
    """
    - nomStation
    - ...
    """

    def __init__(self):
        self.nomStation = "default"

class Arc :
    """
    - sommet1
    - sommet2
    """

    def __init__(self, sommet1, sommet2):
        self.sommet1 = sommet1
        self.sommet2 = sommet2

