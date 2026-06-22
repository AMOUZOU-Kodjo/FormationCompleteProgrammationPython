"""
Exercice 26.2 : Framework de logging configurable
Crée un système de logging avec :

- Logger (Singleton) : point d'entrée
- Appenders (Strategy) : ConsoleAppender, FileAppender, HTTPAppender
- Formatters (Strategy) : SimpleFormatter, JSONFormatter, DateFormatter
- Levels : DEBUG, INFO, WARNING, ERROR, CRITICAL
"""

from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

# À compléter
class LogLevel(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

class Formatter(ABC):
    @abstractmethod
    def formater(self, niveau, message, date=None):
        pass

class Appender(ABC):
    @abstractmethod
    def ecrire(self, message_formate):
        pass

class Logger:
    pass


# Tests
if __name__ == "__main__":
    logger = Logger()
    logger.set_level(LogLevel.DEBUG)
    logger.add_appender(ConsoleAppender(SimpleFormatter()))
    logger.add_appender(FileAppender("app.log", JSONFormatter()))

    logger.info("Application démarrée")
    logger.warning("Mémoire faible")
    logger.error("Erreur de connexion")
