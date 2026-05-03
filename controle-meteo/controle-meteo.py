#laboratoire freecodecamp - certification python
# mes variables
distance_mi = 30
is_raining = False
has_bike = False
has_car = True
has_ride_share_app = True

# 1. Vérification si la distance est fausse (0 ou None)
if not distance_mi:
    print(False)

# 2. Distance courte (0 à 1 mile) : Marche possible seulement s'il ne pleut pas
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)

# 3. Distance moyenne (1 à 6 miles) : Vélo ET pas de pluie nécessaires
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)

# 4. Longue distance (> 6 miles) : Voiture OU application nécessaires
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)