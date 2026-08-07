import os
import re

folder1 = r"/Users/rutvikbarbhai/Desktop/Directory /folder1"
folder2 = r"/Users/rutvikbarbhai/Desktop/Directory /folder2"
folder3 = r"/Users/rutvikbarbhai/Desktop/Directory /folder3"

os.makedirs(folder3, exist_ok=True)

# Matches:
# EXEC PC#E1D1W
# EXEC [PC#E1D1W]
exec_pattern = re.compile(
    r'EXEC\s+\[?([A-Za-z0-9@#$]+)\]?',
    re.IGNORECASE
)

# Marks the beginning of the executable section of the PROC.
# Everything after this line will NOT be copied.
step_exec_pattern = re.compile(
    r"^//STEP\S*\s+EXEC\b",
    re.IGNORECASE
)

processed = 0
skipped = 0
missing = 0

for filename in os.listdir(folder1):

    if not filename.lower().endswith(".txt"):
        continue

    file1_path = os.path.join(folder1, filename)

    # --------------------------
    # Read Folder1 file
    # --------------------------
    with open(file1_path, "r", encoding="utf-8", errors="ignore") as f:
        content1 = f.read()

    proc_name = None

    # --------------------------
    # Find PROC name
    # --------------------------
    for match in exec_pattern.finditer(content1):

        candidate = match.group(1).strip()

        # Ignore system EXECs
        if candidate.startswith("@"):
            continue

        # We only care about PROC names
        if candidate.upper().startswith("PC"):
            proc_name = candidate
            break

    if proc_name is None:
        print(f"[SKIPPED] {filename} - PROC not found")
        skipped += 1
        continue

    proc_filename = proc_name + ".txt"
    file2_path = os.path.join(folder2, proc_filename)

    if not os.path.exists(file2_path):
        print(f"[MISSING] {proc_filename}")
        missing += 1
        continue

    # --------------------------
    # Read PROC file
    # --------------------------
    with open(file2_path, "r", encoding="utf-8", errors="ignore") as f:
        proc_lines = f.readlines()

    # --------------------------
    # Keep only PROC definition.
    # Stop before first STEP...EXEC
    # --------------------------
    filtered_proc = []

    for line in proc_lines:

        # Stop when executable section starts
        if step_exec_pattern.match(line):
            break

        filtered_proc.append(line)

    proc_content = "".join(filtered_proc).rstrip()

    # --------------------------
    # Write Output
    # --------------------------
    output_path = os.path.join(folder3, filename)

    with open(output_path, "w", encoding="utf-8") as out:

        # Original Folder1 file
        out.write(content1.rstrip())

        # Blank line
        out.write("\n\n")

        # Only PROC header (not STEP010 onwards)
        out.write(proc_content)

        out.write("\n")

    processed += 1
    print(f"[CREATED] {filename}  <-- appended {proc_filename}")

print("\n==============================")
print(f"Completed!")
print(f"Created : {processed}")
print(f"Skipped : {skipped}")
print(f"Missing : {missing}")
print("==============================")