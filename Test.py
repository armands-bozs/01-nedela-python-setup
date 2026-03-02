# Vienkārša datu analīzes programma

print("Ievadi skaitļus (atdalītus ar komatiem):")
raw = input("> ")

# Pārvēršam ievadi par skaitļu sarakstu
numbers = [float(x.strip()) for x in raw.split(",")]

avg = sum(numbers) / len(numbers)
mn = min(numbers)
mx = max(numbers)

print("\n--- Rezultāti ---")
print(f"Skaitļu skaits: {len(numbers)}")
print(f"Minimums: {mn}")
print(f"Maksimums: {mx}")
print(f"Vidējā vērtība: {avg:.2f}")

# Vienkārša analīze
if avg > 100:
    print("Vidējā vērtība ir diezgan liela.")
elif avg > 10:
    print("Vidējā vērtība ir vidēja.")
else:
    print("Vidējā vērtība ir maza.")
