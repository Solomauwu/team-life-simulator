"""
Модуль классов организмов: базовый класс Organism и его наследники.
"""

from abc import ABC, abstractmethod

class Organism(ABC):
    """Абстрактный базовый класс для всех организмов."""
    
    def __init__(self, name: str, energy: float, max_energy: float):
        self.name = name
        self.energy = energy
        self.max_energy = max_energy
        self.alive = True
    
    @abstractmethod
    def eat(self, amount: float):
        """Абстрактный метод питания."""
        pass
    
    def is_alive(self) -> bool:
        return self.alive and self.energy > 0
    
    def update_energy(self, delta: float):
        self.energy += delta
        if self.energy <= 0:
            self.alive = False
            self.energy = 0
        elif self.energy > self.max_energy:
            self.energy = self.max_energy
    
    def __repr__(self):
        return f"{self.name} (Энергия: {self.energy:.1f}/{self.max_energy})"


class Herbivore(Organism):
    """Травоядное животное — ест растения."""
    
    def eat(self, amount: float):
        # Травоядное получает энергию от растений
        self.update_energy(amount * 0.8)  # 80% усвояемость


class Predator(Organism):
    """Хищник — ест травоядных."""
    
    def eat(self, amount: float):
        # Хищник получает больше энергии от мяса
        self.update_energy(amount * 1.2)


class Plant(Organism):
    """Растение — восстанавливает энергию за счёт фотосинтеза."""
    
    def eat(self, amount: float):
        # Растения не едят, а фотосинтезируют
        self.update_energy(amount * 0.5)