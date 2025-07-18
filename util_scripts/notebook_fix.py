"""
TypeError: cell.source.join is not a function
If this error occurs when rendering the pages, run this script.
This will convert teh Jupyter notebook cell into an array of strings.
"""
import json

notebook_path = "../posts/13-Announcing-pharmacophore-toolkit.ipynb"


def fix_notebook(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    changed = False
    for cell in nb.get('cells', []):
        source = cell.get('source')
        if isinstance(source, str):
            # Convert string to single-item list
            cell['source'] = [source]
            changed = True
        elif isinstance(source, list) and any(not isinstance(line, str) for line in source):
            # Ensure all elements are strings
            cell['source'] = [str(line) for line in source]
            changed = True

    if changed:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print(f"✅ Fixed notebook: {filename}")
    else:
        print(f"✔️ Notebook is already valid: {filename}")


if __name__ == "__main__":
    fix_notebook(notebook_path)
