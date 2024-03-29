from fleet.ambulance import Ambulance
from fleet.station import Station
from operations import *
from personnel import *


def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 12000.0)
    employee2 = Employee("Jane", "Smith", 8000.0)

    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

    # sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie 2 zgłoszeń
    incident1 = Incident("Power outage in sector 4", (50, 20), 10, "12:00", "Bananas Schody-Hak")
    incident2 = Incident("Fire alarm in building 21", (55, 18), 1, "13:02", "Heniek Miska-Lama")
    queue += incident1
    queue += incident2

    # wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")

    station1 = Station((50.5, 18.5), ambulance1, driver1, employee1)
    print()
    print(f'Pierwsza stacja: {station1}')
    print()
    station1.check_location()
    ambulance1.location = (50.5, 18.5)
    station1.check_location()

    #zarządzanie incydentami 
    print()
    print("Aktualne zgłoszenia:")
    print(queue)
    incident1.add_ambulance(ambulance1) #dodaje ambulans do incydentu
    incident2.add_ambulance(ambulance1) #dodaje ambulans do incydentu
    print(queue[0].ambulance) #ambulans dodany
    assert queue[0].ambulance is not None
    print(ambulance1.incident) #incydent do ambulansu dodany
    assert ambulance1.incident is not None
    print()
    ambulance1.ambulance_works()
    print()
    for incident in queue:
        assert incident.status =="done"


if __name__ == "__main__":
    run_application()