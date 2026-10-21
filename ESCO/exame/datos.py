REGISTROS_TELEMETRIA = [
    {"id_sesion": "SES-101", "cliente": "VIP", "conector": "CCS2", "kw_h": 45.5, "duracion_min": 30, "hora": 14, "activa": True},
    {"id_sesion": "SES-102", "cliente": "ESTANDAR", "conector": "CHADEMO", "kw_h": -12.0, "duracion_min": 15, "hora": 9, "activa": False}, # Error: kw_h negativo
    {"id_sesion": "SES-103", "cliente": "FLOTA", "conector": "MENNEKES", "kw_h": 22.0, "duracion_min": 120, "hora": 23, "activa": True},
    {"id_sesion": "SES-104", "cliente": "ESTANDAR", "conector": "CCS2", "kw_h": 60.0, "duracion_min": 40, "hora": 18, "activa": True},
    {"id_sesion": "CORRUPTO", "cliente": "DESCONOCIDO"}, # Error: falta información obligatoria
    {"id_sesion": "SES-105", "cliente": "VIP", "conector": "SCHUKO", "kw_h": 11.5, "duracion_min": 90, "hora": 2, "activa": True}
]

RED_DISTRIBUCION = [
    15.5, # Carga directa en Hub Central
    [22.0, 45.0, [10.5, 60.0]], # Subred Norte con ramificación interna
    [30.0, [12.5, [5.0, 18.0]]], # Subred Sur con triple anidamiento
    8.0 # Carga directa en Estación Auxiliar
]