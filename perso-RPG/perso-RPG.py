#projet pris depuis freecodecamp - certificat python!
full_dot = '●'
empty_dot = '○'

def create_character(name, force, intelligence, charisme):
    stats = [force, intelligence, charisme]
    
    if type(name) is not str:
        return "The character name should be a string"
    if name == '':
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'
    if type(stats[0]) is not int or type(stats[1]) is not int or type(stats[2]) is not int:
         return 'All stats should be integers'
    if stats[0] < 1 or stats[1] < 1 or stats[2] < 1:
        return 'All stats should be no less than 1'
    if stats[0] > 4 or stats[1] > 4 or stats[2] > 4:
        return 'All stats should be no more than 4'
    if sum(stats) != 7:
        return 'The character should start with 7 points'

    barre_force = "●" * stats[0] + "○" * (10 - stats[0])
    barre_intel = "●" * stats[1] + "○" * (10 - stats[1])
    barre_charisme = "●" * stats[2] + "○" * (10 - stats[2])
    
    resultat = f"{name}\nSTR {barre_force}\nINT {barre_intel}\nCHA {barre_charisme}"
    
    return resultat