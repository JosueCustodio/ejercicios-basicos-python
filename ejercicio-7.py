print('Este programa intercambia los valores de dos variables. /n')
print('Introduce las dos variables')

var1 = input('Variable 1 >')
var2 = input('Variable 2 >')

varControl = var2
var2 = var1
var1 = varControl

print(var1, var2)