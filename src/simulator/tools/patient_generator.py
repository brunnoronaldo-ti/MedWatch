# @author: Brunno Ronaldo
# @created: 2026-06-19
# @version: 0.1.0

import json
import random
import os
from typing import List, Dict, Optional
from simulator.patient import Patient, Condition
from simulator.hospital import HospitalConfig

# Seed data for names
male_names = [
    "John", "Michael", "Robert", "James", "William",
    "David", "Richard", "Joseph", "Thomas", "Charles",
    "Daniel", "Matthew", "Anthony", "Mark", "Donald",
    "Steven", "Paul", "Andrew", "Joshua", "Kenneth",
    "Christopher", "George", "Edward", "Ronald", "Timothy"
]

female_names = [
    "Mary", "Patricia", "Jennifer", "Linda", "Barbara",
    "Elizabeth", "Susan", "Jessica", "Sarah", "Karen",
    "Nancy", "Lisa", "Betty", "Margaret", "Sandra",
    "Ashley", "Kimberly", "Emily", "Donna", "Michelle",
    "Dorothy", "Carol", "Amanda", "Melissa", "Deborah"
]

# Cache for loaded diseases
_disease_cache = None

def load_diseases() -> Dict:
    """
    Load disease library from JSON file and cache result.
    Returns dict of disease_name -> disease_attributes.
    """
    global _disease_cache

    if _disease_cache is not None:
        return _disease_cache

    disease_file = os.path.join(
        os.path.dirname(__file__),
        'tools',
        'disease_library.json'
    )

    try:
        with open(disease_file, 'r') as f:
            data = json.load(f)
            _disease_cache = data.get('content', {}).get('disease_library', {})
            return _disease_cache
    except FileNotFoundError:
        print(f"Warning: Disease library not found at {disease_file}")
        return {}
    except json.JSONDecodeError:
        print(f"Warning: Failed to parse disease library JSON")
        return {}


def generate_random_name(gender: Optional[str] = None) -> str:
    """
    Generate a random patient name.

    Args:
        gender: "M" for male, "F" for female, None for random

    Returns:
        Random name string
    """
    if gender == "M":
        return random.choice(male_names)
    elif gender == "F":
        return random.choice(female_names)
    else:
        return random.choice(male_names + female_names)


def generate_age() -> int:
    """
    Generate realistic patient age with weighted distribution:
    - 60% adults (18-65)
    - 25% elderly (65+)
    - 15% pediatric (0-17)

    Returns:
        Age as integer
    """
    distribution = random.choices(
        ['adult', 'elderly', 'pediatric'],
        weights=[60, 25, 15],
        k=1
    )[0]

    if distribution == 'adult':
        return random.randint(18, 65)
    elif distribution == 'elderly':
        return random.randint(65, 100)
    else:  # pediatric
        return random.randint(0, 17)


def generate_condition(disease_name: str, severity_override: Optional[float] = None) -> Optional[Condition]:
    """
    Create a Condition object from disease library data.

    Args:
        disease_name: Name of disease from disease_library.json
        severity_override: Optional custom severity (0-10), otherwise uses base with ±10% variance

    Returns:
        Condition object or None if disease not found
    """
    diseases = load_diseases()
    disease_data = diseases.get(disease_name.lower())

    if not disease_data:
        print(f"Warning: Disease '{disease_name}' not found in library")
        return None

    # Calculate severity with variance if not overridden
    if severity_override is not None:
        severity = severity_override
    else:
        base_severity = disease_data.get('severity', 5)
        variance = base_severity * 0.1
        severity = max(0, min(10, base_severity + random.uniform(-variance, variance)))

    condition = Condition(
        name=disease_name,
        severity=severity,
        base_recovery_time=disease_data.get('recovery_time', 7),
        contagious=disease_data.get('contagious', False),
        treatments=disease_data.get('treatments', []),
        symptoms=disease_data.get('symptoms', [])
    )

    return condition


def generate_patient(patient_id: int, num_conditions: Optional[int] = None) -> Patient:
    """
    Generate a single patient with random demographics and conditions.

    Args:
        patient_id: Unique patient identifier
        num_conditions: Number of conditions for patient.
                       If None: 70% chance 1 condition, 30% chance 2-3 conditions
                       If int: exactly that many random conditions

    Returns:
        Patient object with assigned conditions
    """
    name = generate_random_name()
    age = generate_age()

    patient = Patient(patient_id, name, age)

    # Determine number of conditions
    if num_conditions is None:
        if random.random() < 0.7:
            num_conditions = 1
        else:
            num_conditions = random.randint(2, 3)

    # Load available diseases and randomly select conditions
    diseases = load_diseases()
    if not diseases:
        return patient

    disease_names = list(diseases.keys())

    for _ in range(num_conditions):
        disease_name = random.choice(disease_names)
        condition = generate_condition(disease_name)
        if condition:
            patient.add_condition(condition)

    return patient


def generate_patients_batch(count: int, hospital_config: HospitalConfig) -> List[Patient]:
    """
    Generate multiple patients and admit them to hospital.

    Args:
        count: Number of patients to generate
        hospital_config: HospitalConfig instance to admit patients to

    Returns:
        List of generated Patient objects that were admitted
    """
    admitted_patients = []
    patient_id = 1

    for _ in range(count):
        # Check if hospital has capacity
        if len(hospital_config.patients) >= hospital_config.capacity:
            print(f"Warning: Hospital at capacity. Only generated {len(admitted_patients)} of {count} patients.")
            break

        patient = generate_patient(patient_id)
        if hospital_config.admit_patient(patient):
            admitted_patients.append(patient)
            patient_id += 1

    return admitted_patients
