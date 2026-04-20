class Vehicle:
    Brands = [
        "Alfa Romeo,Italy",
        "Audi,Germany",
        "BMW,Germany",
        "Chevrolet,USA",
        "Dodge,USA",
        "Ferrari,Italy",
        "Honda,Japan",
        "Jaguar,UK",
        "Lamborghini,Italy",
        "Mazda,Japan",
        "McLaren,UK",
        "Mercedes-Benz,Germany",
        "Nissan,Japan",
        "Porsche,Germany",
        "Fiat,Italy",
        "Mini,Germany",
        "Subaru,Japan",
        "Bentley,UK",
        "Buick,USA",
        "Ford,USA",
        "Hyundai,South Korea",
        "Lexus,Japan",
        "Maserati,Italy",
        "Roush,USA",
        "Volkswagen,Germany",
        "Acura,Japan",
        "Cadillac,USA",
        "Infiniti,Hong Kong",
        "Kia,South Korea",
        "Mitsubishi,Japan",
        "Rolls-Royce,UK",
        "Toyota,Japan",
        "Volvo,Sweden",
        "Chrysler,USA",
        "Lincoln,USA",
        "GMC,USA",
        "Chevrolet,USA",
        "Jeep,USA",
        "Land Rover,UK",
    ]

    Colors = [
        ("Pure White", "40", "#FDFDF7"),
        ("Silver Metallic", "1F7", "#D7D7CB"),
        ("Magnetic Gray Metallic", "1G3", "#7E7A7A"),
        ("Cement Gray Metallic", "1H5", "#807E7A"),
        ("Mercury Gray Metallic", "1H9", "#48433A"),
        ("Sonic Silver Metallic", "1J2", "#F4F4F2"),
        ("Platinum Silver Metallic", "1J4", "#C3C1B9"),
        ("Sonic Titanium Metallic", "1J7", "#77726F"),
        ("Shimmering Silver", "1LO", "#808080"),
        ("Cement Gray Metallic", "1H5", "#807E7A"),
        ("Eclipse Black", "209", "#0A1A10"),
        ("Matador Red Tricoat", "3R1", "#7C1010"),
        ("Red Pearl", "3T3", "#9B2825"),
        ("Imperial Red", "3U5", "#F31515"),
        ("Amber Pearl", "4X2", "#80391A"),
        ("Oxide Bronze", "6X1", "#C27842"),
        ("Dark Blue Metallic", "8W7", "#351FA7"),
        ("Blue Pearl Tricoat", "8X1", "#23128C"),
        ("Medium Blue Tricoat", "8X2", "#597DF3"),
        ("Deep Blue Pearl", "8X5", "#281F4F"),
        ("Light Topaz Metallic", "40", "#E2C496"),
        ("Blizzard Pearl Tricoat", "70", "#F4F1DE"),
        ("White Nova GF Pearl Tricoat", "83", "#F9F9F1"),
        ("Sonic Quartz Tricoat", "85", "#E7E1D3"),
        ("Platinum Pearl White", "89", "#FFFFFF"),
        ("Black", "212", "#0E0E0E"),
        ("Attitude Black Pearl", "218", "#0E0E0E"),
        ("Graphite Black Gf Effect", "223", "#2F2919"),
        ("Gloss Trim Black", "39063", "#463838"),
    ]

    _id_counter = 0
    _brands_map = {}

    for entry in Brands:
        brand_name, brand_country = [part.strip() for part in entry.split(",", 1)]
        _brands_map[brand_name] = brand_country

    def __init__(self, brand, color, vin=""):
        self.brand = brand
        self.country = self._brands_map.get(brand)
        self.id = 0
        self.vin = ""
        self.color = None
        self._fuel_log = []

        if self.country is not None:
            type(self)._id_counter += 1
            self.id = type(self)._id_counter
            self.setColor(color)
            if vin:
                self.setVIN(vin)

    @staticmethod
    def getBrands(country=""):
        if not country:
            return [entry.split(",", 1)[0].strip() for entry in Vehicle.Brands]

        country_normalized = country.strip().lower()
        return [
            entry.split(",", 1)[0].strip()
            for entry in Vehicle.Brands
            if entry.split(",", 1)[1].strip().lower() == country_normalized
        ]

    def setColor(self, color):
        if color is None:
            return False

        probe = str(color).strip().lower()
        for name, code, hex_code in self.Colors:
            if probe in (name.lower(), code.lower(), hex_code.lower()):
                self.color = (name, code, hex_code)
                return True
        return False

    def setVIN(self, vin):
        if isinstance(vin, str) and len(vin) == 17:
            self.vin = vin
            return True
        return False

    def addFuel(self, odometer, fuel):
        self._fuel_log.append((float(odometer), float(fuel)))

    def fuelConsumption(self):
        if len(self._fuel_log) < 2:
            return None

        start_odometer = self._fuel_log[0][0]
        end_odometer = self._fuel_log[-1][0]
        distance = end_odometer - start_odometer
        if distance <= 0:
            return None

        fuel_used = sum(fuel for _, fuel in self._fuel_log[:-1])
        return (fuel_used / distance) * 100

    def __str__(self):
        if self.country is None:
            return f"{self.id}: {self.brand} (N/A)"

        details = [f"{self.id}: {self.brand} ({self.country})"]

        if self.vin:
            details.append(f"...{self.vin[-4:]}")

        if self.color is not None:
            name, code, _ = self.color
            details.append(f"{name} ({code})")

        avg = self.fuelConsumption()
        details.append(f"{avg:.2f} [l/km]" if avg is not None else "-")

        return ", ".join(details)


if __name__ == "__main__":
    vehicle_1 = Vehicle("Volvo", "1J4", vin="1234567890ABCDEFG")
    vehicle_1.addFuel(0, 20)
    vehicle_1.addFuel(234.2, 40)
    vehicle_1.addFuel(689.5, 30)
    vehicle_1.addFuel(984.1, 30)

    vehicle_2 = Vehicle("Polonez", "Amber Pearl", vin="ABCDEFG1234567890")

    vehicle_3 = Vehicle("Kia", "8W7", vin="WNFKEZ2390JK342CF")

    vehicle_4 = Vehicle("Toyota", "Silver Metallic", vin="ANCBDHKEIO2345BFK")
    vehicle_4.addFuel(0, 30)
    vehicle_4.addFuel(487.8, 40)
    vehicle_4.addFuel(1029.2, 20)

    print(vehicle_1)
    print(vehicle_2)
    print(vehicle_3)
    print(vehicle_4)
