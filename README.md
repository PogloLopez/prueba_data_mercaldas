# 📦 Análisis de Demanda y Compras – Mercaldas

Este proyecto corresponde a una prueba técnica avanzada para el cargo de analista de planeación de la demanda en **Mercaldas**. El objetivo es demostrar habilidades en integración de datos, análisis estratégico, modelado predictivo y visualización de insights accionables para el área de compras.

---

## 📁 Estructura del Proyecto

```bash
project-root/
├── data/
│   ├── raw/              # Datos originales (Excel .xlsx)
│   ├── processed/        # Tabla analítica procesada (CSV listo para análisis)
├── notebooks/
│   ├── 01_etl_preparacion.ipynb   # Construcción de tabla consolidada desde fuentes crudas
│   └── 02_analisis_modelo.ipynb   # Análisis exploratorio, visualización y modelado
├── output/               # Gráficos, reportes PDF, screenshots de dashboard
├── models/               # Modelos predictivos entrenados (formato .pkl)
└── README.md             # Documentación general
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

#### 🔹 Productos de Alta Rotación

* Se identificaron los **top 10 productos más vendidos por sucursal** durante el último semestre.
* Se evidenció una alta rotación de productos en las categorías **Lácteos** y **Bebidas**, lo cual sugiere líneas prioritarias para abastecimiento y renegociación.

#### 🔹 Proveedores Problemáticos

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

### 3. Visualización

* Se desarrollará un dashboard dinámico (Power BI o Python) con:

  * Evolución del margen por categoría
  * Ranking de productos más vendidos vs. rentables
  * Panel de monitoreo para proveedores y riesgo operativo

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
