from abc import ABC, abstractmethod

# 1. Базовый компонент "Заказ"

'''Создаем Order — это абстрактный интерфейс заказа (Компонент в паттерне «Декоратор»).
        Все заказы должны уметь:
        - Возвращать цену
        - Возвращать описание заказа'''
class Order(ABC):
    @abstractmethod
    def get_total_cost(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

'''Создаем BasicOrder — конкретный заказ (реализация базового компонента).
   В нём хранится цена (cost) и описание (description).
   _delivery_strategy является ссылкой на стратегию расчёта доставки (будет установлена позже).'''

class BasicOrder(Order):
    def __init__(self, cost: float, description: str):
        self._cost = cost
        self._description = description
        self._delivery_strategy = None  # стратегия доставки

    '''Создаем метод set_delivery_strategy. Он используется, чтобы «подключить» стратегию доставки к заказу.
       Внутри можно менять стратегию на любую (например, стандартная доставка или экспресс).'''

    def set_delivery_strategy(self, strategy):
        self._delivery_strategy = strategy

    '''Создаем метод calculate_delivery, который вычисляет цену доставки.
       Он делегирует расчёт подключённой стратегии (self._delivery_strategy).
       Если стратегия не задана — выдаёт ошибку.'''

    def calculate_delivery(self, distance: float, weight: float) -> float:
        if not self._delivery_strategy:
            raise ValueError("Стратегия доставки не установлена")
        return self._delivery_strategy.calculate_cost(distance, weight)

    '''Далее прописываем реализацию интерфейса Order.
       Интерфейс просто возвращает цену и описание базового заказа.'''

    def get_total_cost(self) -> float:
        return self._cost

    def get_description(self) -> str:
        return self._description


# 2. Декоратор для скидок (реализация паттерна Декоратор)
'''Создаем базовый абстрактный декоратор OrderDiscountDecorator.
   Он хранит внутри «обёрнутый» заказ (wrapped_order).
   Все конкретные скидки будут наследовать этот класс и модифицировать цену/описание.'''

class OrderDiscountDecorator(Order, ABC):
    def __init__(self, wrapped_order: Order):
        self._wrapped_order = wrapped_order

'''Реализация конкретного декоратора на примере процентной скидки PercentageDiscount. 
   Каждый конкретный декоратор должен уметь:
   - Модифицировать общую стоимость заказа с учетом скидки
   - Модифицировать описание заказа для добавления описания скидки'''

class PercentageDiscount(OrderDiscountDecorator):
    def __init__(self, wrapped_order: Order, percent: float):
        super().__init__(wrapped_order)
        self._percent = percent

    def get_total_cost(self) -> float:
        base_cost = self._wrapped_order.get_total_cost()
        return base_cost * (1 - self._percent / 100)

    def get_description(self) -> str:
        return f"{self._wrapped_order.get_description()} + скидка {self._percent}%"

'''Фиксированная по сумме скидка'''
class FixedAmountDiscount(OrderDiscountDecorator):
    def __init__(self, wrapped_order: Order, amount: float):
        super().__init__(wrapped_order)
        self._amount = amount

    def get_total_cost(self) -> float:
        base_cost = self._wrapped_order.get_total_cost()
        return max(0, base_cost - self._amount) #Реализация для случая, когда скидка превышает сумму заказа

    def get_description(self) -> str:
        return f"{self._wrapped_order.get_description()} - скидка {self._amount} руб."

'''Скидка по программе лояльности'''
class LoyaltyDiscount(OrderDiscountDecorator):
    def __init__(self, wrapped_order: Order):
        super().__init__(wrapped_order)

    def get_total_cost(self) -> float:
        base_cost = self._wrapped_order.get_total_cost()
        return base_cost * 0.9  # 10% скидка для лояльных клиентов

    def get_description(self) -> str:
        return f"{self._wrapped_order.get_description()} + скидка для лояльного клиента"

# 3. Стратегии доставки (реализация паттерна Стратегия)

'''Далее создадим класс DeliveryCostStrategy, который является абстрактным интерфейсом 
   стратегии доставки (компонент паттерна "Стратегия". Каждая стратегия должна уметь 
   считать цену доставки в зависимости от distance (расстояния) и weight (веса).'''
class DeliveryCostStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, distance: float, weight: float) -> float:
        pass

'''Далее создаем конкретные интерфейсы стратегий (разные алгоритмы, объединяемые в паттерне).
   Рассмотрим код такого интерфейса на примере стратегии стандартной доставки (StandardDelivery).'''
class StandardDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return 5 + 0.5 * distance + 0.2 * weight # Алгоритм подсчета цены стандартной доставки


class ExpressDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return 10 + 1.0 * distance + 0.5 * weight


class FreeDeliveryThreshold(DeliveryCostStrategy):
    def __init__(self, threshold: float):
        self._threshold = threshold

    def calculate_cost(self, distance: float, weight: float) -> float:
        # Бесплатно при заказе выше порога
        return 0.0



# 4. Демонстрация работы
'''Далее представлен фрагмент клиентского кода'''
# Создаём заказ®
order = BasicOrder(1000, "Заказ: ноутбук")

# Применяем скидки через декораторы
discounted_order = PercentageDiscount(order, 15)       # 15% скидка
discounted_order = LoyaltyDiscount(discounted_order)  # скидка для лояльного
discounted_order = FixedAmountDiscount(discounted_order, 100)  # минус 100 руб.

print("Описание заказа:", discounted_order.get_description())
print("Цена после скидок:", discounted_order.get_total_cost())

# Устанавливаем разные стратегии доставки
order.set_delivery_strategy(StandardDelivery())
print("Стандартная доставка:", order.calculate_delivery(distance=10, weight=2))

order.set_delivery_strategy(ExpressDelivery())
print("Экспресс-доставка:", order.calculate_delivery(distance=10, weight=2))

# Бесплатная доставка (например, при акционной сумме)
order.set_delivery_strategy(FreeDeliveryThreshold(threshold=500))
print("Бесплатная доставка:", order.calculate_delivery(distance=10, weight=2))
