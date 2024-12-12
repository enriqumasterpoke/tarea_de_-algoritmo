"""
   dada una nota almacenada en una variable,imprime su equivalente:
.mayor o igual a 0,pero menor que 5,SUSPENSO.
.mayor o igual a 5,pero menor que 6,SUFICIENTE.
.mayor o igual a 6,pero menor que 7,BIEN.
.mayor o igual a 7,pero menor que 9,NOTABLE.
.mayor o igual a 9,pero menor o igual a 10,SOBRESALIENTE.
en cualquier otro caso,imprimir el texto:NOTA NO VALIDA.
"""
nota=19
if nota>0 and nota<5:
    print("SUSPENSO")
elif nota>=5 and nota<6:
    print("SUFICIENTE")
elif nota>=6 and nota<7:
    print("BIEN")
elif nota>=7 and nota<9:
    print("NOTABLE")
elif nota>=9 and nota<=10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VALIDA")