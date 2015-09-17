from archivoHTML import Archivo_HTML;
from archivador import Comprobar_Archivos;
from navegador import Navegador;

class Manage:

    def __init__(self,url):
        self.url = url;

    # ---------------------
    # No retorna nada.
    # En un atributo de clase graba el nombre de la página.
    
    def obtener_nombre_url(self,string_url):
        temp = string_url.split(".");
        self.nombre_url = temp[1];

    # ---------------------
    # No retorna nada.
    # En un atributo de clase graba la fecha de hoy.
    
    def que_dia_es_hoy(self):
        import time;
        from datetime import date;
        temp = date.today();
        self.hoy = str(temp);        

    # ---------------------
        
    def manage_inicial(self):
        ca1 = Comprobar_Archivos();
        self.obtener_nombre_url(self.url);
        ca1.crear_carpeta(self.nombre_url);        
        self.que_dia_es_hoy();
        ca1.crear_carpeta(self.nombre_url+'/'+self.hoy);

        n1 = Navegador()
        n1.abrir();
        n1.direccion(self.url);
        codigo_fuente = n1.obtener_codigo_fuente();

        archivo_inicial = self.nombre_url+'/'+self.hoy+'/ginicial.html';
        archivo_modificado =  self.nombre_url+'/'+self.hoy+'/gbuscador.html';

        ca1.crear_archivo(archivo_inicial,codigo_fuente);

        n1.cerrar();

        aH = Archivo_HTML(archivo_inicial,archivo_modificado);
        aH.codigo_HTML(aH.archivo_destino,aH.archivo_original);
        
