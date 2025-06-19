import pandas as pd

def cargar_datos_ventas(ruta_archivo='../data/processed/tabla_consolidada.csv'):
    """
    Carga el DataFrame de ventas consolidado con un esquema de tipos predefinido.

    Args:
        ruta_archivo (str): La ruta al archivo CSV a cargar.

    Returns:
        pd.DataFrame: El DataFrame cargado con los tipos de datos especificados.
    """
    # Esquema de tipos para leer el CSV procesado
    dtype_dict = {
        'sucursal': 'category',
        'producto_id': 'category',
        'unidades_vendidas': 'int16',
        'precio_venta': 'float32',
        'unidades_compradas': 'int16',
        'costo_unitario': 'float32',
        'margen_bruto': 'float32',
        'nombre_producto': 'category',
        'categoria': 'category',
        'marca': 'category',
        'unidad_medida': 'category',
        'tipo_promocion': 'category',
        'descuento_porcentual': 'float32',
        'producto_en_promocion': 'int8'
    }

    # Cargar el DataFrame y aplicar el esquema de tipos
    df = pd.read_csv(
        ruta_archivo,
        parse_dates=['fecha'],
        dtype=dtype_dict,
        low_memory=False
    )
    return df