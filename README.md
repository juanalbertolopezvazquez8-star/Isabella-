# ISABELLA v7.0 - PLATAFORMA PROFESIONAL DE PENTESTING

**© 2024 Juan Alberto López Vázquez - Único Creador y Propietario**

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)]

---

## ⚠️ DISCLAIMER LEGAL

```
RESPONSABILIDAD TOTAL DEL USUARIO FINAL

Esta herramienta es ÚNICAMENTE para:
✓ Sistemas propios
✓ Auditorías autorizadas por escrito
✓ Laboratorios de prueba
✓ Programas de bug bounty públicos

USO ILEGAL:
✗ Acceso no autorizado a sistemas
✗ Robo de datos
✗ Crimen cibernético
✗ Cualquier violación de ley

El usuario ASUME TOTAL RESPONSABILIDAD por cualquier daño.
Juan Alberto López Vázquez no es responsable del mal uso.
```

---

## 🚀 CARACTERÍSTICAS PRINCIPALES

### 🌐 Navegación Web Profesional
- ✅ Navegación a cualquier sitio web
- ✅ Proxy chains (múltiples proxies en cadena)
- ✅ Tor integration (anonimato completo)
- ✅ VPN + SSH tunneling
- ✅ Spoofing de User-Agent
- ✅ Cambio de IP automático
- ✅ Manejo avanzado de cookies/sesiones

### 📥 Extracción de Archivos
- ✅ Búsqueda de archivos por tipo
- ✅ Descarga individual o por lotes
- ✅ Espejeo completo de sitios web
- ✅ Preservación de estructura
- ✅ Resume de descargas interrumpidas

### 💥 Explotación Web Real
- ✅ Inyección SQL (SQLi) - 4 tipos
- ✅ Cross-Site Scripting (XSS) - Múltiples vectores
- ✅ CSRF detection
- ✅ Escaneo completo de vulnerabilidades
- ✅ Bypass de WAF automático

### 🔓 Ataque de Credenciales
- ✅ SSH Brute Force (multi-threading)
- ✅ FTP Brute Force
- ✅ HTTP/HTTPS Brute Force
- ✅ Ataque paralelo (hasta 10 workers)
- ✅ Diccionarios preinstalados

### 🛠️ 600+ Herramientas Kali Integradas
- ✅ Reconocimiento (nmap, zmap, masscan)
- ✅ Vulnerabilidades (nikto, sqlmap, openvas)
- ✅ Explotación (metasploit, beef)
- ✅ Wireless (aircrack-ng, reaver)
- ✅ Forense (volatility, autopsy)
- ✅ Bypass (Tor, iodine, dnscat2)

### 🤖 Agente Isabella Inteligente
- ✅ Auto-aprendizaje de feedback
- ✅ Auto-actualización controlada
- ✅ Metaprogramación segura
- ✅ Respuestas contextuales
- ✅ Auditoría completa

---

## 📋 REQUISITOS DEL SISTEMA

```bash
# Sistema Operativo
✓ Linux (Ubuntu 20.04+, Debian, Kali)
✓ macOS 10.15+
✓ Windows 10/11 (con WSL2)

# Software
✓ Python 3.9+
✓ pip (gestor de paquetes Python)
✓ git

# Hardware Mínimo
✓ 4GB RAM
✓ 2GB espacio disco
✓ Procesador dual-core
```

---

## ⚡ INSTALACIÓN RÁPIDA (5 MINUTOS)

### Opción 1: Script Automático (Recomendado)

```bash
# Clonar repositorio
git clone https://github.com/juanalbertolopezvazquez8-star/Isabella-.git
cd Isabella-

# Ejecutar instalador
chmod +x install_dependencies.sh
./install_dependencies.sh

# Iniciar
./run.sh
```

### Opción 2: Manual

```bash
# 1. Clonar
git clone https://github.com/juanalbertolopezvazquez8-star/Isabella-.git
cd Isabella-

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Instalar herramientas del sistema (Linux/Mac)
sudo apt-get install nmap sqlmap aircrack-ng hashcat hydra

# 5. Inicializar base de datos
python init_db.py

# 6. Ejecutar
python app.py
```

### Opción 3: Docker (Más Fácil)

```bash
# Construir imagen
docker-compose build

# Ejecutar
docker-compose up

# Acceder
http://localhost:5000
```

---

## 🎯 USO RÁPIDO

### 1. Navegar a una Web
```bash
curl -X POST http://localhost:5000/api/pentesting/navigate \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "use_tor": true}'
```

### 2. Rastrear un Sitio Completo
```bash
curl -X POST http://localhost:5000/api/pentesting/crawl \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com", "max_depth": 2}'
```

### 3. Extraer Archivos
```bash
curl -X POST http://localhost:5000/api/pentesting/extract-files \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com",
    "file_types": [".pdf", ".zip", ".doc"],
    "output_dir": "./downloads"
  }'
```

### 4. Escanear Vulnerabilidades
```bash
curl -X POST http://localhost:5000/api/pentesting/scan-vulnerabilities \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/admin.php"}'
```

### 5. Brute Force HTTP
```bash
curl -X POST http://localhost:5000/api/pentesting/http-bruteforce \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://example.com/login",
    "usernames": ["admin", "user"],
    "passwords": ["123456", "password"]
  }'
```

---

## 📡 API ENDPOINTS COMPLETOS

### Navegación Web
- `POST /api/pentesting/navigate` - Navegar a URL
- `POST /api/pentesting/crawl` - Rastrear sitio
- `POST /api/pentesting/extract-files` - Descargar archivos
- `POST /api/pentesting/mirror` - Espejear sitio completo

### Explotación
- `POST /api/pentesting/scan-vulnerabilities` - Escaneo completo
- `POST /api/pentesting/test-sqli` - Prueba SQLi
- `POST /api/pentesting/test-xss` - Prueba XSS
- `POST /api/pentesting/get-headers` - Headers HTTP

### Credenciales
- `POST /api/pentesting/ssh-bruteforce` - SSH
- `POST /api/pentesting/http-bruteforce` - HTTP login
- `POST /api/pentesting/ftp-bruteforce` - FTP

### Herramientas
- `POST /api/tools/nmap` - Escaneo de puertos
- `POST /api/tools/hashcat` - Cracking de hashes
- `POST /api/tools/sqlmap` - Automatización SQLi

### Sistema
- `GET /api/admin/status` - Estado del sistema
- `GET /api/admin/logs` - Logs de auditoría
- `POST /api/admin/report` - Generar reporte

---

## 🎓 TUTORIALES

### Tutorial 1: Auditoría Web Completa
1. Navegar al sitio
2. Rastrear estructura
3. Extraer información
4. Escanear vulnerabilidades
5. Generar reporte

### Tutorial 2: Cracking de Contraseñas
1. Obtener hashes
2. Identificar tipo de hash
3. Ejecutar hashcat
4. Analizar resultados

### Tutorial 3: Penetration Testing
1. Reconocimiento (OSINT)
2. Escaneo de puertos
3. Enumeración de servicios
4. Búsqueda de vulnerabilidades
5. Explotación
6. Post-explotación
7. Reporte final

---

## 📊 DASHBOARD

Accede a: `http://localhost:5000`

**Características:**
- 📈 Gráficos de auditorías
- 🔍 Historial de escaneos
- 📥 Archivos descargados
- 🚨 Vulnerabilidades encontradas
- 👤 Usuarios y permisos
- 📝 Reportes generados

---

## 🔧 CONFIGURACIÓN AVANZADA

### Usar con Tor
```python
navigator = AdvancedWebNavigator(use_tor=True)
# Todos los requests se harán a través de Tor
```

### Configurar Proxies
```python
proxies = ['http://proxy1.com:8080', 'http://proxy2.com:8080']
navigator = AdvancedWebNavigator(use_proxy=True)
navigator._configure_proxy(session, proxies)
```

### Multi-threading
```python
forcer = SSHBruteForcer(target)
results = forcer.brute_force(usernames, passwords, max_workers=10)
# Ataque paralelo con 10 hilos
```

---

## 📚 DOCUMENTACIÓN

- [LEGAL.md](docs/LEGAL.md) - Términos legales completos
- [USUARIO_FINAL.md](docs/USUARIO_FINAL.md) - Guía del usuario
- [API_REFERENCE.md](docs/API_REFERENCE.md) - Referencia API
- [TUTORIAL.md](docs/TUTORIAL.md) - Tutoriales paso a paso
- [INSTALACION.md](docs/INSTALACION.md) - Problemas de instalación

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Error: "No module named 'paramiko'"
```bash
pip install paramiko
```

### Error: "Connection refused"
```bash
# Verificar que el servidor está corriendo
python app.py

# Verificar puerto 5000
lsof -i :5000
```

### Error: "Tor no está disponible"
```bash
# Instalar Tor
sudo apt-get install tor
sudo service tor start
```

---

## 🤝 CONTRIBUIR

Para reportar bugs o sugerir mejoras:

1. Abre un Issue en GitHub
2. Describe el problema detalladamente
3. Incluye pasos para reproducir
4. Adjunta logs si es necesario

---

## 📄 LICENCIA

```
MIT License

Copyright (c) 2024 Juan Alberto López Vázquez

Permiso concedido, gratuito, a cualquier persona que obtenga una copia
de este software y archivos de documentación asociados ("Software"),
para tratar el Software sin restricción, incluyendo sin limitación
los derechos de usar, copiar, modificar, fusionar, publicar, distribuir,
de sublicenciar y/o vender copias del Software...

RESPONSABILIDAD: El usuario final es completamente responsable del
uso de esta herramienta. El autor no es responsable de daños causados
por mal uso.
```

---

## 📞 SOPORTE

- 🐛 **Issues**: [GitHub Issues](https://github.com/juanalbertolopezvazquez8-star/Isabella-/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/juanalbertolopezvazquez8-star/Isabella-/discussions)
- 📧 **Email**: juanalbertolopezvazquez8@gmail.com

---

## 🎖️ CRÉDITOS

**Creador y Propietario**: Juan Alberto López Vázquez

**Herramientas Integradas**:
- Kali Linux Tools
- Metasploit Framework
- Burp Suite Community
- OWASP ZAP
- Nmap
- Wireshark

---

## 🚀 ROADMAP

- [ ] Integración con Shodan
- [ ] Módulo de análisis forense
- [ ] Reportes en PDF
- [ ] Mobile app
- [ ] Cloud deployment
- [ ] Inteligencia artificial mejorada

---

**Isabella v7.0** - *La plataforma profesional de pentesting*

© 2024 Juan Alberto López Vázquez - Todos los derechos reservados

⚠️ **USO RESPONSABLE** - Esta herramienta es solo para auditorías autorizadas
