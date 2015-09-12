from archivador import Comprobar_Archivos;

class Archivo_HTML:

    def __init__(self,original="nada",destino="nada"):

        self.archivo_original = original;
        self.archivo_destino = destino;

  # ---------------------------------

    def sangria(self):
        return "\t"

    def nuevorenglon(self):
        return "\n"

  # ---------------------------------
  # comandos

    def tag(self,lista_codigo,nombre_inicio_tag,posicion = [],temp = ['<html','<head','<body','<title','<div','<span']):

        for i in range(len(lista_codigo)):

          if nombre_inicio_tag in lista_codigo[i]:
              posicion.append(i);

        if (nombre_inicio_tag in temp):
            nombre_inicio_tag = '</'+nombre_inicio_tag[1:];
            self.tag(lista_codigo,nombre_inicio_tag,posicion);

        return posicion;

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

        if cantSaltoRenglon != 0:
            temp = parte_lista;
            temp = temp.split(obj);
            string = obj+cantSaltoRenglon*"\n"+cantTab*"\t";
            temp = string.join(temp);

        elif cantTab == 1:
            temp = cantTab*"\t"+parte_lista;

        else:
            pass;

        return temp;

    # ---------------------------------

    def codigo_HTML(self,archivo_destino,archivo_origen):
      
        tag_nombres = ['<html','<head','<body'];
        temp_l = [];

        for tn in tag_nombres:

            if tn is '<html':
                temp_l = self.archivo_TAG('leer',archivo_origen);
                temp_l[0] = self.acomodador_TAG(temp_l[0], ">" ,0,1);
                self.archivo_TAG('escribir',archivo_destino,temp_l);

            else:
                temporal = [];
                temp_l = self.archivo_TAG('leer',archivo_destino);
                temporal = self.tag(temp_l,tn);

                if len(temporal)>2:
                    temporal = temporal[2:];

                for j in range(temporal[1]-temporal[0]-1):

                    res = j + temporal[0]+1;
                    temp_l[res] = self.acomodador_TAG(temp_l[res], "<" ,1,0);

                self.archivo_TAG('escribir',archivo_destino,temp_l);

        temp_l = self.archivo_TAG('leer',archivo_destino);
        self.multiple_TAG(archivo_destino,temp_l);