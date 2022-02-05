from kivy.app import App
from kivy.lang import Builder
import requests

gui = Builder.load_file("screen.kv")

class MyApp(App):
	def build(self):
		return gui
		
	def on_start(self):
		self.root.ids['currency1'].text = f"Dolar R${self.get_quotation('USD')}"
		self.root.ids['currency2'].text = f"Euro R${self.get_quotation('EUR')}"
		self.root.ids['currency3'].text = f"Bitcoin R${self.get_quotation('BTC')}"
		self.root.ids['currency4'].text = f"Ethereum R${self.get_quotation('ETH')}"
		
	def get_quotation(self, currency):
		link = f"https://economia.awesomeapi.com.br/last/{currency}-BRL"
		req = requests.get(link)
		req_dict = req.json()
		quot = req_dict[f'{currency}BRL']['bid']
		return quot

if __name__ == "__main__":	
	MyApp().run()
