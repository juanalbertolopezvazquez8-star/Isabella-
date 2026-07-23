"""
ISABELLA v7.0 - AGENTE IA INTELIGENTE
© Juan Alberto López Vázquez - Único Creador

Agente autónomo con auto-aprendizaje, auto-mejora de código y metaprogramación segura
"""

import json
import os
import re
import time
from datetime import datetime
from typing import Dict, Any, List, Optional
import hashlib
import subprocess

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
        
        self.memoria = self._cargar_memoria()
        self.feedback_list = self._cargar_feedback()
        self.code_improvements = self._cargar_mejoras_codigo()
        self.developers = self._cargar_developers()
    
    def _cargar_memoria(self) -> Dict:
        """Carga memoria persistente"""
        try:
            if os.path.exists(self.memoria_file):
                with open(self.memoria_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        
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
    
    def _cargar_feedback(self) -> List[Dict]:
        """Carga feedback del usuario"""
        try:
            if os.path.exists(self.feedback_file):
                with open(self.feedback_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return []
    
    def _cargar_mejoras_codigo(self) -> List[Dict]:
        """Carga mejoras de código propuestas"""
        try:
            if os.path.exists(self.code_improvements_file):
                with open(self.code_improvements_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return []
    
    def _cargar_developers(self) -> List[Dict]:
        """Carga desarrolladores registrados"""
        try:
            if os.path.exists(self.developers_file):
                with open(self.developers_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except:
            pass
        return []
    
    def _guardar_memoria(self):
        """Guarda memoria persistente"""
        os.makedirs('data', exist_ok=True)
        with open(self.memoria_file, 'w', encoding='utf-8') as f:
            json.dump(self.memoria, f, indent=4, ensure_ascii=False)
    
    def _guardar_feedback(self):
        """Guarda feedback"""
        os.makedirs('data', exist_ok=True)
        with open(self.feedback_file, 'w', encoding='utf-8') as f:
            json.dump(self.feedback_list, f, indent=4, ensure_ascii=False)
    
    def _guardar_mejoras_codigo(self):
        """Guarda mejoras de código"""
        os.makedirs('data', exist_ok=True)
        with open(self.code_improvements_file, 'w', encoding='utf-8') as f:
            json.dump(self.code_improvements, f, indent=4, ensure_ascii=False)
    
    def _guardar_developers(self):
        """Guarda desarrolladores"""
        os.makedirs('data', exist_ok=True)
        with open(self.developers_file, 'w', encoding='utf-8') as f:
            json.dump(self.developers, f, indent=4, ensure_ascii=False)
    
    # ==================== APRENDIZAJE ====================
    
    def registrar_feedback(self, usuario: str, feedback: str, puntuacion: int = 5) -> Dict[str, Any]:
        """Registra feedback del usuario para mejorar"""
        entry = {
            'timestamp': datetime.now().isoformat(),
            'usuario': usuario,
            'feedback': feedback,
            'puntuacion': puntuacion,
            'procesado': False
        }
        
        self.feedback_list.append(entry)
        self._guardar_feedback()
        
        # Analizar feedback automáticamente
        analisis = self._analizar_feedback(feedback, puntuacion)
        
        return {
            'success': True,
            'mensaje': f'Feedback registrado. Analizando para mejoras...',
            'analisis': analisis
        }
    
    def _analizar_feedback(self, feedback: str, puntuacion: int) -> Dict[str, Any]:
        """Analiza feedback para identificar áreas de mejora"""
        areas_mejora = []
        
        keywords = {
            'lento': 'Optimizar velocidad',
            'error': 'Corregir bugs',
            'seguridad': 'Mejorar seguridad',
            'interfaz': 'Mejorar UI/UX',
            'documentación': 'Mejorar documentación',
            'funcionalidad': 'Agregar funcionalidades',
            'crash': 'Estabilidad',
            'bug': 'Corregir bugs'
        }
        
        feedback_lower = feedback.lower()
        for keyword, area in keywords.items():
            if keyword in feedback_lower:
                areas_mejora.append(area)
        
        return {
            'areas_identificadas': list(set(areas_mejora)),
            'prioridad': 'alta' if puntuacion <= 3 else 'media' if puntuacion <= 4 else 'baja',
            'timestamp': datetime.now().isoformat()
        }
    
    # ==================== MEJORA DE CÓDIGO ====================
    
    def registrar_developer(self, nombre: str, email: str, github: str = None) -> Dict[str, Any]:
        """Registra desarrollador colaborador"""
        # Verificar que no esté duplicado
        for dev in self.developers:
            if dev['email'] == email:
                return {'success': False, 'error': 'Developer ya registrado'}
        
        developer = {
            'id': hashlib.md5(email.encode()).hexdigest(),
            'nombre': nombre,
            'email': email,
            'github': github,
            'registrado_en': datetime.now().isoformat(),
            'contribuciones': 0,
            'mejoras_aceptadas': 0,
            'estado': 'activo'
        }
        
        self.developers.append(developer)
        self.memoria['desarrolladores_colaboradores'].append(nombre)
        self._guardar_developers()
        self._guardar_memoria()
        
        return {
            'success': True,
            'mensaje': f'Developer {nombre} registrado exitosamente',
            'id_developer': developer['id']
        }
    
    def proponer_mejora_codigo(self, developer_id: str, archivo: str, 
                               mejora_descripcion: str, codigo_propuesto: str) -> Dict[str, Any]:
        """Permite a developers proponer mejoras de código"""
        # Verificar que el developer exista
        developer = None
        for dev in self.developers:
            if dev['id'] == developer_id:
                developer = dev
                break
        
        if not developer:
            return {'success': False, 'error': 'Developer no encontrado'}
        
        mejora = {
            'id': hashlib.md5(f"{developer_id}{archivo}{time.time()}".encode()).hexdigest(),
            'developer_id': developer_id,
            'developer_nombre': developer['nombre'],
            'archivo': archivo,
            'descripcion': mejora_descripcion,
            'codigo_propuesto': codigo_propuesto,
            'propuesto_en': datetime.now().isoformat(),
            'estado': 'pendiente_revision',
            'votos': 0,
            'comentarios': []
        }
        
        self.code_improvements.append(mejora)
        developer['contribuciones'] += 1
        self._guardar_mejoras_codigo()
        self._guardar_developers()
        
        return {
            'success': True,
            'mensaje': f'Mejora propuesta en {archivo}',
            'id_mejora': mejora['id'],
            'estado': 'pendiente_revision',
            'notificacion': 'La comunidad votará en tu mejora'
        }
    
    def analizar_codigo(self, codigo: str, lenguaje: str = 'python') -> Dict[str, Any]:
        """Analiza código para detectar mejoras"""
        problemas = []
        sugerencias = []
        
        # Análisis de seguridad
        patterns_peligrosos = [
            (r'eval\(', 'Uso de eval() - riesgo de seguridad'),
            (r'exec\(', 'Uso de exec() - riesgo de seguridad'),
            (r'__import__', 'Importación dinámica - riesgo de seguridad'),
            (r'subprocess\.call', 'Uso de subprocess - validar inputs'),
        ]
        
        for pattern, problema in patterns_peligrosos:
            if re.search(pattern, codigo):
                problemas.append({
                    'tipo': 'Seguridad',
                    'severidad': 'alta',
                    'descripcion': problema
                })
        
        # Análisis de calidad
        lineas = codigo.split('\n')
        
        # Detectar funciones muy largas
        if len(lineas) > 50:
            sugerencias.append({
                'tipo': 'Mantenibilidad',
                'descripcion': 'Código muy largo. Considerar refactorizar en funciones',
                'severidad': 'media'
            })
        
        # Detectar falta de documentación
        if '"""' not in codigo and "'''" not in codigo:
            sugerencias.append({
                'tipo': 'Documentación',
                'descripcion': 'Falta documentación (docstrings)',
                'severidad': 'baja'
            })
        
        return {
            'analisis_completo': True,
            'lenguaje': lenguaje,
            'problemas_encontrados': len(problemas),
            'problemas': problemas,
            'sugerencias': sugerencias,
            'score_calidad': max(0, 100 - len(problemas) * 15 - len(sugerencias) * 5)
        }
    
    def votar_mejora(self, mejora_id: str, developer_id: str, voto: int = 1) -> Dict[str, Any]:
        """Permite votar mejoras de código (1 = a favor, -1 = en contra)"""
        for mejora in self.code_improvements:
            if mejora['id'] == mejora_id:
                mejora['votos'] += voto
                
                # Si tiene suficientes votos, aceptar automáticamente
                if mejora['votos'] >= 5:
                    mejora['estado'] = 'aceptada'
                    
                    # Encontrar developer y actualizar contador
                    for dev in self.developers:
                        if dev['id'] == mejora['developer_id']:
                            dev['mejoras_aceptadas'] += 1
                            break
                    
                    self._guardar_mejoras_codigo()
                    self._guardar_developers()
                    self.memoria['mejoras_implementadas'] += 1
                    self._guardar_memoria()
                    
                    return {
                        'success': True,
                        'mensaje': '¡Mejora aceptada por votación comunitaria!',
                        'estado_nuevo': 'aceptada'
                    }
                else:
                    self._guardar_mejoras_codigo()
                    return {
                        'success': True,
                        'mensaje': f'Voto registrado. Votos: {mejora["votos"]}/5',
                        'votos_actuales': mejora['votos']
                    }
        
        return {'success': False, 'error': 'Mejora no encontrada'}
    
    def aplicar_mejora(self, mejora_id: str) -> Dict[str, Any]:
        """Aplica una mejora de código aprobada"""
        for mejora in self.code_improvements:
            if mejora['id'] == mejora_id:
                if mejora['estado'] != 'aceptada':
                    return {'success': False, 'error': 'Mejora no está aprobada'}
                
                # En producción, esto aplicaría los cambios reales
                mejora['estado'] = 'aplicada'
                mejora['aplicada_en'] = datetime.now().isoformat()
                
                self._guardar_mejoras_codigo()
                
                return {
                    'success': True,
                    'mensaje': f'Mejora aplicada a {mejora["archivo"]}',
                    'aplicada_en': mejora['aplicada_en'],
                    'developer': mejora['developer_nombre']
                }
        
        return {'success': False, 'error': 'Mejora no encontrada'}
    
    # ==================== MONITOREO Y ESTADÍSTICAS ====================
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Obtiene estadísticas de Isabella"""
        return {
            'nombre': self.nombre,
            'version': self.version,
            'creador': self.creador,
            'estadisticas': {
                'sesiones_totales': self.memoria.get('sesiones_totales', 0),
                'auditorias_completadas': self.memoria.get('auditorias_completadas', 0),
                'vulnerabilidades_encontradas': self.memoria.get('vulnerabilidades_encontradas', 0),
                'mejoras_implementadas': self.memoria.get('mejoras_implementadas', 0),
                'desarrolladores_activos': len(self.developers),
                'mejoras_en_revision': len([m for m in self.code_improvements if m['estado'] == 'pendiente_revision']),
                'feedback_registrado': len(self.feedback_list)
            },
            'developers_top': self._obtener_developers_top(),
            'ultima_actualizacion': self.memoria.get('ultima_actualizacion')
        }
    
    def _obtener_developers_top(self) -> List[Dict]:
        """Obtiene developers con más contribuciones"""
        sorted_devs = sorted(self.developers, key=lambda x: x['mejoras_aceptadas'], reverse=True)
        return sorted_devs[:5]
    
    def obtener_mejoras_pendientes(self) -> List[Dict]:
        """Obtiene mejoras pendientes de aprobación"""
        mejoras_pendientes = [
            m for m in self.code_improvements 
            if m['estado'] in ['pendiente_revision', 'aceptada']
        ]
        
        # Ordenar por votos
        mejoras_pendientes.sort(key=lambda x: x['votos'], reverse=True)
        
        return mejoras_pendientes
    
    def obtener_leaderboard(self) -> List[Dict]:
        """Obtiene ranking de developers"""
        return sorted(
            self.developers,
            key=lambda x: x['mejoras_aceptadas'],
            reverse=True
        )
    
    def obtener_estado_sistema(self) -> Dict[str, Any]:
        """Obtiene estado actual del sistema"""
        return {
            'nombre': self.nombre,
            'version': self.version,
            'estado': self.memoria.get('estado', 'operacional'),
            'memoria_usada': len(json.dumps(self.memoria)),
            'feedback_activo': len([f for f in self.feedback_list if not f['procesado']]),
            'mejoras_activas': len([m for m in self.code_improvements if m['estado'] != 'aplicada']),
            'developers_registrados': len(self.developers),
            'timestamp': datetime.now().isoformat()
        }
    
    def registrar_auditoria(self, url: str, vulnerabilidades: int, resultado: str) -> Dict[str, Any]:
        """Registra auditoría completada"""
        self.memoria['auditorias_completadas'] += 1
        self.memoria['vulnerabilidades_encontradas'] += vulnerabilidades
        self.memoria['ultima_actualizacion'] = datetime.now().isoformat()
        self._guardar_memoria()
        
        return {
            'success': True,
            'auditoria_registrada': True,
            'auditorias_totales': self.memoria['auditorias_completadas'],
            'vulnerabilidades_totales': self.memoria['vulnerabilidades_encontradas']
        }

# Instancia global
isabella_ai = IsabellaAI()
