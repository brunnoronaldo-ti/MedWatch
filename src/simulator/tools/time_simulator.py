# @author: Brunno Ronaldo
# @created: 2026-07-10
# @last updated: 2026-07-21
# @version: 0.5.0

from datetime import datetime, timedelta

class SimulationTime:
    # Atributo de classe (compartilhado)
    simulated_data = datetime.now()

    @staticmethod
    def advance_time(): # we access this method to advance the simulation time by one day with "Name"
        SimulationTime.simulated_data += timedelta(days=1)
        return SimulationTime.simulated_data.strftime('%m/%d/%Y (%A)')

    @staticmethod
    def next_day():
        SimulationTime.advance_time()