names = []

for _ in range(5):
    names.append(input("¿Cuál es su nombre?"))

for name in sorted(names):
    print(f"hello, {name}")
