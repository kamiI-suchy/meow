# Definicja klasy Vehicle (Pojazd), która reprezentuje pojazd samochodowy
class Vehicle:
    # Atrybut klasy: lista marek samochodów wraz z krajem ich pochodzenia
    # Każdy wpis ma format "Marka,Kraj"
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
        "Jeep,USA",
        "Land Rover,UK",
    ]

    # Atrybut klasy: lista dostępnych kolorów jako krotki (nazwa, kod, kolor hex)
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

    # Atrybut klasy: licznik ID pojazdów; wspólny dla wszystkich instancji klasy
    _id_counter = 0

    # Konstruktor klasy – wywoływany przy tworzeniu nowego obiektu Vehicle
    # Parametry: brand (marka), color (kolor), vin (opcjonalny numer VIN, domyślnie pusty string)
    def __init__(self, brand, color, vin=""):
        self.brand = brand  # Zapisuje markę pojazdu jako atrybut instancji
        self.country = self._get_country_by_brand(brand)  # Pobiera kraj producenta na podstawie marki
        self.id = 0         # Inicjalizuje ID pojazdu jako 0 (zostanie nadpisane jeśli marka jest znana)
        self.vin = ""       # Inicjalizuje numer VIN jako pusty string
        self.color = None   # Inicjalizuje kolor jako None (zostanie ustawiony jeśli marka jest znana)
        self._fuel_log = [] # Inicjalizuje prywatną listę do przechowywania wpisów o tankowaniu

        # Jeśli marka jest znana (kraj nie jest None), inicjalizuj pełny pojazd
        if self.country is not None:
            type(self)._id_counter += 1       # Zwiększa licznik ID klasy o 1
            self.id = type(self)._id_counter  # Przypisuje aktualne ID temu pojazdowi
            self.setColor(color)              # Próbuje ustawić kolor pojazdu
            if vin:
                self.setVIN(vin)              # Jeśli podano VIN, próbuje go ustawić

    # Metoda statyczna – dostępna bez tworzenia instancji klasy
    # Zwraca listę marek; opcjonalnie filtruje po kraju (parametr country domyślnie pusty)
    @staticmethod
    def getBrands(country=""):
        # Jeśli nie podano kraju, zwróć wszystkie marki
        if not country:
            return [entry.split(",", 1)[0].strip() for entry in Vehicle.Brands]

        # Normalizacja nazwy kraju: usuń białe znaki i zamień na małe litery
        country_normalized = country.strip().lower()
        # Zwróć tylko marki, których kraj pasuje do podanego (porównanie bez uwzględniania wielkości liter)
        return [
            entry.split(",", 1)[0].strip()
            for entry in Vehicle.Brands
            if entry.split(",", 1)[1].strip().lower() == country_normalized
        ]

    # Prywatna metoda statyczna – wyszukuje kraj producenta na podstawie nazwy marki
    @staticmethod
    def _get_country_by_brand(brand):
        # Iteruje po każdym wpisie na liście Brands
        for entry in Vehicle.Brands:
            # Rozdziela wpis na nazwę marki i kraj, usuwając białe znaki z obu części
            brand_name, brand_country = [part.strip() for part in entry.split(",", 1)]
            # Jeśli marka pasuje do szukanej, zwróć kraj
            if brand_name == brand:
                return brand_country
        # Jeśli nie znaleziono marki, zwróć None
        return None

    # Metoda ustawiająca kolor pojazdu
    # Akceptuje nazwę koloru, kod koloru lub wartość hex; zwraca True jeśli sukces, False jeśli błąd
    def setColor(self, color):
        # Jeśli podano None, zwróć False (nie można ustawić koloru)
        if color is None:
            return False

        # Konwertuj wejście na string, usuń białe znaki i zamień na małe litery
        probe = str(color).strip().lower()
        # Przeszukaj listę kolorów szukając dopasowania po nazwie, kodzie lub hex
        for name, code, hex_code in self.Colors:
            if probe in (name.lower(), code.lower(), hex_code.lower()):
                self.color = (name, code, hex_code)  # Ustaw kolor jako krotkę (nazwa, kod, hex)
                return True  # Kolor znaleziony i ustawiony
        return False  # Kolor nie pasuje do żadnej pozycji na liście

    # Metoda ustawiająca numer VIN pojazdu
    # VIN musi być stringiem o długości dokładnie 17 znaków; zwraca True jeśli sukces, False jeśli błąd
    def setVIN(self, vin):
        if isinstance(vin, str) and len(vin) == 17:
            self.vin = vin  # Przypisuje VIN do atrybutu instancji
            return True
        return False  # VIN nieprawidłowy – zły typ lub niewłaściwa długość

    # Metoda dodająca wpis o tankowaniu do dziennika paliwa
    # Parametry: odometer (stan licznika w km), fuel (ilość paliwa w litrach)
    def addFuel(self, odometer, fuel):
        # Dodaje krotkę (stan licznika, ilość paliwa) do listy, konwertując na float
        self._fuel_log.append((float(odometer), float(fuel)))

    # Metoda obliczająca średnie zużycie paliwa w litrach na 100 km
    def fuelConsumption(self):
        # Potrzebne są co najmniej 2 wpisy (początek i koniec trasy), by obliczyć zużycie
        if len(self._fuel_log) < 2:
            return None

        start_odometer = self._fuel_log[0][0]   # Stan licznika przy pierwszym tankowaniu
        end_odometer = self._fuel_log[-1][0]     # Stan licznika przy ostatnim tankowaniu
        distance = end_odometer - start_odometer # Pokonany dystans
        # Jeśli dystans jest zerowy lub ujemny, nie można obliczyć zużycia
        if distance <= 0:
            return None

        # Suma paliwa ze wszystkich tankowań poza ostatnim
        # (ostatni wpis to końcowy stan licznika, nie tankowanie zużyte na trasie)
        fuel_used = sum(fuel for _, fuel in self._fuel_log[:-1])
        # Oblicza zużycie: (litry / km) * 100 = l/100km
        return (fuel_used / distance) * 100

    # Metoda specjalna __str__ – definiuje tekstową reprezentację obiektu (np. przy print())
    def __str__(self):
        # Jeśli kraj jest None, marka jest nieznana – zwróć uproszczony opis
        if self.country is None:
            return f"{self.id}: {self.brand} (N/A)"

        # Zaczyna budować listę szczegółów od ID, marki i kraju
        details = [f"{self.id}: {self.brand} ({self.country})"]

        # Jeśli VIN jest ustawiony, dodaj ostatnie 4 znaki poprzedzone "..."
        if self.vin:
            details.append(f"...{self.vin[-4:]}")

        # Jeśli kolor jest ustawiony, dodaj nazwę koloru i jego kod
        if self.color is not None:
            name, code, _ = self.color  # Rozpakuj krotkę koloru (ignorujemy hex "_")
            details.append(f"{name} ({code})")

        # Oblicz średnie zużycie paliwa
        avg = self.fuelConsumption()
        # Jeśli zużycie jest dostępne, sformatuj do 2 miejsc po przecinku; w przeciwnym razie wstaw "-"
        details.append(f"{avg:.2f} [l/100km]" if avg is not None else "-")

        # Połącz wszystkie elementy listy details przecinkami i zwróć jako jeden string
        return ", ".join(details)


# Blok wykonywany tylko gdy skrypt uruchamiany jest bezpośrednio (nie importowany jako moduł)
if __name__ == "__main__":
    # Tworzy pojazd Volvo z kolorem o kodzie "1J4" i numerem VIN
    vehicle_1 = Vehicle("Volvo", "1J4", vin="1234567890ABCDEFG")
    vehicle_1.addFuel(0, 20)        # Pierwsze tankowanie: licznik 0 km, 20 litrów
    vehicle_1.addFuel(234.2, 40)    # Drugie tankowanie: licznik 234.2 km, 40 litrów
    vehicle_1.addFuel(689.5, 30)    # Trzecie tankowanie: licznik 689.5 km, 30 litrów
    vehicle_1.addFuel(984.1, 30)    # Czwarte tankowanie: licznik 984.1 km, 30 litrów

    # Tworzy pojazd marki "Polonez" – marka nieznana (nie ma jej w Brands), więc ID=0 i brak kraju
    vehicle_2 = Vehicle("Polonez", "Amber Pearl", vin="ABCDEFG1234567890")

    # Tworzy pojazd Kia z kolorem "8W7" i numerem VIN
    vehicle_3 = Vehicle("Kia", "8W7", vin="WNFKEZ2390JK342CF")

    # Tworzy pojazd Toyota z kolorem "Silver Metallic" i numerem VIN
    vehicle_4 = Vehicle("Toyota", "Silver Metallic", vin="ANCBDHKEIO2345BFK")
    vehicle_4.addFuel(0, 30)        # Pierwsze tankowanie: licznik 0 km, 30 litrów
    vehicle_4.addFuel(487.8, 40)    # Drugie tankowanie: licznik 487.8 km, 40 litrów
    vehicle_4.addFuel(1029.2, 20)   # Trzecie tankowanie: licznik 1029.2 km, 20 litrów

    # Wyświetla tekstową reprezentację każdego pojazdu (wywołuje __str__)
    print(vehicle_1)
    print(vehicle_2)
    print(vehicle_3)
    print(vehicle_4)
