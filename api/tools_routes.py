"""
ISABELLA v7.0 - BLUEPRINT DE HERRAMIENTAS
Endpoints para usar herramientas integradas
"""

from flask import Blueprint, request, jsonify
import subprocess
import os
import json
from datetime import datetime

tools_bp = Blueprint('tools', __name__, url_prefix='/api/tools')

# ==================== NMAP ====================

@tools_bp.route('/nmap', methods=['POST'])
def run_nmap():
    """Ejecutar nmap"""
    try:
        data = request.get_json()
        target = data.get('target')
        arguments = data.get('arguments', '-sV -p- -A')
        
        if not target:
            return jsonify({'error': 'Target requerido'}), 400
        
        cmd = f"nmap {arguments} {target}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        
        return jsonify({
            'success': result.returncode == 0,
            'target': target,
            'output': result.stdout,
            'errors': result.stderr if result.returncode != 0 else None,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en nmap'}), 500
    except FileNotFoundError:
        return jsonify({
            'error': 'nmap no está instalado',
            'install': 'sudo apt-get install nmap'
        }), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== HASHCAT ====================

@tools_bp.route('/hashcat', methods=['POST'])
def run_hashcat():
    """Ejecutar hashcat"""
    try:
        data = request.get_json()
        hash_file = data.get('hash_file')
        wordlist = data.get('wordlist')
        hash_type = data.get('hash_type', '0')  # 0 = MD5
        
        if not hash_file or not wordlist:
            return jsonify({'error': 'hash_file y wordlist requeridos'}), 400
        
        # Validar que los archivos existen
        if not os.path.exists(hash_file):
            return jsonify({'error': f'Archivo {hash_file} no encontrado'}), 400
        if not os.path.exists(wordlist):
            return jsonify({'error': f'Archivo {wordlist} no encontrado'}), 400
        
        cmd = f"hashcat -m {hash_type} -a 0 {hash_file} {wordlist}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=600)
        
        return jsonify({
            'success': result.returncode == 0,
            'output': result.stdout,
            'errors': result.stderr if result.returncode != 0 else None,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en hashcat'}), 500
    except FileNotFoundError:
        return jsonify({
            'error': 'hashcat no está instalado',
            'install': 'sudo apt-get install hashcat'
        }), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== SQLMAP ====================

@tools_bp.route('/sqlmap', methods=['POST'])
def run_sqlmap():
    """Ejecutar sqlmap"""
    try:
        data = request.get_json()
        url = data.get('url')
        arguments = data.get('arguments', '--dbs')
        
        if not url:
            return jsonify({'error': 'URL requerida'}), 400
        
        cmd = f"sqlmap -u '{url}' {arguments}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        
        return jsonify({
            'success': result.returncode == 0,
            'url': url,
            'output': result.stdout,
            'vulnerable': 'vulnerable' in result.stdout.lower(),
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en sqlmap'}), 500
    except FileNotFoundError:
        return jsonify({
            'error': 'sqlmap no está instalado',
            'install': 'sudo apt-get install sqlmap'
        }), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== NIKTO ====================

@tools_bp.route('/nikto', methods=['POST'])
def run_nikto():
    """Ejecutar nikto"""
    try:
        data = request.get_json()
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL requerida'}), 400
        
        cmd = f"nikto -h {url}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        
        return jsonify({
            'success': result.returncode == 0,
            'url': url,
            'output': result.stdout,
            'vulnerabilities_found': result.stdout.count('+ '),
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en nikto'}), 500
    except FileNotFoundError:
        return jsonify({
            'error': 'nikto no está instalado',
            'install': 'sudo apt-get install nikto'
        }), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ==================== INFORMACIÓN ====================

@tools_bp.route('/available', methods=['GET'])
def available_tools():
    """Obtiene herramientas disponibles"""
    tools = []
    
    # Verificar disponibilidad
    commands = ['nmap', 'nikto', 'sqlmap', 'hashcat', 'john', 'hydra', 'curl', 'wget']
    
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
    
    return jsonify({
        'tools': tools,
        'total': len(tools),
        'available': sum(1 for t in tools if t['available']),
        'timestamp': datetime.now().isoformat()
    }), 200

@tools_bp.route('/john', methods=['POST'])
def run_john():
    """Ejecutar john the ripper"""
    try:
        data = request.get_json()
        hash_file = data.get('hash_file')
        wordlist = data.get('wordlist')
        
        if not hash_file:
            return jsonify({'error': 'hash_file requerido'}), 400
        
        if not os.path.exists(hash_file):
            return jsonify({'error': f'Archivo {hash_file} no encontrado'}), 400
        
        cmd = f"john {hash_file}"
        if wordlist and os.path.exists(wordlist):
            cmd += f" --wordlist={wordlist}"
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=600)
        
        return jsonify({
            'success': result.returncode == 0,
            'output': result.stdout,
            'errors': result.stderr if result.returncode != 0 else None,
            'timestamp': datetime.now().isoformat()
        }), 200
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en john'}), 500
    except FileNotFoundError:
        return jsonify({
            'error': 'john no está instalado',
            'install': 'sudo apt-get install john'
        }), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tools_bp.route('/hydra', methods=['POST'])
def run_hydra():
    """Ejecutar hydra (brute force)"""
    try:
        data = request.get_json()
        target = data.get('target')
        service = data.get('service', 'ssh')  # ssh, ftp, http-post, etc
        usernames = data.get('usernames', ['admin'])
        passwords = data.get('passwords', ['password'])
        
        if not target:
            return jsonify({'error': 'Target requerido'}), 400
        
        # Crear archivos temporales
        import tempfile
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as ufile:
            for username in usernames:
                ufile.write(username + '\n')
            usernames_file = ufile.name
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as pfile:
            for password in passwords:
                pfile.write(password + '\n')
            passwords_file = pfile.name
        
        try:
            cmd = f"hydra -L {usernames_file} -P {passwords_file} {service}://{target}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
            
            return jsonify({
                'success': result.returncode == 0,
                'target': target,
                'service': service,
                'output': result.stdout,
                'timestamp': datetime.now().isoformat()
            }), 200
        
        finally:
            # Limpiar archivos temporales
            os.unlink(usernames_file)
            os.unlink(passwords_file)
    
    except subprocess.TimeoutExpired:
        return jsonify({'error': 'Timeout en hydra'}), 500
    except FileNotFoundError:
        return jsonify({
            'error': 'hydra no está instalado',
            'install': 'sudo apt-get install hydra'
        }), 503
    except Exception as e:
        return jsonify({'error': str(e)}), 500
