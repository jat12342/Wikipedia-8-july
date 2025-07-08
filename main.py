from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
import requests
import webbrowser
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image,AsyncImage
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDRoundFlatIconButton, MDRoundFlatButton, MDFloatingActionButton, MDIconButton
from kivy.metrics import dp
import requests
import time
import mimetypes
import random
from android.permissions import request_permissions, Permission
from kivy.animation import Animation
from kivy.utils import platform
from android.storage import primary_external_storage_path
import os
import wikipedia
import re
import datetime
from kivy.clock import Clock
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
        
    MDIconButton:
        id:ib1
        icon:'magnify'        
        pos_hint:{'center_x':0.5,'center_y':0.75}
        on_release:app.ad()
        
        
        
    MDCard:
        orientation: 'vertical'
        size_hint_y: 0.65
        pos_hint: {'center_y': 0.35}
        padding: dp(10)
        elevation: 5
        radius: [100,100,100, 100]
        md_bg_color: 0.95, 0.95, 0.95, 1  # Light grey
        size_hint_x: 0.95
        pos_hint: {'center_x': 0.5}        
        
        ScrollView:
            id:sv1
                   
            MDBoxLayout:
                id:b1
                orientation:'vertical'
                adaptive_height:True
                spacing:20
                padding:25
                MDCard:
                    id:md1
                    adaptive_height:True
                    md_bg_color:0.862, 0.973, 0.776, 1
                    halign:'left'
                    size_hint_x:None
                    width:dp(250)
                    pos_hint:{'left':1}
                    MDLabel:
                        text:'HAR HAR MAHADEV'
                        adaptive_height:True
                      
    
    
    
    MDTopAppBar:
        title:'APK'
        id:ta1
        pos_hint:{'top':1}
        left_action_items:[['menu']]





'''

class Manager(ScreenManager):
    pass
    

class Fir(Screen):
    pass
    
class Sec(Screen):
    pass







class demo(MDApp):
    def build(self):
        self.b=Builder.load_string(kv)
       
      
        return self.b
        
        
    def ad(self,*args):
        s=self.b.get_screen('home').ids.b1
        t1=self.b.get_screen('home').ids.tf1.text
        try:
            if t1.strip()=='':
                toast(str('PLEASE ENTER FIRST'))

            else:          
                try:                   
                    w1=wikipedia.summary(t1)                           
                    um=MDCard(md_bg_color=(0.862, 0.973, 0.776, 1),adaptive_height=True,halign='right',size_hint_x=None,width=dp(250),pos_hint={'right':1},radius=[0,0,0,0])
                    wm=MDCard(md_bg_color=(0.839, 0.925, 0.976, 1),adaptive_height=True,halign='left',size_hint_x=None,width=dp(250),pos_hint={'left':1},radius=[0,0,0,0])
                    
                    ul=MDLabel(text=t1,adaptive_height=True)
                    wl=MDLabel(text=w1,adaptive_height=True)
                    um.add_widget(ul)      
                    wm.add_widget(wl)  
                    s.add_widget(um)
                    s.add_widget(wm)
                    
                except wikipedia.exceptions.DisambiguationError:
                    toast(" Too many results found. Please be more specific.")

                except wikipedia.exceptions.PageError:
                    toast(" No matching page found on Wikipedia.")
    
                except wikipedia.exceptions.RedirectError:
                    toast("Unexpected redirect error occurred.")
        
                except wikipedia.exceptions.HTTPTimeoutError:
                    toast("Wikipedia request timed out. Try again.")
        
                except wikipedia.exceptions.WikipediaException:
                    toast("An unexpected Wikipedia error occurred.")    
                    
                except requests.exceptions.RequestException:
                    toast(" Network connection error")                                    
                                                                    
            
        except Exception as e:
            toast(str(e))   
        
                










                                                                

demo().run()

















