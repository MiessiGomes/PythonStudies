Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 10
10
>>> type(10)
<class 'int'>
>>> type("tudo bem?")
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type('true')
<class 'str'>
>>> type(5/2)
<class 'float'>
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> 10 % 3
1
>>> peso = 78
>>> altura = 1.83
>>> peso
78
>>> type(altura)
<class 'float'>
>>> altura
1.83
>>> IMC = peso / altura
>>> IMC = peso / (altura ** 2)
>>> IMC
23.291229956104985
>>> IMCInteiro = int(IMC)
>>> 
>>> 
>>> 
>>> 
>>> IMCInteiro
23
>>> 
>>> 
>>> 

>>> 

>>> textp = "bom dia, tudo bem ?"
>>> texto = "bom dia, tudo bem ?"
>>> texto
'bom dia, tudo bem ?'
>>> len(texto)
19
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> temp = str(texto)
>>> temp
'bom dia, tudo bem ?'
>>> 
>>> 
>>> 
>>> temp = str(IMC)
>>> temp
'23.291229956104985'
>>> len(temp)
18
>>> 
>>> 
>>> 
>>> 
>>> 
>>> len(str(IMC))
18
>>> 10 / 2
5.0
>>> cumprimento = "Olá"
>>> nome = "Ana"
>>> turno = "bom dia"
>>> print(len(cumprimento+nome+turno))
13
>>> 22 % 3
1
>>> 10 / 6
1.6666666666666667
>>> 10 // 6
1
>>> 2 * 1 ** 2
2
>>> 2*1**2
2
>>> 2**2
4
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 

>>> 

>>> 
>>> x = 10.5
>>> int(x)
10
>>> y = "tudo bem?"
>>> y
'tudo bem?'
>>> x + y
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    x + y
TypeError: unsupported operand type(s) for +: 'float' and 'str'
>>> cumprimento
'Olá'
>>> nome
'Ana'
>>> turno
'bom dia'
>>> len(cumprimento)+len(nome)+len(turno)
13
>>> 
>>> 
>>> tamanho = len(cumprimento) + len(nome) + len(turno)
>>> tamanho
13
>>> 22 % 3
1
>>> 