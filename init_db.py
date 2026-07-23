#!/usr/bin/env python
"""
INIT_DB.py - Inicialización de Base de Datos
© Juan Alberto López Vázquez
"""

import os
import json
from datetime import datetime

def init_database():
    """Inicializa la base de datos y archivos necesarios"""
    
    # Crear directorios
    directories = [
        'data',
        'data/isabella_versions',
        'logs',
        'uploads',
        'downloads',
        'extractions',
        'reports',
        'wordlists',
        'static',
        'static/css',
        'static/js',
        'static/img',
        'templates'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Crear archivo de memoria de Isabella
    memoria_file = 'data/isabella_memoria.json'
    if not os.path.exists(memoria_file):
        memoria = {
            "version": "7.0",
            "creador": "Juan Alberto López Vázquez",
            "creada_en": datetime.now().isoformat(),
            "estado": "operacional",
            "sesiones_totales": 0,
            "auditorias_completadas": 0,
            "vulnerabilidades_encontradas": 0,
            "herramientas_ejecutadas": {},
            "mejoras_implementadas": 0,
            "codigo_mejorado": [],
            "desarrolladores_colaboradores": [],
            "ultima_actualizacion": datetime.now().isoformat()
        }
        with open(memoria_file, 'w', encoding='utf-8') as f:
            json.dump(memoria, f, indent=4, ensure_ascii=False)
        print(f"✓ Memoria de Isabella creada: {memoria_file}")
    
    # Crear archivo de feedback
    feedback_file = 'data/isabella_feedback.json'
    if not os.path.exists(feedback_file):
        with open(feedback_file, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)
        print(f"✓ Archivo de feedback creado: {feedback_file}")
    
    # Crear archivo de mejoras de código
    improvements_file = 'data/isabella_code_improvements.json'
    if not os.path.exists(improvements_file):
        with open(improvements_file, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)
        print(f"✓ Archivo de mejoras creado: {improvements_file}")
    
    # Crear archivo de developers
    developers_file = 'data/registered_developers.json'
    if not os.path.exists(developers_file):
        with open(developers_file, 'w', encoding='utf-8') as f:
            json.dump([], f, indent=4)
        print(f"✓ Archivo de developers creado: {developers_file}")
    
    # Crear archivo de logs
    log_file = 'logs/audit.log'
    if not os.path.exists(log_file):
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(f"[{datetime.now().isoformat()}] Isabella v7.0 inicializada\n")
        print(f"✓ Archivo de logs creado: {log_file}")
    
    print("\n" + "="*60)
    print("✓ Base de datos inicializada correctamente")
    print("="*60)
    print("\nArchivos creados:")
    print("  - data/isabella_memoria.json (Memoria de Isabella)")
    print("  - data/isabella_feedback.json (Feedback del usuario)")
    print("  - data/isabella_code_improvements.json (Mejoras de código)")
    print("  - data/registered_developers.json (Developers colaboradores)")
    print("  - logs/audit.log (Logs de auditoría)")
    print("\nDirectorios creados:")
    print("  - data/ (Almacenamiento de datos)")
    print("  - logs/ (Logs del sistema)")
    print("  - uploads/ (Archivos cargados)")
    print("  - downloads/ (Descargas)")
    print("  - extractions/ (Extracciones web)")
    print("  - reports/ (Reportes)")
    print("  - wordlists/ (Diccionarios de contraseñas)")
    print("\n¡Sistema listo para usar! Ejecuta: python app.py")

if __name__ == '__main__':
    print("""
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║           ISABELLA v7.0 - INICIALIZANDO BASE DE DATOS        ║
    ║                                                              ║
    ║        © 2024 Juan Alberto López Vázquez                  ║
    ║                                                              ║
    ╚════════════════════════════════════════════════════════════════╝
    """)
    init_database()
