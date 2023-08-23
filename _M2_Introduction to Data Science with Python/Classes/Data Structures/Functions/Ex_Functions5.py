def addcar1(model, year, license, /, brand, motor, fuel):
    print(model, year, license, brand, motor, fuel)

addcar1('Palio', '1999', 'XVY2511', brand='Fiat', motor='1.0', fuel='flex')
addcar1('Palio', '1999', 'XVY2511', 'Fiat', '1.0', 'flex')
# addcar1(model='Palio', year='1999', license='XVY2511', brand='Fiat', motor='1.0', fuel='flex')

print('----------------------------------------------------------')

def addcar2(*,model, year, license, brand, motor, fuel):
    print(model, year, license, brand, motor, fuel)


addcar2(model='Palio', year='1999', license='XVY2511', brand='Fiat', motor='1.0', fuel='flex')
# addcar2('Palio', '1999', 'XVY2511', brand='Fiat', motor='1.0', fuel='flex')
# addcar2('Palio', '1999', 'XVY2511', 'Fiat', '1.0', 'flex')

print('----------------------------------------------------------')

def addcar3(model, year, license, /, *, brand, motor, fuel):
    print(model, year, license, brand, motor, fuel)

addcar3('Palio', '1999', 'XVY2511', brand='Fiat', motor='1.0', fuel='flex')
addcar3('Palio', '1999', 'XVY2511', 'Fiat', '1.0', 'flex')