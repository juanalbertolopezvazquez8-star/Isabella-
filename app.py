"""
ISABELLA v7.0 - ACTUALIZACIÓN DEL SERVIDOR PRINCIPAL
© Juan Alberto López Vázquez - Único Creador
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import CURRENT_CONFIG, ENV, BASE_DIR
from datetime import datetime
import os

# Importar blueprints
from api.pentesting_routes import pentesting_bp
from api.tools_routes import tools_bp
from api.admin_routes import admin_bp

# Crear aplicación
app = Flask(__name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)

app.config.from_object(CURRENT_CONFIG)

# Inicializar extensiones
CORS(app, resources={r"/api/*": {"origins": "*"}})
jwt = JWTManager(app)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# Registrar blueprints
app.register_blueprint(pentesting_bp)
app.register_blueprint(tools_bp)
app.register_blueprint(admin_bp)

# ==================== INICIALIZACIÓN ====================

def init_app():
    """Inicializar aplicación"""
    dirs = [
        os.path.join(BASE_DIR, 'data'),
        os.path.join(BASE_DIR, 'data', 'isabella_versions'),
        os.path.join(BASE_DIR, 'logs'),
        os.path.join(BASE_DIR, 'uploads'),
        os.path.join(BASE_DIR, 'downloads'),
        os.path.join(BASE_DIR, 'extractions'),
        os.path.join(BASE_DIR, 'reports')
    ]
    
    for directory in dirs:
        os.makedirs(directory, exist_ok=True)
    
    # Inicializar memoria
    import json
    memoria_path = app.config['ISABELLA_MEMORY_FILE']
    
    if not os.path.exists(memoria_path):
        memoria = {
            "version": "7.0",
            "creador": "Juan Alberto López Vázquez",
            "creada_en": datetime.now().isoformat(),
            "estado": "operacional",
            "auditorias": [],
            "vulnerabilidades_encontradas": 0,
            "sesiones_activas": 0
        }
        with open(memoria_path, 'w', encoding='utf-8') as f:
            json.dump(memoria, f, indent=4, ensure_ascii=False)

init_app()

# ==================== RUTAS PRINCIPALES ====================

@app.route('/')
def index():
    """Página de inicio"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Panel de control"""
    return render_template('dashboard.html')

@app.route('/pentesting')
def pentesting():
    """Panel de pentesting"""
    return render_template('pentesting.html')

@app.route('/admin')
def admin():
    """Panel administración"""
    return render_template('admin.html')

# ==================== API SALUD ====================

@app.route('/api/health', methods=['GET'])
@limiter.limit("60/minute")
def health():
    """Estado del sistema"""
    return jsonify({
        'status': 'healthy',
        'version': '7.0',
        'creador': 'Juan Alberto López Vázquez',
        'timestamp': datetime.now().isoformat(),
        'entorno': ENV
    }), 200

@app.route('/api/info', methods=['GET'])
def info():
    """Información de Isabella"""
    return jsonify({
        'nombre': 'Isabella',
        'version': '7.0',
        'creador': 'Juan Alberto López Vázquez',
        'descripcion': 'Plataforma profesional de pentesting y ciberseguridad',
        'caracteristicas': [
            'Navegación web avanzada',
            'Explotación web (SQLi, XSS, CSRF)',
            'Brute force de credenciales',
            'Extracción de archivos',
            '600+ herramientas Kali integradas',
            'Bypass de firewalls',
            'Agente inteligente autónomo'
        ]
    }), 200

# ==================== MANEJO DE ERRORES ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Recurso no encontrado'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Error interno del servidor'}), 500

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({'error': 'Demasiadas solicitudes. Intenta más tarde.'}), 429

# ==================== CONTEXTO ====================

@app.shell_context_processor
def make_shell_context():
    return {'app': app}

# ==================== EJECUCIÓN ====================

if __name__ == '__main__':
    print("""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║                 🔥 ISABELLA v7.0 - INICIANDO 🔥                 ║
║                                                                  ║
║                © 2024 Juan Alberto López Vázquez                 ║
║                                                                  ║
║       Plataforma Profesional de Pentesting y Ciberseguridad      ║
║                                                                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  📍 URL: http://localhost:5000                                  ║
║  📊 Modo: {}                                           ║
║  🔌 Puerto: 5000                                                 ║
║  🗄️  BD: SQLite                                                  ║
║                                                                  ║
║  ⚠️  DISCLAIMER:                                                 ║
║  • Solo usar en sistemas autorizados                            ║
║  • Cumplir todas las leyes aplicables                           ║
║  • Usuario responsable de cualquier daño                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """.format(ENV.upper()))
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=CURRENT_CONFIG.DEBUG,
        use_reloader=CURRENT_CONFIG.DEBUG
    )
