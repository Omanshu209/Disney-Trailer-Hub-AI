from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.swiper.swiper import MDSwiperItem
from kivymd.uix.fitimage.fitimage import FitImage
from kivymd.uix.button.button import MDFloatingActionButton

from json import load
from webview import WebView
from PIL import Image
from Deep_Learning.DisneyCharacterClassifier import DisneyCharacterClassifier

with open("assets/description.json", 'r') as file:
	movie_description = load(file)

classifier = DisneyCharacterClassifier(model_path = "Deep_Learning/Model/DisneyCharactersClassifier_CNN_Model.pt")

data = [
	["assets/images/Toy-Story.jpg", "https://youtube.com/embed/tN1A2mVnrOM"], 
	["assets/images/Frozen.jpg", "https://youtube.com/embed/TbQm5doF_Uc"], 
	["assets/images/Elemental.jpeg", "https://youtube.com/embed/hXzcyx9V0xw"], 
	["assets/images/Wreck-It-Ralph.jpeg", "https://youtube.com/embed/87E6N7ToCxs"], 
	["assets/images/Toy-Story-2.jpg", "https://youtube.com/embed/xNWSGRD5CzU"], 
	["assets/images/Monsters.jpeg", "https://youtube.com/embed/6tCxnHCqqxg"], 
	["assets/images/Ralph-Breaks-The-Internet.jpeg", "https://youtube.com/embed/_BcYBFC6zfY"], 
	["assets/images/Toy-Story-3.jpg", "https://youtube.com/embed/JcpWXaA2qeg"], 
	["assets/images/Inside-Out.jpeg", "https://youtube.com/embed/1HFv47QHWJU"], 
	["assets/images/Zootopia.jpeg", "https://youtube.com/embed/jWM0ct-OLsM"], 
	["assets/images/Finding-Dory.jpeg", "https://youtube.com/embed/JhvrQeY3doI"], 
	["assets/images/Toy-Story-4.jpg", "https://youtube.com/embed/wmiIUN-7qhE"], 
	["assets/images/Monsters-University.jpeg", "https://youtube.com/embed/xBzPioph8CI"], 
	["assets/images/Frozen-2.jpg", "https://youtube.com/embed/Zi4LMpSDccc"], 
	["assets/images/Encanto.jpeg", "https://youtube.com/embed/CaimKeDcudo"], 
	["assets/images/Coco.jpeg", "https://youtube.com/embed/Rvr68u6k5sI"], 
	["assets/images/Moana.jpeg", "https://youtube.com/embed/LKFuXETZUsI"], 
	["assets/images/Finding-Nemo.jpeg", "https://youtube.com/embed/2zLkasScy7A"]
]

class DisneyApp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Blue"
		self.theme_cls.material_style = "M3"
		return Builder.load_file("Design.kv")
	
	def on_start(self):
		for _, (image_path, trailer_link) in enumerate(data):
			movie_name = (image_path.split('/')[2]).split('.')[0]
			
			self.root.ids.swiper.add_widget(
				MDSwiperItem(
				
					FitImage(
						radius = [20,], 
						source = image_path
					), 
					
					MDFloatingActionButton(
						icon = "information", 
						md_bg_color = "#f8d7e3", 
						theme_icon_color = "Custom", 
						icon_color = "#311021", 
						type = "standard", 
						on_release = lambda x, parameter = movie_name: self.update_info_screen(parameter)
					)
				)
			)
	
	def update_info_screen(self, movie_name):
		self.root.ids.info_box.text = movie_description[movie_name]
		for _, (image_path, trailer_link) in enumerate(data):
			if movie_name == (image_path.split('/')[2]).split('.')[0]:
				self.root.ids.movie_image.source = image_path
				self.root.ids.trailer_button.on_release = lambda parameter = trailer_link: WebView(parameter)
	
	def capture_and_predict(self):
		self.root.ids.camera.export_to_png("assets/clicked_image.png")
		image = classifier.transform_image(Image.open("assets/clicked_image.png"))
		self.root.ids.prediction.text = classifier.predict(image)

DisneyApp().run()