import time
import numpy as np
import matplotlib.pyplot as plt
from Turing_Machine import generar_cinta, construir_maquina

def mostrar_banner():
    print("=" * 60)
    print("🚀  BIENVENIDO A LA MÁQUINA DE TURING - FIBONACCI  🚀")
    print("=" * 60)

def mostrar_resultado(num, resultado, execution_time):
    print("\n" + "-" * 60)
    print(f"🎯 Fibonacci({num}) = {resultado}")
    print(f"⏳ Tiempo de ejecución: {execution_time:.6f} segundos")
    print("-" * 60 + "\n")

def medir_tiempos(max_n=19):
    tamanos_entrada = []
    tiempos_ejecucion = []

    print("\n📊 Iniciando análisis empírico de la ejecución...\n")

    for n in range(1, max_n + 1):
        input_cinta = generar_cinta(n)
        maquina = construir_maquina(input_cinta)

        start_time = time.time()
        resultado = maquina.calcular_fibonacci(mostrar_proceso=False).count('1')
        end_time = time.time()
        execution_time = end_time - start_time

        tamanos_entrada.append(n)
        tiempos_ejecucion.append(execution_time)

        print(f"🔢 n={n:2} | Fibonacci({n:2})={resultado:5} | ⏳ Tiempo={execution_time:.6f} s")

    # Graficar resultados
    plt.figure(figsize=(10, 6))
    plt.scatter(tamanos_entrada, tiempos_ejecucion, color='blue', label="Tiempos de ejecución")

    coeficientes = np.polyfit(tamanos_entrada, tiempos_ejecucion, 3)  
    polinomio = np.poly1d(coeficientes)
    x_vals = np.linspace(min(tamanos_entrada), max(tamanos_entrada), 100)
    y_vals = polinomio(x_vals)

   

    plt.plot(x_vals, y_vals, color='red', label="Regresión polinomial (O(n³))")

    plt.plot(x_vals, x_vals * 1e-3, 'g--', label="O(n)")
    plt.plot(x_vals, 2**x_vals * 1e-6, 'm--', label="O(2ⁿ)")

    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("📈 Análisis empírico de la Máquina de Turing - Fibonacci")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    mostrar_banner()

    # Solicitar solo un número y calcular su Fibonacci
    num = input("\n🔢 Ingresa un número para calcular Fibonacci: ")

    try:
        num = int(num)
        if num < 0:
            print("⚠️ Ingresa un número natural válido (mayor o igual a 0).")
            exit()
    except ValueError:
        print("❌ Entrada inválida. Ingresa un número válido.")
        exit()

    # Medir tiempo de ejecución para la entrada del usuario
    start_time = time.time()
    input_cinta = generar_cinta(num)
    maquina = construir_maquina(input_cinta)
    resultado = maquina.calcular_fibonacci(mostrar_proceso=True).count('1')
    end_time = time.time()
    execution_time = end_time - start_time

    mostrar_resultado(num, resultado, execution_time)

    # Ejecutar análisis empírico después del cálculo
    medir_tiempos()
