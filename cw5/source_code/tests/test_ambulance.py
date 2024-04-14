import pytest
from fleet.ambulance import Ambulance
from fleet.station import Station
from operations import *
from personnel import *


def test_ambulans():

    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    assert ambulance1 is not None, f'ambulans sie nie zrobil'


def test_station():

    ambulance1=1
    driver1=1
    employee1=1

    station1 = Station((50.5, 18.5), ambulance1, driver1, employee1)
    assert station1 is not None, f'ambulans sie nie zrobil'


def test_employee():

    employee1 = Employee("John", "Doe", 12000.0)
    assert employee1 is not None, f'employe sie nie zrobil'


def test_driver():

    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    assert driver1 is not None, f'driver sie nie zrobil'


def test_queue():

    queue = IncidentQueue()
    assert queue is not None, f'queue sie nie zrobil'

