


nota_1 = float(input("Qual a nota 1?"))
nota_2 = float(input("Qual a nota 2?"))
nota_3 = float(input("Qual a nota 3?"))
nota_final = (nota_1+nota_2+nota_3)/3
aproveitamento = (nota_final)*10
nota_maxima = 10
if nota_final > nota_maxima:
    print("algumas de suas notas foram digitadas incorretamente sua nota 1 foi {}, sua nota 2 foi {},sua nota 3 foi {}, verifique qual nota foi digitada maior que a nota maxima permitida, nota maxima:{}".format(nota_1,nota_2,nota_3,nota_maxima))
elif nota_final == 10:
    print("Parabéns você foi muito bem!!, sua nota foi {} e seu aproveitamento foi {}%".format(nota_final,aproveitamento))
elif nota_final == 9:
    print("Parabéns você foi muito bem!!, sua nota foi {} e seu aproveitamento foi {}%".format(nota_final,aproveitamento))
elif nota_final == 8:
    print("você foi aprovado, porem passou raspando, estude mais da proxima para passar com tranquilidade, sua nota foi {} e seu aproveitamento foi {}%".format(nota_final,aproveitamento))
elif nota_final == 7:
    print("você foi aprovado, porem passou raspando, estude mais da proxima para passar com tranquilidade, sua nota foi {} e seu aproveitamento foi {}%".format(nota_final,aproveitamento))
else:
    print("Infelizmente você foi reprovado, sua nota foi {}, mas não se preocupe, entre em contato com seu tutor,e verifique as opções de reclassificação, seu aproveitamento foi de {}%".format(nota_final,aproveitamento))






