from neuron import h, gui
from neuron.units import um
import plotly
h.load_file("stdrun.hoc")


class Cell:
    def __int__(self):
        main = h.Section(name="main", cell=self)
        dend1 = h.Section(name="dend1", cell=self)
        dend2 = h.Section(name="dend2", cell=self)

        dend1.connect(main)
        dend2.connect(main)

        main.diam = 10
        dend1.diam = 2
        dend2.diam = 2

        # important: store the sections
        self.main = main
        self.dend1 = dend1
        self.dend2 = dend2
        self.all = main.wholetree()


myCell = Cell()
ps = h.PlotShape(False)
ps.plot(plotly).show()
