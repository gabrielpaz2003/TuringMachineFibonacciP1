# 🚀 Máquina de Turing - Cálculo de Fibonacci

Este proyecto implementa una **Máquina de Turing** que calcula la sucesión de Fibonacci utilizando una cinta y una serie de transiciones definidas en un archivo de configuración. Además, se realiza un **análisis empírico del tiempo de ejecución**, generando una regresión polinomial y comparando la complejidad teórica con los datos obtenidos.

---

## 📌 **Características del Proyecto**
- Implementación de una **Máquina de Turing Determinista**.
- Definición de **transiciones** en un archivo externo (`turing_rules.txt`).
- Uso de una **cinta infinita** simulada para el almacenamiento de estados.
- Representación de números naturales mediante **secuencias de 1s**.
- **Visualización** del proceso de cálculo de Fibonacci paso a paso.
- Análisis de **complejidad temporal** con regresión polinomial.

---

## 📂 **Estructura del Proyecto**

```
📂 TuringMachineFibonacci
├── 📁 config
│   ├── turing_rules.txt   # Reglas de transición de la Máquina de Turing
│   ├── turing_setup.txt   # Configuración inicial de la máquina
├── simulator.py          # Código principal para la ejecución y análisis empírico
├── Turing_Machine.py     # Implementación de la Máquina de Turing
├── README.md             # Documentación del proyecto
```

---

## 📜 **Convenciones Utilizadas**

### **📌 Representación de números en la cinta**
- Los números se representan con **secuencias de 1s**:
  - `111` representa el número `3`
  - `11` representa el número `2`
  - `1` representa el número `1`
- Se usa `B` como **símbolo en blanco**.
- Se usa `X` para marcar el inicio del cálculo.

### **📌 Formato de las transiciones (`turing_rules.txt`)**
Cada línea define una transición con la estructura:

```
('Estado actual', 'Símbolo leído'): ('Nuevo estado', 'Símbolo escrito', 'Dirección')
```

Ejemplo:
```
('q0', '1'): ('q101', 'X', 'R')
```

---

## 🚀 **Ejecución del Proyecto**

### **📥 Instalación de dependencias**
Asegúrate de tener **Python 3** instalado. Luego, instala las dependencias necesarias:

```bash
pip install numpy matplotlib graphviz
```

### **🏃‍♂️ Ejecutar el simulador**
Para iniciar la simulación, ejecuta:
```bash
python simulator.py
```

El programa pedirá un número para calcular Fibonacci y mostrará la ejecución paso a paso en la cinta.

### **📊 Generar análisis empírico**
Después de la simulación inicial, el programa ejecutará varias pruebas para analizar el tiempo de ejecución. Se mostrará una gráfica con la regresión polinomial:
```bash
python simulator.py
```

---

## 📈 **Análisis de Complejidad**
- Se ajustó una **regresión polinomial \(O(n^3)\)** al tiempo de ejecución medido.
- La implementación es **más eficiente** que la recursión ingenua \(O(2^n)\).
- Para valores pequeños de \(n\), el tiempo es **casi constante**, pero crece considerablemente para \(n > 10\).

📌 **Conclusión:** La máquina de Turing implementada **es viable** para calcular Fibonacci de forma eficiente dentro de ciertos límites de \( n \).

---

## 📌 **Ejemplo de Salida**

```
🚀  BIENVENIDO A LA MÁQUINA DE TURING - FIBONACCI  🚀

🔢 Ingresa un número para calcular Fibonacci: 3

🌐 Estado: q101  | 📍 Posición: 1
📜 Cinta: X[1]BBBBBBBB
---------------------------------------------
🌐 Estado: q601  | 📍 Posición: 3
📜 Cinta: X11[*]BBBBBBBB
---------------------------------------------
🎯 Fibonacci(3) = 2
⏳ Tiempo de ejecución: 0.042589 segundos
```

📊 **Análisis empírico:**
Se muestra una gráfica con la evolución del tiempo de ejecución respecto al tamaño de la entrada.

---

## 🛠 **Mejoras Futuras**
✅ Optimizar la representación de los números en la cinta.  
✅ Mejorar la eficiencia de las transiciones.  
✅ Implementar otras funciones matemáticas en la Máquina de Turing.  
✅ Refinar la regresión polinomial para mejorar la precisión del modelo.  

---

### 📌 **Autor:**
👨‍💻 *Desarrollado por Gabriel Paz*  
📅 *2025*