import yaml
import os

current_path = os.path.abspath(os.getcwd())

# Maestro de ubicaciones
maestro_ubicaciones = os.path.join(current_path, 'queries','maestro_ubicaciones.sql')
with open(maestro_ubicaciones) as fichero:
    Q_UBICACIONES = yaml.safe_load(fichero)
    
# Pallets por ubicacion
pallets_ubicaciones = os.path.join(current_path, 'queries', 'pallets_ubicaciones.sql')
with open(pallets_ubicaciones) as fichero:
    Q_UBICACIONES_PALLETS = yaml.safe_load(fichero)

# Maestro de andenes
maestro_andenes = os.path.join(current_path, 'queries', 'maestro_andenes.sql')
with open(maestro_andenes) as fichero:
    Q_ANDENES = yaml.safe_load(fichero)

# Pallets por anden
pallets_andenes_entrada = os.path.join(current_path, 'queries', 'pallets_andenes_entrada.sql')
with open(pallets_andenes_entrada) as fichero:
    Q_ANDENES_PALLETS_ENTRADA = yaml.safe_load(fichero)
    
# Pallets por anden
pallets_andenes_salida = os.path.join(current_path, 'queries', 'pallets_andenes_salida.sql')
with open(pallets_andenes_salida) as fichero:
    Q_ANDENES_PALLETS_SALIDA = yaml.safe_load(fichero)

# maestro productos
dim_productos = os.path.join(current_path, 'queries', 'maestro_productos.sql')
with open(dim_productos) as fichero:
    Q_PRODUCTOS = yaml.safe_load(fichero)

    
# control ejecucion
control = os.path.join(current_path, 'queries', 'control_ejecucion.sql')
with open(control) as fichero:
    Q_CONTROL = yaml.safe_load(fichero)
    
    