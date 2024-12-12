# BOT DE AUTOMATIZACIÓN PARA VIAJES ÉXITO

Este proyecto consiste en el desarrollo de un bot de automatización utilizando **Selenium** y **Python** para interactuar con el sitio web de Viajes Éxito ([https://www.viajesexito.com](https://www.viajesexito.com)). El bot realiza una serie de tareas específicas para buscar paquetes de vuelo + hotel, filtrar resultados y extraer información de precios de manera automática.

---

## **Características del BOT**

1. **Ingreso al sitio web**:
   - El bot accede al sitio web de Viajes Éxito y navega al apartado de paquetes de vuelo + hotel.

2. **Configuración de búsqueda**:
   - Origen: Aeropuerto José María Córdova de Medellín.
   - Destino: Aeropuerto de Cancún, México.
   - Fechas:
     - Salida: 2X de diciembre de 2024 (X = 6).
     - Regreso: 0X de enero de 2025 (X = 7).
   - Habitaciones:
     - 1 habitación para 2 adultos.
     - 1 habitación para 3 adultos.

3. **Extracción de precios**:
   - El bot recopila los precios de todos los paquetes en la primera página de resultados y los muestra en la consola.

4. **Búsqueda avanzada**:
   - Filtra los resultados por una aerolínea seleccionada (por ejemplo, United Airlines) y realiza nuevamente la búsqueda.

5. **Acceso al contacto**:
   - Navega a la sección de "Contáctanos" y hace clic en el enlace de WhatsApp de la agencia.

6. **Cierre del WebDriver**:
   - Finaliza el proceso de automatización cerrando el navegador correctamente para evitar procesos en segundo plano.

---

## **Requisitos del sistema**

- Python 3.x
- Google Chrome (versión compatible con el controlador `chromedriver`)
- `chromedriver` (colocado en la carpeta `driver/` del proyecto)
- Librerías Python:
  - Selenium

Para instalar Selenium, ejecuta:
```bash
pip install selenium
```

---

## **Cómo ejecutar el proyecto**

1. Clona este repositorio:
   ```bash
   git clone https://github.com/IsaMontoya17/Ejercicio-Selenium.git
   ```

2. Abre la carpeta en donde quedó el repositorio de Visual Studio Code.
3. Ejecuta el archivo index.py.

---

## **Video demostrativo**

Puedes ver el bot ejecutándose en el siguiente enlace:
[Video del bot en acción](ENLACE_DEL_VIDEO)

---

## **Estructura del código**

El código está documentado con comentarios detallados para facilitar su comprensión y mantenimiento. Las tareas se realizan en el siguiente orden:

1. **Inicio del WebDriver**: Configura y maximiza el navegador.
2. **Selección de vuelos y configuración de filtros**:
   - Establece origen, destino y fechas.
   - Configura habitaciones para los pasajeros.
3. **Extracción de precios**: Recolecta y muestra los precios de los paquetes disponibles en la consola.
4. **Búsqueda avanzada**: Filtra resultados por aerolínea.
5. **Acceso a "Contáctanos"**: Navega al enlace de WhatsApp.
6. **Cierre del WebDriver**: Finaliza el proceso correctamente.

---

## **Colaboradores**

- **Isabela Montoya**  
  [GitHub: IsaMontoya17](https://github.com/IsaMontoya17)

- **Sara Castañeda**  
  [GitHub: Saraccee25](https://github.com/Saraccee25)

---


---

¡Gracias por usar nuestro bot de automatización para Viajes Éxito! Si tienes dudas o problemas, no dudes en contactarnos.

