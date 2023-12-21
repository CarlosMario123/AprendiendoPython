from UtilSelenium.Driver import Driver
from saveLocal.saveLocal import saveLocalFile
driver = Driver("https://www.mercadolibre.com.mx/ofertas#nav-header")
#script para traer imagenes de producto de mercado libre
imgRuta = driver.get_imagenes()

for i in range(10):
   saveLocalFile(imgRuta[i])
