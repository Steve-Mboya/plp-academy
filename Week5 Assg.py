class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery
        self.power_on = False

    def turn_on(self):
        self.power_on = True
        print(f"{self.model} is ON")

    def install_app(self, app):
        print(f"Installing {app}...")

class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, battery, cooling):
        super().__init__(brand, model, battery)
        self.cooling = cooling

    def install_app(self, app):
        if "game" in app.lower():
            print(f"Optimizing {app} for gaming on {self.model}!")
        else:
            super().install_app(app)

phone = Smartphone("Apple", "iPhone 14", 3200)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 6")

phone.turn_on()
phone.install_app("WhatsApp")

gaming_phone.turn_on()
gaming_phone.install_app("PUBG Mobile")
