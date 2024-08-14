paranoid_android = "Marvin, the paranoid Android"
letter = list(paranoid_android)
for char in letter[:6]:
    print('\t', char)
print()
for char in letter[-7:]:
    print('\t' * 2, char)
print()
for char in letter[12:20]:
    print('\t' * 3, char)

