premio = float(input("Digite o valor do premio: "))
imposto = (7 / 100)
premio2 = (premio * imposto)
premiofinal = (premio - premio2)
primeirodescont = (32/100)
amg1 = (premiofinal * primeirodescont)
segundodescont = (46/100)
amg2 = (premiofinal * segundodescont)
terceirodescont = (22/100)
amg3 = (premiofinal * terceirodescont)
print("O premio com o imposto descontado ficará:", premiofinal,".O primeiro amigo receberá:", amg1,".O segundo amigo receberá:", amg2,".e o terceiro:", amg3)


