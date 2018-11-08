import os
from PyPDF2 import PdfFileMerger
import pandas as pd 

class Devolutiva:
  def __init__(self, file, sheet):
    self.merger = PdfFileMerger()
    self.path = 'D:/Escola/'
    self.capa = '_Capa.pdf'
    self.txtAbertura = '_Texto abertura.pdf'
    self.escola = 'Escola V2 - '
    self.escola_turma = 'Escola-Turma V2 - '

    # import dataset 
    self.df_database = pd.read_excel(pd.ExcelFile(file), sheet)
    self.read_database(self.df_database)

  def read_database(self,df1):
    k = 0
    temp = 2
    for i in df1.itertuples():
      if not i.escola_v2 == 1:
        if k == 0:
          k = k + 1
          self.merger.append(self.path + self.capa)
          self.merger.append(self.path + self.txtAbertura)
          self.merger.append(self.path + self.escola + str(i.escola_v2) + '.pdf') 
        
        if i.escola_v2 == temp:
          self.merger.append(self.path + self.escola_turma + str(i.escola_turma_v2) + '.pdf')
          print('escola_turma_v2: ' + str(i.escola_turma_v2))
          print('escola_v2: ' + str(i.escola_v2))
        else:
          if not os.path.exists('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output_escola/IAS Relatorio Escola ' + str(temp) + '.pdf'):
            self.merger.write('C:/Users/kleytonramos/Documents/Join pdf - IAS Devolutiva CE/Output_escola/IAS Relatorio Escola ' + str(temp) + '.pdf')
            temp = i.escola_v2
            self.merger.close()
            self.merger = PdfFileMerger()
            self.merger.append(self.path + self.capa)
            self.merger.append(self.path + self.txtAbertura)
            self.merger.append(self.path + self.escola + str(i.escola_v2) + '.pdf') 
            self.merger.append(self.path + self.escola_turma + str(i.escola_turma_v2) + '.pdf')
            print('escola_turma_v2: ' + str(i.escola_turma_v2))
            print('escola_v2: ' + str(i.escola_v2))
            
      

