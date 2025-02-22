# while - mientras

counter = 0

# while counter < 10:
#     counter += 1
#     print(counter)


# while counter < 10:
#     counter += 1
#     if counter == 5:
#         break        # Romper un ciclo
#     print(counter)

while counter < 20:
    counter += 1
    if counter < 15:
        continue        # continuar un ciclo saltando ciertas pasos
    print(counter)

# out :15, 16, 17, 18, 19, 20