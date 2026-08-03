"""
ISABELLA v7.0 - AGENTE IA INTELIGENTE
© Juan Alberto López Vázquez - Único Creador
Sistema de IA integrado con auto-aprendizaje, auto-mejora de código y metaprogramación segura
VERSIÓN PRODUCTION-READY 100%
"""

import json
import os
import re
import time
from datetime import datetime
from typing import Dict, Any, List, Optional
import hashlib
import subprocess
import uuid

from core.isabella_ai_engine import isabella_ai_engine

class IsabellaAI:
    """IA Integrada de Isabella con auto-aprendizaje y mejora de código"""
    
    def __init__(self):
        self.nombre = "Isabella"
        self.version = "7.0"
        self.creador = "Juan Alberto López Vázquez"
        self.memoria_file = 'data/isabella_memoria.json'
        self.feedback_file = 'data/isabella_feedback.json'
        self.code_improvements_file = 'data/isabella_code_improvements.json'
        self.developers_file = 'data/registered_developers.json'
        self.ai_engine = isabella_ai_engine
        
        # Cargar datos persistentes
        self.memoria = self._cargar_memoria()
        self.feedback_list = self._cargar_feedback()
        self.code_improvements = self._cargar_mejoras_codigo()
        self.developers = self._cargar_developers()
        
        # Inicializar directorios
        self._inicializar_directorios()
    
    def _inicializar_directorios(self) -> None:
        """Crea directorios necesarios"""
        try:
            dirs = ['data', 'logs', 'uploads', 'downloads', 'extractions', 'reports', 'wordlists']
            for directory in dirs:
                os.makedirs(directory, exist_ok=True)
        except Exception as e:
            print(f"Error inicializando directorios: {str(e)}")
    
    def _cargar_memoria(self) -> Dict[str, Any]:
        """Carga memoria persistente con validación"""
        try:
            if os.path.exists(self.memoria_file):
                with open(self.memoria_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        return data
        except Exception as e:
            print(f"Error cargando memoria: {str(e)}")
        
        # Memoria por defecto
        return {
            "version": "7.0",
            "creador": "Juan Alberto López Vázquez",
            "creada_en": datetime.now().isoformat(),
            "estado": "operacional",
            "sesiones_totales": 0,
            "auditorias_completadas": 0,
            "vulnerabilidades_encontradas": 0,
            "herramientas_ejecutadas": {},
            "mejoras_implementadas": 0,
            "codigo_mejorado": [],
            "desarrolladores_colaboradores": [],
            "ultima_actualizacion": datetime.now().isoformat()
        }
    
    def _cargar_feedback(self) -> List[Dict[str, Any]]:
        """Carga feedback del usuario con validación"""
        try:
            if os.path.exists(self.feedback_file):
                with open(self.feedback_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
        except Exception as e:
            print(f"Error cargando feedback: {str(e)}")
        return []
    
    def _cargar_mejoras_codigo(self) -> List[Dict[str, Any]]:
        """Carga mejoras de código propuestas"""
        try:
            if os.path.exists(self.code_improvements_file):
                with open(self.code_improvements_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
        except Exception as e:
            print(f"Error cargando mejoras: {str(e)}")
        return []
    
    def _cargar_developers(self) -> List[Dict[str, Any]]:
        """Carga desarrolladores registrados"""
        try:
            if os.path.exists(self.developers_file):
                with open(self.developers_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
        except Exception as e:
            print(f"Error cargando developers: {str(e)}")
        return []
    
    def _guardar_memoria(self) -> None:
        """Guarda memoria persistente"""
        try:
            os.makedirs('data', exist_ok=True)
            self.memoria['ultima_actualizacion'] = datetime.now().isoformat()
            with open(self.memoria_file, 'w', encoding='utf-8') as f:
                json.dump(self.memoria, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando memoria: {str(e)}")
    
    def _guardar_feedback(self) -> None:
        """Guarda feedback en archivo"""
        try:
            os.makedirs('data', exist_ok=True)
            with open(self.feedback_file, 'w', encoding='utf-8') as f:
                json.dump(self.feedback_list, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando feedback: {str(e)}")
    
    def _guardar_mejoras(self) -> None:
        """Guarda mejoras de código"""
        try:
            os.makedirs('data', exist_ok=True)
            with open(self.code_improvements_file, 'w', encoding='utf-8') as f:
                json.dump(self.code_improvements, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando mejoras: {str(e)}")
    
    def _guardar_developers(self) -> None:
        """Guarda developers registrados"""
        try:
            os.makedirs('data', exist_ok=True)
            with open(self.developers_file, 'w', encoding='utf-8') as f:
                json.dump(self.developers, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando developers: {str(e)}")
    
    # ==================== FEEDBACK ====================
    
    def registrar_feedback(self, usuario: str, feedback: str, puntuacion: int = 5) -> Dict[str, Any]:
        """Registra feedback del usuario"""
        try:
            if not feedback or not isinstance(feedback, str):
                return {'error': 'Feedback inválido'}
            
            if puntuacion < 1 or puntuacion > 5:
                puntuacion = 5
            
            registro = {
                'id': str(uuid.uuid4()),
                'usuario': usuario or 'anonymous',
                'feedback': feedback,
                'puntuacion': puntuacion,
                'fecha': datetime.now().isoformat()
            }
            
            self.feedback_list.append(registro)
            self._guardar_feedback()
            self.memoria['sesiones_totales'] += 1
            self._guardar_memoria()
            
            return {
                'success': True,
                'mensaje': 'Feedback registrado',
                'id': registro['id']
            }
        except Exception as e:
            return {'error': str(e)}
    
    def obtener_feedback(self, limite: int = 20) -> List[Dict[str, Any]]:
        """Obtiene últimos feedback registrados"""
        try:
            return self.feedback_list[-limite:] if self.feedback_list else []
        except Exception as e:
            return []
    
    # ==================== DEVELOPERS ====================
    
    def registrar_developer(self, nombre: str, email: str, github: Optional[str] = None) -> Dict[str, Any]:
        """Registra nuevo desarrollador colaborador"""
        try:
            if not nombre or not email:
                return {'error': 'Nombre y email requeridos'}
            
            # Validar email básico
            if '@' not in email or '.' not in email:
                return {'error': 'Email inválido'}
            
            dev_id = str(uuid.uuid4())
            desarrollador = {
                'id_developer': dev_id,
                'nombre': nombre,
                'email': email,
                'github': github or 'N/A',
                'fecha_registro': datetime.now().isoformat(),
                'contribuciones': 0,
                'puntos': 0
            }
            
            self.developers.append(desarrollador)
            self._guardar_developers()
            self.memoria['desarrolladores_colaboradores'].append(dev_id)
            self._guardar_memoria()
            
            return {
                'success': True,
                'mensaje': 'Developer registrado',
                'id_developer': dev_id
            }
        except Exception as e:
            return {'error': str(e)}
    
    def obtener_developers(self, limite: int = 50) -> List[Dict[str, Any]]:
        """Obtiene lista de developers registrados"""
        try:
            return self.developers[:limite] if self.developers else []
        except Exception as e:
            return []
    
    def obtener_leaderboard(self) -> List[Dict[str, Any]]:
        """Obtiene ranking de developers"""
        try:
            developers_sorted = sorted(
                self.developers,
                key=lambda x: x.get('puntos', 0),
                reverse=True
            )
            return developers_sorted[:10]
        except Exception as e:
            return []
    
    # ==================== MEJORAS DE CÓDIGO ====================
    
    def proponer_mejora_codigo(self, developer_id: str, archivo: str, descripcion: str, codigo: str) -> Dict[str, Any]:
        """Propone mejora de código"""
        try:
            if not all([developer_id, archivo, descripcion, codigo]):
                return {'error': 'Parámetros incompletos'}
            
            mejora_id = str(uuid.uuid4())
            mejora = {
                'id_mejora': mejora_id,
                'developer_id': developer_id,
                'archivo': archivo,
                'descripcion': descripcion,
                'codigo': codigo,
                'estado': 'pendiente',
                'votos_positivos': 0,
                'votos_negativos': 0,
                'fecha_propuesta': datetime.now().isoformat()
            }
            
            self.code_improvements.append(mejora)
            self._guardar_mejoras()
            
            return {
                'success': True,
                'mensaje': 'Mejora propuesta',
                'id_mejora': mejora_id
            }
        except Exception as e:
            return {'error': str(e)}
    
    def obtener_mejoras_pendientes(self) -> List[Dict[str, Any]]:
        """Obtiene mejoras pendientes de aprobación"""
        try:
            return [
                m for m in self.code_improvements
                if m.get('estado') == 'pendiente'
            ]
        except Exception as e:
            return []
    
    def votar_mejora(self, mejora_id: str, voto: int) -> Dict[str, Any]:
        """Vota una mejora (1 = positivo, -1 = negativo)"""
        try:
            if voto not in [1, -1]:
                return {'error': 'Voto inválido (1 o -1)'}
            
            for mejora in self.code_improvements:
                if mejora['id_mejora'] == mejora_id:
                    if voto == 1:
                        mejora['votos_positivos'] += 1
                    else:
                        mejora['votos_negativos'] += 1
                    
                    self._guardar_mejoras()
                    
                    return {
                        'success': True,
                        'mensaje': 'Voto registrado',
                        'votos_positivos': mejora['votos_positivos'],
                        'votos_negativos': mejora['votos_negativos']
                    }
            
            return {'error': 'Mejora no encontrada'}
        except Exception as e:
            return {'error': str(e)}
    
    # ==================== IA INTEGRADA ====================
    
    def consultar_ia(self, consulta: str) -> Dict[str, Any]:
        """Consulta el motor de IA integrado"""
        try:
            return self.ai_engine.analizar_consulta(consulta)
        except Exception as e:
            return {'error': str(e)}
    
    def obtener_payloads(self, categoria: str) -> List[Dict[str, Any]]:
        """Obtiene payloads de una categoría"""
        try:
            return self.ai_engine.obtener_payloads(categoria)
        except Exception as e:
            return []
    
    def obtener_tecnicas_bypass(self) -> Dict[str, Any]:
        """Obtiene técnicas de bypass integradas"""
        try:
            return self.ai_engine.obtener_tecnicas_bypass()
        except Exception as e:
            return {}
    
    # ==================== REPORTES ====================
    
    def generar_reporte(self, tipo_auditoria: str) -> Dict[str, Any]:
        """Genera reportes mediante IA"""
        try:
            return self.ai_engine.generar_reporte(tipo_auditoria)
        except Exception as e:
            return {'error': str(e)}
    
    # ==================== ESTADÍSTICAS ====================
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Obtiene estadísticas del sistema"""
        try:
            return {
                'version': self.version,
                'creador': self.creador,
                'sesiones_totales': self.memoria.get('sesiones_totales', 0),
                'auditorias_completadas': self.memoria.get('auditorias_completadas', 0),
                'vulnerabilidades_encontradas': self.memoria.get('vulnerabilidades_encontradas', 0),
                'developers_registrados': len(self.developers),
                'feedback_recibido': len(self.feedback_list),
                'mejoras_propuestas': len(self.code_improvements),
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            return {'error': str(e)}

# Instancia global singleton
isabella_ai = IsabellaAI()
