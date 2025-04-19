import csv

def save_to_csv(data, filename):
    if not data:
        print("[Storage] Aucune donnée à sauvegarder.")
        return

    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
