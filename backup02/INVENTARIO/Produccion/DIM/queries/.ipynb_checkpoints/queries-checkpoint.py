import yaml
import os

current_path = os.path.abspath(os.getcwd())

# Dimension de Divisiones
dim_division_source = os.path.join(current_path, 'queries','dim_divisiones_source.sql')
with open(dim_division_source) as fichero:
    Q_DIVISIONES_SOURCE = yaml.safe_load(fichero)

dim_division_target = os.path.join(current_path, 'queries','dim_divisiones_target.sql')
with open(dim_division_target) as fichero:
    Q_DIVISIONES_TARGET = yaml.safe_load(fichero)
    
    
# Dimension de estados de ubicaciones
dim_estado_ubicacion_source = os.path.join(current_path, 'queries','dim_estado_ubicacion_source.sql')
with open(dim_estado_ubicacion_source) as fichero:
    Q_ESTADO_UBICACION_SOURCE = yaml.safe_load(fichero)

dim_estado_ubicacion_target = os.path.join(current_path, 'queries','dim_estado_ubicacion_target.sql')
with open(dim_estado_ubicacion_target) as fichero:
    Q_ESTADO_UBICACION_TARGET = yaml.safe_load(fichero)
    
    
# Dimension de tipo de rack
dim_tipo_rack_source = os.path.join(current_path, 'queries','dim_tipo_rack_source.sql')
with open(dim_tipo_rack_source) as fichero:
    Q_TIPO_RACK_SOURCE = yaml.safe_load(fichero)   
    
dim_tipo_rack_target = os.path.join(current_path, 'queries','dim_tipo_rack_target.sql')
with open(dim_tipo_rack_target) as fichero:
    Q_TIPO_RACK_TARGET = yaml.safe_load(fichero)   


# Dimension de zona
dim_zona_source = os.path.join(current_path, 'queries','dim_zona_source.sql')
with open(dim_zona_source) as fichero:
    Q_ZONA_SOURCE = yaml.safe_load(fichero) 

dim_zona_target = os.path.join(current_path, 'queries','dim_zona_target.sql')
with open(dim_zona_target) as fichero:
    Q_ZONA_TARGET = yaml.safe_load(fichero) 
    
    
# Dimension de codigo inutilizacion
dim_codigo_inutilizacion_source = os.path.join(current_path, 'queries','dim_codigo_inutilizacion_source.sql')
with open(dim_codigo_inutilizacion_source) as fichero:
    Q_CODIGO_INUTILIZACION_SOURCE = yaml.safe_load(fichero) 

dim_codigo_inutilizacion_target = os.path.join(current_path, 'queries','dim_codigo_inutilizacion_target.sql')
with open(dim_codigo_inutilizacion_target) as fichero:
    Q_CODIGO_INUTILIZACION_TARGET = yaml.safe_load(fichero) 


# Dimension de tipo ubicacion
dim_tipo_ubicacion_source = os.path.join(current_path, 'queries','dim_tipo_ubicacion_source.sql')
with open(dim_tipo_ubicacion_source) as fichero:
    Q_TIPO_UBICACION_SOURCE = yaml.safe_load(fichero) 

dim_tipo_ubicacion_target = os.path.join(current_path, 'queries','dim_tipo_ubicacion_target.sql')
with open(dim_tipo_ubicacion_target) as fichero:
    Q_TIPO_UBICACION_TARGET = yaml.safe_load(fichero) 

    
# Dimension de tipo zona
dim_tipo_zona_source = os.path.join(current_path, 'queries','dim_tipo_zona_source.sql')
with open(dim_tipo_zona_source) as fichero:
    Q_TIPO_ZONA_SOURCE = yaml.safe_load(fichero) 
    
dim_tipo_zona_target = os.path.join(current_path, 'queries','dim_tipo_zona_target.sql')
with open(dim_tipo_zona_target) as fichero:
    Q_TIPO_ZONA_TARGET = yaml.safe_load(fichero) 
    
    
# Dimension de motivos bloqueo de pallets
dim_motivos_bloqueo_source = os.path.join(current_path, 'queries','dim_motivos_bloqueo_source.sql')
with open(dim_motivos_bloqueo_source) as fichero:
    Q_MOTIVO_BLOQUEO_SOURCE = yaml.safe_load(fichero) 

dim_motivos_bloqueo_target = os.path.join(current_path, 'queries','dim_motivos_bloqueo_target.sql')
with open(dim_motivos_bloqueo_target) as fichero:
    Q_MOTIVO_BLOQUEO_TARGET = yaml.safe_load(fichero) 
    