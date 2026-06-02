# @author: Brunno Ronaldo
# @created: 2026-03-22
# @last updated: 2026-05-31
# @version: 0.4.1

import random
from simulator import patient
from simulator import nurse 

class Doctor_config:
    def __init__(self, name,  specialty, doctor_id, experience_years):
        self.name = name
        self.specialty = specialty
        self.doctor_id = doctor_id
        self.experience_years = experience_years
        

    def __str__(self):
        return f"Doctor {self.doctor_id} - {self.name} - Specialty: {self.specialty} - {self.experience_years} years of experience"
    
class Doctor:
    def __init__(self, config: Doctor_config, burnout_meditor=10, working=False, eficacy=1.0, sucesses_rate=100):
        self.config = config

        self.burnout_meditor = burnout_meditor
        self.working = working
        self.eficacy = eficacy
        self.sucesses_rate = int(self.eficacy * 100)

    def doctor_burnout(self):
        #this function will decrease the eficacy of the doctor based on the burnout_meditor and the working hours
        if self.working:
            self.burnout_meditor += 1

            if self.burnout_meditor >= 10:
                self.eficacy -= 0.1
                self.burnout_meditor = 0

        #aleatory burnout event
        personal_problems_chance = random.randint(1, 10)
        if personal_problems_chance == 1:
            self.eficacy -= 0.05

        #limit
        self.eficacy = max(0, self.eficacy)

    def work(self):
        self.working = True
        self.doctor_burnout()
        self.sucesses_rate = int(self.eficacy * 100)

    #
    def treat_patient(self, patient):
        success = random.random() #o sucesso é aleatório por enquanto, mas no futuro podemos adicionar um bônus de eficácia baseado na experiência do médico e na especialidade relacionada ao problema do paciente.

        # calculate the sucesses based on the doctor atributes
         

        if success < self.eficacy:
            patient.condition.severity -= 2
        else:
            patient.condition.severity += 1

  
# Experiência médica não serve para nada
# A experiência médica é apenas um número que não tem impacto real na eficácia do tratamento. O que realmente importa é a dedicação e o cuidado do médico com o paciente.
# no futuro add um def que dá bonus de eficácia baseado na experiência, mas por enquanto é só um número decorativo.

# Especialidade também não serve para nada
# A especialidade do médico é apenas um título que não tem impacto real na eficácia do tratamento. O que realmente importa é a dedicação e o cuidado do médico com o paciente.
# temos cardiologia, neurologia, ortopedia, pediatria, psiquiatria, dermatologia, ginecologia, urologia, oftalmologia, otorrinolaringologia, endocrinologia, gastroenterologia, 
# nefrologia, reumatologia, hematologia, oncologia, imunologia, alergologia, infectologia, geriatria e medicina de emergência. No futuro podemos adicionar um bônus de eficácia para tratamentos relacionados à especialidade do médico.
# além de add problemas que necessitem de uma especialidade específica, e o médico que tiver essa especialidade terá um bônus de eficácia no tratamento. Por exemplo, um paciente com um problema cardíaco terá um bônus de eficácia se for tratado por um cardiologista.