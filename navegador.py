from selenium import webdriver;

class Navegador:

	def abrir(self):
		self.navegador = webdriver.Firefox()

	def cerrar(self):
  		self.navegador.close();

	def direccion(self,url):
  		self.navegador.get('http://'+url);

  	# ----------------------

	def obtener_codigo_fuente(self):
  		pagina_fuente = (self.navegador.page_source).encode('utf-8');
  		return pagina_fuente;

	def buscar_elemento_tag(self,nombre_tag,otro = False):

		if otro:
			resultado = otro.find_element_by_tag_name(nombre_tag);
		else:
			resultado = self.navegador.find_element_by_tag_name(nombre_tag);
		return resultado;	

	def buscar_elemento_id(self,nombre_id,otro = False):

		if otro:
			resultado = otro.find_element_by_id(nombre_id);
		else:
  			resultado = self.navegador.find_element_by_id(nombre_id);
		return resultado;

	def buscar_elemento_class(self,nombre_class,otro = False):

		if otro:
			resultado = otro.find_element_by_class_name(nombre_class);
		else:
			resultado = self.navegador.find_element_by_class_name(nombre_class);
		return resultado;

	def buscar_elemento_nombre(self,nombre,otro = False):

		if otro:
			resultado = otro.find_element_by_name(nombre);
		else:
			resultado = self.navegador.find_element_by_name(nombre);
		return resultado;

	# ----------------------

	def enviar_info(self,adonde,info):

		adonde.send_keys(info);