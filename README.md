# 📦 Análisis de Demanda y Compras – Mercaldas

Este proyecto corresponde a una prueba técnica avanzada para el cargo de analista de planeación de la demanda en **Mercaldas**. El objetivo es demostrar habilidades en integración de datos, análisis estratégico, modelado predictivo y visualización de insights accionables para el área de compras.

---

## 📁 Estructura del Proyecto

```

project-root/
├── data/
│   ├── raw/              # Datos originales (Excel .xlsx)
│   ├── processed/        # Tabla analítica procesada (CSV listo para análisis)
├── notebooks/
│   ├── 01\_etl\_preparacion.ipynb   # Construcción de tabla consolidada desde fuentes crudas
│   └── 02\_analisis\_modelo.ipynb   # Análisis exploratorio, visualización y modelado
├── outputs/              # Gráficos, reportes PDF, screenshots de dashboard
├── models/               # Modelos predictivos entrenados (formato .pkl)
└── README.md             # Documentación general

````

---

## ⚙️ Requisitos

Este proyecto fue desarrollado en Python 3.11 y usa las siguientes bibliotecas principales:

```bash
pandas
numpy
matplotlib / seaborn
scikit-learn
xgboost
openpyxl
````

Puedes instalar los requerimientos con:

```bash
pip install -r requirements.txt
```

---

## 🧪 Flujo de Trabajo

### 1. ETL y Preparación

* Limpieza y tipado de datos desde Excel (`/data/raw/`)
* Generación de una tabla analítica diaria por `producto-sucursal-fecha`
* Cálculo de métricas como:

  * Margen bruto (`precio_venta - costo_unitario`)
  * Flag de producto en promoción
  * Consolidación de compras y ventas

#### 🔍 Nota sobre "Días de Inventario Estimado"

El cálculo de esta métrica fue **intencionalmente descartado**, pese a estar planteada en el enunciado de la prueba, debido a la naturaleza de los datos disponibles. La baja densidad de registros (solo \~100 compras y \~100 ventas distribuidas en un rango de más de 800 días) hace inviable una estimación confiable y representativa.

Incluir este indicador en este contexto introduciría ruido estadístico y visual, generando valores artificialmente altos, divisiones por cero y sin interpretación operativa válida.

Esta decisión se alinea con buenas prácticas analíticas y refleja un criterio profesional al evitar métricas irrelevantes cuando los datos no las sustentan.

### 2. Análisis Estratégico

* Identificación de productos de alta rotación
* Detección de rupturas de inventario (ventas = 0 con demanda histórica)
* Evaluación de proveedores problemáticos (plazo y precio)

### 3. Visualización

* Dashboard dinámico en Power BI  
* Ranking de productos más rentables vs más vendidos
* Alertas por categoría y quiebres

### 4. Modelado Predictivo

* Predicción de demanda semanal para productos clave
* Integración de variables como promociones, historial y comportamiento por sucursal
* Evaluación con MAE / RMSE
* Exportación de modelo y recomendaciones para ajustar compras

---

## 📌 Notas Técnicas

* Todos los archivos `.csv` procesados son generados desde notebooks. No deben editarse manualmente.
* La tabla final se guarda en `data/processed/tabla_consolidada.csv`.
* El uso de `category` y `parse_dates` está optimizado para eficiencia de memoria.

---

## 🧠 Autor

**Pablo Alejandro López Sánchez**  
Data Analyst - Business Analyst
