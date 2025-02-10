import pandas as pd

def date_validator(date_series, date_format='%d-%m-%Y', default_value='01-01-1900'):
    """
    Valida que una Serie de pandas contenga fechas en el formato especificado. 
    Si no cumple, reemplaza el registro con una fecha por defecto.
    
    Args:
        date_series (pd.Series): Serie de pandas con las fechas a validar.
        date_format (str): Formato esperado para las fechas (por defecto 'dd-mm-aaaa').
        default_date (str): Fecha por defecto a usar en caso de valores no válidos.

    Returns:
        pd.Series: Serie con fechas válidas o reemplazadas por la fecha por defecto, 
                   con tipo datetime64[ns].
    """
    # Convertir la fecha por defecto al formato datetime
    default_date_dt = pd.to_datetime(default_value, format=date_format)

    # Función auxiliar para intentar convertir una fecha
    def try_parse_date(date):
        try:
            return pd.to_datetime(date, format=date_format, errors='raise')  # Forzar error si no es válida
        except:
            return default_date_dt  # Usar la fecha por defecto

    # Aplicar la validación a cada elemento de la serie
    validated_series = date_series.apply(try_parse_date)
    
    # Asegurar que la serie sea de tipo datetime64[ns]
    return pd.to_datetime(validated_series)

def int_validator(int_series, default_value=0):
    """
    Valida que una Serie de pandas contenga solo valores enteros. 
    Si no cumple, reemplaza los valores no válidos con un valor predeterminado.
    
    Args:
        int_series (pd.Series): Serie de pandas con los valores a validar.
        default_value (int): Valor predeterminado para reemplazar valores no válidos.

    Returns:
        pd.Series: Serie con valores enteros válidos o reemplazados, 
                   con tipo int64.
    """
    # Función auxiliar para validar si el valor es un entero
    def try_parse_int(value):
        try:
            return int(value)  # Intenta convertir a entero
        except (ValueError, TypeError):
            return default_value  # Reemplaza con el valor predeterminado si falla

    # Aplicar la validación a cada elemento de la serie
    validated_series = int_series.apply(try_parse_int)
    
    # Asegurar que la serie sea de tipo int64
    return validated_series.astype('int64')


def float_validator(float_series, default_value=0.0):
    """
    Valida que una Serie de pandas contenga solo valores de tipo float. 
    Si no cumple, reemplaza los valores no válidos con un valor predeterminado.
    
    Args:
        float_series (pd.Series): Serie de pandas con los valores a validar.
        default_value (float): Valor predeterminado para reemplazar valores no válidos.

    Returns:
        pd.Series: Serie con valores float válidos o reemplazados, 
                   con tipo float64.
    """
    # Función auxiliar para validar si el valor es un float
    def try_parse_float(value):
        try:
            return float(value)  # Intenta convertir a float
        except (ValueError, TypeError):
            return default_value  # Reemplaza con el valor predeterminado si falla

    # Aplicar la validación a cada elemento de la serie
    validated_series = float_series.apply(try_parse_float)
    
    # Asegurar que la serie sea de tipo float64
    return validated_series.astype('float64')

def str_validator(string_series, default_value=""):
    """
    Valida que una Serie de pandas contenga solo valores de tipo string.
    Si no cumple, reemplaza los valores no válidos con un valor predeterminado.
    
    Args:
        string_series (pd.Series): Serie de pandas con los valores a validar.
        default_value (str): Valor predeterminado para reemplazar valores no válidos.

    Returns:
        pd.Series: Serie con valores string válidos o reemplazados, 
                   con tipo string.
    """
    # Función auxiliar para validar si el valor es una cadena
    def try_parse_string(value):
        try:
            return str(value) if pd.notna(value) else default_value  # Convertir a cadena si no es nulo
        except:
            return default_value  # Reemplaza con el valor predeterminado si falla

    # Aplicar la validación a cada elemento de la serie
    validated_series = string_series.apply(try_parse_string)
    
    # Asegurar que la serie sea de tipo string
    return validated_series.astype('string')

validators = {
    'date': date_validator,
    'int': int_validator,
    'float': float_validator,
    'str': str_validator
}