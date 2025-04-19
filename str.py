import os

# Chemin du dossier à analyser
root_dir = r"C:\Users\Abdel\Desktop\qq"
output_file = os.path.join(root_dir, "folder_structure.txt")

with open(output_file, "w", encoding="utf-8") as f:
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Calcul de l'indentation pour afficher la hiérarchie
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = ' ' * 4 * level
        f.write(f"{indent}[{os.path.basename(dirpath)}]\n")
        subindent = ' ' * 4 * (level + 1)
        for file in filenames:
            f.write(f"{subindent}{file}\n")

print(f"Structure du dossier enregistrée dans : {output_file}")
