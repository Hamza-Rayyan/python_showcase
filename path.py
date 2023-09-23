from pathlib import Path

path = Path("ecomerce")
for file in path.glob('*.py'):
    print(file)

