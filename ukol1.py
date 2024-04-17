from dataclasses import dataclass
from typing import Dict, List

# ==== 1.CAST  DEFINICE TRID ===

@dataclass
class Item:
    name: str
    price: float

    def__str__(self):
       return f"{self.name}: {self.price} Kc."

@dataclass
class Pizza (Item):
        ingredients: Dict [str,int]

    def add_extra(self, ingredient, quantity, price_per_ingredient)
        ingredient: str
        quantity: int
        price_per_ingredient: float

        self.ingredients[ingredient]=quantity
        self.price += price_per_ingredient * quantity

    def__str__(self):
        return f"Pizza {self.name} and ingredient/s {self.ingredients} the total price is{self.price} Kc."


@dataclass
class Drink (Item):
      volume: int   #objem napoje v ml

      def__str__(self):
        return f"{self.name}, volume: {self.volume}, Price:{self.price} Kc."


# ======= 2.CAST ORDER========

@dataclass
class Order:
      customer_name: str
      delivery_address: str
      items: List[Item]
      status: str = "Nova" #stav objednavky
      
      def mark_delivered(self):
        self.status = "Doruceno"

      def__str__(self):
        return f" Shrnuti objednavky. Zakaznik: {self.customer_name}, adresa: {self.delivery_address}, objenavka: {self.items}, stav: {self.status}."
    
    
# === 3. CAST DELIVERY PERSON===

@dataclass
class DeliveryPerson:
        name: str
        phone_number: str
        available: bool
        current_order: Order

        def assign_order(order):
             pass
        
        def complete_delivery(self):
             pass
        
        def__str__(self):
            return f"Dorucovatel: {self.name}, dostupny: {self.available}."
