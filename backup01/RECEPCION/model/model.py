# import datetime.datetime


class Model():
        
    def get_fields(self):
        fields = []
        attributes = []
        metrics = []
        fields_detail = []
        
        for field, field_detail in self.__dict__.items():
            fields.append(field)
            fields_detail.append(field_detail)
            if field_detail['bi_type'] == 'attribute':
                attributes.append(field)
            else:
                metrics.append(field)
        
        return fields, attributes, metrics, fields_detail
    
    def validate_dataframe(self, df, drop_columns=False, rename=True):
        
        # Check columns
        cols_df = list(df.columns)
        cols_model, _ , _, _ = self.get_fields() 
        cols_ok = []
        cols_leftover = []
        cols_missing = []
        
        print(cols_model)
        
        # Separo las columnas que se ajustan al modelo de las sobrantes
        for col_df in cols_df:
            if col_df.lower() in cols_model:
                cols_ok.append(col_df.lower())
            else:
                cols_leftover.append(col_df.lower())
       
        # Verifico que el df tenga todas las columnas del modelo
        for col_model in cols_model:
            if col_model.lower() not in col_df.lower():
                cols_missing.append(col_model.lower())

        # Renombro las columnas
        if rename:
            df.columns = df.columns.str.lower()
        
        # Dropeo las columnas que sobran
        if drop_columns & (len(cols_leftover)>0):
            df= df.drop(columns=cols_leftover)

        return df, cols_missing
    
    def validate_data_types(self, df):
        pass

    def validate_integrity(self, df, fill_ids= True):
        """
        Verifica que no existan atributos nulos y si existen aplica valores por defecto
        """
        
        cols_df = list(df.columns)
        _, _ , _, fields_detail = self.get_fields()
        
        for col in cols_df:
            df[col] = df[col].fillna(fields_detail['default'])
        
        return df
            
            

#########################################################################################################################                

class Inventario_BT(Model):
    
    def __init__(self):
        
        # Atributos
        self.id_dia = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        self.id_empresa= {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_almacen = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_zona = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_pasillo = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_zona = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_rack = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_pallet = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_estado_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_division_asignada = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_producto = {'bi_type':'attribute','data_type': int, 'default': -1}
        # id_division_producto
        # id_departamento_ubicacion
        # id_clase_ubicacion
        # id_gran_categoria_ubicacion
        self.id_departamento = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_clase = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_gran_categoria = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_gerente_comercial = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_consignatario = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_dia_ingreso_pallet = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        self.id_dia_caducidad_pallet = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        # id_tipo_flujo (andenes de entrada, salida, pulomon, racks)
        
        # Metricas
        self.capacidad_ubicacion = {'bi_type':'metric','data_type': int, 'default': 0}
        self.antiguedad_pallet = {'bi_type':'metric','data_type': int, 'default': 0}
        # self.pallets = {'bi_type':'attribute','metric': int, 'default': 0}
        self.bultos = {'bi_type':'attribute','metric': int, 'default': 0}
        self.unidades = {'bi_type':'attribute','metric': int, 'default': 0}
        

#########################################################################################################################

class Inventario_Agg(Model):
    
    def __init__(self):
        
        # Atributos
        self.id_dia = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        self.id_empresa= {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_almacen = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_zona = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_pasillo = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_zona = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_rack = {'bi_type':'attribute','data_type': int, 'default': -1}
        # self.id_pallet = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_estado_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_division_asignada = {'bi_type':'attribute','data_type': int, 'default': -1}
        # self.id_producto = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_departamento = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_clase = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_gran_categoria = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_gerente_comercial = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_consignatario = {'bi_type':'attribute','data_type': int, 'default': -1}
        # self.id_dia_ingreso_pallet = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        # self.id_dia_caducidad_pallet = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        # id_tipo_flujo (andenes de entrada, salida, pulomon, racks)
        
        # Metricas
        self.capacidad_ubicacion = {'bi_type':'metric','data_type': int, 'default': 0}
        # self.antiguedad_promedio_pallet = {'bi_type':'metric','data_type': int, 'default': 0}
        self.pallets = {'bi_type':'attribute','metric': int, 'default': 0}
        self.bultos = {'bi_type':'attribute','metric': int, 'default': 0}
        self.unidades = {'bi_type':'attribute','metric': int, 'default': 0}
        
        
#########################################################################################################################

class Inventario_Agg_Evolutivo(Model):
    
    def __init__(self):
        
        # Atributos
        self.id_dia = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        self.id_empresa = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_almacen = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_zona = {'bi_type':'attribute','data_type': int, 'default': -1}
        # self.id_pasillo = {'bi_type':'attribute','data_type': int, 'default': -1}
        # self.id_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_zona = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_tipo_rack = {'bi_type':'attribute','data_type': int, 'default': -1}
        # self.id_pallet = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_estado_ubicacion = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_division_asignada = {'bi_type':'attribute','data_type': int, 'default': -1}
        # self.id_producto = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_departamento = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_clase = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_gran_categoria = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_gerente_comercial = {'bi_type':'attribute','data_type': int, 'default': -1}
        self.id_consignatario = {'bi_type':'attribute','data_type': int, 'default': -1}
        # self.id_dia_ingreso_pallet = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        # self.id_dia_caducidad_pallet = {'bi_type':'attribute','data_type': str, 'default': '01-01-1900'}
        # id_tipo_flujo (andenes de entrada, salida, pulomon, racks)
        
        # Metricas
        self.capacidad_ubicaciones = {'bi_type':'metric','data_type': int, 'default': 0}
        self.antiguedad_promedio_pallet = {'bi_type':'metric','data_type': int, 'default': 0}
        self.pallets = {'bi_type':'attribute','metric': int, 'default': 0}
        self.bultos = {'bi_type':'attribute','metric': int, 'default': 0}
        self.unidades = {'bi_type':'attribute','metric': int, 'default': 0}
        self.ubicaciones_ocupadas = {'bi_type':'attribute','metric': int, 'default': 0}
        self.ubicaciones_semi_ocupadas = {'bi_type':'attribute','metric': int, 'default': 0}
        self.ubicaciones_libres = {'bi_type':'attribute','metric': int, 'default': 0}
        self.ubicaciones_disponibles = {'bi_type':'attribute','metric': int, 'default': 0}
        self.ubicaciones_inutilizadas = {'bi_type':'attribute','metric': int, 'default': 0}
        
        