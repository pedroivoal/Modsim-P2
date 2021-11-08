def retorno_bovespa(di, df):

    with open('bovespa.csv', 'r') as arq:
        bovespa = arq.read()

    if di not in bovespa or df not in bovespa:
        return 'sem dados'
    else:
        bovespa_ls = bovespa.split('\n')
        for bovespa_l in bovespa_ls:
            bovespa_e = bovespa_l.split(',')
            if di == bovespa_e[0]:
                Fi = float(bovespa_e[4])
                break
        for bovespa_l in bovespa_ls:
            bovespa_e = bovespa_l.split(',')
            if df == bovespa_e[0]:
                Ff = float(bovespa_e[4])
                break

        retorno = (Ff - Fi)/Fi

        return retorno

print(retorno_bovespa('2020-10-26', '2020-10-28'))
print((95369 - 101017)/101017)