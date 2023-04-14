def somar(x,y):
    resultado=x+y
    return resultado
def subtrair(x,y):
    resultado=x-y
    return resultado
def multiplicar(x,y):
    resultado=x*y
    return resultado
def dividir(x,y):
    resultado=x/y
    return resultado    
def calcular(x,y):
    a=x**2
    b=x**y
    c=(a+b)**y
    d=x+1
    c=(y/d)+1
    resultado=int(c)/int(e)
    return resultado
a=int(input("digite A:"))
b=int(input("digite B:"))
print("a+b=",somar(a,b))
print("a-b=",subtrair(a,b))
print("a*b=",multiplicar(a,b))
print("a/b=",dividir(a,b))
print("(((a2)+(ab))^b)=",calcular(a,b))
