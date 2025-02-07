import yaml

# Defino el ambiente
DEBUG = False

# Levanto los parametros de las conexiones 
with open("./config.yaml") as fichero:
    # connections = yaml.safe_load(fichero)
    connections = yaml.load(fichero, Loader=yaml.FullLoader)

# En funcion del ambiente tomo las conexiones
if DEBUG:
    
    source = connections['connections']['source']['dev']
    target = connections['connections']['target']['dev']

else:
    
    source = connections['connections']['source']['prd']
    target = connections['connections']['target']['prd']


if __name__ == "__main__":
    print(source)
    print(target)