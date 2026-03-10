import statistics as st
#leitura
lote1 = float(input('Produção do lote 1: '))
lote2 = float(input('Produção do lote 2: '))
lote3 = float(input('Produção do lote 3: '))
#processamento
media = st.mean((lote1, lote2, lote3))
desvio = st.stdev((lote1, lote2, lote3))
#saída
print (f'Média {media:.2f}')
print (f'Desvio padrão {desvio:.2f}')