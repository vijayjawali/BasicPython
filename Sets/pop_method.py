# drugs
amlodipine = ("amlodipine", "Blood pressure")
buspirone = ("buspirone", "Anxiety disorders")
carbimazole = ("carbimazole", "Antithyroid agent")
citalopram = ("citalopram", "Antidepressant")
edoxaban = ("edoxaban", "anti-coagulant")
erythromycin = ("erythromycin", "Antibiotic")
lusinopril = ("lusinopril", "High blood pressure")
metformin = ("metformin", "Type 2 diabetes")
methotrexate = ("methotrexate", "Rheumatoid arthritis")
paracetamol = ("paracetamol", "Painkiller")
propranol = ("propranol", "Beta blocker")
simvastatin = ("simvastatin", "High cholesterol")
warfarin = ("warfarin", "anti-coagulant")

# Patient prescriptions
patients = {
    "Anne": {methotrexate, paracetamol},
    "Bob": {carbimazole, erythromycin, methotrexate, paracetamol},
    "Charley": {buspirone, lusinopril, metformin},
    "Denise": {amlodipine, lusinopril, metformin, warfarin},
    "Eddie": {amlodipine, propranol, simvastatin, warfarin},
    "Frank": {buspirone, citalopram, propranol, warfarin},
    "Georgia": {carbimazole, edoxaban, warfarin},
    "Helmut": {erythromycin, paracetamol, propranol, simvastatin},
    "Izabella": {amlodipine, citalopram, simvastatin, warfarin},
    "John": {simvastatin},
    "Kenny": {amlodipine, citalopram, metformin},
}

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)