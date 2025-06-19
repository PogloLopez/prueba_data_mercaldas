# 📦 Análisis de Demanda y Compras – Mercaldas

Este proyecto corresponde a una prueba técnica avanzada para el cargo de analista de planeación de la demanda en **Mercaldas**. El objetivo es demostrar habilidades en integración de datos, análisis estratégico, modelado predictivo y visualización de insights accionables para el área de compras.

---

## 📁 Estructura del Proyecto

```bash
project-root/
├── data/
│   ├── raw/                       # Datos originales (Excel .xlsx)
│   └── processed/                 # Tabla analítica procesada (CSV listo para análisis)
├── dashboard/
│   └── mercaldas_analytics.pbix   # Dashboard interactivo en Power BI
├── notebooks/
│   ├── 01_etl.ipynb               # Construcción de tabla consolidada desde fuentes crudas
│   ├── 02_analisis_modelo.ipynb   # Análisis exploratorio, visualización y modelado
│   └── 03_modelo_predictivo.ipynb # Análisis exploratorio, visualización y modelado
├── src/                           # Código fuente de funciones y clases reutilizables
│   └── data_loader.py             # Módulo para cargar datos (ej. la función cargar_datos_ventas)
├── output/                        # Gráficos, reportes PDF, screenshots de dashboard
├── models/                        # Modelos predictivos entrenados (formato .pkl)
├── requirements.txt               # Librerias requeridas para usar este repositorio
└── README.md                      # Documentación general
```

---

## ⚙️ Requisitos

Este proyecto fue desarrollado en Python 3.11 y utiliza las siguientes bibliotecas principales:

```bash
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
openpyxl
```

Puedes instalar los requerimientos con:

```bash
pip install -r requirements.txt
```

---

## 🧪 Flujo de Trabajo

### 1. ETL y Preparación

* Lectura y tipado de datos desde archivo Excel (`/data/raw/`)
* Limpieza y consolidación en una única tabla analítica diaria a nivel `producto–sucursal–fecha`
* Uso de `category` y `datetime64` para eficiencia de memoria
* Cálculo de columnas derivadas:

  * Margen bruto (`precio_venta - costo_unitario`)
  * Indicador binario de si el producto estuvo en promoción
* Exportación final como `.csv` en `data/processed/tabla_consolidada.csv`

#### ❌ Exclusión justificada: Días de Inventario Estimado

El cálculo fue **descartado intencionalmente**. La base de datos tiene muy baja densidad temporal (\~100 compras y \~100 ventas distribuidas en más de 800 días), lo que hace inviable una estimación confiable. Cualquier intento generaría valores sin significado estadístico o divisiones por cero.

Esta decisión refleja criterio técnico, evitando forzar métricas que no están respaldadas por los datos disponibles.

---

### 2. Análisis Estratégico

####  Productos de Alta Rotación

* Se identificaron los **top 10 productos más vendidos por sucursal** durante el último semestre.
* Se evidenció una alta rotación de productos en las categorías **Lácteos** y **Bebidas**, lo cual sugiere líneas prioritarias para abastecimiento y renegociación.

####  Proveedores Problemáticos

* Se analizaron métricas como **plazo de entrega** y **calificación** por proveedor.
* En lugar de umbrales fijos, se aplicaron métodos estadísticos (z-score e IQR) para identificar outliers negativos de forma robusta.
* El proveedor **V010** fue marcado como riesgo potencial por su **plazo de entrega inusualmente alto**, aunque su calificación es buena.
* No se identificaron proveedores con riesgo conjunto (mala calificación y mal plazo).

#### ❌ Exclusión justificada: Rupturas de Inventario

Aunque el enunciado sugiere detectar días con ventas nulas y demanda esperada, esta sección fue excluida tras análisis detallado:

* El volumen de datos es muy bajo (\~100 ventas en 800 días).
* La mayoría de productos tienen muy pocos días con actividad de venta, lo que impide establecer patrones de demanda confiables.
* La inclusión de este análisis introduciría falsos positivos sin sustento real.

Evitarlo preserva la calidad del análisis y refleja una aplicación profesional del criterio analítico.

---

### 3. Dashboard interactivo – Power BI

El archivo `dashboard/mercaldas_analytics.pbix` contiene un dashboard interactivo construido con Power BI, utilizando como insumo principal la tabla consolidada (`tabla_consolidada.csv`).

El dashboard incluye:

1. **Evolución del margen bruto por categoría**

   * Visualizado en cuatro gráficos de líneas, uno por categoría.
   * Cada gráfico incluye una línea de tendencia para facilitar la interpretación del comportamiento en el tiempo.

2. **Relación entre margen bruto y unidades vendidas**

   * Representada mediante un scatterplot, útil para identificar productos con alto volumen y bajo margen, o viceversa.

3. **Top productos más vendidos por sucursal**

   * Mostrado como gráfico de barras horizontales apiladas, lo que permite comparar fácilmente las preferencias por sucursal.

4. **Tabla de evaluación de proveedores**

   * Incluye nombre, calificación y plazo de entrega de cada proveedor (excluye columnas técnicas como z-scores).
   * Útil para identificar proveedores estratégicos o con potencial de revisión.

5. **Filtros dinámicos**

   * Se incorporaron slicers para categoría de producto, sucursal y rango de fechas, permitiendo segmentaciones interactivas por el usuario final.

![Dashboard analítica Mercaldas](output/dashboard.png)
---

### 4. Modelado Predictivo

* Entrenamiento de un modelo de regresión para **predecir demanda semanal** de productos clave
* Incorporación de variables como:

  * Historial de ventas
  * Días de la semana
  * Promociones activas
  * Ubicación de la sucursal
* Evaluación con **MAE y RMSE**
* Recomendaciones para ajustar niveles de compra y negociar cantidades óptimas

---

## 📌 Notas Técnicas

* Todos los `.csv` procesados son generados automáticamente desde notebooks.
* No se deben modificar manualmente.
* Se implementó uso de `category` para columnas categóricas y `parse_dates` para columnas de fechas, con el objetivo de optimizar consumo de memoria y velocidad de procesamiento.

---

## 🧠 Autor

**Pablo Alejandro López Sánchez**  
Data Analyst – Business Analyst
