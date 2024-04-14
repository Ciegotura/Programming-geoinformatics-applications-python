import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Sprawdź zadoby, weźnice, pracownicy_pospolici, stacja")
    parser.add_argument("--ambulanse", "-a", required=True, help="ambulanse do sprawdzenia")
    parser.add_argument("--woznice", "-w", required=True, help="woznice do wyswietlenia")
    parser.add_argument("--pracownice", "-p", required=True, help="pracownice do wyświetlenia")
    parser.add_argument("--stacje", "-s", required=True, help="stacje do wyświetlenia")
    
    return parser.parse_args()