class libro:
  def __init__(self,titulo,anio,genero):
    self.titulo = titulo
    self.anio = anio
    self.genero = genero
  def __str__(self):
        return '{} ({})- {}'.format(self.titulo, self.anio, self.genero)

class catalogo:
  librosss = []
  def __init__(self, librosss=[]):
        self.librosss = librosss
  def agregar(self, l):  # l puede ser un objeto libro
        self.librosss.append(l)
  def mostrar(self):
        for l in self.librosss:
            print(l)  
l = libro('Bodas de sangre', anio= 1933, genero = 'Dramático')
catalogodolibros = catalogo([l])   # Añado una lista con un libro

catalogodolibros.agregar(libro(titulo='Romeo y Julieta', anio =1595, genero= 'Dramático'))
catalogodolibros.agregar(libro(titulo='La divina comedia', anio = 1307, genero= 'Épico'))
catalogodolibros.agregar(libro(titulo='Rayuela', anio = 1963, genero= 'Novela'))

catalogodolibros.mostrar()
