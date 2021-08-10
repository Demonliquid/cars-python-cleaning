def motor(pais, columnamodelo = 'MODELO/VERSION', columnadestino = "MOTOR"):
    pais[columnadestino] = pais[columnamodelo].str.extract(r'(\d\.\d)', expand=False).str.strip()
    pais[columnadestino].replace(r'', None)
    return pais


def quitardecimal(pais, columna = "AÑO"):
    pais[columna] = pais[columna].astype("float").map('{:.0f}'.format)
    return pais


def valores(pais, columna):
    return dict(pais[columna].value_counts())
    

def modelogeneral(pais, modeloorigen = 'MODELO/VERSION', modelodestino = "MODELO"):
    new = pais[modeloorigen].str.split(" ", n = 1, expand = True)
    pais[modelodestino] = new[0]
    return pais


def especifico(pais, columnasutiles, columnaorigen = 'MODELO/VERSION', columnadestino = 'MODELO'):
    import pandas as pd
    listamodelo =  pd.read_csv(r"D:\Basededatos\Listamodelos.csv", sep=";")
    listamodelo = list(dict(listamodelo["MODELOS"].value_counts()))
    separator = "|"
    listamodelo = separator.join(listamodelo)
    listamodelo = f"({listamodelo})"

    pais["MODELO2"] = pais[columnaorigen].str.extract(listamodelo, expand=False).str.strip()
    condicion = pais["MODELO2"].notna()
    pais.loc[condicion, columnadestino] = pais.loc[condicion, "MODELO2"]
    pais = pais[columnasutiles]
    return pais


def origensegunvin(pais, columnaorigen = "NUMERO CHASIS / VIN", columnadestino = "ORIGEN"):
    import pandas as pd
    from vininfo import Vin
    # CARACTERISTICAS DE UN BUEN VIN
    sincaracter = pais[columnaorigen].str.isalnum() == True
    cantidad = pais[columnaorigen].str.len() == 17
    letras = pais[columnaorigen].str.contains('Q|O|I|q|o|i', regex=True) == False

    # SEPARAR DATOS CON Y SIN VIN
    paisconvin = pais[sincaracter & cantidad & letras]
    paissinvin = pd.concat([pais, paisconvin]).drop_duplicates(keep=False)

    # ORIGEN SEGUN VIN
    paisconvin[columnadestino] = paisconvin[columnaorigen].map(lambda x: Vin(x).country)

    # TRADUCCION MANUAL
    paisconvin[columnadestino].replace('China (Mainland)', 'China', inplace=True)
    paisconvin[columnadestino].replace('Taiwan, China', 'China', inplace=True)
    paisconvin[columnadestino].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
    paisconvin[columnadestino].replace(r"Germany/West Germany", 'Alemania', inplace=True)
    paisconvin[columnadestino].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
    paisconvin[columnadestino].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
    paisconvin[columnadestino].replace(r"United Kingdom", 'Reino Unido', inplace=True)
    paisconvin[columnadestino].replace(r"Italy", 'Italia', inplace=True)
    paisconvin[columnadestino].replace(r"Greece", 'Grecia', inplace=True)
    paisconvin[columnadestino].replace(r"Belgium", 'Belgica', inplace=True)
    paisconvin[columnadestino].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
    paisconvin[columnadestino].replace(r"United States", 'Estados Unidos', inplace=True)
    paisconvin[columnadestino].replace(r"Japan", 'Japon', inplace=True)
    paisconvin[columnadestino].replace(r"Czech Republic", 'Republica Checa', inplace=True)
    paisconvin[columnadestino].replace(r"United Arab Emirates", 'Emiratos Arabes Unidos', inplace=True)
    paisconvin[columnadestino].replace(r"Ethiopia", 'Etiopia', inplace=True)
    paisconvin[columnadestino].replace(r"Hungary", 'Hungria', inplace=True)
    paisconvin[columnadestino].replace(r"Brazil", 'Brasil', inplace=True)
    paisconvin[columnadestino].replace(r"Spain", 'España', inplace=True)
    paisconvin[columnadestino].replace(r"France", 'Francia', inplace=True)
    paisconvin[columnadestino].replace(r"Switzerland", 'Suiza', inplace=True)
    paisconvin[columnadestino].replace(r"Thailand", 'Tailandia', inplace=True)
    paisconvin[columnadestino].replace(r"Denmark", 'Dinamarca', inplace=True)
    paisconvin[columnadestino].replace(r"Finland", 'Finlandia', inplace=True)
    paisconvin[columnadestino].replace(r"Poland", 'Polonia', inplace=True)
    paisconvin[columnadestino].replace(r"Myanmar", 'Birmania', inplace=True)
    paisconvin[columnadestino].replace(r"Ireland", 'Irlanda', inplace=True)
    paisconvin[columnadestino].replace(r"Netherlands", 'Paises Bajos', inplace=True)
    paisconvin[columnadestino].replace(r"South Africa", 'Sudafrica', inplace=True)
    paisconvin[columnadestino].replace(r"Sweden", 'Suecia', inplace=True)
    paisconvin[columnadestino].replace(r"Malaysia", 'Malasia', inplace=True)
    paisconvin[columnadestino].replace(r"USSR/CIS", 'Rusia', inplace=True)
    paisconvin[columnadestino].replace(r"Germany/East Germany", 'Alemania', inplace=True)
    paisconvin[columnadestino].replace(r"Turkey", 'Turquia', inplace=True)
    paisconvin[columnadestino].replace(r"Cayman Islands", 'Islas Caiman', inplace=True)
    paisconvin[columnadestino].replace(r"Morocco", 'Marruecos', inplace=True)
    pais = pd.concat([paisconvin, paissinvin])
    return pais


def version(pais, versionorigen = 'MODELO/VERSION', versiondestino = "VERSION"):
    new = pais[versionorigen].str.split(" ", n = 1, expand = True)
    condicion = pais[versiondestino].isna()
    pais.loc[condicion, versiondestino] = new[1]
    new = None
    return pais


def versionurgencia(pais, versionorigen = 'MODELO/VERSION', versiondestino = "VERSION"):
    import pandas as pd
    new = pais[versiondestino].str.split(" ", n = 1, expand = True)

    condicion = new[1].notna()
    condicion2 = pais[versiondestino].isna()

    pais.loc[condicion2, versiondestino] = new.loc[condicion, 1]

    condicion = new[1].isna()
    condicion2 = pais[versiondestino].isna()

    pais.loc[condicion2, versiondestino] = new.loc[condicion, 0]

    condicion = pais[versiondestino] == pais[versionorigen]
    pais.loc[condicion, versiondestino] = None
    return pais

def versionespecifico(pais, columnaorigen="MODELO/VERSION",columnadestino="VERSION"):
    import pandas as pd

    listaversiones = pd.read_csv(r"D:\Basededatos\Listaversiones.csv")

    regex = list(listaversiones["VERSIONES"])
    separator = "|"
    regex = separator.join(str(r) for r in regex)
    regex = f"({regex})"

    condicion = pais[columnadestino].isna()
    pais.loc[condicion, columnadestino] = pais.loc[condicion, columnaorigen].str.extract(regex, expand=False)
    return pais



def modelogenerico(pais, modeloorigen = 'MODELO', modelodestino = "MODELO GENERICO"):
    pais[modelodestino] = pais[modeloorigen].str.extract(r'^([A-Z]{1,3})\s*[0-9]{1,9}[A-Z]{0,9}$', expand=False).str.strip()
    return pais

def especifico2(pais, columnasutiles, columnaorigen="MODELO/VERSION", columnadestino = 'MODELO'):
    # CARGA MODELOS
    import pandas as pd
    listamodelo =  pd.read_csv(r"D:\Basededatos\Listamodelos.csv", sep=";")
    listamodelo = listamodelo[["MARCAS", "MODELOS", "TIPOS_VEHICULO"]]


    # CARGA MARCAS UNICAS
    listamarcas= list(dict(listamodelo["MARCAS"].value_counts()))

    # POR CADA UNA DE LAS MARCAS, EXTRAER MODELOS
    for marca in listamarcas:
        # MARCA QUE SE MODIFICA EN BASE
        condicion = pais["MARCA"] == marca
        # MARCA ESPECIFICA
        condicion2 = listamodelo["MARCAS"] == marca


        # CREAR BUSCADOR
        regex = listamodelo.loc[condicion2, "MODELOS"].tolist()
        separator = "|"
        regex = separator.join(str(r) for r in regex)
        regex = f"({regex})"


        # EXTRAER DE MODELO/VERSION Y GUARDAR EN MODELO
        pais.loc[condicion, columnadestino] = pais.loc[condicion, columnaorigen].str.extract(regex, expand=False)
    return pais

def corregirmodelo(pais,columnasutiles, columnadestino = 'MODELO'):
    import pandas as pd
    listamodelo =  pd.read_csv(r"D:\Basededatos\Listamodelosparacorregir.csv", sep=";")
    listamodelo = listamodelo[["MARCAS", "MODELOS", "NOMBRE ALTERNATIVO"]]
    condicion = listamodelo["NOMBRE ALTERNATIVO"].notna()
    corregir = listamodelo[condicion]
    pais = pd.merge(pais, corregir, how="left", left_on=["MARCA","MODELO"], right_on=["MARCAS","MODELOS"])
    corregir = None
    condicion = pais["NOMBRE ALTERNATIVO"].notna()
    pais.loc[condicion, "MODELO"] = pais.loc[condicion, "NOMBRE ALTERNATIVO"]
    condicion = None
    pais = pais[columnasutiles]    
    return pais


def segmentacion(pais, columnasutiles):
    # CREAR TIPO_VEHICULO, SEGMENTO.1, CARROCERIA en df
    import pandas as pd
    listamodelo =  pd.read_csv(r"D:\Basededatos\Listamodelosparasegmento.csv", sep=";")
    listamodelo = listamodelo[["MARCAS", "MODELOS", "TIPOS_VEHICULO", "CLASIFICACIONES", "CARROCERIAS"]]
    condicion = listamodelo["TIPOS_VEHICULO"].notna()
    corregir = listamodelo[condicion]
    listamodelo=None
    condicion = None
    pais = pd.merge(pais, corregir, how="left", left_on=["MARCA", "MODELO"], right_on=["MARCAS","MODELOS"])

    condicion = pais["TIPOS_VEHICULO"].notna()
    pais.loc[condicion, "TIPO_VEHICULO"] = pais.loc[condicion, "TIPOS_VEHICULO"]
    condicion = pais["CLASIFICACIONES"].notna()
    pais.loc[condicion, "SEGMENTO.1"] = pais.loc[condicion, "CLASIFICACIONES"]
    condicion = pais["CARROCERIAS"].notna()
    pais.loc[condicion, "CARROCERIA"] = pais.loc[condicion, "CARROCERIAS"]


    pais = pais[columnasutiles]
    return pais


def cilindrada(pais, columnasutiles, columnaorigen="MODELO/VERSION"):
    # CREAR COLUMNA CILINDRADA
    #regex = r"(\d+)\s*[Cc]{1,2}\.*[Cc]{0,1}"
    regex = r"\s?[Cc]\.?[Cc]:?\s?(\d{3,5})"
    regex2 = r"CIL:?\s?(\d{3,5})"
    pais["CILINDRADA1"] = pais[columnaorigen].str.extract(regex, expand=False)
    pais["CILINDRADA2"] = pais[columnaorigen].str.extract(regex2, expand=False)
    condicion = pais["CILINDRADA1"].notna()
    pais.loc[condicion, "CILINDRADA"] = pais["CILINDRADA1"]
    condicion = pais["CILINDRADA2"].notna()
    pais.loc[condicion, "CILINDRADA"] = pais["CILINDRADA2"]
    pais = pais[columnasutiles]
    return pais


def traccion(pais, columnadestino="TRACCION", columnaorigen="MODELO/VERSION"):
    # CREAR COLUMNA TRACCION
    regex = r"(\d\s?[\*xX]\s?\d)"
    pais[columnadestino] = pais[columnaorigen].str.extract(regex, expand=False)
    return pais


def marca(pais, columnadestino="MARCA", columnaorigen="MODELO/VERSION"):
    import pandas as pd
    listamarcas = pd.read_csv(r"D:\Basededatos\Listamodelos.csv", sep=";")
    listamarcas= list(dict(listamarcas["MARCAS"].value_counts()))
    separator = "|"
    listamarcas = separator.join(listamarcas)
    pais[columnadestino] = pais[columnaorigen].str.extract(f"({listamarcas})")[0]
    return pais


def progreso(pais):
    import pandas as pd
    progreso = pd.DataFrame(columns=["COLUMNAS","CANTIDAD", "PROGRESO"])
    progreso["COLUMNAS"] = pais.columns

    for column in list(pais.columns ):
        condicion = progreso["COLUMNAS"] == column
        progreso.loc[condicion, "CANTIDAD"] = pais[column].notna().sum()
        progreso.loc[condicion, "PROGRESO"] = pais[column].notna().mean()

    progreso["PROGRESO"] = (progreso["PROGRESO"]*100).astype(str) + "%"
    return progreso


def corregirmarca(pais, columnasutiles):
    import pandas as pd
    marcas = pd.read_csv(r"D:\Basededatos\Listamodelos.csv", sep=";")
    marcas = marcas[["MARCAS", "MARCA CORREGIDO"]]
    condicion = marcas["MARCA CORREGIDO"].notna()
    marcas = marcas[condicion]
    pais = pd.merge(pais, marcas, left_on="MARCA", right_on="MARCAS", how="left")
    condicion = pais["MARCA CORREGIDO"].notna()
    pais.loc[condicion, "MARCA"] = pais.loc[condicion, "MARCA CORREGIDO"]
    pais = pais[columnasutiles]
    return pais


def traducirpais(pais, columnadestino="ORIGEN"):
    pais[columnadestino] = pais[columnadestino].str.capitalize()
    pais[columnadestino].replace('China (Mainland)', 'China', inplace=True)
    pais[columnadestino].replace('Taiwan, China', 'China', inplace=True)
    pais[columnadestino].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
    pais[columnadestino].replace(r"Germany/West Germany", 'Alemania', inplace=True)
    pais[columnadestino].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
    pais[columnadestino].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
    pais[columnadestino].replace(r"United Kingdom", 'Reino Unido', inplace=True)
    pais[columnadestino].replace(r"Italy", 'Italia', inplace=True)
    pais[columnadestino].replace(r"Greece", 'Grecia', inplace=True)
    pais[columnadestino].replace(r"Belgium", 'Belgica', inplace=True)
    pais[columnadestino].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
    pais[columnadestino].replace(r"United States", 'Estados Unidos', inplace=True)
    pais[columnadestino].replace(r"Japan", 'Japon', inplace=True)
    pais[columnadestino].replace(r"Czech Republic", 'Republica Checa', inplace=True)
    pais[columnadestino].replace(r"United Arab Emirates", 'Emiratos Arabes Unidos', inplace=True)
    pais[columnadestino].replace(r"Ethiopia", 'Etiopia', inplace=True)
    pais[columnadestino].replace(r"Hungary", 'Hungria', inplace=True)
    pais[columnadestino].replace(r"Brazil", 'Brasil', inplace=True)
    pais[columnadestino].replace(r"Spain", 'España', inplace=True)
    pais[columnadestino].replace(r"France", 'Francia', inplace=True)
    pais[columnadestino].replace(r"Switzerland", 'Suiza', inplace=True)
    pais[columnadestino].replace(r"Thailand", 'Tailandia', inplace=True)
    pais[columnadestino].replace(r"Denmark", 'Dinamarca', inplace=True)
    pais[columnadestino].replace(r"Finland", 'Finlandia', inplace=True)
    pais[columnadestino].replace(r"Poland", 'Polonia', inplace=True)
    pais[columnadestino].replace(r"Myanmar", 'Birmania', inplace=True)
    pais[columnadestino].replace(r"Ireland", 'Irlanda', inplace=True)
    pais[columnadestino].replace(r"Netherlands", 'Paises Bajos', inplace=True)
    pais[columnadestino].replace(r"South Africa", 'Sudafrica', inplace=True)
    pais[columnadestino].replace(r"Sweden", 'Suecia', inplace=True)
    pais[columnadestino].replace(r"Malaysia", 'Malasia', inplace=True)
    pais[columnadestino].replace(r"USSR/CIS", 'Rusia', inplace=True)
    pais[columnadestino].replace(r"Germany/East Germany", 'Alemania', inplace=True)
    pais[columnadestino].replace(r"Turkey", 'Turquia', inplace=True)
    pais[columnadestino].replace(r"Cayman Islands", 'Islas Caiman', inplace=True)
    pais[columnadestino].replace(r"Morocco", 'Marruecos', inplace=True)
    return pais

def indice(pais, columnaid):
    pais[columnaid] = range(1, len(pais) + 1)
    return pais

def motorseguncilindrada(pais, columnasutiles):
    # DICCIONARIO DE CILINDRADAS
    import pandas as pd
    diccionario = pd.read_csv(r"D:\Basededatos\Cilindradas.csv", sep=";")
    diccionario["CILINDRADA"] = diccionario["CILINDRADA"].astype(float)
    diccionario["CILINDRADA LTS"] = diccionario["CILINDRADA LTS"].astype(float)


    # CILINDRADA no tiene que tener nulls y estar ordenada
    condicion = pais["CILINDRADA"].isna()
    pais.loc[condicion, "CILINDRADA"] = 0
    pais["CILINDRADA"] = pais["CILINDRADA"].astype(float)
    condicion = pais["CILINDRADA"] > 40000
    pais.loc[condicion, "CILINDRADA"] = 0
    condicion = None

    pais = pais.sort_values(by="CILINDRADA")

    # UNIR SEGUN CILINDRADA
    pais = pd.merge_asof(pais, diccionario, on='CILINDRADA')

    # MOTOR SEGUN CILINDRADA
    pais["MOTOR"] = pais["CILINDRADA LTS"]

    # LIMPIAR DATAFRAME
    pais = pais[columnasutiles]

    # VUELVO A DEJAR LOS 0 EN NULL PARA CONTEO DE COMPLETOS
    condicion = pais["CILINDRADA"] == 0
    pais.loc[condicion, "CILINDRADA"] =  None
    return pais

def identificacionmotor(pais, columnasutiles):

    # CARGA DICCIONARIO Y COLUMNA NUEVA
    import pandas as pd
    diccionario =  pd.read_csv(r"D:\Basededatos\Motores.csv", sep=";")
    pais["IDENTIFICACION MOTOR"] = None

    # LISTA DE MARCAS
    listamarcasvin = list(dict(diccionario["MARCA MOTOR"].value_counts()))


    # POR CADA MARCA EN LA LISTA, TOMAR CUANTOS NUMEROS SIRVEN DEL MOTOR
    for marca in listamarcasvin:
        condicion = diccionario["MARCA MOTOR"] == f"{marca}"
        cantidadletras = diccionario.loc[condicion, "PRIMEROS DIGITOS MOTOR"]
        cantidadletras = cantidadletras.values[0]
        condicion = pais["MARCA"] == f"{marca}"
        condicion2 = pais["NUMERO MOTOR"].notna()
        pais.loc[condicion & condicion2, "IDENTIFICACION MOTOR"] = pais.loc[condicion & condicion2, "NUMERO MOTOR"].str[0:cantidadletras]
        condicion = None
        condicion2 = None
        cantidadletras = None

    diccionario = None
    listamarcasvin = None
    return pais

def versionfinal(pais, destino="VERSION", origen="MODELO/VERSION", eliminar="MODELO"):
    pais[destino] = pais.apply(lambda x: str(x[origen]).replace(str(x[eliminar]), ""), axis=1)
    pais[destino] = pais[destino].str.replace(r'(\b\d.\d\b)', '', regex=True)
    pais[destino] = pais[destino].str.replace(r'(\b[24][x*][24]b)', '', regex=True)
    pais[destino] = pais[destino].str.replace(r'(\d{3,4}\s?[Cc]{2})', '', regex=True)
    pais[destino] = pais[destino].str.strip()
    
    condicion = pais[destino] == ""
    pais.loc[condicion, destino] = None
       
    return pais