class Perro:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
    #self.peso=''
    
    
  def ladrido(self):
    print('{} dice guau'.format(self.nombre))
    
  def __str__(self):
    return "Soy el perro " + self.nombre

chicho= Perro('chicho', 4)
chicho.peso=12

print(chicho)
print(chicho.peso)


