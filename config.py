"""
ISABELLA v7.0 - CONFIGURACIÓN
© Juan Alberto López Vázquez
"""

import os
from datetime import timedelta

ENV = os.getenv('FLASK_ENV', 'development')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Config:
    """Configuración base"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'isabella-v7-dev-key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'isabella-jwt-dev-key')
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///data/isabella.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # Files
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    
    # Isabella
    ISABELLA_MEMORY_FILE = os.path.join(BASE_DIR, 'data', 'isabella_memoria.json')
    ISABELLA_AUTO_UPDATE = os.getenv('ISABELLA_AUTO_UPDATE', 'true').lower() == 'true'
    ISABELLA_SANDBOX_ENABLED = os.getenv('ISABELLA_SANDBOX_ENABLED', 'true').lower() == 'true'
    ISABELLA_AUDIT_ENABLED = os.getenv('ISABELLA_AUDIT_ENABLED', 'true').lower() == 'true'
    
    # CORS
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:5000,http://localhost:3000').split(',')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.path.join(BASE_DIR, 'logs', 'isabella.log')
    
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Configuración de desarrollo"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Configuración de producción"""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

class TestingConfig(Config):
    """Configuración de testing"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

# Seleccionar configuración según entorno
if ENV == 'production':
    CURRENT_CONFIG = ProductionConfig
elif ENV == 'testing':
    CURRENT_CONFIG = TestingConfig
else:
    CURRENT_CONFIG = DevelopmentConfig
