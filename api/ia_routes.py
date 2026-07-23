"""
ISABELLA v7.0 - BLUEPRINT DE IA Y DEVELOPERS
© Juan Alberto López Vázquez
"""

from flask import Blueprint, request, jsonify
from core.isabella_ai import isabella_ai
import json

ia_bp = Blueprint('ia', __name__, url_prefix='/api/ia')

# ==================== RETROALIMENTACIÓN ====================

@ia_bp.route('/feedback/registrar', methods=['POST'])
def registrar_feedback():
    """Registra feedback del usuario"""
    data = request.get_json()
    usuario = data.get('usuario', 'anonymous')
    feedback = data.get('feedback')
    puntuacion = data.get('puntuacion', 5)
    
    if not feedback:
        return jsonify({'error': 'Feedback requerido'}), 400
    
    result = isabella_ai.registrar_feedback(usuario, feedback, puntuacion)
    return jsonify(result), 200

@ia_bp.route('/feedback/lista', methods=['GET'])
def listar_feedback():
    """Lista todo el feedback registrado"""
    return jsonify({
        'total': len(isabella_ai.feedback_list),
        'feedback': isabella_ai.feedback_list[-20:]  # Últimos 20
    }), 200

# ==================== DEVELOPERS Y COLABORADORES ====================

@ia_bp.route('/developers/registrar', methods=['POST'])
def registrar_developer():
    """Registra nuevo desarrollador colaborador"""
    data = request.get_json()
    nombre = data.get('nombre')
    email = data.get('email')
    github = data.get('github')
    
    if not nombre or not email:
        return jsonify({'error': 'Nombre y email requeridos'}), 400
    
    result = isabella_ai.registrar_developer(nombre, email, github)
    return jsonify(result), 200

@ia_bp.route('/developers/lista', methods=['GET'])
def listar_developers():
    """Lista todos los developers registrados"""
    return jsonify({
        'total': len(isabella_ai.developers),
        'developers': isabella_ai.developers
    }), 200

@ia_bp.route('/developers/leaderboard', methods=['GET'])
def leaderboard():
    """Obtiene ranking de developers"""
    return jsonify({
        'ranking': isabella_ai.obtener_leaderboard()
    }), 200

# ==================== MEJORAS DE CÓDIGO ====================

@ia_bp.route('/mejoras/proponer', methods=['POST'])
def proponer_mejora():
    """Propone mejora de código"""
    data = request.get_json()
    developer_id = data.get('developer_id')
    archivo = data.get('archivo')
    descripcion = data.get('descripcion')
    codigo = data.get('codigo')
    
    if not all([developer_id, archivo, descripcion, codigo]):
        return jsonify({'error': 'Parámetros requeridos'}), 400
    
    result = isabella_ai.proponer_mejora_codigo(developer_id, archivo, descripcion, codigo)
    return jsonify(result), 200

@ia_bp.route('/mejoras/pendientes', methods=['GET'])
def mejoras_pendientes():
    """Obtiene mejoras pendientes de aprobación"""
    mejoras = isabella_ai.obtener_mejoras_pendientes()
    return jsonify({
        'total': len(mejoras),
        'mejoras': mejoras
    }), 200

@ia_bp.route('/mejoras/votar/<mejora_id>', methods=['POST'])
def votar_mejora(mejora_id):
    """Vota una mejora"""
    data = request.get_json()
    developer_id = data.get('developer_id')
    voto = data.get('voto', 1)  # 1 o -1
    
    if not developer_id:
        return jsonify({'error': 'Developer ID requerido'}), 400
    
    result = isabella_ai.votar_mejora(mejora_id, developer_id, voto)
    return jsonify(result), 200

@ia_bp.route('/mejoras/aplicar/<mejora_id>', methods=['POST'])
def aplicar_mejora(mejora_id):
    """Aplica una mejora aprobada"""
    result = isabella_ai.aplicar_mejora(mejora_id)
    return jsonify(result), 200

# ==================== ANÁLISIS DE CÓDIGO ====================

@ia_bp.route('/codigo/analizar', methods=['POST'])
def analizar_codigo():
    """Analiza código para detectar mejoras"""
    data = request.get_json()
    codigo = data.get('codigo')
    lenguaje = data.get('lenguaje', 'python')
    
    if not codigo:
        return jsonify({'error': 'Código requerido'}), 400
    
    analisis = isabella_ai.analizar_codigo(codigo, lenguaje)
    return jsonify(analisis), 200

# ==================== ESTADÍSTICAS ====================

@ia_bp.route('/estadisticas', methods=['GET'])
def obtener_estadisticas():
    """Obtiene estadísticas de Isabella"""
    stats = isabella_ai.obtener_estadisticas()
    return jsonify(stats), 200

@ia_bp.route('/estado', methods=['GET'])
def obtener_estado():
    """Obtiene estado actual del sistema"""
    estado = isabella_ai.obtener_estado_sistema()
    return jsonify(estado), 200

@ia_bp.route('/info', methods=['GET'])
def obtener_info():
    """Obtiene información de Isabella"""
    return jsonify({
        'nombre': isabella_ai.nombre,
        'version': isabella_ai.version,
        'creador': isabella_ai.creador,
        'descripcion': 'IA Integrada con auto-aprendizaje y mejora de código comunitaria',
        'caracteristicas': [
            'Auto-aprendizaje de feedback',
            'Análisis de código inteligente',
            'Votación comunitaria de mejoras',
            'Registro de developers colaboradores',
            'Leaderboard de contribuidores',
            'Auto-mejora controlada',
            'Auditoría completa'
        ]
    }), 200

# ==================== AUDITORÍA ====================

@ia_bp.route('/auditoria/registrar', methods=['POST'])
def registrar_auditoria():
    """Registra auditoría completada"""
    data = request.get_json()
    url = data.get('url')
    vulnerabilidades = data.get('vulnerabilidades', 0)
    resultado = data.get('resultado', 'completada')
    
    if not url:
        return jsonify({'error': 'URL requerida'}), 400
    
    result = isabella_ai.registrar_auditoria(url, vulnerabilidades, resultado)
    return jsonify(result), 200
