#!/bin/bash
# ISABELLA v7.0 - INSTALADOR AUTOMÁTICO
# © Juan Alberto López Vázquez

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║          🔥 ISABELLA v7.0 - INSTALADOR AUTOMÁTICO 🔥        ║"
echo "║                                                              ║"
echo "║     © 2024 Juan Alberto López Vázquez - Único Creador       ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Detectar sistema operativo
OS=$(uname -s)
echo "[*] Sistema Operativo detectado: $OS"

# Actualizar repositorios
echo "[+] Actualizando repositorios del sistema..."
if [ "$OS" = "Linux" ]; then
    sudo apt-get update -qq
    sudo apt-get upgrade -y -qq
elif [ "$OS" = "Darwin" ]; then
    brew update -q
fi

# Instalar Python 3.9+
echo "[+] Verificando Python..."
python3 --version
if ! command -v python3 &> /dev/null; then
    echo "[!] Python 3 no encontrado. Instalando..."
    if [ "$OS" = "Linux" ]; then
        sudo apt-get install -y python3 python3-pip python3-dev
    elif [ "$OS" = "Darwin" ]; then
        brew install python3
    fi
fi

# Crear entorno virtual
echo "[+] Creando entorno virtual..."
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias Python
echo "[+] Instalando dependencias Python (esto puede tardar)..."
pip install --upgrade pip setuptools wheel -q
pip install -r requirements.txt -q

# Instalar herramientas del sistema
echo "[+] Instalando herramientas de pentesting..."

if [ "$OS" = "Linux" ]; then
    # Reconocimiento
    echo "[*] Instalando herramientas de reconocimiento..."
    sudo apt-get install -y -qq nmap zmap whois curl wget dnsutils \
        traceroute mtr hping3 netcat-openbsd socat arp-scan 2>/dev/null
    
    # Análisis
    echo "[*] Instalando herramientas de análisis..."
    sudo apt-get install -y -qq sqlmap nikto dirb gobuster wfuzz 2>/dev/null
    
    # Cracking
    echo "[*] Instalando herramientas de cracking..."
    sudo apt-get install -y -qq john hashcat hydra medusa ncrack 2>/dev/null
    
    # Wireless
    echo "[*] Instalando herramientas inalámbricas..."
    sudo apt-get install -y -qq aircrack-ng reaver pixiewps 2>/dev/null
    
    # Sniffing
    echo "[*] Instalando herramientas de sniffing..."
    sudo apt-get install -y -qq wireshark tcpdump ettercap-common \
        mitmproxy bettercap macchanger 2>/dev/null
    
    # Tunelización
    echo "[*] Instalando herramientas de tunelización..."
    sudo apt-get install -y -qq openssh-client openssh-server openvpn \
        strongswan tor torsocks proxychains sshuttle 2>/dev/null
    
    # Forense
    echo "[*] Instalando herramientas forenses..."
    sudo apt-get install -y -qq volatility autopsy sleuthkit \
        binwalk foremost scalpel 2>/dev/null
    
    # Utilidades
    echo "[*] Instalando utilidades..."
    sudo apt-get install -y -qq git build-essential gcc g++ make \
        libssl-dev git-core 2>/dev/null

elif [ "$OS" = "Darwin" ]; then
    echo "[*] Sistema macOS detectado. Instalando con Homebrew..."
    brew install -q nmap wget curl dnsutils hashcat john hydra \
        wireshark tor mitmproxy 2>/dev/null
fi

# Instalar diccionarios
echo "[+] Configurando diccionarios de palabras..."
mkdir -p wordlists
if [ ! -f "wordlists/rockyou.txt" ]; then
    echo "[*] Descargando rockyou.txt (puede tardar)..."
    cd wordlists
    # Usar un mirror si rockyou está disponible
    if command -v wget &> /dev/null; then
        wget -q https://github.com/danielmiessler/SecLists/raw/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt -O rockyou-top10k.txt 2>/dev/null
    fi
    cd ..
fi

# Crear directorios necesarios
echo "[+] Creando estructura de directorios..."
mkdir -p data logs uploads downloads extractions reports
mkdir -p data/isabella_versions

# Configurar archivo .env
echo "[+] Configurando archivo .env..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "[*] Archivo .env creado (editar con tus valores)"
fi

# Inicializar base de datos
echo "[+] Inicializando base de datos..."
python init_db.py

# Mostrar información final
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                   ✅ INSTALACIÓN COMPLETADA                   ║"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""
echo "[✓] Todas las herramientas instaladas correctamente"
echo ""
echo "📝 PRÓXIMOS PASOS:"
echo "─────────────────────────────────────────────────────────────"
echo "1. Activar entorno virtual:"
echo "   source venv/bin/activate"
echo ""
echo "2. Editar configuración (opcional):"
echo "   nano .env"
echo ""
echo "3. Iniciar Isabella:"
echo "   python app.py"
echo ""
echo "4. Acceder a:"
echo "   http://localhost:5000"
echo ""
echo "📚 DOCUMENTACIÓN:"
echo "─────────────────────────────────────────────────────────────"
echo "- Guía de usuario: docs/USUARIO_FINAL.md"
echo "- API Reference: docs/API_REFERENCE.md"
echo "- Tutoriales: docs/TUTORIAL.md"
echo "- Términos legales: docs/LEGAL.md"
echo ""
echo "⚠️  DISCLAIMER:"
echo "─────────────────────────────────────────────────────────────"
echo "Isabella v7.0 es solo para auditorías AUTORIZADAS."
echo "El usuario es completamente responsable de su uso."
echo "© 2024 Juan Alberto López Vázquez"
echo ""
