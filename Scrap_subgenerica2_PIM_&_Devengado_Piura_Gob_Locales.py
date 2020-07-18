#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import re
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


r = requests.get("https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&21=20&1=M&37=M&5=20&7=301581&23=2&25=2-6-2&26=2-6-2-2&27=2-6-2-2-2&31=&y=2019&psize=3000")
q = requests.get("https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?_uhc=yes&0=&24=6-2-6&21=20&1=M&37=M&5=20&7=301581&25=2-6-2&26=2-6-2-2&27=2-6-2-2-2&31=&y=2019&psize=3000")
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
E22=[]
E23=[]
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
Especifica1=[1]
Especifica2=[1,2,3,4,5,6]
Especifica3=[1,2,3,4,5,6,7,99]
Años=[2020]
Generica=['6-2-6']
Municipalidades=['301529','301530','301531','301532','301533','301534','301535','301536','301537','301849','301538','301539','301540','301541','301542','301543','301544','301545','301546','301547','301548','301549','301550','301551','301552','301553','301554','301555','301556','301557','301558','301559','301560','301561','301562','301563','301564','301565','301566','301567','301568','301569','301570','301571','301572','301573','301574','301575','301576','301577','301578','301579','301580','301581','301582','301583','301584','301585','301586','301587','301588','301589','301590','301591','301592']


# In[4]:


for muni in Municipalidades:
    if muni=='301529':
        Municipalidad="Municipalidad Provincial de Piura"
    if muni=='301530':
        Municipalidad="Municipalidad Distrital de Castilla"
    if muni=='301531':
        Municipalidad="Municipalidad Distrital de Catacaos"
    if muni=='301532':
        Municipalidad="Municipalidad Distrital de Cura Mori"
    if muni=='301533':
        Municipalidad="Municipalidad Distrital de El Tallán"
    if muni=='301534':
        Municipalidad="Municipalidad Distrital de La Arena"
    if muni=='301535':
        Municipalidad="Municipalidad Distrital de La Unión"
    if muni=='301536':
        Municipalidad="Municipalidad Distrital de Las Lomas"
    if muni=='301537':
        Municipalidad="Municipalidad Distrital de Tambo Grande"
    if muni=='301849':
        Municipalidad="Municipalidad Distrital Veintiséis de Octubre"
    if muni=='301538':
        Municipalidad="Municipalidad Provincial de Ayabaca"
    if muni=='301539':
        Municipalidad="Municipalidad Distrital de Frías"
    if muni=='301540':
        Municipalidad="Municipalidad Distrital de Jililí"
    if muni=='301541':
        Municipalidad="Municipalidad Distrital de Lagunas"
    if muni=='301542':
        Municipalidad="Municipalidad Distrital de Montero"
    if muni=='301543':
        Municipalidad="Municipalidad Distrital de Pacaipampa"
    if muni=='301544':
        Municipalidad="Municipalidad Distrital de Paimas"
    if muni=='301545':
        Municipalidad="Municipalidad Distrital de Sapillica"
    if muni=='301546':
        Municipalidad="Municipalidad Distrital de Sícchez"
    if muni=='301547':
        Municipalidad="Municipalidad Distrital de Suyo"
    if muni=='301548':
        Municipalidad="Municipalidad Provincial de Huancabamba"
    if muni=='301549':
        Municipalidad="Municipalidad Distrital de Canchaque"
    if muni=='301550':
        Municipalidad="Municipalidad Distrital de El Carmen de la Frontera"
    if muni=='301551':
        Municipalidad="Municipalidad Distrital de Huarmaca"
    if muni=='301552':
        Municipalidad="Municipalidad Distrital de Lalaquiz"
    if muni=='301553':
        Municipalidad="Municipalidad Distrital de San Miguel de el Faique"
    if muni=='301554':
        Municipalidad="Municipalidad Distrital de Sóndor"
    if muni=='301555':
        Municipalidad="Municipalidad Distrital de Sondorillo"
    if muni=='301556':
        Municipalidad="Municipalidad Provincial de Morropón - Chulucanas"
    if muni=='301557':
        Municipalidad="Municipalidad Distrital de Buenos Aires"
    if muni=='301558':
        Municipalidad="Municipalidad Distrital de Chalaco"
    if muni=='301559':
        Municipalidad="Municipalidad Distrital de La Matanza"
    if muni=='301560':
        Municipalidad="Municipalidad Distrital de Morropón"
    if muni=='301561':
        Municipalidad="Municipalidad Distrital de Salitral"
    if muni=='301562':
        Municipalidad="Municipalidad Distrital de San Juan de Bigote"
    if muni=='301563':
        Municipalidad="Municipalidad Distrital de Santa Catalina de Mossa"
    if muni=='301564':
        Municipalidad="Municipalidad Distrital de Santo Domingo"
    if muni=='301565':
        Municipalidad="Municipalidad Distrital de Yamango"
    if muni=='301566':
        Municipalidad="Municipalidad Provincial de Paita"
    if muni=='301567':
        Municipalidad="Municipalidad Distrital de Amotape"
    if muni=='301568':
        Municipalidad="Municipalidad Distrital de El Arenal"
    if muni=='301569':
        Municipalidad="Municipalidad Distrital de Colán"
    if muni=='301570':
        Municipalidad="Municipalidad Distrital de La Huaca"
    if muni=='301571':
        Municipalidad="Municipalidad Distrital de Tamarindo"
    if muni=='301572':
        Municipalidad="Municipalidad Distrital de Vichayal"
    if muni=='301573':
        Municipalidad="Municipalidad Provincial de Sullana"
    if muni=='301574':
        Municipalidad="Municipalidad Distrital de Bellavista"
    if muni=='301575':
        Municipalidad="Municipalidad Distrital de Ignacio Escudero"
    if muni=='301576':
        Municipalidad="Municipalidad Distrital de Lancones"
    if muni=='301577':
        Municipalidad="Municipalidad Distrital de Marcavelica"
    if muni=='301578':
        Municipalidad="Municipalidad Distrital de Miguel Checa"
    if muni=='301579':
        Municipalidad="Municipalidad Distrital de Querecotillo"
    if muni=='301580':
        Municipalidad="Municipalidad Distrital de Salitral"
    if muni=='301581':
        Municipalidad="Municipalidad Provincial de Talara - Pariñas"
    if muni=='301582':
        Municipalidad="Municipalidad Distrital de El Alto"
    if muni=='301583':
        Municipalidad="Municipalidad Distrital de La Brea"
    if muni=='301584':
        Municipalidad="Municipalidad Distrital de Lobitos"
    if muni=='301585':
        Municipalidad="Municipalidad Distrital de Los Órganos"
    if muni=='301586':
        Municipalidad="Municipalidad Distrital de Máncora"
    if muni=='301587':
        Municipalidad="Municipalidad Provincial de Sechura"
    if muni=='301588':
        Municipalidad="Municipalidad Distrital de Bellavista de la Unión"
    if muni=='301589':
        Municipalidad="Municipalidad Distrital de Bernal"
    if muni=='301590':
        Municipalidad="Municipalidad Distrital de Cristo Nos Valga"
    if muni=='301591':
        Municipalidad="Municipalidad Distrital de Vice"
    if muni=='301592':
        Municipalidad="Municipalidad Distrital de Rinconada Llicuar"

    for año in Años:
        for mes in Meses:
            for SG in [i for i in range(2,3)]:
                for SGD in [i for i in range(1,2)]:
                    for esp in Especifica1:
                        ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?__uhc=yes&0=&24=6-2-6&21=20&1=M&37=M&5=20"
                        d=f"&25=2-6- {SG} &26=2-6- {SG} - {SGD} &27=2-6- {SG} - {SGD} - {esp} &31=&y="
                        url=ab+'&7='+str(muni)+'&23='+str(mes)+d.replace(" ","")+str(año)+'&psize=3000'
                        #'&6='+str(prov)+
                        print(url)
                        r = requests.get(url)
                        soup = BeautifulSoup(r.text,'lxml')
                        try:
                            htmltable = soup.find('table', { 'class' : 'Data' })
                            i=1
                            for element in htmltable.find_all('td'):
                                if i==12:
                                    i=1  
                                if i == 2:
                                    A = str(element.text.strip("\r\n").strip())
                                    E1.append(A[0:7])
                                    E2.append(Municipalidad)
                                    E3.append(año)
                                    E4.append(str(muni)+str(A[0:7]) + str(mes))
                                    E7.append(mes)           
                                    E17.append(muni)
                                    E30.append(str(A[9:]))
                                    E31.append("GL")
                                    if esp==1:
                                        E11.append("Edificios residenciales")

                                    E13.append("PIURA")
       
                                    E14.append(A[0:])
                                    E28.append(str(SGD)+str(esp))

                                if i == 8:
                                    Z = str(element.text.strip("\r\n").strip())
                                    #print(element.text)
                                    E5.append(Z[0:])
                                i = i+1
                        except: 
                            continue

                for SGD in [i for i in range (2,3)]:
                    for esp in Especifica2:
                        ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?__uhc=yes&0=&24=6-2-6&21=20&1=M&37=M&5=20"
                        d=f"&25=2-6- {SG} &26=2-6- {SG} - {SGD} &27=2-6- {SG} - {SGD} - {esp} &31=&y="
                        url=ab+'&7='+str(muni)+'&23='+str(mes)+d.replace(" ","")+str(año)+'&psize=3000'
                        #'&6='+str(prov)+
                        print(url)
                        r = requests.get(url)
                        soup = BeautifulSoup(r.text,'lxml')
                        try:
                            htmltable = soup.find('table', { 'class' : 'Data' })
                            i=1
                            for element in htmltable.find_all('td'):
                                if i==12:
                                    i=1  
                                if i == 2:
                                    A = str(element.text.strip("\r\n").strip())
                                    E1.append(A[0:7])
                                    E2.append(Municipalidad)
                                    E3.append(año)
                                    E4.append(str(muni)+str(A[0:7]) + str(mes))
                                    E7.append(mes)    
                                    E17.append(muni)
                                    E30.append(str(A[9:]))
                                    E31.append("GL")
                                    if esp==1:
                                        E11.append("Edificios administrativos")
                                    if esp==2:
                                        E11.append("Instalaciones educativas")
                                    if esp==3:
                                        E11.append("Instalaciones médicas")
                                    if esp==4:
                                        E11.append("Instalaciones sociales y culturales")
                                    if esp==5:
                                        E11.append("Centros de reclusión")
                                    if esp==6:
                                        E11.append("Otros edificios o unidades no residenciales")

                                    E13.append("PIURA")
                                    E28.append(str(SGD)+str(esp))
                                    E14.append(A[0:])
                                if i == 8:
                                    Z = str(element.text.strip("\r\n").strip())
                                    #print(element.text)
                                    E5.append(Z[0:])
                                i = i+1
                        except:
                            continue

                for SGD in [i for i in range (3,4)]:
                    for esp in Especifica3:
                        ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?__uhc=yes&0=&24=6-2-6&21=20&1=M&37=M&5=20"
                        d=f"&25=2-6- {SG} &26=2-6- {SG} - {SGD} &27=2-6- {SG} - {SGD} - {esp} &31=&y="
                        url=ab+'&7='+str(muni)+'&23='+str(mes)+d.replace(" ","")+str(año)+'&psize=3000'
                        #'&6='+str(prov)+
                        print(url)
                        r = requests.get(url)
                        soup = BeautifulSoup(r.text,'lxml')
                        try:
                            htmltable = soup.find('table', { 'class' : 'Data' })
                            i=1
                            for element in htmltable.find_all('td'):
                                if i==12:
                                    i=1  
                                if i == 2:
                                    A = str(element.text.strip("\r\n").strip())
                                    E1.append(A[0:7])
                                    E2.append(Municipalidad)
                                    E3.append(año)
                                    E4.append(str(muni)+str(A[0:7]) + str(mes))
                                    E7.append(mes)
                                    E17.append(muni)
                                    E30.append(str(A[9:]))
                                    E31.append("GL")
                                    if esp==1:
                                        E11.append("Puertos y aeropuertos")
                                    if esp==2:
                                        E11.append("Infraestructura vial")
                                    if esp==3:
                                        E11.append("Infraestructura eléctrica")
                                    if esp==4:
                                        E11.append("Infraestructura agrícola")
                                    if esp==5:
                                        E11.append("Agua y saneamiento")
                                    if esp==6:
                                        E11.append("Plazuelas, parques y jardines")
                                    if esp==7:
                                        E11.append("Monumentos históricos")
                                    if esp==99:
                                        E11.append("Otras estructuras diversas")

                                    E13.append("PIURA")
                                    E28.append(str(SGD)+str(esp))
                                    E14.append(A[0:])
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
print(len(E28))


# In[6]:


df = pd.DataFrame(columns=['Código','Proyecto','Completo','Departamento','Nivel de Gobierno','Código Nivel de Gobierno','Nombre de Nivel de Gobierno','Año','Mes','D_SG + Especifica','Categoría','Dv_2','ID'])
df['Código'] = E1
df['Nombre de Nivel de Gobierno'] = E2
df['Año'] = E3
df['Dv_2'] = E5
df['Mes'] = E7
df['Categoría']= E11
df['Departamento'] = E13
df['Completo'] = E14
df['Código Nivel de Gobierno']=E17
df['ID']=E4
df['D_SG + Especifica'] = E28
df['Proyecto']=E30
df['Nivel de Gobierno']=E31

df.head()
#No se incluyen Provincia ni genérica porque ya esta incluido el tag en PIM1.


# In[7]:


for muni in Municipalidades:
    if muni=='301529':
        Municipalidad="Municipalidad Provincial de Piura"
    if muni=='301530':
        Municipalidad="Municipalidad Distrital de Castilla"
    if muni=='301531':
        Municipalidad="Municipalidad Distrital de Catacaos"
    if muni=='301532':
        Municipalidad="Municipalidad Distrital de Cura Mori"
    if muni=='301533':
        Municipalidad="Municipalidad Distrital de El Tallán"
    if muni=='301534':
        Municipalidad="Municipalidad Distrital de La Arena"
    if muni=='301535':
        Municipalidad="Municipalidad Distrital de La Unión"
    if muni=='301536':
        Municipalidad="Municipalidad Distrital de Las Lomas"
    if muni=='301537':
        Municipalidad="Municipalidad Distrital de Tambo Grande"
    if muni=='301849':
        Municipalidad="Municipalidad Distrital Veintiséis de Octubre"
    if muni=='301538':
        Municipalidad="Municipalidad Provincial de Ayabaca"
    if muni=='301539':
        Municipalidad="Municipalidad Distrital de Frías"
    if muni=='301540':
        Municipalidad="Municipalidad Distrital de Jililí"
    if muni=='301541':
        Municipalidad="Municipalidad Distrital de Lagunas"
    if muni=='301542':
        Municipalidad="Municipalidad Distrital de Montero"
    if muni=='301543':
        Municipalidad="Municipalidad Distrital de Pacaipampa"
    if muni=='301544':
        Municipalidad="Municipalidad Distrital de Paimas"
    if muni=='301545':
        Municipalidad="Municipalidad Distrital de Sapillica"
    if muni=='301546':
        Municipalidad="Municipalidad Distrital de Sícchez"
    if muni=='301547':
        Municipalidad="Municipalidad Distrital de Suyo"
    if muni=='301548':
        Municipalidad="Municipalidad Provincial de Huancabamba"
    if muni=='301549':
        Municipalidad="Municipalidad Distrital de Canchaque"
    if muni=='301550':
        Municipalidad="Municipalidad Distrital de El Carmen de la Frontera"
    if muni=='301551':
        Municipalidad="Municipalidad Distrital de Huarmaca"
    if muni=='301552':
        Municipalidad="Municipalidad Distrital de Lalaquiz"
    if muni=='301553':
        Municipalidad="Municipalidad Distrital de San Miguel de el Faique"
    if muni=='301554':
        Municipalidad="Municipalidad Distrital de Sóndor"
    if muni=='301555':
        Municipalidad="Municipalidad Distrital de Sondorillo"
    if muni=='301556':
        Municipalidad="Municipalidad Provincial de Morropón - Chulucanas"
    if muni=='301557':
        Municipalidad="Municipalidad Distrital de Buenos Aires"
    if muni=='301558':
        Municipalidad="Municipalidad Distrital de Chalaco"
    if muni=='301559':
        Municipalidad="Municipalidad Distrital de La Matanza"
    if muni=='301560':
        Municipalidad="Municipalidad Distrital de Morropón"
    if muni=='301561':
        Municipalidad="Municipalidad Distrital de Salitral"
    if muni=='301562':
        Municipalidad="Municipalidad Distrital de San Juan de Bigote"
    if muni=='301563':
        Municipalidad="Municipalidad Distrital de Santa Catalina de Mossa"
    if muni=='301564':
        Municipalidad="Municipalidad Distrital de Santo Domingo"
    if muni=='301565':
        Municipalidad="Municipalidad Distrital de Yamango"
    if muni=='301566':
        Municipalidad="Municipalidad Provincial de Paita"
    if muni=='301567':
        Municipalidad="Municipalidad Distrital de Amotape"
    if muni=='301568':
        Municipalidad="Municipalidad Distrital de El Arenal"
    if muni=='301569':
        Municipalidad="Municipalidad Distrital de Colán"
    if muni=='301570':
        Municipalidad="Municipalidad Distrital de La Huaca"
    if muni=='301571':
        Municipalidad="Municipalidad Distrital de Tamarindo"
    if muni=='301572':
        Municipalidad="Municipalidad Distrital de Vichayal"
    if muni=='301573':
        Municipalidad="Municipalidad Provincial de Sullana"
    if muni=='301574':
        Municipalidad="Municipalidad Distrital de Bellavista"
    if muni=='301575':
        Municipalidad="Municipalidad Distrital de Ignacio Escudero"
    if muni=='301576':
        Municipalidad="Municipalidad Distrital de Lancones"
    if muni=='301577':
        Municipalidad="Municipalidad Distrital de Marcavelica"
    if muni=='301578':
        Municipalidad="Municipalidad Distrital de Miguel Checa"
    if muni=='301579':
        Municipalidad="Municipalidad Distrital de Querecotillo"
    if muni=='301580':
        Municipalidad="Municipalidad Distrital de Salitral"
    if muni=='301581':
        Municipalidad="Municipalidad Provincial de Talara - Pariñas"
    if muni=='301582':
        Municipalidad="Municipalidad Distrital de El Alto"
    if muni=='301583':
        Municipalidad="Municipalidad Distrital de La Brea"
    if muni=='301584':
        Municipalidad="Municipalidad Distrital de Lobitos"
    if muni=='301585':
        Municipalidad="Municipalidad Distrital de Los Órganos"
    if muni=='301586':
        Municipalidad="Municipalidad Distrital de Máncora"
    if muni=='301587':
        Municipalidad="Municipalidad Provincial de Sechura"
    if muni=='301588':
        Municipalidad="Municipalidad Distrital de Bellavista de la Unión"
    if muni=='301589':
        Municipalidad="Municipalidad Distrital de Bernal"
    if muni=='301590':
        Municipalidad="Municipalidad Distrital de Cristo Nos Valga"
    if muni=='301591':
        Municipalidad="Municipalidad Distrital de Vice"
    if muni=='301592':
        Municipalidad="Municipalidad Distrital de Rinconada Llicuar"

    for año in Años:

        for SG in [i for i in range(2,3)]:
            for SGD in [i for i in range(1,2)]:
                for esp in Especifica1:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?__uhc=yes&0=&24=6-2-6&21=20&1=M&37=M&5=20"
                    d=f"&25=2-6- {SG} &26=2-6- {SG} - {SGD} &27=2-6- {SG} - {SGD} - {esp} &31=&y="
                    url2=ab+'&7='+str(muni)+d.replace(" ","")+str(año)+'&psize=3000'
                    #'&6='+str(prov)+
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
                                E19.append(muni)
                                E20.append(str(muni)+str(B[0:7]) + '6')
                                E22.append(str(SGD)+str(esp))
                                E24.append(Municipalidad)
                                E25.append("PIURA")
                                E26.append(str(B[9:]))
                                E27.append(str(B[0:]))
                                E29.append(año)
                                E32.append("GL")

                                if esp==1:
                                    E23.append("Edificios residenciales")



                            if j == 4:
                                C = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E21.append(C[0:])
                            j = j+1
                    except: 
                        continue

            for SGD in [i for i in range (2,3)]:
                for esp in Especifica2:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?__uhc=yes&0=&24=6-2-6&21=20&1=M&37=M&5=20"
                    d=f"&25=2-6- {SG} &26=2-6- {SG} - {SGD} &27=2-6- {SG} - {SGD} - {esp} &31=&y="
                    url2=ab+'&7='+str(muni)+d.replace(" ","")+str(año)+'&psize=3000'
                    #'&6='+str(prov)+
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
                                D = str(element.text.strip("\r\n").strip())
                                E18.append(D[0:7])
                                E19.append(muni)
                                E20.append(str(muni)+str(D[0:7]) + '6')
                                E22.append(str(SGD)+str(esp))
                                E24.append(Municipalidad)
                                E25.append("PIURA")
                                E26.append(str(D[9:]))
                                E27.append(str(D[0:]))
                                E29.append(año)
                                E32.append("GL")
                                if esp==1:
                                    E23.append("Edificios administrativos")
                                if esp==2:
                                    E23.append("Instalaciones educativas")
                                if esp==3:
                                    E23.append("Instalaciones médicas")
                                if esp==4:
                                    E23.append("Instalaciones sociales y culturales")
                                if esp==5:
                                    E23.append("Centros de reclusión")
                                if esp==6:
                                    E23.append("Otros edificios o unidades no residenciales")


                            if j == 4:
                                E = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E21.append(E[0:])
                            j = j+1
                    except: 
                        continue


            for SGD in [i for i in range (3,4)]:
                for esp in Especifica3:
                    ab="https://apps5.mineco.gob.pe/transparencia/mensual/Navegar_6.aspx?__uhc=yes&0=&24=6-2-6&21=20&1=M&37=M&5=20"
                    d=f"&25=2-6- {SG} &26=2-6- {SG} - {SGD} &27=2-6- {SG} - {SGD} - {esp} &31=&y="
                    url2=ab+'&7='+str(muni)+d.replace(" ","")+str(año)+'&psize=3000'
                    #'&6='+str(prov)+
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
                                F = str(element.text.strip("\r\n").strip())
                                E18.append(F[0:7])
                                E19.append(muni)
                                E20.append(str(muni)+str(F[0:7]) + '6')
                                E22.append(str(SGD)+str(esp))
                                E24.append(Municipalidad)
                                E25.append("PIURA")
                                E26.append(str(F[9:]))
                                E27.append(str(F[0:]))
                                E29.append(año)
                                E32.append("GL")
                                if esp==1:
                                    E23.append("Puertos y aeropuertos")
                                if esp==2:
                                    E23.append("Infraestructura vial")
                                if esp==3:
                                    E23.append("Infraestructura eléctrica")
                                if esp==4:
                                    E23.append("Infraestructura agrícola")
                                if esp==5:
                                    E23.append("Agua y saneamiento")
                                if esp==6:
                                    E23.append("Plazuelas, parques y jardines")
                                if esp==7:
                                    E23.append("Monumentos históricos")
                                if esp==99:
                                    E23.append("Otras estructuras diversas")

                            if j == 4:
                                G = str(element.text.strip("\r\n").strip())
                                #print(element.text)
                                E21.append(G[0:])
                            j = j+1
                    except: 
                        continue


    print(len(E18))
    print(len(E19))
    print(len(E20))
    print(len(E21))


# In[8]:


df2 = pd.DataFrame(columns=['Código','Proyecto','Completo','Departamento','Nivel de Gobierno','Código Nivel de Gobierno','Nombre de Nivel de Gobierno','Año','D_SG + Especifica','Categoría','PIM_2','ID'])
df2['Código'] = E18
df2['Código Nivel de Gobierno'] = E19
df2['ID'] = E20
df2['PIM_2'] = E21
df2['D_SG + Especifica'] = E22
df2['Categoría'] = E23
df2['Nombre de Nivel de Gobierno'] = E24
df2['Departamento'] = E25
df2['Proyecto'] = E26
df2['Completo'] = E27
df2['Año'] = E29
df2['Nivel de Gobierno'] = E32
df2.head()


# In[9]:


df2.to_excel("PIU_LOC_CONSTR_PIM2_2020.xlsx", index=False)


# In[10]:


df.to_excel("PIU_LOC_CONSTR_DV2_2020.xlsx", index=False)


# In[ ]:




