# @author: Brunno Ronaldo
# @created: 2026-06-29
# @last updated: 2026-06-29
# @version: 0.1.0

# fix here later

class TriageEngine: # Remember: use the results from triage in dashboard in the future.

    @staticmethod
    def evaluate(patient):

        reasons = []

        if patient.vitals["oxygen"] < 90:
            reasons.append("Low oxygen saturation")

            return {
                "color": "RED",
                "wait_time": 0,
                "reasons": reasons
            }

        condition = patient.get_most_severe_condition()

        if condition:

            if condition.severity >= 9:
                reasons.append(
                    f"Critical condition: {condition.name}"
                )

                return {
                    "color": "RED",
                    "wait_time": 0,
                    "reasons": reasons
                }

            elif condition.severity >= 7:

                reasons.append(
                    f"Severe condition: {condition.name}"
                )

                return {
                    "color": "ORANGE",
                    "wait_time": 10,
                    "reasons": reasons
                }

        return {
            "color": "GREEN",
            "wait_time": 120,
            "reasons": ["Stable patient"]
        }

""" backup of the calculate_triage method from the Patient class, in case we need to revert to it later.

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
"""