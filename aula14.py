a = 'A'
b = 'B'
c = 1.1
string = 'a = {nome1}, b = {nome2}, c = {nome3:.2f}'
formato = string.format(
    nome1 = a, nome2 = b, nome3 = c # Parâmetro nomeado - Todo e qualquer parâmetro que vier depois do nomeado, também precisa receber uma id.
)

print(formato)