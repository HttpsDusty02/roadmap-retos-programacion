# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# -----------------------------------------------------
# * SOLID: RINCIPIO DE INVERSIÓN DE DEPENDENCIAS (DIP)
# -----------------------------------------------------
# Los módulos de alto nivel no deben depender de módulos de bajo nivel, sino de abstracciones. A su vez, las 
# abstracciones no deben depender de detalles concretos; los detalles deben depender de las abstracciones.

from abc import ABC, abstractmethod

"""
* EJERCICIO #1:
 * Explora el "Principio SOLID de Inversión de Dependencias (Dependency Inversion
 * Principle, DIP)" y crea un ejemplo simple donde se muestre su funcionamiento 
 * de forma correcta e incorrecta.
"""
# __________________________________________________
# De manera INCORRECTA:

class FileStorage_:
    def save(self, data):
        print(f"Datos guardados en archivo: {data}")

class DataManager_:
    def __init__(self):
        # Dependencia directa de una clase concreta
        self.file_storage = FileStorage()
    
    def store_data(self, data):
        self.file_storage.save(data)


# __________________________________________________
# De manera CORRECTA:

# Abstracción
class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass

# Implementación concreta
class FileStorage(Storage):
    def save(self, data):
        print(f"Guardado en archivo: {data}")

# Implementación concreta
class DatabaseStorage(Storage):
    def save(self, data):
        print(f"Guardado en base de datos: {data}")

# Módulo de alto nivel
class DataManager:
    def __init__(self, storage: Storage):
        # Dependencia de la abstracción
        self.storage = storage
    
    def store_data(self, data):
        self.storage.save(data)

# Comprobación:
data_to_store = "Ejemplo de datos x"

file_storage = FileStorage()
database_storage = DatabaseStorage()

data_manager_file = DataManager(file_storage)
data_manager_database = DataManager(database_storage)

data_manager_file.store_data(data_to_store)
data_manager_database.store_data(data_to_store)

"""
* EJERCICIO #2:
* Crea un sistema de notificaciones.
* Requisitos:
* 1. El sistema puede enviar Email, PUSH y SMS (implementaciones específicas).
* 2. El sistema de notificaciones no puede depender de las implementaciones específicas.
* Instrucciones:
* 1. Crea la interfaz o clase abstracta.
* 2. Desarrolla las implementaciones específicas.
* 3. Crea el sistema de notificaciones usando el DIP.
* 4. Desarrolla un código que compruebe que se cumple el principio.
"""

# Abstracción
class MessageService(ABC):
    @abstractmethod
    def send(self, to: int | str, message: str) -> None:
        pass

# Implementación
class EmailService(MessageService):
    def send(self, to: str, message: str) -> None:
        print("Correo enviado a:", to)
        print("Mensaje:", message)

# Implementación
class PUSHService(MessageService):
    def send(self, to: str, message: str) -> None:
        print("Notificación PUSH enviada a:", to)
        print("Mensaje:", message)

# Implementación
class SMSService(MessageService):
    def send(self, to: int, message: str) -> None:
        print("Mensaje SMS enviado a:", to)
        print("Mensaje:", message)

# Módulo de alto nivel
class NotificationSystem:
    def __init__(self, service: MessageService) -> None:
        # Dependencia de la abstracción
        self.service = service
    
    def notify(self, to: int | str, message: str) -> None:
        self.service.send(to, message)

# Comprobación:
def test_notification_system(to: int | str, message: str, service: MessageService):
    service_notifier = NotificationSystem(service)
    service_notifier.notify(to, message)

print("\nEJERCICIO #2")

email_service = EmailService()
push_service = PUSHService()
sms_service = SMSService()

test_notification_system("ejm@gg.com", "abcdsf", email_service)
test_notification_system("user01", "123456", push_service)
test_notification_system(123456789, "aeiou", sms_service)

