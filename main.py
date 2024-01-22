from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.swiper.swiper import MDSwiperItem
from kivymd.uix.fitimage.fitimage import FitImage
from kivymd.uix.button.button import MDFloatingActionButton
from webview import WebView
from PIL import Image
from Deep_Learning.DisneyCharacterClassifier import DisneyCharacterClassifier

classifier = DisneyCharacterClassifier(model_path = "Deep_Learning/Model/DisneyCharactersClassifier_CNN_Model.pt")

data = [
	["assets/images/Toy-Story.jpg", "https://youtu.be/tN1A2mVnrOM"], 
	["assets/images/Frozen.jpg", "https://youtu.be/TbQm5doF_Uc"], 
	["assets/images/Elemental.jpeg", "https://youtu.be/hXzcyx9V0xw"], 
	["assets/images/Wreck-It-Ralph.jpeg", "https://youtu.be/87E6N7ToCxs"], 
	["assets/images/Toy-Story-2.jpg", "https://youtu.be/xNWSGRD5CzU"], 
	["assets/images/Monsters.jpeg", "https://youtu.be/6tCxnHCqqxg"], 
	["assets/images/Ralph-Breaks-The-Internet.jpeg", "https://youtu.be/_BcYBFC6zfY"], 
	["assets/images/Toy-Story-3.jpg", "https://youtu.be/JcpWXaA2qeg"], 
	["assets/images/Zootopia.jpeg", "https://youtu.be/jWM0ct-OLsM"], 
	["assets/images/Toy-Story-4.jpg", "https://youtu.be/wmiIUN-7qhE"], 
	["assets/images/Monsters-University.jpeg", "https://youtu.be/xBzPioph8CI"], 
	["assets/images/Frozen-2.jpg", "https://youtu.be/Zi4LMpSDccc"], 
	["assets/images/Encanto.jpeg", "https://youtu.be/CaimKeDcudo"], 
	["assets/images/Moana.jpeg", "https://youtu.be/LKFuXETZUsI"]
]

class DisneyApp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Blue"
		return Builder.load_file("Design.kv")
	
	def on_start(self):
		for _, (image_path, trailer_link) in enumerate(data):
			self.root.ids.swiper.add_widget(
				MDSwiperItem(
				
					FitImage(
						radius = [20,], 
						source = image_path
					), 
					
					MDFloatingActionButton(
						icon = "movie-filter", 
						md_bg_color = "blue", 
						type = "standard", 
						on_release = lambda x, parameter = trailer_link: WebView(parameter)
					)
				)
			)
	
	def capture_and_predict(self):
		self.root.ids.camera.export_to_png("assets/clicked_image.png")
		image = classifier.transform_image(Image.open("assets/clicked_image.png"))
		self.root.ids.prediction.text = classifier.predict(image)

DisneyApp().run()