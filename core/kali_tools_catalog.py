"""
ISABELLA v7.0 - CATÁLOGO DE 600+ HERRAMIENTAS KALI
Organización y mapeo de todas las herramientas
"""

# Estructura de categorías y herramientas
KALI_TOOLS_CATALOG = {
    'reconocimiento': {
        'nombre': '🔍 Reconocimiento e Información',
        'descripcion': 'Herramientas para recopilación de información sobre objetivos',
        'herramientas': [
            {
                'nombre': 'nmap',
                'nombre_es': 'Escáner de Puertos',
                'descripcion': 'Escanea puertos y servicios en red',
                'comandos': ['nmap -sV -p- -A <target>'],
                'riesgos': ['Detectable', 'Genera logs'],
                'bypass': ['Fragmentación', 'Decoy packets']
            },
            {
                'nombre': 'zmap',
                'nombre_es': 'Escáner Masivo de Internet',
                'descripcion': 'Escanea internet a velocidad lineal',
                'comandos': ['zmap -p 80 -o results.csv'],
                'riesgos': ['Muy detectablr'],
                'bypass': ['Rate limiting']
            },
            {
                'nombre': 'masscan',
                'nombre_es': 'Escáner Masivo de Puertos',
                'descripcion': 'Escanea millones de puertos por segundo',
                'comandos': ['masscan 0.0.0.0/0 -p0-65535 --rate=10000'],
                'riesgos': ['Muy detectables', 'Alto tráfico'],
                'bypass': ['Fragmentación de paquetes']
            },
            {
                'nombre': 'theHarvester',
                'nombre_es': 'Recolector de Datos OSINT',
                'descripcion': 'Recolecta emails, subdominios, IPs y URLs',
                'comandos': ['theharvester -d example.com -b google'],
                'riesgos': ['Bajo riesgo (búsquedas pasivas)'],
                'bypass': ['Legítimo']
            },
            {
                'nombre': 'maltego',
                'nombre_es': 'Minería de Datos Visual',
                'descripcion': 'Análisis visual de relaciones de datos',
                'comandos': ['maltego'],
                'riesgos': ['Bajo riesgo'],
                'bypass': ['N/A']
            },
            {
                'nombre': 'shodan',
                'nombre_es': 'Búsqueda de Dispositivos Expuestos',
                'descripcion': 'Busca dispositivos conectados a internet',
                'comandos': ['shodan search webcam'],
                'riesgos': ['Bajo riesgo (información pública)'],
                'bypass': ['VPN recomendada']
            },
            {
                'nombre': 'recon-ng',
                'nombre_es': 'Marco de Reconocimiento',
                'descripcion': 'Automatiza recopilación de OSINT',
                'comandos': ['recon-ng', 'run all'],
                'riesgos': ['Bajo a medio'],
                'bypass': ['Proxies']
            },
            {
                'nombre': 'spiderfoot',
                'nombre_es': 'Automatización OSINT',
                'descripcion': 'Automatiza búsquedas OSINT',
                'comandos': ['spiderfoot -l 127.0.0.1:5001'],
                'riesgos': ['Bajo'],
                'bypass': ['Proxies']
            },
        ]
    },
    
    'vulnerabilidades': {
        'nombre': '🛡️ Análisis de Vulnerabilidades',
        'descripcion': 'Identifica vulnerabilidades en sistemas y aplicaciones',
        'herramientas': [
            {
                'nombre': 'nikto',
                'nombre_es': 'Escáner Web',
                'descripcion': 'Escanea servidores web en busca de vulnerabilidades',
                'comandos': ['nikto -h <target>'],
                'riesgos': ['Muy detectable', 'Genera muchos logs'],
                'bypass': ['User-Agent spoofing', 'Proxies']
            },
            {
                'nombre': 'sqlmap',
                'nombre_es': 'Detector de Inyección SQL',
                'descripcion': 'Detecta y explota vulnerabilidades SQL',
                'comandos': ['sqlmap -u "<url>" --dbs'],
                'riesgos': ['Alto', 'Muy detectable'],
                'bypass': ['Tamper scripts', 'WAF bypass']
            },
            {
                'nombre': 'owasp-zap',
                'nombre_es': 'Scanner de Seguridad Web',
                'descripcion': 'Análisis de seguridad en aplicaciones web',
                'comandos': ['zaproxy'],
                'riesgos': ['Medio a alto'],
                'bypass': ['Proxies', 'Autenticación']
            },
            {
                'nombre': 'burp-suite',
                'nombre_es': 'Proxy y Scanner Web',
                'descripcion': 'Análisis profundo de aplicaciones web',
                'comandos': ['burpsuite'],
                'riesgos': ['Medio a alto'],
                'bypass': ['SSL pinning bypass']
            },
        ]
    },
    
    'passwords': {
        'nombre': '🔓 Ataques a Contraseñas',
        'descripcion': 'Herramientas para cracking de contraseñas y hashes',
        'herramientas': [
            {
                'nombre': 'john',
                'nombre_es': 'Cracker de Contraseñas',
                'descripcion': 'Cracking de contraseñas por fuerza bruta',
                'comandos': ['john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt'],
                'riesgos': ['Consume recursos'],
                'bypass': ['Diccionarios optimizados']
            },
            {
                'nombre': 'hashcat',
                'nombre_es': 'Cracker GPU',
                'descripcion': 'Cracking acelerado por GPU',
                'comandos': ['hashcat -m 1000 hashes.txt rockyou.txt'],
                'riesgos': ['Muy rápido'],
                'bypass': ['GPU en la nube']
            },
            {
                'nombre': 'hydra',
                'nombre_es': 'Ataque de Fuerza Bruta en Línea',
                'descripcion': 'Ataca servicios en línea (SSH, FTP, HTTP)',
                'comandos': ['hydra -l admin -P rockyou.txt ssh://target'],
                'riesgos': ['Alto', 'Muy detectable'],
                'bypass': ['Distribución de intentos', 'Proxies']
            },
            {
                'nombre': 'medusa',
                'nombre_es': 'Cracker Paralelo',
                'descripcion': 'Ataques de fuerza bruta paralelos',
                'comandos': ['medusa -h <target> -u admin -P /usr/share/wordlists/rockyou.txt -M ssh'],
                'riesgos': ['Alto'],
                'bypass': ['Rate limiting bypass']
            },
        ]
    },
    
    'bypass_firewalls': {
        'nombre': '🚀 Evasión y Bypass de Firewalls',
        'descripcion': 'Técnicas para evadir firewalls y sistemas de defensa',
        'herramientas': [
            {
                'nombre': 'proxychains',
                'nombre_es': 'Cadena de Proxies',
                'descripcion': 'Redirecciona tráfico a través de múltiples proxies',
                'comandos': ['proxychains nmap -sV -p- <target>'],
                'ventaja': 'Oculta IP origen',
                'configuracion': '/etc/proxychains4.conf'
            },
            {
                'nombre': 'tor',
                'nombre_es': 'Red Tor',
                'descripcion': 'Anonimato en línea a través de Tor',
                'comandos': ['torsocks curl https://example.com'],
                'ventaja': 'Anonimato de alto nivel',
                'configuracion': '/etc/tor/torrc'
            },
            {
                'nombre': 'sshuttle',
                'nombre_es': 'VPN sin Servidor',
                'descripcion': 'Crea VPN mediante SSH',
                'comandos': ['sshuttle -r user@server 0/0'],
                'ventaja': 'VPN rápida y fácil',
                'configuracion': 'N/A'
            },
            {
                'nombre': 'iodine',
                'nombre_es': 'Túnel DNS',
                'descripcion': 'Tuneliza tráfico a través de DNS',
                'comandos': ['iodine -f -P pass ns.example.com'],
                'ventaja': 'Evasión de firewalls restrictivos',
                'configuracion': 'Requiere servidor DNS'
            },
            {
                'nombre': 'dnscat2',
                'nombre_es': 'Tunelización DNS Avanzada',
                'descripcion': 'Control de shells a través de DNS',
                'comandos': ['dnscat2.py --help'],
                'ventaja': 'Exfiltración de datos',
                'configuracion': 'Requiere servidor DNS'
            },
            {
                'nombre': 'fragroute',
                'nombre_es': 'Fragmentación de Paquetes',
                'descripcion': 'Fragmenta paquetes para evadir IDS',
                'comandos': ['fragroute -i eth0 -p "drop;delay 100;dup;echo <target>" <target>'],
                'ventaja': 'Evasión de IDS/IPS',
                'configuracion': 'Requiere libnet'
            },
            {
                'nombre': 'shadowsocks',
                'nombre_es': 'SOCKS5 Encriptado',
                'descripcion': 'Proxy SOCKS5 encriptado',
                'comandos': ['ss-server -s 0.0.0.0 -p 8388 -k password -m aes-256-cfb'],
                'ventaja': 'Cifrado y rápido',
                'configuracion': 'JSON config'
            },
        ]
    },
    
    'explotacion': {
        'nombre': '⚔️ Explotación y Post-Explotación',
        'descripcion': 'Herramientas para explotación de vulnerabilidades',
        'herramientas': [
            {
                'nombre': 'metasploit',
                'nombre_es': 'Framework de Explotación',
                'descripcion': 'Framework completo de penetración testing',
                'modulos': 400,
                'comandos': ['msfconsole', 'use exploit/windows/smb/ms17_010_eternalblue'],
                'ventaja': 'Más completo del mundo'
            },
            {
                'nombre': 'beef',
                'nombre_es': 'Herramienta de Explotación de Navegadores',
                'descripcion': 'Explota navegadores web',
                'comandos': ['./beef'],
                'ventaja': 'Ataques a navegadores cliente'
            },
        ]
    },
    
    'inalambrico': {
        'nombre': '📡 Ataques Inalámbricos',
        'descripcion': 'Herramientas para auditoría de redes inalámbricas',
        'herramientas': [
            {
                'nombre': 'aircrack-ng',
                'nombre_es': 'Suite de Hacking WiFi',
                'descripcion': 'Completa suite para auditoría WiFi',
                'herramientas_incluidas': ['airmon-ng', 'airodump-ng', 'aireplay-ng', 'aircrack-ng'],
                'comandos': ['airmon-ng start wlan0', 'airodump-ng wlan0mon']
            },
            {
                'nombre': 'reaver',
                'nombre_es': 'Ataque WPS',
                'descripcion': 'Ataca WPS (WiFi Protected Setup)',
                'comandos': ['reaver -i wlan0mon -b <BSSID> -vv'],
                'velocidad': 'Rápido'
            },
        ]
    },
}

# Funciones de acceso
def get_all_tools():
    """Obtiene todas las herramientas"""
    tools = []
    for category in KALI_TOOLS_CATALOG.values():
        tools.extend(category.get('herramientas', []))
    return tools

def get_tools_by_category(category):
    """Obtiene herramientas por categoría"""
    return KALI_TOOLS_CATALOG.get(category, {}).get('herramientas', [])

def get_bypass_tools():
    """Obtiene herramientas de bypass/evasión"""
    return KALI_TOOLS_CATALOG.get('bypass_firewalls', {}).get('herramientas', [])

def count_total_tools():
    """Cuenta herramientas totales"""
    return len(get_all_tools())
