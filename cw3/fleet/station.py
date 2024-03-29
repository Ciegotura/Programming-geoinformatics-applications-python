class Station:
    __station_id = 200
    def __init__(self, location, ambulance, driver, employee):
        self.location = location # as (northing, easting)
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        self.id = Station.__station_id
        Station.__station_id += 1

    def __str__(self):
        return f"Station {self.id}: location: {self.location}, ambulance: {self.ambulance}, driver: {self.driver}, employee: {self.employee}"
    
    def check_location(self):

        if self.location == self.ambulance.location:
            print("Ambulance is in station")
        else:
            print("Ambulance is elswhere")