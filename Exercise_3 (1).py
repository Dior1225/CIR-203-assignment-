# ==============================================
# **EXERCISE 3: PYTHON TUPLES (HEALTHCARE SECTOR)**
# ==============================================

print("EXERCISE 3: PYTHON TUPLES (HEALTHCARE SECTOR)")
patient = ("Justine Otiso", 45, "120/80", 72)
print("Patient tuple:", patient)
print("Age:", patient[1], "Heart Rate:", patient[3])

print("WHY TUPLES? They are immutable, ensuring patient vitals are not accidentally changed.")

patient_list = list(patient)
patient_list[3] = 75
patient = tuple(patient_list)
print("Updated patient tuple:", patient)

patients = (
    ("Justine Otiso", 45, "120/80", 75),
    ("Jane Smith", 30, "110/70", 80),
    ("Paul Kamau", 55, "140/90", 85),
    ("Alice Wanjiku", 40, "125/85", 78),
    ("Peter Otieno", 60, "135/88", 82)
)
names = [p[0] for p in patients]
print("Patient names:", names)
