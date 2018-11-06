import os
from PyPDF2 import PdfFileMerger
 
# Regional 2
path = 'D:/Regional/Regional 2/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 2.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 119

for i in range(25):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 2.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 2.pdf')
merger.close()

# Reginal 3
path = 'D:/Regional/Regional 3/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 3.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 155

for i in range(25):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 3.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 3.pdf')
merger.close()

# Regional 4
path = 'D:/Regional/Regional 4/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 4.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 200

for i in range(16):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 4.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 4.pdf')
merger.close()

# Regional 5
path = 'D:/Regional/Regional 5/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 5.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 213

for i in range(25):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 5.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 5.pdf')
merger.close()

# Regional 6
path = 'D:/Regional/Regional 6/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 6.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 235

for i in range(6):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 6.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 6.pdf')
merger.close()


# Regional 7
path = 'D:/Regional/Regional 7/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 7.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 238

for i in range(9):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 7.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 7.pdf')
merger.close()


# Regional 8
path = 'D:/Regional/Regional 8/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 8.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 244

for i in range(16):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 8.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 8.pdf')
merger.close()

# Regional 9
path = 'D:/Regional/Regional 9/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 9.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 257

for i in range(8):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 9.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 9.pdf')
merger.close()



# Regional 10
path = 'D:/Regional/Regional 10/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 10.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 17

for i in range(19):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 10.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 10.pdf')
merger.close()

# Regional 11
path = 'D:/Regional/Regional 11/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 11.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 33

for i in range(8):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 11.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 11.pdf')
merger.close()


# Regional 12
path = 'D:/Regional/Regional 12/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 12.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 38

for i in range(13):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 12.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 12.pdf')
merger.close()

# Regional 13
path = 'D:/Regional/Regional 13/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 13.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 48

for i in range(13):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 13.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 13.pdf')
merger.close()

# Regional 14
path = 'D:/Regional/Regional 14/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 14.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 58

for i in range(12):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 14.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 14.pdf')
merger.close()


# Regional 15
path = 'D:/Regional/Regional 15/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 15.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 67

for i in range(9):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 15.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 15.pdf')
merger.close()

# Regional 16
path = 'D:/Regional/Regional 16/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 16.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 73

for i in range(20):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 16.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 16.pdf')
merger.close()


# Regional 17
path = 'D:/Regional/Regional 17/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 17.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 90

for i in range(16):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 17.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 17.pdf')
merger.close()

# Regional 18
path = 'D:/Regional/Regional 18/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 18.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 103

for i in range(5):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 18.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 18.pdf')
merger.close()

# Regional 19
path = 'D:/Regional/Regional 19/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 19.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 105

for i in range(17):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 19.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 19.pdf')
merger.close()


# Regional 20
path = 'D:/Regional/Regional 20/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 20.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 141

for i in range(17):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 20.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio CREDE 20.pdf')
merger.close()


# Regional 21
path = 'D:/Regional/Regional 21/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 21.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 177

for i in range(22):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio SEFOR 1.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio SEFOR 1.pdf')
merger.close()


# Regional 22
path = 'D:/Regional/Regional 22/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 22.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 196

for i in range(6):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio SEFOR 2.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio SEFOR 2.pdf')
merger.close()


# Regional 23
path = 'D:/Regional/Regional 23/'
merger = PdfFileMerger()
capa = '_Capa.pdf'
txtAbertura = '_Texto abertura.pdf'
regional = 'Regional V2 - 23.pdf'
escola_regional = 'Escola-Regional V2 - '
cont = 199

for i in range(4):
  if i == 0:
    merger.append(path + capa)
  elif i == 1:
    merger.append(path + txtAbertura)
  elif i == 2:
    merger.append(path + regional)
  else:
    print(cont)
    merger.append(path + escola_regional + str(cont) +'.pdf' )
    cont = cont + 1

if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio SEFOR 3.pdf'):
  merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output/IAS Relatorio SEFOR 3.pdf')
merger.close()