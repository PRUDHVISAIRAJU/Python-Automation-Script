import os

folder = "test_files"

files = os.listdir(folder)

i = 1
for filename in files:
    # Skip python files
    if filename.endswith(".py"):
        continue

    old_path = os.path.join(folder, filename)
    new_name = f"file_{i}.txt"
    new_path = os.path.join(folder, new_name)

    os.rename(old_path, new_path)
    i += 1

print("All files renamed successfully!")