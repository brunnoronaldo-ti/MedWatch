# @author: Brunno Ronaldo
# @created: 2026-07-26
# @last updated: 2026-07-26
# @version: 0.5.1

class SimulationMetrics:
    def __init__(self):
        self.total_patients = 0
        self.attended_patients = 0
        self.deaths = 0
        self.discharges = 0

        self.red = 0
        self.orange = 0
        self.yellow = 0
        self.green = 0
        self.blue = 0

        self.total_wait_time = 0

        self.total_treatment = 0

        self.doctor_statistics = {}
        self.nurse_statistics = {}

    
