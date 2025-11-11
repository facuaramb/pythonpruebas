"""comprension"""



usuarios = [["chanchito", 4], ["felipe", 1], ["pulga", 5]]

#nombres = []
#for user in usuarios:
#    nombres.append(user[0])

nombres = [user[0] for user in usuarios]

print(nombres)