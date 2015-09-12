from archivoHTML import Archivo_HTML;
from archivador import Comprobar_Archivos;
from navegador import Navegador;

class Tester:

    def test_basico(self):

        n1 = Navegador();
        n1.abrir();
        n1.direccion('www.google.com.ar');

        ca1 = Comprobar_Archivos();
        ca1.crear_carpeta("Google");
        ca1.crear_carpeta("Google/Codigo_Fuente");

        cf = n1.obtener_codigo_fuente();

        ca1.crear_archivo("Google/Codigo_Fuente/google_buscador.html",cf);

        ca1.crear_carpeta("Google/Codigo_Modificado");
        ca1.crear_archivo("Google/Codigo_Modificado/google_buscador.html");

        aH = Archivo_HTML("Google/Codigo_Fuente/google_buscador.html","Google/Codigo_Modificado/google_buscador.html");
        aH.codigo_HTML(aH.archivo_destino,aH.archivo_original);

        n1.cerrar();


if __name__=='__main__':

    t = Tester().test_basico();
