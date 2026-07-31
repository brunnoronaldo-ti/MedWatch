# Forms to generate patients (examples):


## form 1 (I call this "normal form"):

```form_1.py
from simulator.patient_generator import generate_patient
from simulator.hospital import HospitalConfig, Hospital

patient = generate_patient(patient_id=1)
print(patient)  # Patient 1 - John (45)
```

## form 2 (With specific conditions):

```form_2.py
# 2 disease
patient = generate_patient(patient_id=1, num_conditions=2)

# 3 disease
patient = generate_patient(patient_id=2, num_conditions=3)
```