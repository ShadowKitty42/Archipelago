import re
import shutil
from pathlib import Path

# Paths (update if different)
project_root = Path(r"C:\Users\shado\source\repos")
arch_cs = project_root / "ArchipelagoNotIncluded" / "ArchipelagoNotIncluded.cs"
locations_py = project_root / "oni" / "Locations.py"

def parse_resources(cs_text: str):
    # find the Resources dictionary block
    m = re.search(r'public\s+static\s+Dictionary<\s*string\s*,\s*string\s*>\s+Resources\s*=\s*new\s*Dictionary<[^>]*>\s*\(\s*\)\s*{', cs_text)
    if not m:
        raise RuntimeError("Resources dictionary start not found in ArchipelagoNotIncluded.cs")
    start = m.end()
    # find closing "};" for that dictionary (first occurrence after start)
    end_match = re.search(r'\n\s*}\s*;', cs_text[start:])
    if not end_match:
        raise RuntimeError("Resources dictionary end not found in ArchipelagoNotIncluded.cs")
    block = cs_text[start:start + end_match.start()]
    # parse entries like {"Key", "Value" }
    pairs = re.findall(r'\{\s*"([^"]+)"\s*,\s*"([^"]+)"\s*\}', block)
    return {k: v for k, v in pairs}

def replace_in_locations(loc_text: str, mapping: dict):
    counts = {}
    # For deterministic behavior, sort keys by length descending to avoid partial overlap issues
    for key in sorted(mapping.keys(), key=len, reverse=True):
        value = mapping[key]
        # replace both single and double quoted forms exactly
        dq_pat = re.compile(rf'("){re.escape(key)}(")')
        sq_pat = re.compile(rf"('){re.escape(key)}(')")
        new_text, c1 = dq_pat.subn(rf'\1{value}\2', loc_text)
        loc_text = new_text
        new_text, c2 = sq_pat.subn(rf"\1{value}\2", loc_text)
        loc_text = new_text
        counts[key] = c1 + c2
    return loc_text, counts

def main():
    if not arch_cs.exists():
        print(f"ERROR: {arch_cs} not found.")
        return
    if not locations_py.exists():
        print(f"ERROR: {locations_py} not found.")
        return

    cs_text = arch_cs.read_text(encoding="utf-8")
    mapping = parse_resources(cs_text)
    print(f"Parsed {len(mapping)} Resources entries from {arch_cs}")

    loc_text = locations_py.read_text(encoding="utf-8")
    new_loc_text, counts = replace_in_locations(loc_text, mapping)

    total_replacements = sum(counts.values())
    if total_replacements == 0:
        print("No exact ItemID string-literal matches were found in Locations.py. No file changes made.")
        return

    # Backup original
    bak_path = locations_py.with_suffix(locations_py.suffix + ".bak")
    shutil.copy2(locations_py, bak_path)
    print(f"Backup written to: {bak_path}")

    # Write new file
    locations_py.write_text(new_loc_text, encoding="utf-8")
    print(f"Wrote updated {locations_py}")

    # Print summary of replacements (only keys that changed)
    print("Replacements summary (key -> count):")
    for k, v in counts.items():
        if v:
            print(f"  {k} -> {mapping[k]} : {v}")

if __name__ == "__main__":
    main()