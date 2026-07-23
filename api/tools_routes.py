"""
ISABELLA v7.0 - BLUEPRINT DE HERRAMIENTAS
Endpoints para usar herramientas integradas
"""

from flask import Blueprint, request, jsonify
import subprocess
import os
import json

tools_bp = Blueprint('tools', __name__, url_prefix='/api/tools')

# ==================== NMAP ====================

@tools_bp.route('/nmap', methods=['POST'])
def run_nmap():
    """Ejecutar nmap"""
    data = request.get_json()
    target = data.get('target')
    arguments = data.get('arguments', '-sV -p- -A')
    
    if not target:
        return jsonify({'error': 'Target requerido'}), 400
    
    try:
        cmd = f"nmap {arguments} {target}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        
        return jsonify({
            'success': result.returncode == 0,
            'target': target,
            'output': result.stdout,
            'errors': result.stderr if result.returncode != 0 else None
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en nmap'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== HASHCAT ====================

@tools_bp.route('/hashcat', methods=['POST'])
def run_hashcat():
    """Ejecutar hashcat"""
    data = request.get_json()
    hash_file = data.get('hash_file')
    wordlist = data.get('wordlist')
    hash_type = data.get('hash_type', '0')  # 0 = MD5
    
    if not hash_file or not wordlist:
        return jsonify({'error': 'hash_file y wordlist requeridos'}), 400
    
    try:
        cmd = f"hashcat -m {hash_type} -a 0 {hash_file} {wordlist}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=600)
        
        return jsonify({
            'success': result.returncode == 0,
            'output': result.stdout,
            'errors': result.stderr if result.returncode != 0 else None
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en hashcat'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== SQLMAP ====================

@tools_bp.route('/sqlmap', methods=['POST'])
def run_sqlmap():
    """Ejecutar sqlmap"""
    data = request.get_json()
    url = data.get('url')
    arguments = data.get('arguments', '--dbs')
    
    if not url:
        return jsonify({'error': 'URL requerida'}), 400
    
    try:
        cmd = f"sqlmap -u '{url}' {arguments}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        
        return jsonify({
            'success': result.returncode == 0,
            'url': url,
            'output': result.stdout,
            'vulnerable': 'vulnerable' in result.stdout.lower()
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en sqlmap'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== NIKTO ====================

@tools_bp.route('/nikto', methods=['POST'])
def run_nikto():
    """Ejecutar nikto"""
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL requerida'}), 400
    
    try:
        cmd = f"nikto -h {url}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        
        return jsonify({
            'success': result.returncode == 0,
            'url': url,
            'output': result.stdout,
            'vulnerabilities_found': result.stdout.count('+ ')
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en nikto'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== INFORMACIÓN ====================

@tools_bp.route('/available', methods=['GET'])
def available_tools():
    """Obtiene herramientas disponibles"""
    tools = []
    
    # Verificar disponibilidad
    commands = ['nmap', 'nikto', 'sqlmap', 'hashcat', 'john', 'hydra']
    
    for cmd in commands:
        result = subprocess.run(f"which {cmd}", shell=True, capture_output=True)
        if result.returncode == 0:
            tools.append({
                'name': cmd,
                'available': True,
                'path': result.stdout.decode().strip()
            })
        else:
            tools.append({
                'name': cmd,
                'available': False,
                'path': None
            })
    
    return jsonify({'tools': tools}), 200
