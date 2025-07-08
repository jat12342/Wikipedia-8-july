from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivymd.toast import toast
import wikipedia
import requests

kv='''
Manager:
	Fir:
	Sec:
				
<Fir>:
	name:'home'
	
	MDTextField:
		id:tf1
		mode:'rectangle'
        pos_hint:{'center_x':0.5,'center_y':0.85}  
        
	MDTextButton:
	    text:'SEARCH'        
        pos_hint:{'center_x':0.5,'center_y':0.78}  	 
        on_press:app.ad()      
        

	MDCard:
		id:mc1
		pos_hint:{'center_y':0.37}
		size_hint_y:0.7
		md_bg_color:1,1,1,0.5
		elevation:3
		radius:[30,30,30,30]
		ScrollView:
			id:sv1
			MDBoxLayout:
				id:b1
				adaptive_height:True
				orientation:'vertical'
				spacing:10
				padding:10
				MDCard:
					adaptive_height:True
					md_bg_color:1,0,0,0.5
					halign:'left'
					size_hint_x:None
					width:dp(250)
					radius:[0,0,0,0]
					MDLabel:
						text:'Jai Mahakal JAI MAHAKAL JAI MAHAKAL JAI MAHAKAL JAI MAHAKAL JAI MAHAKAL'
						adaptive_height:True
				





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
	

		
class Demo(MDApp):
	def build(self):
		self.b=Builder.load_string(kv)
		self.a=False
		return self.b
		
	def ad(self):
		tex=self.b.get_screen('home').ids.tf1.text
		b=self.b.get_screen('home').ids.b1
		if tex.strip()=='':
			toast(str('PLEASE ENTER PARAMETER FIRST'))
			
		else:							
			try:
				s1=wikipedia.summary(tex)
				m=MDCard(adaptive_height=True,md_bg_color=(0,0,1,1),radius=[0,0,0,0],halign='center3')		
				if self.a:
					m.md_bg_color=(1,0,0,1)
					
				else:
					m.md_bg_color=(0,1,0,1)										
				l=MDLabel(text=s1,adaptive_height=True)
				m.add_widget(l)
				b.add_widget(m)
				self.a = not self.a
				
			except requests.exceptions.RequestException:
				toast(str('NO INTERNET CONNECTION'))		
				
						
				
				
				
			except Exception as e:
				toast(str(e))																									
			
		
			






				
Demo().run()

