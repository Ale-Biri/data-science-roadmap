is_male = True
is_tall = False

if is_male or is_tall: #si es hombre o alto imprime el mensaje
    print("You are a male or tall or both")

if is_male and is_tall: #si es hombre y alto imprime el mensaje
    print("You are a tall male")

elif is_male and not(is_tall): #si es hombre y no es alto imprime el mensaje
    print("You are a short male")

elif not(is_male) and is_tall: #si no es hombre y es alto imprime el mensaje
    print("You are not a male but you are tall")

else: #si no es hombre ni alto imprime el mensaje
    print("You neither male nor tall")
