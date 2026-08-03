"""
ISABELLA v7.0 - BLUEPRINT DE ADMINISTRACIÓN
Endpoints para administración y auditoría
"""

from flask import Blueprint, request, jsonify
import json
import os
from datetime import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

# ==================== ESTADO DEL SISTEMA ====================

@admin_bp.route('/status', methods=['GET'])
def status():
    """Obtener estado del sistema"""
    try:
        import psutil
        
        return jsonify({
            'system': {
                'cpu_percent': psutil.cpu_percent(interval=1),
                'memory_percent': psutil.virtual_memory().percent,
                'disk_percent': psutil.disk_usage('/').percent
            },
            'isabella': {
                'version': '7.0',
                'status': 'operational',
                'uptime': 'running'
            },
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== LOGS ====================

@admin_bp.route('/logs', methods=['GET'])
def logs():
    """Obtener logs de auditoría"""
    try:
        log_file = 'logs/audit.log'
        
        if not os.path.exists(log_file):
            return jsonify({
                'logs': [],
                'total': 0,
                'timestamp': datetime.now().isoformat()
            }), 200
        
        with open(log_file, 'r', encoding='utf-8') as f:
            logs_content = f.readlines()
        
        # Obtener últimos 100 logs
        recent_logs = logs_content[-100:]
        
        return jsonify({
            'logs': recent_logs,
            'total': len(logs_content),
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== REPORTE ====================

@admin_bp.route('/report', methods=['POST'])
def generate_report():
    """Generar reporte de auditoría"""
    try:
        data = request.get_json()
        report_type = data.get('type', 'general')
        
        report = {
            'tipo': report_type,
            'fecha': datetime.now().isoformat(),
            'creador': 'Isabella v7.0',
            'contenido': {
                'resumen': 'Reporte de auditoría generado',
                'vulnerabilidades': [],
                'herramientas_ejecutadas': [],
                'recomendaciones': [
                    'Mantener sistemas actualizados',
                    'Aplicar patches de seguridad',
                    'Usar contraseñas fuertes'
                ]
            }
        }
        
        # Guardar reporte
        report_dir = 'reports'
        os.makedirs(report_dir, exist_ok=True)
        
        report_file = os.path.join(report_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        
        return jsonify({
            'success': True,
            'report_file': report_file,
            'report': report,
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== CONFIGURACIÓN ====================

@admin_bp.route('/config', methods=['GET'])
def get_config():
    """Obtener configuración"""
    try:
        from config import CURRENT_CONFIG, ENV
        
        return jsonify({
            'environment': ENV,
            'debug': CURRENT_CONFIG.DEBUG,
            'testing': CURRENT_CONFIG.TESTING,
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== MEMORIA DE ISABELLA ====================

@admin_bp.route('/memory', methods=['GET'])
def get_memory():
    """Obtener memoria de Isabella"""
    try:
        memoria_file = 'data/isabella_memoria.json'
        
        if os.path.exists(memoria_file):
            with open(memoria_file, 'r', encoding='utf-8') as f:
                memoria = json.load(f)
        else:
            memoria = {'status': 'not initialized'}
        
        return jsonify(memoria), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== ACTUALIZAR MEMORIA ====================

@admin_bp.route('/memory/update', methods=['POST'])
def update_memory():
    """Actualizar memoria de Isabella"""
    try:
        data = request.get_json()
        memoria_file = 'data/isabella_memoria.json'
        
        os.makedirs('data', exist_ok=True)
        
        if os.path.exists(memoria_file):
            with open(memoria_file, 'r', encoding='utf-8') as f:
                memoria = json.load(f)
        else:
            memoria = {}
        
        # Actualizar con nuevos datos
        memoria.update(data)
        memoria['ultima_actualizacion'] = datetime.now().isoformat()
        
        with open(memoria_file, 'w', encoding='utf-8') as f:
            json.dump(memoria, f, indent=4, ensure_ascii=False)
        
        return jsonify({
            'success': True,
            'message': 'Memoria actualizada',
            'timestamp': datetime.now().isoformat()
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
