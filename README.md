# Pez: Asistente Personal Basado en Arduino y Python

**Pez** es un asistente personal que combina hardware y software, diseñado para ejecutar múltiples tareas mediante comandos de voz. Este asistente está basado en Arduino y Python y permite desde el control de luces LED RGB y un motor hasta la reproducción de música y videos mediante integración con Spotify y YouTube, además de realizar búsquedas en internet y generar respuestas conversacionales.

## Funcionalidades

- **Control de LEDs RGB**: Enciende y apaga luces de diferentes colores en respuesta a comandos.
- **Control de Motor y Servo**: Realiza acciones mecánicas controlando un motor DC y un servo, con comandos como encender y apagar el motor y abrir o cerrar una puerta.
- **Reproducción de Música y Video**: Controla la reproducción en Spotify y YouTube mediante comandos de voz.
- **Búsqueda en Internet**: Ejecuta búsquedas en Google usando comandos de voz.
- **Interacciones Inteligentes**: Usa la API de OpenAI para respuestas conversacionales en tiempo real.
  
## Componentes de Hardware

1. **Arduino** para el control de hardware.
   - **Motor DC**: Controlado mediante un puente H y modulación PWM.
   - **Servo Motor**: Control para la apertura y cierre de puertas.
   - **LED RGB**: LED que cambia de color según comandos.
2. **Microfono**: Captura comandos de voz para su procesamiento.

## Tecnologías Utilizadas

- **Arduino** para control y manipulación de hardware.
- **Python** para procesamiento de comandos, gestión de APIs y procesamiento de voz.
- **Spotify API** para reproducción y control de música.
- **OpenAI API** para interacciones y respuestas conversacionales.
 
## Resultados y Mejoras

**Resultados Actuales**: Pez permite controlar dispositivos físicos como motores y LEDs, y gestionar contenido multimedia mediante comandos de voz. La integración con Arduino y varias APIs proporciona una experiencia interactiva y personalizada.

**Posibles Mejoras**:
- Optimizar el reconocimiento de voz para mayor precisión en comandos.
- Expandir las capacidades de IA para mejorar la interacción conversacional.
- Agregar sensores adicionales para un asistente más reactivo.
  
---
