"""
ISABELLA v7.0 - BLUEPRINT ADMINISTRATIVO
© Juan Alberto López Vázquez
"""

from flask import Blueprint, request, jsonify
import json
import os
from datetime import datetime

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin_bp.route('/status', methods=['GET'])
def system_status():
    """Estado del sistema"""
    import psutil
    
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return jsonify({
            'cpu': {
                'percent': cpu_percent,
                'cores': psutil.cpu_count()
            },
            'memory': {
                'percent': memory.percent,
                'total_gb': memory.total / (1024**3),
                'available_gb': memory.available / (1024**3)
            },
            'disk': {
                'percent': disk.percent,
                'total_gb': disk.total / (1024**3),
                'free_gb': disk.free / (1024**3)
            },
            'timestamp': datetime.now().isoformat()
        }), 200
    except:
        return jsonify({'error': 'No se pudo obtener estado del sistema'}), 500

@admin_bp.route('/logs', methods=['GET'])
def get_logs():
    """Obtiene logs de auditoría"""
    log_file = 'logs/audit.log'
    
    if not os.path.exists(log_file):
        return jsonify({'logs': [], 'total': 0}), 200
    
    try:
        with open(log_file, 'r') as f:
            logs = f.readlines()[-100:]  # Últimas 100 líneas
        
        return jsonify({
            'logs': logs,
            'total': len(logs)
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/report', methods=['POST'])
def generate_report():
    """Genera reporte de auditoría"""
    data = request.get_json()
    
    report = {
        'title': data.get('title', 'Reporte de Auditoría'),
        'date': datetime.now().isoformat(),
        'creator': 'Juan Alberto López Vázquez',
        'findings': data.get('findings', []),
        'vulnerabilities': data.get('vulnerabilities', []),
        'recommendations': data.get('recommendations', [])
    }
    
    # Guardar reporte
    report_file = f"reports/reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    os.makedirs('reports', exist_ok=True)
    
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    
    return jsonify({
        'success': True,
        'report_file': report_file
    }), 200
