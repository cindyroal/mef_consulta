#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


r= requests.get("https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M&5=20&6=01&7=301212&23=1&31=&y=2019&cpage=1&psize=3000")
q= requests.get("https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M&5=20&6=01&7=301212&31=&y=2019&cpage=1&psize=3000")
soup = BeautifulSoup(r.text,'lxml')
htmltable = soup.find('table', { 'class' : 'Data' })
htmltable2=htmltable.findAll('tr')


# In[3]:


E1=[]
E2=[]
E3=[]
E4=[]
E5=[]
E6=[]
E7=[]
E8=[]
E9=[]
E10=[]
E11=[]
E12=[]
E13=[]
E14=[]
E15=[]
E16=[]
E17=[]
E18=[]
E19=[]
E20=[]
E21=[]
E24=[]
E25=[]
E26=[]
E27=[]
E28=[]
E29=[]
E30=[]
E31=[]
E32=[]
Meses=[6]
Años=[2020]
Generica=['6-2-6']
Provincias=['01','02','03','04','05','06','07','08']
Municipalidades_1=['301529','301530','301531','301532','301533','301534','301535','301536','301537','301849'] 
Municipalidades_2= ['301538','301539','301540','301541','301542','301543','301544','301545','301546','301547']
Municipalidades_3=['301548','301549','301550','301551','301552','301553','301554','301555']
Municipalidades_4=['301556','301557','301558','301559','301560','301561','301562','301563','301564','301565']
Municipalidades_5=['301566','301567','301568','301569','301570','301571','301572']
Municipalidades_6=['301573','301574','301575','301576','301577','301578','301579','301580']
Municipalidades_7=['301581','301582','301583','301584','301585','301586']
Municipalidades_8=['301587','301588','301589','301590','301591','301592']


# In[4]:


for prov in Provincias:
    if prov=='01':
        Provincia="Piura"
        
        for muni1 in Municipalidades_1:

            if muni1=='301529':
                Municipalidad_1="Municipalidad Provincial de Piura"
            if muni1=='301530':
                Municipalidad_1="Municipalidad Distrital de Castilla"
            if muni1=='301531':
                Municipalidad_1="Municipalidad Distrital de Catacaos"
            if muni1=='301532':
                Municipalidad_1="Municipalidad Distrital de Cura Mori"
            if muni1=='301533':
                Municipalidad_1="Municipalidad Distrital de El Tallán"
            if muni1=='301534':
                Municipalidad_1="Municipalidad Distrital de La Arena"
            if muni1=='301535':
                Municipalidad_1="Municipalidad Distrital de La Unión"
            if muni1=='301536':
                Municipalidad_1="Municipalidad Distrital de Las Lomas"
            if muni1=='301537':
                Municipalidad_1="Municipalidad Distrital de Tambo Grande"
            if muni1=='301849':
                Municipalidad_1="Municipalidad Distrital Veintiséis de Octubre"

            for año in Años:
                for mes in Meses:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                    url_1=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni1)+'&23='+str(mes)+'&31=&y='+str(año)+'&psize=3000'
                    print(url_1)
                    r = requests.get(url_1)
                    soup_1 = BeautifulSoup(r.text,'lxml')
                    try:
                        htmltable_1 = soup_1.find('table', { 'class' : 'Data' })
                        i=1
                        for element in htmltable_1.find_all('td'):
                            if i==12:
                                i=1  
                            if i == 2:
                                A = str(element.text.strip("\r\n").strip())
                                E1.append(A[0:7])
                                E2.append(Municipalidad_1)
                                E3.append(año)
                                E4.append(A[9:])
                                E6.append(str(muni1)+str(A[0:7]) + str(mes))
                                E7.append(mes)
                                E12.append(A[0:])
                                E13.append("PIURA")
                                E14.append("GL")
                                E15.append(Provincia)
                                E16.append("Adquisición de Activos No Financieros")
                                E17.append(muni1)
                                #print(element.text.strip("\\r\\n"))
                            if i == 8: 
                                Z = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E5.append(Z[0:])
                            i = i+1
                    except:
                        continue   

    if prov=='02':
        Provincia="Ayabaca"
        for muni2 in Municipalidades_2:

            if muni2=='301538':
                Municipalidad_2="Municipalidad Provincial de Ayabaca"
            if muni2=='301539':
                Municipalidad_2="Municipalidad Distrital de Frías"
            if muni2=='301540':
                Municipalidad_2="Municipalidad Distrital de Jililí"
            if muni2=='301541':
                Municipalidad_2="Municipalidad Distrital de Lagunas"
            if muni2=='301542':
                Municipalidad_2="Municipalidad Distrital de Montero"
            if muni2=='301543':
                Municipalidad_2="Municipalidad Distrital de Pacaipampa"
            if muni2=='301544':
                Municipalidad_2="Municipalidad Distrital de Paimas"
            if muni2=='301545':
                Municipalidad_2="Municipalidad Distrital de Sapillica"
            if muni2=='301546':
                Municipalidad_2="Municipalidad Distrital de Sícchez"
            if muni2=='301547':
                Municipalidad_2="Municipalidad Distrital de Suyo"     

            for año in Años:
                for mes in Meses:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                    url_2=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni2)+'&23='+str(mes)+'&31=&y='+str(año)+'&psize=3000'
                    print(url_2)
                    r = requests.get(url_2)
                    soup_2 = BeautifulSoup(r.text,'lxml')
                    try:
                        htmltable_2 = soup_2.find('table', { 'class' : 'Data' })
                        i=1
                        for element in htmltable_2.find_all('td'):
                            if i==12:
                                i=1  
                            if i == 2:
                                A = str(element.text.strip("\r\n").strip())
                                E1.append(A[0:7])
                                E2.append(Municipalidad_2)
                                E3.append(año)
                                E4.append(A[9:])
                                E6.append(str(muni2)+str(A[0:7]) + str(mes))
                                E7.append(mes)                     
                                E12.append(A[0:])
                                E13.append("PIURA")
                                E14.append("GL")
                                E15.append(Provincia)
                                E16.append("Adquisición de Activos No Financieros")
                                E17.append(muni2)
                                #print(element.text.strip("\\r\\n"))
                            if i == 8: 
                                Z = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E5.append(Z[0:])
                            i = i+1
                    except:
                        continue       
    if prov=='03':
        Provincia="Huancabamba"
        
        for muni3 in Municipalidades_3:
            if muni3=='301548':
                Municipalidad_3="Municipalidad Provincial de Huancabamba"
            if muni3=='301549':
                Municipalidad_3="Municipalidad Distrital de Canchaque"
            if muni3=='301550':
                Municipalidad_3="Municipalidad Distrital de El Carmen de la Frontera"
            if muni3=='301551':
                Municipalidad_3="Municipalidad Distrital de Huarmaca"
            if muni3=='301552':
                Municipalidad_3="Municipalidad Distrital de Lalaquiz"
            if muni3=='301553':
                Municipalidad_3="Municipalidad Distrital de San Miguel de el Faique"
            if muni3=='301554':
                Municipalidad_3="Municipalidad Distrital de Sóndor"
            if muni3=='301555':
                Municipalidad_3="Municipalidad Distrital de Sondorillo"            

            for año in Años:
                for mes in Meses:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                    url_3=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni3)+'&23='+str(mes)+'&31=&y='+str(año)+'&psize=3000'
                    print(url_3)
                    r = requests.get(url_3)
                    soup_3 = BeautifulSoup(r.text,'lxml')
                    try:
                        htmltable_3 = soup_3.find('table', { 'class' : 'Data' })
                        i=1
                        for element in htmltable_3.find_all('td'):
                            if i==12:
                                i=1  
                            if i == 2:
                                A = str(element.text.strip("\r\n").strip())
                                E1.append(A[0:7])
                                E2.append(Municipalidad_3)
                                E3.append(año)
                                E4.append(A[9:])
                                E6.append(str(muni3)+str(A[0:7]) + str(mes))
                                E7.append(mes)                             
                                E12.append(A[0:])
                                E13.append("PIURA")
                                E14.append("GL")
                                E15.append(Provincia)
                                E16.append("Adquisición de Activos No Financieros")
                                E17.append(muni3)
                                #print(element.text.strip("\\r\\n"))
                            if i == 8: 
                                Z = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E5.append(Z[0:])
                            i = i+1
                    except:
                        continue
                    
    if prov=='04':
        Provincia="Morropón"
        
        for muni4 in Municipalidades_4:
            if muni4=='301556':
                Municipalidad_4="Municipalidad Provincial de Morropón - Chulucanas"
            if muni4=='301557':
                Municipalidad_4="Municipalidad Distrital de Buenos Aires"
            if muni4=='301558':
                Municipalidad_4="Municipalidad Distrital de Chalaco"
            if muni4=='301559':
                Municipalidad_4="Municipalidad Distrital de La Matanza"
            if muni4=='301560':
                Municipalidad_4="Municipalidad Distrital de Morropón"
            if muni4=='301561':
                Municipalidad_4="Municipalidad Distrital de Salitral"
            if muni4=='301562':
                Municipalidad_4="Municipalidad Distrital de San Juan de Bigote"
            if muni4=='301563':
                Municipalidad_4="Municipalidad Distrital de Santa Catalina de Mossa"
            if muni4=='301564':
                Municipalidad_4="Municipalidad Distrital de Santo Domingo"
            if muni4=='301565':
                Municipalidad_4="Municipalidad Distrital de Yamango"      

            for año in Años:
                for mes in Meses:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                    url_4=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni4)+'&23='+str(mes)+'&31=&y='+str(año)+'&psize=3000'
                    print(url_4)
                    r = requests.get(url_4)
                    soup_4 = BeautifulSoup(r.text,'lxml')
                    try:
                        htmltable_4 = soup_4.find('table', { 'class' : 'Data' })
                        i=1
                        for element in htmltable_4.find_all('td'):
                            if i==12:
                                i=1  
                            if i == 2:
                                A = str(element.text.strip("\r\n").strip())
                                E1.append(A[0:7])
                                E2.append(Municipalidad_4)
                                E3.append(año)
                                E4.append(A[9:])
                                E6.append(str(muni4)+str(A[0:7]) + str(mes))
                                E7.append(mes)                               
                                E12.append(A[0:])
                                E13.append("PIURA")
                                E14.append("GL")
                                E15.append(Provincia)
                                E16.append("Adquisición de Activos No Financieros")
                                E17.append(muni4)
                                #print(element.text.strip("\\r\\n"))
                            if i == 8: 
                                Z = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E5.append(Z[0:])
                            i = i+1
                    except:
                        continue
                    
    if prov=='05':
        Provincia="Paita"
        
        for muni5 in Municipalidades_5:
            if muni5=='301566':
                Municipalidad_5="Municipalidad Provincial de Paita"
            if muni5=='301567':
                Municipalidad_5="Municipalidad Distrital de Amotape"
            if muni5=='301568':
                Municipalidad_5="Municipalidad Distrital de El Arenal"
            if muni5=='301569':
                Municipalidad_5="Municipalidad Distrital de Colán"
            if muni5=='301570':
                Municipalidad_5="Municipalidad Distrital de La Huaca"
            if muni5=='301571':
                Municipalidad_5="Municipalidad Distrital de Tamarindo"
            if muni5=='301572':
                Municipalidad_5="Municipalidad Distrital de Vichayal"

            for año in Años:
                for mes in Meses:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                    url_5=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni5)+'&23='+str(mes)+'&31=&y='+str(año)+'&psize=3000'
                    print(url_5)
                    r = requests.get(url_5)
                    soup_5 = BeautifulSoup(r.text,'lxml')
                    try:
                        htmltable_5 = soup_5.find('table', { 'class' : 'Data' })
                        i=1
                        for element in htmltable_5.find_all('td'):
                            if i==12:
                                i=1  
                            if i == 2:
                                A = str(element.text.strip("\r\n").strip())
                                E1.append(A[0:7])
                                E2.append(Municipalidad_5)
                                E3.append(año)
                                E4.append(A[9:])
                                E6.append(str(muni5)+str(A[0:7]) + str(mes))
                                E7.append(mes)                               
                                E12.append(A[0:])
                                E13.append("PIURA")
                                E14.append("GL")
                                E15.append(Provincia)
                                E16.append("Adquisición de Activos No Financieros")
                                E17.append(muni5)
                                #print(element.text.strip("\\r\\n"))
                            if i == 8: 
                                Z = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E5.append(Z[0:])
                            i = i+1
                    except:
                        continue
                    
    if prov=='06':
        Provincia="Sullana"
        
        for muni6 in Municipalidades_6:
            if muni6=='301573':
                Municipalidad_6="Municipalidad Provincial de Sullana"
            if muni6=='301574':
                Municipalidad_6="Municipalidad Distrital de Bellavista"
            if muni6=='301575':
                Municipalidad_6="Municipalidad Distrital de Ignacio Escudero"
            if muni6=='301576':
                Municipalidad_6="Municipalidad Distrital de Lancones"
            if muni6=='301577':
                Municipalidad_6="Municipalidad Distrital de Marcavelica"
            if muni6=='301578':
                Municipalidad_6="Municipalidad Distrital de Miguel Checa"
            if muni6=='301579':
                Municipalidad_6="Municipalidad Distrital de Querecotillo"
            if muni6=='301580':
                Municipalidad_6="Municipalidad Distrital de Salitral"

            for año in Años:
                for mes in Meses:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                    url_6=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni6)+'&23='+str(mes)+'&31=&y='+str(año)+'&psize=3000'
                    print(url_6)
                    r = requests.get(url_6)
                    soup_6 = BeautifulSoup(r.text,'lxml')
                    try:
                        htmltable_6 = soup_6.find('table', { 'class' : 'Data' })
                        i=1
                        for element in htmltable_6.find_all('td'):
                            if i==12:
                                i=1  
                            if i == 2:
                                A = str(element.text.strip("\r\n").strip())
                                E1.append(A[0:7])
                                E2.append(Municipalidad_6)
                                E3.append(año)
                                E4.append(A[9:])
                                E6.append(str(muni6)+str(A[0:7]) + str(mes))
                                E7.append(mes)
                                E12.append(A[0:])
                                E13.append("PIURA")
                                E14.append("GL")
                                E15.append(Provincia)
                                E16.append("Adquisición de Activos No Financieros")
                                E17.append(muni6)
                                #print(element.text.strip("\\r\\n"))
                            if i == 8: 
                                Z = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E5.append(Z[0:])
                            i = i+1
                    except:
                        continue
                    
    if prov=='07':
        Provincia="Talara"  
        
        for muni7 in Municipalidades_7:
            if muni7=='301581':
                Municipalidad_7="Municipalidad Provincial de Talara - Pariñas"
            if muni7=='301582':
                Municipalidad_7="Municipalidad Distrital de El Alto"
            if muni7=='301583':
                Municipalidad_7="Municipalidad Distrital de La Brea"
            if muni7=='301584':
                Municipalidad_7="Municipalidad Distrital de Lobitos"
            if muni7=='301585':
                Municipalidad_7="Municipalidad Distrital de Los Órganos"
            if muni7=='301586':
                Municipalidad_7="Municipalidad Distrital de Máncora"
            for año in Años:
                for mes in Meses:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                    url_7=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni7)+'&23='+str(mes)+'&31=&y='+str(año)+'&psize=3000'
                    print(url_7)
                    r = requests.get(url_7)
                    soup_7 = BeautifulSoup(r.text,'lxml')
                    try:
                        htmltable_7 = soup_7.find('table', { 'class' : 'Data' })
                        i=1
                        for element in htmltable_7.find_all('td'):
                            if i==12:
                                i=1  
                            if i == 2:
                                A = str(element.text.strip("\r\n").strip())
                                E1.append(A[0:7])
                                E2.append(Municipalidad_7)
                                E3.append(año)
                                E4.append(A[9:])
                                E6.append(str(muni7)+str(A[0:7]) + str(mes))
                                E7.append(mes)
                                E12.append(A[0:])
                                E13.append("PIURA")
                                E14.append("GL")
                                E15.append(Provincia)
                                E16.append("Adquisición de Activos No Financieros")
                                E17.append(muni7)
                                #print(element.text.strip("\\r\\n"))
                            if i == 8: 
                                Z = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E5.append(Z[0:])
                            i = i+1
                    except:
                        continue

    if prov=='08':
        Provincia="Sechura"  
        
        for muni8 in Municipalidades_8:
            if muni8=='301587':
                Municipalidad_8="Municipalidad Provincial de Sechura"
            if muni8=='301588':
                Municipalidad_8="Municipalidad Distrital de Bellavista de la Unión"
            if muni8=='301589':
                Municipalidad_8="Municipalidad Distrital de Bernal"
            if muni8=='301590':
                Municipalidad_8="Municipalidad Distrital de Cristo Nos Valga"
            if muni8=='301591':
                Municipalidad_8="Municipalidad Distrital de Vice"
            if muni8=='301592':
                Municipalidad_8="Municipalidad Distrital de Rinconada Llicuar"

            for año in Años:
                for mes in Meses:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                    url_8=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni8)+'&23='+str(mes)+'&31=&y='+str(año)+'&psize=3000'
                    print(url_8)
                    r = requests.get(url_8)
                    soup_8 = BeautifulSoup(r.text,'lxml')
                    try:
                        htmltable_8 = soup_8.find('table', { 'class' : 'Data' })
                        i=1
                        for element in htmltable_8.find_all('td'):
                            if i==12:
                                i=1  
                            if i == 2:
                                A = str(element.text.strip("\r\n").strip())
                                E1.append(A[0:7])
                                E2.append(Municipalidad_8)
                                E3.append(año)
                                E4.append(A[9:])
                                E6.append(str(muni8)+str(A[0:7]) + str(mes))
                                E7.append(mes)                                
                                E12.append(A[0:])
                                E13.append("PIURA")
                                E14.append("GL")
                                E15.append(Provincia)
                                E16.append("Adquisición de Activos No Financieros")
                                E17.append(muni8)
                                #print(element.text.strip("\\r\\n"))
                            if i == 8: 
                                Z = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E5.append(Z[0:])
                            i = i+1
                    except:
                        continue
            print(len(E1))
            print(len(E2))
            print(len(E3))
            print(len(E4))
            print(len(E5))
            print(len(E7))
            print(len(E8))
            print(len(E9))
            print(len(E10))
            print(len(E11))


# In[5]:


A[0:6]


# In[6]:


df = pd.DataFrame(columns=['Código', 'Proyecto','Completo','Departamento','Provincia','Nivel de Gobierno','Código Nivel de Gobierno','Nombre de Nivel de Gobierno','Año','Mes','Genérica','Dv_1','ID'])
df['Completo']= E12
df['Código'] = E1
df['Proyecto'] = E4
df['Mes'] = E7
df['Año'] = E3
df['Dv_1'] = E5
df['ID'] = E6
df['Nombre de Nivel de Gobierno'] = E2
df['Departamento'] = E13
df['Nivel de Gobierno'] = E14
df['Provincia'] = E15
df['Genérica'] = E16
df['Código Nivel de Gobierno']=E17
df.head()


# In[7]:


for prov in Provincias:
    if prov=='01':
        Provincia="Piura"
        
        for muni1 in Municipalidades_1:

            if muni1=='301529':
                Municipalidad_1="Municipalidad Provincial de Piura"
            if muni1=='301530':
                Municipalidad_1="Municipalidad Distrital de Castilla"
            if muni1=='301531':
                Municipalidad_1="Municipalidad Distrital de Catacaos"
            if muni1=='301532':
                Municipalidad_1="Municipalidad Distrital de Cura Mori"
            if muni1=='301533':
                Municipalidad_1="Municipalidad Distrital de El Tallán"
            if muni1=='301534':
                Municipalidad_1="Municipalidad Distrital de La Arena"
            if muni1=='301535':
                Municipalidad_1="Municipalidad Distrital de La Unión"
            if muni1=='301536':
                Municipalidad_1="Municipalidad Distrital de Las Lomas"
            if muni1=='301537':
                Municipalidad_1="Municipalidad Distrital de Tambo Grande"
            if muni1=='301849':
                Municipalidad_1="Municipalidad Distrital Veintiséis de Octubre"

            for año in Años:

                ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                url2=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni1)+'&31=&y='+str(año)+'&psize=3000'
                print(url2)
                q = requests.get(url2)
                soup2 = BeautifulSoup(q.text,'lxml')
                try:
                    htmltable2 = soup2.find('table', { 'class' : 'Data' })
                    j=1
                    for element in htmltable2.find_all('td'):
                        if j==12:
                            j=1  
                        if j == 2:
                            B = str(element.text.strip("\r\n").strip())
                            E18.append(B[0:7])
                            E19.append(muni1)
                            E20.append(str(muni1)+str(B[0:7]) + '6')
                            E24.append(Municipalidad_1)
                            E25.append("PIURA")
                            E26.append(str(B[9:]))
                            E27.append(str(B[0:]))
                            E28.append("Adquisición de Activos No Financieros")
                            E29.append("GL")
                            E30.append(Provincia)
                            E31.append(año)
                        if j == 4:
                            C = str(element.text.strip("\r\n").strip())
                            #print(element.text)
                            E32.append(C[0:])
                        j = j+1
                except: 
                    continue

    if prov=='02':
        Provincia="Ayabaca"
        for muni2 in Municipalidades_2:

            if muni2=='301538':
                Municipalidad_2="Municipalidad Provincial de Ayabaca"
            if muni2=='301539':
                Municipalidad_2="Municipalidad Distrital de Frías"
            if muni2=='301540':
                Municipalidad_2="Municipalidad Distrital de Jililí"
            if muni2=='301541':
                Municipalidad_2="Municipalidad Distrital de Lagunas"
            if muni2=='301542':
                Municipalidad_2="Municipalidad Distrital de Montero"
            if muni2=='301543':
                Municipalidad_2="Municipalidad Distrital de Pacaipampa"
            if muni2=='301544':
                Municipalidad_2="Municipalidad Distrital de Paimas"
            if muni2=='301545':
                Municipalidad_2="Municipalidad Distrital de Sapillica"
            if muni2=='301546':
                Municipalidad_2="Municipalidad Distrital de Sícchez"
            if muni2=='301547':
                Municipalidad_2="Municipalidad Distrital de Suyo"      

            for año in Años:

                ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                url3=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni2)+'&31=&y='+str(año)+'&psize=3000'
                print(url3)
                q = requests.get(url3)
                soup3 = BeautifulSoup(q.text,'lxml')
                try:
                    htmltable3 = soup3.find('table', { 'class' : 'Data' })
                    j=1
                    for element in htmltable3.find_all('td'):
                        if j==12:
                            j=1  
                        if j == 2:
                            B = str(element.text.strip("\r\n").strip())
                            E18.append(B[0:7])
                            E19.append(muni2)
                            E20.append(str(muni2)+str(B[0:7]) + '6')
                            E24.append(Municipalidad_2)
                            E25.append("PIURA")
                            E26.append(str(B[9:]))
                            E27.append(str(B[0:]))
                            E28.append("Adquisición de Activos No Financieros")
                            E29.append("GL")
                            E30.append(Provincia)
                            E31.append(año)
                        if j == 4:
                            C = str(element.text.strip("\r\n").strip())
                            #print(element.text)
                            E32.append(C[0:])
                        j = j+1
                except: 
                    continue        
        
    
    if prov=='03':
        Provincia="Huancabamba"
        
        for muni3 in Municipalidades_3:
            if muni3=='301548':
                Municipalidad_3="Municipalidad Provincial de Huancabamba"
            if muni3=='301549':
                Municipalidad_3="Municipalidad Distrital de Canchaque"
            if muni3=='301550':
                Municipalidad_3="Municipalidad Distrital de El Carmen de la Frontera"
            if muni3=='301551':
                Municipalidad_3="Municipalidad Distrital de Huarmaca"
            if muni3=='301552':
                Municipalidad_3="Municipalidad Distrital de Lalaquiz"
            if muni3=='301553':
                Municipalidad_3="Municipalidad Distrital de San Miguel de el Faique"
            if muni3=='301554':
                Municipalidad_3="Municipalidad Distrital de Sóndor"
            if muni3=='301555':
                Municipalidad_3="Municipalidad Distrital de Sondorillo"                        
            for año in Años:

                ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                url4=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni3)+'&31=&y='+str(año)+'&psize=3000'
                print(url4)
                q = requests.get(url4)
                soup4 = BeautifulSoup(q.text,'lxml')
                try:
                    htmltable4 = soup4.find('table', { 'class' : 'Data' })
                    j=1
                    for element in htmltable4.find_all('td'):
                        if j==12:
                            j=1  
                        if j == 2:
                            B = str(element.text.strip("\r\n").strip())
                            E18.append(B[0:7])
                            E19.append(muni3)
                            E20.append(str(muni3)+str(B[0:7]) + '6')
                            E24.append(Municipalidad_3)
                            E25.append("PIURA")
                            E26.append(str(B[9:]))
                            E27.append(str(B[0:]))
                            E28.append("Adquisición de Activos No Financieros")
                            E29.append("GL")
                            E30.append(Provincia)
                            E31.append(año)
                        if j == 4:
                            C = str(element.text.strip("\r\n").strip())
                            #print(element.text)
                            E32.append(C[0:])
                        j = j+1
                except: 
                    continue
                
    if prov=='04':
        Provincia="Morropón"
        
        for muni4 in Municipalidades_4:
            if muni4=='301556':
                Municipalidad_4="Municipalidad Provincial de Morropón - Chulucanas"
            if muni4=='301557':
                Municipalidad_4="Municipalidad Distrital de Buenos Aires"
            if muni4=='301558':
                Municipalidad_4="Municipalidad Distrital de Chalaco"
            if muni4=='301559':
                Municipalidad_4="Municipalidad Distrital de La Matanza"
            if muni4=='301560':
                Municipalidad_4="Municipalidad Distrital de Morropón"
            if muni4=='301561':
                Municipalidad_4="Municipalidad Distrital de Salitral"
            if muni4=='301562':
                Municipalidad_4="Municipalidad Distrital de San Juan de Bigote"
            if muni4=='301563':
                Municipalidad_4="Municipalidad Distrital de Santa Catalina de Mossa"
            if muni4=='301564':
                Municipalidad_4="Municipalidad Distrital de Santo Domingo"
            if muni4=='301565':
                Municipalidad_4="Municipalidad Distrital de Yamango"        
            for año in Años:

                ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                url5=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni4)+'&31=&y='+str(año)+'&psize=3000'
                print(url5)
                q = requests.get(url5)
                soup5 = BeautifulSoup(q.text,'lxml')
                try:
                    htmltable5 = soup5.find('table', { 'class' : 'Data' })
                    j=1
                    for element in htmltable5.find_all('td'):
                        if j==12:
                            j=1  
                        if j == 2:
                            B = str(element.text.strip("\r\n").strip())
                            E18.append(B[0:7])
                            E19.append(muni4)
                            E20.append(str(muni4)+str(B[0:7]) + '6')
                            E24.append(Municipalidad_4)
                            E25.append("PIURA")
                            E26.append(str(B[9:]))
                            E27.append(str(B[0:]))
                            E28.append("Adquisición de Activos No Financieros")
                            E29.append("GL")
                            E30.append(Provincia)
                            E31.append(año)
                        if j == 4:
                            C = str(element.text.strip("\r\n").strip())
                            #print(element.text)
                            E32.append(C[0:])
                        j = j+1
                except: 
                    continue        
        
    if prov=='05':
        Provincia="Paita"
        
        for muni5 in Municipalidades_5:
            if muni5=='301566':
                Municipalidad_5="Municipalidad Provincial de Paita"
            if muni5=='301567':
                Municipalidad_5="Municipalidad Distrital de Amotape"
            if muni5=='301568':
                Municipalidad_5="Municipalidad Distrital de El Arenal"
            if muni5=='301569':
                Municipalidad_5="Municipalidad Distrital de Colán"
            if muni5=='301570':
                Municipalidad_5="Municipalidad Distrital de La Huaca"
            if muni5=='301571':
                Municipalidad_5="Municipalidad Distrital de Tamarindo"
            if muni5=='301572':
                Municipalidad_5="Municipalidad Distrital de Vichayal"   
            for año in Años:

                ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                url6=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni5)+'&31=&y='+str(año)+'&psize=3000'
                print(url6)
                q = requests.get(url6)
                soup6 = BeautifulSoup(q.text,'lxml')
                try:
                    htmltable6 = soup6.find('table', { 'class' : 'Data' })
                    j=1
                    for element in htmltable6.find_all('td'):
                        if j==12:
                            j=1  
                        if j == 2:
                            B = str(element.text.strip("\r\n").strip())
                            E18.append(B[0:7])
                            E19.append(muni5)
                            E20.append(str(muni5)+str(B[0:7]) + '6')
                            E24.append(Municipalidad_5)
                            E25.append("PIURA")
                            E26.append(str(B[9:]))
                            E27.append(str(B[0:]))
                            E28.append("Adquisición de Activos No Financieros")
                            E29.append("GL")
                            E30.append(Provincia)
                            E31.append(año)
                        if j == 4:
                            C = str(element.text.strip("\r\n").strip())
                            #print(element.text)
                            E32.append(C[0:])
                        j = j+1
                except: 
                    continue        
        
    if prov=='06':
        Provincia="Sullana"
        
        for muni6 in Municipalidades_6:
            if muni6=='301573':
                Municipalidad_6="Municipalidad Provincial de Sullana"
            if muni6=='301574':
                Municipalidad_6="Municipalidad Distrital de Bellavista"
            if muni6=='301575':
                Municipalidad_6="Municipalidad Distrital de Ignacio Escudero"
            if muni6=='301576':
                Municipalidad_6="Municipalidad Distrital de Lancones"
            if muni6=='301577':
                Municipalidad_6="Municipalidad Distrital de Marcavelica"
            if muni6=='301578':
                Municipalidad_6="Municipalidad Distrital de Miguel Checa"
            if muni6=='301579':
                Municipalidad_6="Municipalidad Distrital de Querecotillo"
            if muni6=='301580':
                Municipalidad_6="Municipalidad Distrital de Salitral"     
            for año in Años:

                ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                url7=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni6)+'&31=&y='+str(año)+'&psize=3000'
                print(url7)
                q = requests.get(url7)
                soup7 = BeautifulSoup(q.text,'lxml')
                try:
                    htmltable7 = soup7.find('table', { 'class' : 'Data' })
                    j=1
                    for element in htmltable7.find_all('td'):
                        if j==12:
                            j=1  
                        if j == 2:
                            B = str(element.text.strip("\r\n").strip())
                            E18.append(B[0:7])
                            E19.append(muni6)
                            E20.append(str(muni6)+str(B[0:7]) + '6')
                            E24.append(Municipalidad_6)
                            E25.append("PIURA")
                            E26.append(str(B[9:]))
                            E27.append(str(B[0:]))
                            E28.append("Adquisición de Activos No Financieros")
                            E29.append("GL")
                            E30.append(Provincia)
                            E31.append(año)
                        if j == 4:
                            C = str(element.text.strip("\r\n").strip())
                            #print(element.text)
                            E32.append(C[0:])
                        j = j+1
                except: 
                    continue        
    if prov=='07':
        Provincia="Talara"  
        
        for muni7 in Municipalidades_7:
            if muni7=='301581':
                Municipalidad_7="Municipalidad Provincial de Talara - Pariñas"
            if muni7=='301582':
                Municipalidad_7="Municipalidad Distrital de El Alto"
            if muni7=='301583':
                Municipalidad_7="Municipalidad Distrital de La Brea"
            if muni7=='301584':
                Municipalidad_7="Municipalidad Distrital de Lobitos"
            if muni7=='301585':
                Municipalidad_7="Municipalidad Distrital de Los Órganos"
            if muni7=='301586':
                Municipalidad_7="Municipalidad Distrital de Máncora"
            for año in Años:

                ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                url8=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni7)+'&31=&y='+str(año)+'&psize=3000'
                print(url8)
                q = requests.get(url8)
                soup8 = BeautifulSoup(q.text,'lxml')
                try:
                    htmltable8 = soup8.find('table', { 'class' : 'Data' })
                    j=1
                    for element in htmltable8.find_all('td'):
                        if j==12:
                            j=1  
                        if j == 2:
                            B = str(element.text.strip("\r\n").strip())
                            E18.append(B[0:7])
                            E19.append(muni7)
                            E20.append(str(muni7)+str(B[0:7]) + '6')
                            E24.append(Municipalidad_7)
                            E25.append("PIURA")
                            E26.append(str(B[9:]))
                            E27.append(str(B[0:]))
                            E28.append("Adquisición de Activos No Financieros")
                            E29.append("GL")
                            E30.append(Provincia)
                            E31.append(año)
                        if j == 4:
                            C = str(element.text.strip("\r\n").strip())
                            #print(element.text)
                            E32.append(C[0:])
                        j = j+1
                except: 
                    continue        
    if prov=='08':
        Provincia="Sechura"  
        
        for muni8 in Municipalidades_8:
            if muni8=='301587':
                Municipalidad_8="Municipalidad Provincial de Sechura"
            if muni8=='301588':
                Municipalidad_8="Municipalidad Distrital de Bellavista de la Unión"
            if muni8=='301589':
                Municipalidad_8="Municipalidad Distrital de Bernal"
            if muni8=='301590':
                Municipalidad_8="Municipalidad Distrital de Cristo Nos Valga"
            if muni8=='301591':
                Municipalidad_8="Municipalidad Distrital de Vice"
            if muni8=='301592':
                Municipalidad_8="Municipalidad Distrital de Rinconada Llicuar"
            for año in Años:

                ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&1=M&37=M"
                url9=ab+'&5=20'+'&6='+str(prov)+'&7='+str(muni8)+'&31=&y='+str(año)+'&psize=3000'
                print(url9)
                q = requests.get(url9)
                soup9 = BeautifulSoup(q.text,'lxml')
                try:
                    htmltable9 = soup9.find('table', { 'class' : 'Data' })
                    j=1
                    for element in htmltable9.find_all('td'):
                        if j==12:
                            j=1  
                        if j == 2:
                            B = str(element.text.strip("\r\n").strip())
                            E18.append(B[0:7])
                            E19.append(muni8)
                            E20.append(str(muni8)+str(B[0:7]) + '6')
                            E24.append(Municipalidad_8)
                            E25.append("PIURA")
                            E26.append(str(B[9:]))
                            E27.append(str(B[0:]))
                            E28.append("Adquisición de Activos No Financieros")
                            E29.append("GL")
                            E30.append(Provincia)
                            E31.append(año)
                        if j == 4:
                            C = str(element.text.strip("\r\n").strip())
                            #print(element.text)
                            E32.append(C[0:])
                        j = j+1
                except: 
                    continue                
        
        print(len(E18))
        print(len(E19))
        print(len(E20))
        print(len(E32))


# In[8]:


df2 = pd.DataFrame(columns=['Código','Proyecto','Completo','Departamento','Provincia','Nivel de Gobierno','Código Nivel de Gobierno','Nombre de Nivel de Gobierno','Año','Genérica','PIM_1','ID'])
df2['Código'] = E18
df2['Código Nivel de Gobierno'] = E19
df2['ID'] = E20
df2['Nombre de Nivel de Gobierno'] = E24
df2['Departamento'] = E25
df2['Proyecto'] = E26
df2['Completo'] = E27
df2['Genérica'] = E28
df2['Nivel de Gobierno'] = E29
df2['Provincia'] = E30
df2['Año']=E31
df2['PIM_1'] = E32

df2.head()


# In[9]:


df2.to_excel("PIU_LOC_PIM1_2020.xlsx",index=False)


# In[10]:


df.to_excel("PIU_LOC_DV1_2020.xlsx",index=False)


# In[ ]:





# In[ ]:




