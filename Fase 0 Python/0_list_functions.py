lucky_numbers = [4, 8, 15, 16, 23, 42] # Crea una lista de números de la suerte
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"] # Crea una lista de amigos
friends2 = friends.copy() # Crea una copia de la lista de amigos
# friends.extend(lucky_numbers) | Agrega los números de la suerte a la lista de amigos
friends.append("Creed") # Agrega "Creed" al final de la lista de amigos
friends.insert(1, "Kelly") # Inserta "Kelly" en la posición 1 de la lista de amigos
# friends.remove("Jim") | Elimina "Jim" de la lista de amigos
# friends.pop() | Elimina el último elemento de la lista de amigos (en este caso, no hay elementos para eliminar)
# friends.clear() | Limpia la lista de amigos, dejándola vacía
print(friends) # Imprime la lista de amigos
print(friends.index("Kevin")) # Imprime el índice de "Kevin" en la lista de amigos
print(friends.count("Jim")) # Imprime cuántas veces aparece "Jim" en la lista de amigos
friends.sort() # Ordena la lista de amigos alfabéticamente
print(friends) # Imprime la lista de amigos ordenada
lucky_numbers.reverse() # Invierte el orden de la lista de números de la suerte
print(lucky_numbers) # Imprime la lista de números de la suerte invertida
print(friends2) # Imprime la copia de la lista de amigos (sin modificaciones)