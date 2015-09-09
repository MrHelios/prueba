from archivador import Comprobar_Archivos;

class Archivo_HTML:

  def __init__(self,original="nada",destino="nada"):

    self.archivo_original = original;
    self.archivo_destino = destino;

  def sangria(self):
    return "\t"

  def nuevorenglon(self):
    return "\n"

  # ---------------------------------
  # comandos


  # ---------------------------------
  # busca la posicion inicial de un tag, arbitrario.

  def tag(self,lista,nombre_inicio):

    x0 = 0;
    for i in range(len(lista)):

      if nombre_inicio in lista[i]:
          x0 = i;
          break;

    return x0

  # ---------------------------------
  # busca la posicion final de un tag, arbitrario.

  def fin_tag(self,lista,nombre_final):

    x1 = 0;
    for i in range(len(lista)):

      if nombre_final in lista[i]:
          x1 = i;
          break;

    return x1

  # ---------------------------------
  # El código original estará en un sólo renglon.
  # Creará un archivo nuevo: donde habrá un tag por renglon.

  def primera_pasada_HTML(self,archivo_fin,archivo):

    arch_nuevo = open(archivo_fin,"w");

    temp = '';
    for i in archivo:
      temp += i;

    temp = self.acomodador_TAG(temp, ">" ,0,1);

    for i in temp:
        arch_nuevo.write(i);

    arch_nuevo.close();



  # ---------------------------------

  def pasada_TAG(self,archivo,lista,xi,xf):

    for i in range((xf - xi)-1):
      j = i + 1;
      lista[xi + j] = self.sangria() + lista[xi + j];

    self.archivo_TAG("escribir",archivo,lista);

  # ---------------------------------
  # Sólo retornará un valor en caso de lectura.

  def archivo_TAG(self,accion,archivo,lista = []):

    c1 = Comprobar_Archivos();

    if not(c1.existe_arc(archivo)):
      c1.crear_archivo(archivo);

    if accion is "escribir":
      arch_nuevo = open(archivo,"w");
      for i in lista:
        arch_nuevo.write(i);

      arch_nuevo.close();

    elif accion is "leer":

      arch_nuevo = open(archivo,'r');
      an = arch_nuevo.readlines();
      arch_nuevo.close();

      return an;


  # ---------------------------------
  # En buscar: Ej: <style ,<script ,etc.

  def multiple_TAG(self,archivo,lista,buscar="<style"):

    for i in range(len(lista)):

      if buscar in lista[i]:

        lista[i+1] = self.acomodador_TAG(lista[i+1],"{",3);
        lista[i+1] = self.acomodador_TAG(lista[i+1],";",3);
        lista[i+1] = self.acomodador_TAG(lista[i+1],"}",2,2);

    self.archivo_TAG("escribir",archivo,lista);

  # ---------------------------------

  def acomodador_TAG(self,parte_lista, obj,cantTab=2,cantSaltoRenglon=1):

    temp = parte_lista;
    temp = temp.split(obj);
    string = obj+cantSaltoRenglon*"\n"+cantTab*"\t";
    temp = string.join(temp);

    return temp;

