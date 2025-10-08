import json

script_path = os.path.dirname(__file__)
data_dir = os.path.join(script_path, "..", "data")

file1_path = os.path.join(data_dir, "file1.json")
file2_path = os.path.join(data_dir, "file2.json")

with open("donald_trump.json", "r") as f1, open("george_orwell.json", "r") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

subjects1 = set()
for doc in data1.get("docs", []):
    subjects1.update(doc.get("top_subjects", []))

subjects2 = set()
for doc in data2.get("docs", []):
    subjects2.update(doc.get("top_subjects", []))

common_subjects = subjects1 & subjects2
unique_to_file1 = subjects1 - subjects2
unique_to_file2 = subjects2 - subjects1

print("Subjects in both files:")
print(common_subjects if common_subjects else "None")

print("\nSubjects only in Trump:")
print(unique_to_file1 if unique_to_file1 else "None")

print("\nSubjects only in Orwell:")
print(unique_to_file2 if unique_to_file2 else "None")