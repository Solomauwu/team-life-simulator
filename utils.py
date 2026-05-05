"""
Вспомогательные утилиты для логирования и форматирования.
"""

import logging

def setup_logging(level=logging.INFO):
    """Настраивает логирование в консоль."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )
    return logging.getLogger(__name__)

def format_energy(value: float) -> str:
    """Форматирует значение энергии для вывода."""
    return f"{value:.1f}"