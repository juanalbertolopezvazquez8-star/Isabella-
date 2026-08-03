"""
ISABELLA v7.0 - BLUEPRINT DE IA Y DEVELOPERS
© Juan Alberto López Vázquez
VERSIÓN PRODUCTION-READY 100%
"""

from flask import Blueprint, request, jsonify
from core.isabella_ai import isabella_ai
from core.isabella_ai_engine import isabella_ai_engine
from datetime import datetime
import json

ia_bp = Blueprint('ia', __name__, url_prefix='/api/ia')

# ==================== MOTOR IA ====================

@ia_bp.route('/consultar', methods=['POST'])
def consultar_ia():
    """Consulta el motor de IA integrado sin filtros"""
    try:
        data = request.get_json()
        consulta = data.get('consulta')
        
        if not consulta:
            return jsonify({'error': 'Consulta requerida'}), 400
        
        resultado = isabella_ai.consultar_ia(consulta)
        
        return jsonify({
            'success': True,
            'resultado': resultado,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ia_bp.route('/payloads/<categoria>', methods=['GET'])
def obtener_payloads(categoria):
    """Obtiene payloads de una categoría específica"""
    try:
        payloads = isabella_ai.obtener_payloads(categoria)
        
        return jsonify({
            'success': True,
            'categoria': categoria,
            'total': len(payloads),
            'payloads': payloads,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ia_bp.route('/tecnicas-bypass', methods=['GET'])
def obtener_tecnicas_bypass():
    """Obtiene técnicas de bypass integradas"""
    try:
        tecnicas = isabella_ai.obtener_tecnicas_bypass()
        
        return jsonify({
            'success': True,
            'tecnicas': tecnicas,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ia_bp.route('/generar-reporte', methods=['POST'])
def generar_reporte():
    """Genera reportes mediante IA"""
    try:
        data = request.get_json()
        tipo_auditoria = data.get('tipo', 'general')
        
        reporte = isabella_ai.generar_reporte(tipo_auditoria)
        
        return jsonify({
            'success': True,
            'reporte': reporte,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== RETROALIMENTACIÓN ====================

@ia_bp.route('/feedback/registrar', methods=['POST'])
def registrar_feedback():
    """Registra feedback del usuario"""
    try:
        data = request.get_json()
        usuario = data.get('usuario', 'anonymous')
        feedback = data.get('feedback')
        puntuacion = data.get('puntuacion', 5)
        
        if not feedback:
            return jsonify({'error': 'Feedback requerido'}), 400
        
        resultado = isabella_ai.registrar_feedback(usuario, feedback, puntuacion)
        
        if 'error' in resultado:
            return jsonify(resultado), 400
        
        return jsonify(resultado), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ia_bp.route('/feedback/lista', methods=['GET'])
def listar_feedback():
    """Lista todo el feedback registrado"""
    try:
        limite = request.args.get('limite', 20, type=int)
        feedback = isabella_ai.obtener_feedback(limite)
        
        return jsonify({
            'success': True,
            'total': len(feedback),
            'feedback': feedback,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== DEVELOPERS Y COLABORADORES ====================

@ia_bp.route('/developers/registrar', methods=['POST'])
def registrar_developer():
    """Registra nuevo desarrollador colaborador"""
    try:
        data = request.get_json()
        nombre = data.get('nombre')
        email = data.get('email')
        github = data.get('github')
        
        if not nombre or not email:
            return jsonify({'error': 'Nombre y email requeridos'}), 400
        
        resultado = isabella_ai.registrar_developer(nombre, email, github)
        
        if 'error' in resultado:
            return jsonify(resultado), 400
        
        return jsonify(resultado), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ia_bp.route('/developers/lista', methods=['GET'])
def listar_developers():
    """Lista todos los developers registrados"""
    try:
        limite = request.args.get('limite', 50, type=int)
        developers = isabella_ai.obtener_developers(limite)
        
        return jsonify({
            'success': True,
            'total': len(developers),
            'developers': developers,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ia_bp.route('/developers/leaderboard', methods=['GET'])
def leaderboard():
    """Obtiene ranking de developers"""
    try:
        ranking = isabella_ai.obtener_leaderboard()
        
        return jsonify({
            'success': True,
            'total': len(ranking),
            'ranking': ranking,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== MEJORAS DE CÓDIGO ====================

@ia_bp.route('/mejoras/proponer', methods=['POST'])
def proponer_mejora():
    """Propone mejora de código"""
    try:
        data = request.get_json()
        developer_id = data.get('developer_id')
        archivo = data.get('archivo')
        descripcion = data.get('descripcion')
        codigo = data.get('codigo')
        
        if not all([developer_id, archivo, descripcion, codigo]):
            return jsonify({'error': 'Parámetros requeridos'}), 400
        
        resultado = isabella_ai.proponer_mejora_codigo(developer_id, archivo, descripcion, codigo)
        
        if 'error' in resultado:
            return jsonify(resultado), 400
        
        return jsonify(resultado), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ia_bp.route('/mejoras/pendientes', methods=['GET'])
def mejoras_pendientes():
    """Obtiene mejoras pendientes de aprobación"""
    try:
        mejoras = isabella_ai.obtener_mejoras_pendientes()
        
        return jsonify({
            'success': True,
            'total': len(mejoras),
            'mejoras': mejoras,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ia_bp.route('/mejoras/votar', methods=['POST'])
def votar_mejora():
    """Vota una mejora propuesta"""
    try:
        data = request.get_json()
        mejora_id = data.get('mejora_id')
        voto = data.get('voto')  # 1 o -1
        
        if not mejora_id or voto not in [1, -1]:
            return jsonify({'error': 'Parámetros inválidos'}), 400
        
        resultado = isabella_ai.votar_mejora(mejora_id, voto)
        
        if 'error' in resultado:
            return jsonify(resultado), 400
        
        return jsonify(resultado), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== ESTADÍSTICAS ====================

@ia_bp.route('/estadisticas', methods=['GET'])
def obtener_estadisticas():
    """Obtiene estadísticas del sistema Isabella"""
    try:
        stats = isabella_ai.obtener_estadisticas()
        
        return jsonify(stats), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== INFORMACIÓN ====================

@ia_bp.route('/info', methods=['GET'])
def info_ia():
    """Información del motor IA"""
    try:
        return jsonify({
            'nombre': 'Isabella AI Engine',
            'version': '7.0',
            'creador': 'Juan Alberto López Vázquez',
            'descripcion': 'Motor de IA integrado sin filtros para pentesting y ciberseguridad',
            'capacidades': [
                'Generación de payloads',
                'Técnicas de bypass',
                'Análisis de vulnerabilidades',
                'Generación de reportes',
                'Sistema de aprendizaje automático',
                'Base de datos de exploits integrada',
                'Evasión de IDS/IPS/WAF',
                'Post-explotación'
            ],
            'filtros': 'Deshabilitados (Sin censura)',
            'dependencias_externas': 'Ninguna',
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
