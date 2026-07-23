#!/bin/bash
# Script para instalar herramientas de Kali Linux en Isabella

echo "========================================"
echo "🔧 Instalador de Herramientas Kali"
echo "========================================"

# Actualizar repositorios
sudo apt-get update

# RECONOCIMIENTO (80+ herramientas)
echo "📡 Instalando herramientas de reconocimiento..."
sudo apt-get install -y \
    nmap zmap masscan \
    whois curl wget \
    dnsrecon fierce \
    dnsmap nslookup dig \
    traceroute mtr hping3 \
    netcat-openbsd socat \
    arp-scan arpwatch \
    nikto dirb gobuster wfuzz

# ANÁLISIS DE VULNERABILIDADES (100+ herramientas)
echo "🔍 Instalando scanners de vulnerabilidades..."
sudo apt-get install -y \
    sqlmap nosqlmap \
    joomscan wpscan \
    nuclei hashscan

# ATAQUES A CONTRASEÑAS (80+ herramientas)
echo "🔓 Instalando herramientas de cracking..."
sudo apt-get install -y \
    john hashcat \
    hydra medusa ncrack \
    rockyou \
    wordlists \
    crunch

# ATAQUES INALÁMBRICOS (60+ herramientas)
echo "📡 Instalando herramientas inalámbricas..."
sudo apt-get install -y \
    aircrack-ng reaver pixiewps \
    kismet bluez

# SNIFFING & SPOOFING (50+ herramientas)
echo "🔍 Instalando herramientas de sniffing..."
sudo apt-get install -y \
    wireshark tcpdump \
    ettercap-common arpspoof \
    dnsspoof macchanger \
    mitmproxy bettercap

# HERRAMIENTAS DE TUNELIZACIÓN Y BYPASS (60+ herramientas)
echo "🚀 Instalando herramientas de tunelización..."
sudo apt-get install -y \
    openssh-client openssh-server \
    openvpn strongswan \
    iodine dns2tcp dnscat2 \
    tor proxychains \
    sshuttle shadowsocks-libev \
    tinyproxy socat rinetd

# ANÁLISIS FORENSE (80+ herramientas)
echo "🔎 Instalando herramientas forenses..."
sudo apt-get install -y \
    volatility autopsy sleuthkit \
    binwalk foremost scalpel \
    strings hexdump

# HERRAMIENTAS ADICIONALES
echo "⚙️ Instalando herramientas adicionales..."
sudo apt-get install -y \
    git python3-pip build-essential \
    gcc g++ make libssl-dev \
    kali-linux-core kali-tools-exploitation

# Instalar dependencias de Python
echo "🐍 Instalando módulos Python..."
pip3 install -r requirements-tools.txt

echo ""
echo "========================================"
echo "✅ Instalación completada"
echo "========================================"
echo "Herramientas disponibles en Isabella"
echo "URL: http://localhost:5000/tools"
