# Análisis Bioinformático en Docker con Biopython

Este repositorio contiene un ejemplo simple de cómo usar Docker para analizar secuencias en formato FASTA usando Biopython.

## Archivos

- `analisis.py`: script en Python que analiza el largo y el contenido GC.
- `requirements.txt`: dependencias (solo `biopython`).
- `Dockerfile`: definición del contenedor.
- `ejemplo.fasta`: archivo de ejemplo con secuencias de ADN y proteína.

## Cómo usar

1. Construir la imagen:
```bash
docker build -t bioinfo-analisis .
