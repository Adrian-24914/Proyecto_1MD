# Calculadora de Operaciones de Conjuntos

Implementación en Python de una calculadora completa para operaciones de teoría de conjuntos.

## Autores
- Fatima Navarro
- Adrian Penagos
- Diego Quixchan
- Wilson Peña
- Tracey Dally Ramirez

## Descripción

Este programa permite realizar operaciones matemáticas fundamentales con conjuntos, incluyendo:

- **Unión** (A ∪ B)
- **Intersección** (A ∩ B)
- **Diferencia** (A \ B)
- **Complemento** (¬A)
- **Producto cartesiano** (A × B)
- **Verificación de funciones**
- **Operaciones con paréntesis** ((A ∪ B) ∩ C)

## Conjuntos Predefinidos

El programa incluye conjuntos de ejemplo según la especificación del proyecto:

```
U = {a,b,c,d,e,f,g,h,i,j,k,1,2,3,4,5}  (conjunto universal)
A = {a,1,3,d,g,h,4,5}
B = {2,1,4,e,f,g,k}
C = {b,d,f,h,k,2,4}
D = {}  (conjunto vacío)
E = {(1,a),(2,b),(3,c)}  (para verificación de funciones)
```

## Estructura del Proyecto

```
├── operaciones_conjuntos.py    # Lógica matemática
├── main.py                     # Interfaz de usuario
├── README.md                   # Este archivo
└── documentacion.tex           # Documentación en LaTeX
```

## Requisitos

- Python 3.6 o superior
- No se requieren librerías externas

## Instalación y Uso

1. **Clonar el repositorio:**
   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd calculadora-conjuntos
   ```

2. **Ejecutar el programa:**
   ```bash
   python main.py
   ```
   
   O si tienes Python 3 específicamente:
   ```bash
   python3 main.py
   ```

## Opciones de Inicialización

Al ejecutar el programa, puedes elegir:

1. **Conjuntos predefinidos** - Usar los conjuntos del ejercicio
2. **Crear conjuntos personalizados** - Definir tus propios conjuntos
3. **Empezar desde cero** - Crear conjuntos durante el uso

## Ejemplos de Uso

### Crear elementos simples:
```
Elementos: a,1,b,2,c
```

### Crear parejas ordenadas:
```
Elementos: (1,a),(2,b),(3,c)
```

### Operaciones disponibles:
- Selecciona dos conjuntos para unión, intersección o diferencia
- Usa el conjunto universal U para operaciones de complemento
- Verifica si un conjunto de parejas ordenadas es una función

## Características Técnicas

- **Arquitectura modular** - Separación entre lógica y interfaz
- **Validación robusta** - Manejo de errores sin crashes
- **Soporte de tipos mixtos** - Números y texto en el mismo conjunto
- **Parsing inteligente** - Detecta automáticamente parejas ordenadas
- **Interfaz intuitiva** - Menús claros y fáciles de usar

## Verificación de Funciones

El programa analiza si un conjunto de parejas ordenadas representa una función matemática:

- ✅ **Es función**: Cada elemento del dominio aparece exactamente una vez
- ❌ **No es función**: Hay elementos repetidos en el dominio

Ejemplo:
```
E = {(1,a),(2,b),(3,c)} → ES función
F = {(1,a),(1,b),(2,c)} → NO es función (1 aparece dos veces)
```

## Documentación

La documentación completa está disponible en el archivo `documentacion.tex` con:
- Especificación técnica detallada
- Casos de prueba con pantallazos
- Análisis de resultados
- Código fuente comentado

## Compilar Documentación

```bash
pdflatex documentacion.tex
```

## Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-operacion`)
3. Commit tus cambios (`git commit -am 'Agregar nueva operación'`)
4. Push a la rama (`git push origin feature/nueva-operacion`)
5. Abre un Pull Request

## Licencia

Este proyecto es de uso académico para el curso de Teoría de Conjuntos.

## Soporte

Para preguntas o problemas, contacta a cualquiera de los autores del proyecto.
