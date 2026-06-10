import os
import google.generativeai as genai

# 1. Configuración de la API de Gemini
# Asegúrate de configurar tu API key en las variables de entorno de tu sistema:
# En Windows: setx GEMINI_API_KEY "tu_api_key_aquí"
# En Linux/Mac: export GEMINI_API_KEY="tu_api_key_aquí"

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("[ERROR] No se encontró la variable de entorno GEMINI_API_KEY.")
    print("Por favor, configúrala antes de ejecutar el programa.")
    exit(1)

genai.configure(api_key=API_KEY)

def analizar_sistema_riego(humedad_suelo, nivel_tanque_cm, estado_bomba, flujo_agua_lpm):
    """
    Envía los datos analógicos y de estado del sistema de riego a Gemini 
    para obtener un diagnóstico de ingeniería y optimización de recursos.
    """
    # Usamos el modelo estable actual para tareas de texto y análisis
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Estructuramos un prompt de ingeniería claro y preciso
    prompt = f"""
    Actúa como un Ingeniero experto en Automatización y Gestión de Recursos Hídricos.
    Analiza los siguientes datos en tiempo real de un sistema de riego automatizado:
    
    - Humedad del suelo actual: {humedad_suelo}%
    - Nivel del tanque de agua (distancia al sensor ultrasónico): {nivel_tanque_cm} cm (A mayor distancia, más vacío está el tanque. Máximo vacío: 100cm, Lleno: 10cm).
    - Estado actual de la bomba de agua: {estado_bomba}
    - Flujo de agua detectado: {flujo_agua_lpm} Litros por minuto (LPM)
    
    Por favor, genera un reporte breve y estructurado que incluya:
    1. Diagnóstico de Eficiencia: ¿El estado de la bomba coincide lógicamente con el flujo de agua y la humedad? (Detectar posibles fugas si la bomba está encendida pero el flujo es 0, o anomalías similares).
    2. Alertas de Mantenimiento: Evaluación del nivel del tanque y estado del hardware.
    3. Recomendación de Optimización: Sugerencia de tiempo de activación o apagado basado en la humedad.
    """
    
    try:
        print("\n[INFO] Conectando con Gemini AI para análisis técnico...")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[ERROR] No se pudo conectar o procesar con Gemini: {str(e)}"

def main():
    print("=========================================================")
    print("  SISTEMA INTELIGENTE DE DIAGNÓSTICO DE RIEGO (GEMINI AI) ")
    print("=========================================================")
    
    # Simulación de lectura de sensores (estos datos vendrían de un Arduino/microcontrolador)
    # Escenario de prueba: Bomba encendida pero no hay flujo de agua (Posible falla/tubería tapada)
    humedad = 25          # %
    distancia_tanque = 85 # cm (Tanque casi vacío)
    bomba_estado = "ENCENDIDA"
    flujo = 0.0          # LPM (Anomalía detectada)
    
    print(f"\n--- Datos de Sensores Recibidos ---")
    print(f"* Humedad Suelo: {humedad}%")
    print(f"* Distancia Ultrasónico Tanque: {distancia_tanque} cm")
    print(f"* Estado Bomba: {bomba_estado}")
    print(f"* Sensor de Flujo: {flujo} LPM")
    
    # Ejecutar el análisis con IA
    reporte = analizar_sistema_riego(humedad, distancia_tanque, bomba_estado, flujo)
    
    print("\n================ REPORTES Y DIAGNÓSTICO IA ================")
    print(reporte)
    print("===========================================================")

if __name__ == "__main__":
    main()
