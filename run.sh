#!/bin/bash
# ISABELLA v7.0 - SCRIPT DE EJECUCIÓN
# © Juan Alberto López Vázquez

echo "🚀 Iniciando Isabella v7.0..."

# Activar entorno virtual
if [ ! -d "venv" ]; then
    echo "[!] Entorno virtual no encontrado. Ejecuta primero:"
    echo "    ./install_dependencies.sh"
    exit 1
fi

source venv/bin/activate

# Verificar dependencias
python -c "import flask, paramiko, requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[!] Dependencias faltantes. Ejecuta:"
    echo "    pip install -r requirements.txt"
    exit 1
fi

# Iniciar servidor
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                                                                ║"
echo "║             🔥 ISABELLA v7.0 - INICIANDO 🔥                   ║"
echo "║                                                                ║"
echo "║           © 2024 Juan Alberto López Vázquez                    ║"
echo "║                                                                ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "📍 URL: http://localhost:5000"
echo "🔌 Puerto: 5000"
echo "📊 Modo: Producción"
echo ""
echo "🔓 Atajos:"
echo "  - Dashboard: http://localhost:5000/dashboard"
echo "  - API Docs: http://localhost:5000/api/docs"
echo "  - Admin: http://localhost:5000/admin"
echo ""
echo "⏹️  Presiona CTRL+C para detener"
echo ""

python app.py
