
import abc # Модуль для создания абстрактных базовых классов
# 1. Продукт (Product): Общий интерфейс для всех видов транспорта
class Transport(abc.ABC):
    @abc.abstractmethod
    def deliver(self):
        pass

# 2. Конкретные Продукты (Concrete Products): Реализации различных видов транспорта
class Truck(Transport):
    def deliver(self):
        return "Доставка груза на грузовике по дороге. (Грузоподъемность: 20тонн)"

class Bicycle(Transport):
    def deliver(self):
        return "Доставка посылки на велосипеде по городу. (Экологично ибыстро в пробках)"
class Drone(Transport):
    def deliver(self):
        return "Доставка легкого груза дроном по воздуху. (Быстро, ноограничено по весу)"
class Ship(Transport):
    def deliver(self):
        return "Доставка контейнеров на корабле по морю. (Большие объемы,длительное время)"

# 3. Создатель (Creator): Определяет фабричный метод и содержит основнуюлогику
class Logistics(abc.ABC):
    def plan_delivery(self):
# Основная логика, которая использует транспорт, но не знает егоконкретного типа.
# Эта логика остается неизменной, независимо от того, какой транспортбудет создан.
        transport = self.create_transport()
        result = f"Планирование доставки: {transport.deliver()}"
        return result
@abc.abstractmethod
def create_transport(self) -> Transport:
    pass
# 4. Конкретные Создатели (Concrete Creators): Переопределяют фабричный метод
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()
class UrbanLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Bicycle()
class AirLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Drone()
class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()
# Использование паттерна "Фабричный метод" в клиентском коде
def client_code(creator: Logistics):
    print(f"Клиент: Я не знаю, какая это фабрика, но она работает с {creator.plan_delivery()}")

print("Запуск логистики для дорог:")
road_logistics = RoadLogistics()
client_code(road_logistics)

print("\nЗапуск логистики для города:")
urban_logistics = UrbanLogistics()
client_code(urban_logistics)

print("\nЗапуск логистики для воздуха:")
air_logistics = AirLogistics()
client_code(air_logistics)

print("\nЗапуск логистики для моря:")
sea_logistics = SeaLogistics()
client_code(sea_logistics)
# Демонстрация гибкости: добавление нового типа транспорта
# Если появится новый вид транспорта, например, поезд, мы просто добавляем:
# class Train(Transport):
# def deliver(self):
# return "Доставка груза поездом по железной дороге."
