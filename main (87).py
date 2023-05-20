class Wine:
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price

class WineManager:
    def __init__(self):
        self.wines = []

    def add_wine(self, name, year, price):
        wine = Wine(name, year, price)
        self.wines.append(wine)
        print(f"{wine.name} added to the wine collection.")

    def remove_wine(self, name):
        for wine in self.wines:
            if wine.name == name:
                self.wines.remove(wine)
                print(f"{wine.name} removed from the wine collection.")
                return
        print(f"{name} not found in the wine collection.")

    def display_wines(self):
        if not self.wines:
            print("No wines in the collection.")
        else:
            print("Wine Collection:")
            for wine in self.wines:
                print(f"Name: {wine.name}, Year: {wine.year}, Price: {wine.price}")

# Example usage
wine_manager = WineManager()

wine_manager.display_wines()

wine_manager.add_wine("Chardonnay", 2018, 29.99)
wine_manager.add_wine("Merlot", 2015, 39.99)

wine_manager.display_wines()

wine_manager.remove_wine("Chardonnay")

wine_manager.display_wines()
