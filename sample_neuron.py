from neuron import h
soma = h.Section(name='soma')
axon = h.Section(name='axon')
dend = [h.Section(name='dend[%d]' % i) for i in range(3)]
for sec in dend:
    sec.connect(soma(1), 0)

h.topology()
s = h.Shape()