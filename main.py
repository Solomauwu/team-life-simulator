"""
Точка входа в консольный симулятор экосистемы.
Демонстрирует взаимодействие хищников, травоядных и растений.
"""

from ecosystem import Ecosystem
from organism import Herbivore, Predator, Plant
from utils import setup_logging

def main():
    setup_logging()
    
    # Создаём экосистему
    eco = Ecosystem(name="Лесной биоценоз")
    
    # Добавляем организмы
    rabbit = Herbivore("Заяц", energy=50, max_energy=100)
    wolf = Predator("Волк", energy=80, max_energy=120)
    grass = Plant("Трава", energy=30, max_energy=50)
    
    eco.add_organism(rabbit)
    eco.add_organism(wolf)
    eco.add_organism(grass)
    
    # Симуляция 5 дней
    for day in range(1, 6):
        print(f"\n--- День {day} ---")
        eco.simulate_day()
        eco.show_status()
        
        if not eco.has_alive_organisms():
            print("Экосистема рухнула...")
            break

if __name__ == "__main__":
    main()