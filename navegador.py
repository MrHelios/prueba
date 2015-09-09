from selenium import webdriver;

class Navegador:

  def abrir(self):
    self.navegador = webdriver.Firefox();

  def cerrar(self):
    self.navegador.close();

  def direccion(self,url):
    self.navegador.get('http://'+url);

  def obtener_codigo_fuente(self):
    pagina_fuente = (self.navegador.page_source).encode('utf-8');
    return pagina_fuente;

