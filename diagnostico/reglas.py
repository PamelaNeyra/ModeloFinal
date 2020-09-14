
#sag. height mean, rh f, k1, pachy min
regla1ff = ["<= 1468","> 8.03","<= 41.9","> 546"]
#rh f, k1, k max, rh b
regla2ff = ["> 8.03","<= 41.9","<= 44.98","> 6.59"]
#rh f, k1, pachy min, rhb
regla3ff = ["> 8.03","<= 41.9","> 546","> 6.59"]

regla1q = ["> 1578","<= 7.52","<= 478","> 51.45","<= 486","> 44.6","> 61"," > 59","> 2.43","> 0.54"]
regla2q = ["> 1578","<= 7.52","<= 478","> 51.45","<= 486","> 44.6","> 61"," > 59","> 2.43","> 48.4"]
regla3q = ["> 1578","<= 7.52","> 48.4","> 51.45","> 3.34","> 44.6","> 61"," > 59","> 2.43","> 0.54"]

regla1s = ["<= 478","<= 486","> 1513, <= 1578"]
regla2s = ["<= 478","> 1513, <= 1578","<= 58.1"]

def decidirRegla(variables,clasificacion):
	clase = clasificacion.upper()

	if clase == "SUBCLINICO":
	    return decidirReglaSubclinico(variables)
    

def decidirReglaFormeFruste(variables):
    reglaElegida = 0
    coincidencias = 0
    coincidenciasTemp = 0
    reglas = []
    reglasTemp = []
    caracteristicas = []
    caracteristicasTemp = []
    listas = []

    #análisis de regla 1
    coincidenciasTemp = 0
    if(variables[28] <= 1468):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1ff[0])
        caracteristicasTemp.append("Sag. Height Mean [µm] ("+str(round(variables[28],2))+")")
    if(variables[0] > 8.03):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1ff[1])
        caracteristicasTemp.append("Rh F (mm) ("+str(round(variables[0],2))+")")
    if(variables[15] <= 41.9):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1ff[2])
        caracteristicasTemp.append("K1 (D) ("+str(round(variables[15],2))+")")
    if(variables[10] > 546):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1ff[3])
        caracteristicasTemp.append("Pachy Min ("+str(round(variables[10],2))+")")

    reglaElegida = 1
    coincidencias = coincidenciasTemp
    reglas = reglasTemp
    caracteristicas = caracteristicasTemp

    #análisis de regla 2
    coincidenciasTemp = 0
    reglasTemp = []
    caracteristicasTemp = []
    if(variables[0] > 8.03):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2ff[0])
        caracteristicasTemp.append("Rh F (mm) ("+str(round(variables[0],2))+")")
    if(variables[15] <= 41.9):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2ff[1])
        caracteristicasTemp.append("K1 (D) ("+str(round(variables[15],2))+")")
    if(variables[19] <= 44.98):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2ff[2])
        caracteristicasTemp.append("K max ("+str(round(variables[19],2))+")")
    if(variables[4] > 6.59):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2ff[3])
        caracteristicasTemp.append("Rh B (mm) ("+str(round(variables[4],2))+")")

    if(coincidenciasTemp > coincidencias):
        reglaElegida = 2
        coincidencias = coincidenciasTemp
        reglas = reglasTemp
        caracteristicas = caracteristicasTemp

    #análisis de regla 3
    coincidenciasTemp = 0
    reglasTemp = []
    caracteristicasTemp = []
    if(variables[0] > 8.03):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3ff[0])
        caracteristicasTemp.append("Rh F (mm) ("+str(round(variables[0],2))+")")
    if(variables[15] <= 41.9):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3ff[1])
        caracteristicasTemp.append("K1 (D) ("+str(round(variables[15],2))+")")
    if(variables[10] > 546):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3ff[2])
        caracteristicasTemp.append("Pachy Min ("+str(round(variables[10],2))+")")
    if(variables[4] > 6.59):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3ff[3])
        caracteristicasTemp.append("Rh B (mm) ("+str(round(variables[4],2))+")")

    if(coincidenciasTemp > coincidencias):
        reglaElegida = 3
        coincidencias = coincidenciasTemp
        reglas = reglasTemp
        caracteristicas = caracteristicasTemp

    listas.append(caracteristicas)
    listas.append(reglas)
   
    return listas

def decidirReglaSubclinico(variables):
    reglaElegida = 0
    coincidencias = 0
    coincidenciasTemp = 0
    reglas = []
    reglasTemp = []
    caracteristicas = []
    caracteristicasTemp = []
    listas = []

    #análisis de regla 1
    coincidenciasTemp = 0
    if(variables[10] <= 478):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1s[0])
        caracteristicasTemp.append("Pachy min ("+str(round(variables[10],2))+")")
    if(variables[9] <= 486 ):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1s[1])
        caracteristicasTemp.append("Pachy Apex ("+str(round(variables[9],2))+")")
    if(variables[28] > 1513 and variables[28] <=1578):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1s[2])
        caracteristicasTemp.append("Sag. Height Mean [µm] ("+str(round(variables[28],2))+")")

    reglaElegida = 1
    coincidencias = coincidenciasTemp
    reglas = reglasTemp
    caracteristicas = caracteristicasTemp

    #análisis de regla 2
    coincidenciasTemp = 0
    reglasTemp = []
    caracteristicasTemp = []
    if(variables[10] <= 478):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2s[0])
        caracteristicasTemp.append("Pachy min ("+str(round(variables[10],2))+")")
    if(variables[28] > 1513 and variables[28] <=1578):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2s[1])
        caracteristicasTemp.append("Sag. Height Mean [µm] ("+str(round(variables[28],2))+")")
    if(variables[24] <= 58.1):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2s[2])
        caracteristicasTemp.append("Cor. Vol ("+str(round(variables[24],2))+")")

    if(coincidenciasTemp > coincidencias):
        reglaElegida = 2
        coincidencias = coincidenciasTemp
        reglas = reglasTemp
        caracteristicas = caracteristicasTemp

    listas.append(caracteristicas)
    listas.append(reglas)
   
    return listas

def decidirReglaQueratocono(variables):
    reglaElegida = 0
    coincidencias = 0
    coincidenciasTemp = 0
    reglas = []
    reglasTemp = []
    caracteristicas = []
    caracteristicasTemp = []
    listas = []

    #análisis de regla 1
    coincidenciasTemp = 0
    if(variables[28] > 1578):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[0])
        caracteristicasTemp.append("Sag. Height Mean [µm] ("+str(round(variables[28],2))+")")
    if(variables[0] <= 7.52):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[1])
        caracteristicasTemp.append("Rh F (mm) ("+str(round(variables[0],2))+")")
    if(variables[10] <= 478):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[2])
        caracteristicasTemp.append("Pachy Min ("+str(round(variables[10],2))+")")
    if(variables[19] > 51.45):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[3])
        caracteristicasTemp.append("K Max ("+str(round(variables[19],2))+")")
    if(variables[9] <= 486):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[4])
        caracteristicasTemp.append("Pachy Apex ("+str(round(variables[9],2))+")")
    if(variables[15] > 44.6):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[5])
        caracteristicasTemp.append("K1 (D) ("+str(round(variables[15],2))+")")
    if(variables[11] > 61):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[6])
        caracteristicasTemp.append("ISV ("+str(round(variables[11],2))+")")
    if(variables[14] > 59):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[7])
        caracteristicasTemp.append("IHD ("+str(round(variables[14],2))+")")
    if(variables[18] > 2.43):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[8])
        caracteristicasTemp.append("RPI Max ("+str(round(variables[18],2))+")")
    if(variables[12] > 0.54):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla1q[9])
        caracteristicasTemp.append("IVA ("+str(round(variables[12],2))+")")
    

    reglaElegida = 1
    coincidencias = coincidenciasTemp
    reglas = reglasTemp
    caracteristicas = caracteristicasTemp

    #análisis de regla 2
    coincidenciasTemp = 0
    reglasTemp = []
    caracteristicasTemp = []
    if(variables[28] > 1578):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[0])
        caracteristicasTemp.append("Sag. Height Mean [µm] ("+str(round(variables[28],2))+")")
    if(variables[0] <= 7.52):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[1])
        caracteristicasTemp.append("Rh F (mm) ("+str(round(variables[0],2))+")")
    if(variables[10] <= 478):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[2])
        caracteristicasTemp.append("Pachy Min ("+str(round(variables[10],2))+")")
    if(variables[19] > 51.45):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[3])
        caracteristicasTemp.append("K Max ("+str(round(variables[19],2))+")")
    if(variables[9] <= 486):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[4])
        caracteristicasTemp.append("Pachy Apex ("+str(round(variables[9],2))+")")
    if(variables[15] > 44.6):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[5])
        caracteristicasTemp.append("K1 (D) ("+str(round(variables[15],2))+")")
    if(variables[11] > 61):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[6])
        caracteristicasTemp.append("ISV ("+str(round(variables[11],2))+")")
    if(variables[14] > 59):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[7])
        caracteristicasTemp.append("IHD ("+str(round(variables[14],2))+")")
    if(variables[18] > 2.43):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[8])
        caracteristicasTemp.append("RPI Max ("+str(round(variables[18],2))+")")
    if(variables[16] > 48.4):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla2q[9])
        caracteristicasTemp.append("K2 (D) ("+str(round(variables[16],2))+")")

    if(coincidenciasTemp > coincidencias):
        reglaElegida = 2
        coincidencias = coincidenciasTemp
        reglas = reglasTemp
        caracteristicas = caracteristicasTemp

    #análisis de regla 3
    coincidenciasTemp = 0
    reglasTemp = []
    caracteristicasTemp = []
    if(variables[28] > 1578):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[0])
        caracteristicasTemp.append("Sag. Height Mean [µm] ("+str(round(variables[28],2))+")")
    if(variables[0] <= 7.52):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[1])
        caracteristicasTemp.append("Rh F (mm) ("+str(round(variables[0],2))+")")
    if(variables[16] > 48.4):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[2])
        caracteristicasTemp.append("K2 (D) ("+str(round(variables[16],2))+")")
    if(variables[19] > 51.45):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[3])
        caracteristicasTemp.append("K Max ("+str(round(variables[19],2))+")")
    if(variables[20] > 3.34):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[4])
        caracteristicasTemp.append("I-S ("+str(round(variables[20],2))+")")
    if(variables[15] > 44.6):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[5])
        caracteristicasTemp.append("K1 (D) ("+str(round(variables[15],2))+")")
    if(variables[11] > 61):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[6])
        caracteristicasTemp.append("ISV ("+str(round(variables[11],2))+")")
    if(variables[14] > 59):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[7])
        caracteristicasTemp.append("IHD ("+str(round(variables[14],2))+")")
    if(variables[18] > 2.43):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[8])
        caracteristicasTemp.append("RPI Max ("+str(round(variables[18],2))+")")
    if(variables[12] > 0.54):
        coincidenciasTemp = coincidenciasTemp +1
        reglasTemp.append(regla3q[9])
        caracteristicasTemp.append("IVA ("+str(round(variables[12],2))+")")

    if(coincidenciasTemp > coincidencias):
        reglaElegida = 3
        coincidencias = coincidenciasTemp
        reglas = reglasTemp
        caracteristicas = caracteristicasTemp

    listas.append(caracteristicas)
    listas.append(reglas)
   
    return listas

def decidirReglaSano(variables):
    listas = []

    listas.append(["-"])
    listas.append(["-"])
    
    return listas