import matplotlib.pyplot as plt
plt.style.use('ggplot')

reta_x = [1,10]
reta_y = [1000,15000]

Anos_estudo = [2, 3, 7, 10, 3]
Salario = [3000, 5000, 9000, 15000, 4000]
	
plt.scatter(x=Anos_estudo, y=Salario)
plt.plot(reta_x, reta_y)
plt.xlabel("Anos de estudo")
plt.ylabel("Salario")
plt.show()