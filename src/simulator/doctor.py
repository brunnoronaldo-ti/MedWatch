# @author: Brunno Ronaldo
# @created: 2026-03-22
# @last updated: 2026-03-22
# @version: 0.1.0

class Doctor:
    def __init__(self, doctor_id, name, work_sector, contact):
        self.name = name
        self.work_sector = work_sector
        self.contact = contact
        self.doctor_id = doctor_id

    def get_doctor(self):
        return self.doctor_id, self.name, self.work_sector, self.contact

    def __str__(self):
        return f"doctor {self.doctor_id} - {self.name} - {self.work_sector} - {self.contact}"