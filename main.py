from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDLabel

kv='''
Manager:
	Fir:
	Sec:
				
<Fir>:
	name:'home'
	


	MDLabel:
		text:'HAR HAR MAHADEV'
		halign:'center'		
		
		
	Click:
		id:l1
		text:'click state 1'
		size_hint:0.3,0.1
		pos_hint:{'center_x':0.5,'center_y':0.8}
		on_press:app.c()

	MDTopAppBar:
		id:t1
		title:'HAR HAR MAHADEV'
		pos_hint:{'top':1}



'''

class Manager(ScreenManager):
	pass
	


class Fir(Screen):
	pass
	

class Sec(Screen):
	pass	
	
class Click(ButtonBehavior,MDLabel):
	pass	

		
class Demo(MDApp):
	def build(self):
		self.b=Builder.load_string(kv)
		self.a=False
		return self.b
		
	def c(self):
		aa=self.b.get_screen('home').ids.l1
		if self.a:
			aa.text='click state 1'		
			self.b.get_screen('home').ids.t1.title='HAR HAR MAHADEV'			
								
		else:
			aa.text='click state 2'
			self.b.get_screen('home').ids.t1.title='JAI MAHAKAL'
								
		self.a = not self.a		
		
			






				
Demo().run()

