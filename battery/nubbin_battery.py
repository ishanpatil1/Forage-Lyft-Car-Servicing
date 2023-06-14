from battery.battery import Battery

class NubbinBattery(Battery):
    def needs_servicing(self, last_servicing_date, current_date):
        return (current_date.year - last_servicing_date.year) >=4