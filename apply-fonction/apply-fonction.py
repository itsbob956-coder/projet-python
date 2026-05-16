
#definir une fonction apply_discount avec les parametres price et discount:
def apply_discount(price, discount):

    #si la valeur price n'est pas un nombre:
    if not isinstance(price, (int, float)) :
        return'The price should be a number'

    #si la valeur discount n'est pas un nombre:
    if not isinstance(discount, (int, float)):
        return'The discount should be a number'

    #si la valeur de price est inferieur ou egal à 0:
    if price <= 0:
        return'The price should be greater than 0'
    
    #si la valeur de discount est inferieur ou egal à 0 Or superieur ou egal à 100:
    if discount < 0 or discount > 100:
        return'The discount should be between 0 and 100'
    
    #calcul de la reduction appliquée:
    return price * (1 - discount / 100)

#afficher la fonction:
print(apply_discount(50, 0))