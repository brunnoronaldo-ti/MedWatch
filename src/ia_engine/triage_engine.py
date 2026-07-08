# @author: Brunno Ronaldo
# @created: 2026-06-29
# @last updated: 2026-06-29
# @version: 0.5.0

# fix here later

class TriageEngine: # Remember: use the results from triage in dashboard in the future.

    @staticmethod
    def evaluate(patient):

        reasons = []

        if patient.vitals["oxygen"] < 90:
            reasons.append("Low oxygen saturation")

            return {
                "triage_color": "RED",
                "wait_time": 0,
                "reasons": reasons
            }
        
        #if patient.vitals # 50 < or 100 >
        
        condition = patient.get_most_severe_condition()

        if condition:

            if condition.severity >= 9:
                reasons.append(
                    f"Critical condition: {condition.name}"
                )

                return {
                    "triage_color": "RED",
                    "wait_time": 0,
                    "reasons": reasons
                }

            elif condition.severity >= 7:
                reasons.append(
                    f"Severe condition: {condition.name}"
                )

                return {
                    "triage_color": "ORANGE",
                    "wait_time": 10,
                    "reasons": reasons
                }

            elif condition.severity >= 5:
                reasons.append(
                    f"Moderate condition: {condition.name}"
                )

                return {
                    "triage_color": "YELLOW",
                    "wait_time": 30,
                    "reasons": reasons
                }
            
            elif condition.severity >= 3:
                reasons.append(
                    f"Mild condition: {condition.name}"
                )

                return {
                    "triage_color": "GREEN",
                    "wait_time": 120,
                    "reasons": reasons
                }

        return {
            "triage_color": "BLUE",
            "wait_time": 240,
            "reasons": ["Stable patient"]
        }

# backup of the calculate_triage method from the Patient class, in case we need to revert to it later.
""" 

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