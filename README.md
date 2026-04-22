# Rutinas de Métodos Numéricos 2026.1

Repositorio de apoyo para la asignatura **Métodos Numéricos**, correspondiente al período 2026.1.  
Incluye rutinas básicas para la resolución de sistemas de ecuaciones lineales.
A su vez, incluye un manual de instalacion de **Conda** y **VS Code**.

Para mas detalles del uso de las rutinas
[Manual de Rutinas (notebook de colab)](https://colab.research.google.com/drive/1JiHJ7C_KdygbSoao8jEVzR2YqU7uvw8m#scrollTo=0-czjVAQb-r5)

Unidad 1: Sistemas Lineales
- [RUTINA1](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA1.py): Eliminacion Gaussina (Método Directo)
- [RUTINA2](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA2.py): Gauss-Jacobi (Metodo Iterativo)
- [RUTINA3](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA3.py): Gauss-Seidel (Metodo Iterativo)

Unidad 2: Sistemas No Lineales (Caso Unidimensional)
- [RUTINA4](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA4.py): Método de la Bisección
- [RUTINA5](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA5.py): Método de la Falsa Posición
- [RUTINA6](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA6.py): Método de Newton-Raphson para sistemas no lineales *unidimensionales f(x)=0*
- [RUTINA7](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA7.py): Método del Punto fijo
- [RUTINA8](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA8.py): Método de Secante

Unidad 2.2: Sistemas No Lineales (Caso Multidimensional) y Unidad 3: Optimización numérica
- [RUTINA9](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA9.py): Método de Newton - Raphson para sistemas no lineales *multidimensionales F(X)=0_n*

Unidad 4: Interpolacion e Integración numerica
- [RUTINA10](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA10.py): Calculo del coeficiente de correlación lineal
- [RUTINA11](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA11.py): Polinomio interpolador por matriz de Vandermonde
- [RUTINA12](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA12.py): Polinomio interpolador de Lagrange
- [RUTINA13](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA13.py): Polinomio interpolador de Newton
- [RUTINA14](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA14.py): Integración por el metodo del Trapecio
- [RUTINA14.1](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA14.1.py): Integración por el metodo del Trapecio con datos tabulados
- [RUTINA15](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA15.py): Integración por Simpson 1/3
- [RUTINA15.1](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA15.1.py): Integración por Simpson 1/3 con datos tabulados
- [RUTINA16](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA16.py): Integración por Simpson 3/8
- [RUTINA16](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA16.1.py): Integración por Simpson 3/8 con datos tabulados

Unidad 5: Ecuaciones Diferenciales
- [RUTINA17](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA17.py): Derivada por Diferencias Progresivas
- [RUTINA18](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA18.py): Derivada por Diferencias Centradas
- [RUTINA19](https://github.com/carlobeni/Rutinas-de-Metodos-Numericos-2026.1/blob/main/RUTINA19.py): Derivada por Diferencias Regresivas





#### *Historial de actualizaciones de rutinas*:
- _13/02/2026_: Incorporacion de verificacion por determinante en `RUTINA1`, Actualizacion de producto con np.dot en `RUTINA2` y `RUTINA3`, `RUTINA 6` y `RUTINA 7` intercambiaron de nombre para coincidir con el [RUTINAS.txt](https://eaula.ing.una.py/pluginfile.php/230010/mod_resource/content/1/RUTINAS.txt) oficial de la catedra
- _04/09/2026_: Incorporación del cálculo del coeficiente de correlación de Pearson en `RUTINA010` para evaluar la calidad del ajuste no lineal, implementación de interpolación polinómica mediante matriz de Vandermonde en `RUTINA011`, adición del método de interpolación de Lagrange en `RUTINA012` y construcción incremental del polinomio interpolante mediante el esquema de Newton en `RUTINA013`, además de la reubicación de las rutinas de cálculo de integrales a `RUTINA014`, `RUTINA015` y `RUTINA016`*


##  Para la instalacion de Conda + VS Code

#### Instalación de Conda
Conda es un **gestor de entornos virtuales y paquetes** ampliamente utilizado en ciencia de datos, ingeniería y computación científica.  
Permite crear entornos aislados con versiones específicas de **Python** y sus librerías, evitando conflictos entre proyectos.

1.  **Descarga Miniconda** (recomendado por ser ligero):  
    [Enlace de descarga](https://drive.google.com/open?id=1iDMDOdSDpe13DB6RUY16saTUqJUDocM0&usp=drive_fs)

2.  **Instalación:** Ejecuta el instalador y sigue los pasos por defecto.  
    *Nota: En Windows, se recomienda marcar la opción "Add Miniconda to PATH" para facilitar el uso en la terminal.*

3.  **Verificación:** Abre una terminal (CMD o PowerShell) y ejecuta:
    ```bash
    conda --version
    ```

4.  **Crear un entorno virtual:**
    ```bash
    conda create -n metodos-numericos python=3.12
    ```

5.  **Activar el entorno:**
    ```bash
    conda activate metodos-numericos
    ```

6.  **Instalar dependencias**
    ```bash
    conda install numpy matplotlib scipy pandas ipykernel
    pip install jax jaxlib
    ```
    *(Usamos `pip` para JAX ya que es el método oficial recomendado para obtener las últimas versiones compatibles).*

7. **Registro de entorno en Jupyter**
    ```bash
    python -m ipykernel install --user --name metodos-numericos --display-name "Python (metodos-numericos)"
    ```
---

#### Instalación de VS Code (Visual Studio Code)
Es el editor de código (IDE) donde escribiremos y ejecutaremos nuestras rutinas.

1.  **Descarga VS Code:** [Enlace de descarga](https://drive.google.com/open?id=1X9ZI900FQ-AbXGKRc-z1zBdHEPQif-cL&usp=drive_fs)

2.  **Configuración de Extensiones:** Una vez instalado, abre VS Code, ve al icono de **Extensions** (o presiona `Ctrl+Shift+X`) e instala las siguientes extensiones de Microsoft:
    * **Python**
    * **Jupyter**

---

#### Configuración con Jupyter Notebook
Para ejecutar notebooks (`.ipynb`) utilizando el entorno de Conda creado:

1.  **Crear o abrir un archivo:** Crea un archivo con extensión `.ipynb`.
2.  **Seleccionar el Kernel:** En la esquina superior derecha del editor, haz clic en **"Select Kernel"** (Seleccionar kernel).
3.  **Elegir el entorno:** Selecciona **Python (metodos-numericos)** y busca el entorno que creamos anteriormente: `metodos-numericos`.
4.  **Verificación:** Escribe el siguiente código en una celda y ejecútalo para confirmar que todo funciona:
    ```python
    import jax
    import numpy as np
    print("JAX instalado correctamente. Versión:", jax.__version__)
    ```
