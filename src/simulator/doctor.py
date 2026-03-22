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
    
    def update_contact(self, new_contact):
        self.contact = new_contact

    def update_work_sector(self, new_sector):
        self.work_sector = new_sector

    def update_name(self, new_name):
        self.name = new_name

    def update_doctor_id(self, new_id):
        self.doctor_id = new_id

    def add_doctor(self, doctor_id, name, work_sector, contact):
        self.doctor_id = doctor_id
        self.name = name
        self.work_sector = work_sector
        self.contact = contact

    def __str__(self):
        return f"doctor {self.doctor_id} - {self.name} - {self.work_sector} - {self.contact}"