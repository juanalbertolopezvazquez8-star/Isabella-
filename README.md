# Isabella v7.0 - Asistente de Ciberseguridad Sin Filtros

**Isabella** es una plataforma profesional de pentesting y ciberseguridad con un motor de IA integrado sin filtros de censura.

## 📋 Características

✅ **Motor IA Sin Filtros** - Responde a consultas técnicas sin restricciones éticas  
✅ **600+ Herramientas Kali** - Catálogo completo integrado  
✅ **Generador de Payloads** - SQL Injection, XSS, RCE, y más  
✅ **Técnicas de Bypass** - WAF, IDS, IPS, Antivirus  
✅ **Post-Explotación** - Escalada de privilegios, movimiento lateral  
✅ **API REST Completa** - Endpoints para todas las funciones  
✅ **Interfaz Web Intuitiva** - Panel profesional de control  
✅ **100% Offline** - Funciona sin conexión a internet (con Ollama)  

## 🛠️ Requisitos

- Python 3.8+
- [Ollama](https://ollama.ai) instalado
- Modelo `llama3.2-uncensored` descargado (opcional, usa `llama2` como fallback)

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/juanalbertolopezvazquez8-star/Isabella-.git
cd Isabella-
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Instalar y ejecutar Ollama

Descarga Ollama desde [ollama.ai](https://ollama.ai)

```bash
# Descargar modelo sin filtros
ollama pull llama3.2-uncensored

# O descargar modelo alternativo
ollama pull llama2
```

### 4. Inicializar base de datos

```bash
python init_db.py
```

### 5. Ejecutar servidor

```bash
python app.py
```

El servidor iniciará en `http://localhost:5000`

## 🌐 Uso

### Acceder a la interfaz web

Abre tu navegador en: **http://localhost:5000**

### Estructura de carpetas

```
Isabella/
├── app.py                 # Servidor Flask principal
├── init_db.py            # Inicializador de base de datos
├── requirements.txt      # Dependencias Python
├── templates/
│   ├── index.html        # Interfaz principal
│   └── testing-center.html # Centro de pruebas
├── static/
│   ├── css/              # Estilos
│   └── js/               # JavaScript
├── core/
│   ├── isabella_ai.py           # Sistema IA principal
│   ├── isabella_ai_engine.py    # Motor IA sin filtros
│   ├── kali_tools_catalog.py    # Catálogo de herramientas
│   └── bypass_engine.py         # Técnicas de bypass
├── api/
│   ├── ia_routes.py      # Rutas de IA
│   ├── pentesting_routes.py
│   ├── tools_routes.py
│   └── admin_routes.py
├── data/                 # Datos persistentes
├── logs/                 # Logs de auditoría
└── README.md             # Este archivo
```

## 📡 Endpoints de la API

### Chat Principal

```bash
POST /api/chat
Content-Type: application/json

{
  "prompt": "¿Cuáles son los payloads SQL injection más efectivos?"
}
```

**Respuesta:**
```json
{
  "response": "Respuesta del modelo IA...",
  "timestamp": "2024-01-15T10:30:00",
  "model": "llama3.2-uncensored"
}
```

### Motor IA Integrado

```bash
# Consultar IA integrada
POST /api/ia/consultar
{"consulta": "Payloads XSS"}

# Obtener payloads de categoría
GET /api/ia/payloads/sql_injection

# Técnicas de bypass
GET /api/ia/tecnicas-bypass

# Estadísticas
GET /api/ia/estadisticas
```

### Pentesting

```bash
# Navegación web
POST /api/pentesting/navigate
{"url": "https://example.com"}

# Rastrear sitio
POST /api/pentesting/crawl
{"url": "https://example.com", "max_depth": 2}

# Escanear vulnerabilidades
POST /api/pentesting/scan-vulnerabilities
{"url": "https://example.com"}
```

### Herramientas Integradas

```bash
# Ejecutar Nmap
POST /api/tools/nmap
{"target": "192.168.1.1", "arguments": "-sV -p-"}

# Ejecutar SQLmap
POST /api/tools/sqlmap
{"url": "https://example.com/?id=1"}

# Ejecutar Nikto
POST /api/tools/nikto
{"url": "https://example.com"}
```

## 🔐 Disclaimer

⚠️ **IMPORTANTE:**

Esta herramienta está diseñada para:
- Auditorías de seguridad autorizadas
- Investigación en ciberseguridad
- Entornos de laboratorio controlados
- Sistemas bajo tu control exclusivo

**El usuario asume total responsabilidad por cualquier daño causado.**

Cumple con todas las leyes y regulaciones aplicables en tu jurisdicción.

## 📝 Configuración Avanzada

### Cambiar modelo Ollama

Edita `app.py` línea 33:

```python
MODEL_NAME = "tu-modelo-aqui"
```

### Personalizar system prompt

Edita `app.py` líneas 45-57:

```python
SYSTEM_PROMPT = "Tu instrucción personalizada aquí..."
```

### Configurar puerto

Edita `app.py` línea 315:

```python
app.run(host='0.0.0.0', port=5000)  # Cambiar puerto aquí
```

## 🐛 Solución de Problemas

### "Error: Ollama no está instalado"

```bash
# Descargar desde ollama.ai e instalar
# Luego ejecutar:
pip install ollama
```

### "Error de conexión en http://localhost:5000"

1. Verifica que `app.py` esté ejecutándose
2. Abre http://localhost:5000 en el navegador
3. Verifica el puerto 5000 no esté en uso

### "Modelo no encontrado"

```bash
# Descargar modelo
ollama pull llama3.2-uncensored
```

## 📚 Documentación Técnica

### Arquitectura

- **Frontend:** HTML5 + JavaScript Vanilla (CORS habilitado)
- **Backend:** Python Flask + Ollama
- **Motor IA:** Local (sin dependencias externas de terceros)
- **Base de Datos:** JSON (escalable a SQL)

### Base de Conocimiento

El motor IA integrado incluye:
- 8 categorías de payloads
- 10+ técnicas de bypass
- 600+ herramientas Kali
- Módulos Metasploit
- Técnicas de post-explotación

## 👨‍💻 Desarrollo

### Crear nuevo endpoint

```python
@app.route('/api/tu-endpoint', methods=['POST'])
def tu_endpoint():
    try:
        data = request.get_json()
        # Tu lógica aquí
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

### Ejecutar tests

```bash
pytest tests/
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT.

## 👤 Autor

**Juan Alberto López Vázquez**
- GitHub: [@juanalbertolopezvazquez8-star](https://github.com/juanalbertolopezvazquez8-star)
- Email: juanalbertolopezvazquez8@gmail.com
- Única persona responsable del desarrollo

## ⭐ Soporte

Si encuentras problemas o tienes sugerencias, abre un issue en GitHub.

---

**Isabella v7.0 - Herramienta Profesional de Ciberseguridad**

© 2024 Juan Alberto López Vázquez - Todos los derechos reservados
