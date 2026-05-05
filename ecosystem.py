"""
Модуль экосистемы: управление организмами и их взаимодействиями.
"""

import random
from typing import List
from organism import Organism, Herbivore, Predator, Plant

class Ecosystem:
    """
    Класс, моделирующий экосистему.
    Содержит список организмов и управляет их взаимодействиями.
    """
    
    def __init__(self, name: str = "Ecosystem"):
        self.name = name
        self.organisms: List[Organism] = []
        self.day_count = 0
    
    def add_organism(self, organism: Organism):
        """Добавляет организм в экосистему."""
        self.organisms.append(organism)
    
    def simulate_day(self):
        """Запускает один день симуляции."""
        self.day_count += 1
        
        # Случайные взаимодействия
        for org in self.organisms.copy():  # копия, чтобы менять список
            if not org.is_alive():
                self.organisms.remove(org)
                print(f"{org.name} погиб(ла)")
                continue
            
            # Поиск цели для хищника
            if isinstance(org, Predator):
                prey_candidates = [o for o in self.organisms if isinstance(o, Herbivore) and o.is_alive()]
                if prey_candidates:
                    prey = random.choice(prey_candidates)
                    energy_gain = prey.energy * 0.5
                    org.eat(energy_gain)
                    prey.update_energy(-energy_gain)
                    print(f"{org.name} съел(а) {prey.name}")
            
            # Травоядные едят растения
            elif isinstance(org, Herbivore):
                plants = [o for o in self.organisms if isinstance(o, Plant) and o.is_alive()]
                if plants:
                    plant = random.choice(plants)
                    energy_gain = plant.energy * 0.7
                    org.eat(energy_gain)
                    plant.update_energy(-energy_gain)
                    print(f"{org.name} съел(а) {plant.name}")
        
        # Фотосинтез для растений
        for org in self.organisms:
            if isinstance(org, Plant):
                org.eat(2.0)  # небольшой прирост энергии
    
    def show_status(self):
        """Выводит текущее состояние экосистемы."""
        print(f"\nСостояние экосистемы '{self.name}':")
        for org in self.organisms:
            print(f"  {org}")
    
    def has_alive_organisms(self) -> bool:
        """Проверяет, есть ли живые организмы."""
        return any(org.is_alive() for org in self.organisms)