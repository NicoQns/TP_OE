# 🌡️ Análisis Climático: Temperatura y Precipitaciones

Proyecto desarrollado para la cátedra de **Organización Empresarial** — UTN Tecnicatura Universitaria en Programación (2026).

---

## Descripción

Script en Python que procesa datos meteorológicos históricos para calcular indicadores climáticos básicos y generar visualizaciones de la evolución de temperatura.

## Integrantes

| Rol | Nombre |
|---|---|
| P1 — Líder y Organizador | Nicolas Quinones/Ezequiel Callerame |
| P2 — Desarrollador Técnico | Nicolas Quinones |
| P3 — Revisor y QA | Ezequiel Callerame |

## Escenario

**Escenario A — Análisis de Datos Climáticos**

## Dataset

Archivo CSV con registros de temperatura y precipitaciones almacenado en `/datos/data.csv`. Columnas: `temperatura`, `precipitacion`.

## Resultados generados

Los resultados se guardan automáticamente en `/resultados`:
- `resultados.csv` — tabla con los indicadores calculados
- `temperatura.png` — gráfico de evolución de temperatura

## Instrucciones de ejecución

1. Clonar el repositorio
2. Entrar a la carpeta `/scripts` desde la terminal
3. Ejecutar el script:

```bash
cd scripts
python analisis_datos.py
```
