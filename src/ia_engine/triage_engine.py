# @author: Brunno Ronaldo
# @created: 2026-06-29
# @last updated: 2026-06-29
# @version: 0.1.0

# fix here later

def calculate_triage(self):
        condition = self.get_most_severe_condition()

        if not condition:
            self.triage_level = "BLUE"
            return

        if condition.severity >= 9:
            self.triage_level = "RED"

        elif condition.severity >= 7:
            self.triage_level = "ORANGE"

        elif condition.severity >= 5:
            self.triage_level = "YELLOW"

        elif condition.severity >= 3:
            self.triage_level = "GREEN"

        else:
            self.triage_level = "BLUE"