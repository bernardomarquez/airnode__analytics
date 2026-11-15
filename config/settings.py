
import os


# DIRECTORIOS DEL PROYECTO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_DIR = os.path.join(BASE_DIR, "database")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")


# CONFIGURACIÓN DEL AEROPUERTO

AIRPORT_CODE = "LEMD"
AIRPORT_NAME = "Adolfo Suárez Madrid-Barajas"


# ARCHIVOS

DATABASE_FILE = os.path.join(DATABASE_DIR, "airnode.db")


# RECOPILACIÓN DE DATOS

COLLECTION_INTERVAL = 300  # 5 minutos
