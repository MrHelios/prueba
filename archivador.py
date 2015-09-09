from os.path import exists;
import os;

class Comprobar_Archivos():

  # ---------------------------------
  # constructor

  def __init__(self,arc_orginal="codigo_fuente_google.html",arc_nuevo="html_google.html"):

    self.archivo_original = arc_orginal;
    self.archivo_nuevo = arc_nuevo;
    self.puede = False;

  # ---------------------------------
  # comandos

  def existe_arc(self,nombre):
    return exists(nombre);

  # ---------------------------------

  def borrar_arc(self,nombre):
    self.puede = False;

    if self.existe_arc(nombre):
      os.remove(nombre);
      self.puede = True;

    return self.puede;

  # ---------------------------------


  def crear_archivo(self,nombre,datos="vacio"):
    self.puede = False;

    if not(self.existe_arc(nombre)):
      arc = open(nombre,"w");
      if datos != "vacio":
        arc.write(str(datos));
      arc.close;
      self.puede = True;
    else:
      self.borrar_arc(nombre);
      self.crear_archivo(nombre,datos);

    return self.puede;


  # ---------------------------------

  def crear_carpeta(self,nombre):
    self.puede = False;

    if not(self.existe_arc(nombre)):
      os.mkdir(nombre);
      self.puede = True;

    return self.puede;

