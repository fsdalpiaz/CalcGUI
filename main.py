# creator @fsdalpíaz
# using guizero package

from guizero import *


# janela da calculadora
calcapp = App(title="Calculadora",
                  width=400,
                  height=500)

# box display
displaynumbers = Box(calcapp,
                     width=398,
                     height=100,
                     border=3)

#

calcapp.display()
