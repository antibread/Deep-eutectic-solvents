INPUT_FILE =  "C/Orca/outfile.out"
def parse_orca_out(INPUT_FILE):
  parsed_data = {
        "success": False,
        "final_energy": None,
        "gibbs": None,
        "atoms": [],
    }
  with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if "FINAL SINGLE POINT ENERGY" in line:
            parsed_data["final_energy"] = float(line.split()[4])
        if "Final Gibbs free energy" in line:
            parsed_data["gibbs"] = float(line.split()[5])
        if "ORCA TERMINATED NORMALLY" in line:
            parsed_data["success"] = True
    print(f'Final Gibbs free energy: {parsed_data["gibbs"]} Eh')
    print(f'FINAL SINGLE POINT ENERGY: {parsed_data["final_energy"]} Eh')
    print("ORCA TERMINATED NORMALLY")
    return parsed_data
try:
  parse_orca_out(INPUT_FILE)
except FileNotFoundError:
  print(f"File {INPUT_FILE} not found")


