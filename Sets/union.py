farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)

all_animals_3 = wild_animals | farm_animals
print(all_animals_3)

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

# Drugs that shouldn't be taken together
adverse_interactions = [
    {metformin, amlodipine},
    {simvastatin, erythromycin},
    {citalopram, buspirone},
    {warfarin, citalopram},
    {warfarin, edoxaban},
    {warfarin, erythromycin},
    {warfarin, amlodipine},
]

meds_to_watch = set()

for interaction in adverse_interactions:
    meds_to_watch = meds_to_watch.union(interaction)

print(sorted(meds_to_watch))

# union update
meds_to_watch = set()

for interaction in adverse_interactions:
    meds_to_watch.update(interaction)

print(sorted(meds_to_watch))


