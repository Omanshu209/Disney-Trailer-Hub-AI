from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.swiper.swiper import MDSwiperItem
from kivymd.uix.fitimage.fitimage import FitImage
from kivymd.uix.button.button import MDFloatingActionButton

try:
	from webview import WebView
	webview_is_available = True
	
except ModuleNotFoundError:
	import webbrowser as wb
	webview_is_available = False

from json import load
from PIL import Image

from Deep_Learning.DisneyCharacterClassifier import DisneyCharacterClassifier
from Deep_Learning.DisneyMovieClassifier import DisneyMovieClassifier

with open("assets/description.json", 'r') as file:
	movie_description = load(file)

character_classifier = DisneyCharacterClassifier(model_path = "Deep_Learning/Model/DisneyCharactersClassifier_CNN_Model.pt")

movie_classifier = DisneyMovieClassifier(model_path = "Deep_Learning/Model/DisneyMovieClassifier_CNN_Model.pt")

data = [
	["assets/images/Toy-Story.jpg", "https://youtube.com/embed/tN1A2mVnrOM"], 
	["assets/images/Frozen.jpg", "https://youtube.com/embed/TbQm5doF_Uc"], 
	["assets/images/Elemental.jpg", "https://youtube.com/embed/hXzcyx9V0xw"], 
	["assets/images/Wreck-It-Ralph.jpg", "https://youtube.com/embed/87E6N7ToCxs"], 
	["assets/images/Toy-Story-2.jpg", "https://youtube.com/embed/xNWSGRD5CzU"], 
	["assets/images/Monsters.jpg", "https://youtube.com/embed/6tCxnHCqqxg"], 
	["assets/images/Ralph-Breaks-The-Internet.jpg", "https://youtube.com/embed/_BcYBFC6zfY"], 
	["assets/images/Toy-Story-3.jpg", "https://youtube.com/embed/JcpWXaA2qeg"], 
	["assets/images/Inside-Out.jpg", "https://youtube.com/embed/1HFv47QHWJU"], 
	["assets/images/Brave.jpg", "https://youtube.com/embed/TEHWDA_6e3M"], 
	["assets/images/Incredibles.jpg", "https://youtube.com/embed/-UaGUdNJdRQ"], 
	["assets/images/Zootopia.jpg", "https://youtube.com/embed/jWM0ct-OLsM"], 
	["assets/images/Finding-Dory.jpg", "https://youtube.com/embed/JhvrQeY3doI"], 
	["assets/images/Toy-Story-4.jpg", "https://youtube.com/embed/wmiIUN-7qhE"], 
	["assets/images/Monsters-University.jpg", "https://youtube.com/embed/xBzPioph8CI"], 
	["assets/images/Frozen-2.jpg", "https://youtube.com/embed/Zi4LMpSDccc"], 
	["assets/images/Encanto.jpg", "https://youtube.com/embed/CaimKeDcudo"], 
	["assets/images/Coco.jpg", "https://youtube.com/embed/Rvr68u6k5sI"], 
	["assets/images/Inside-Out-2.jpg", "https://youtube.com/embed/VWavstJydZU"], 
	["assets/images/Moana.jpg", "https://youtube.com/embed/LKFuXETZUsI"], 
	["assets/images/Finding-Nemo.jpg", "https://youtube.com/embed/2zLkasScy7A"], 
	["assets/images/Up.jpg", "https://youtube.com/embed/HWEW_qTLSEE"], 
	["assets/images/Incredibles-2.jpg", "https://youtube.com/embed/i5qOzqD9Rms"]
]

class DisneyApp(MDApp):
	
	def __init__(self):
		super().__init__()
		self.classifier = character_classifier
	
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
		self.root.ids.title_image.source = f"assets/title-images/{movie_name}.webp"
		self.root.ids.info_box.text = movie_description[movie_name]
		self.root.ids.info_box.hint_text = movie_name.replace('-', ' ')
		
		for _, (image_path, trailer_link) in enumerate(data):
			
			if movie_name == (image_path.split('/')[2]).split('.')[0]:
				self.root.ids.movie_image.source = image_path
				
				if webview_is_available:
					self.root.ids.trailer_button.on_release = lambda parameter = trailer_link: WebView(parameter)
				
				else:
					self.root.ids.trailer_button.on_release = lambda parameter = trailer_link: wb.open(parameter)
	
	def switch_classifier(self, segmented_control, segmented_item):
		if segmented_item.text == "Character":
			self.classifier = character_classifier
		else:
			self.classifier = movie_classifier
	
	def capture_and_predict(self):
		self.root.ids.camera.export_to_png("assets/clicked_image.png")
		image = self.classifier.transform_image(Image.open("assets/clicked_image.png"))
		prediction, probability = self.classifier.predict(image)
		self.root.ids.prediction.text = prediction
		
		sorted_prob = sorted(probability.items(), key = lambda item: item[1])
		prob_text = ""
		for _, (item, percentage) in enumerate(sorted_prob):
			prob_text += f"{item} : {percentage}%\n"
		self.root.ids.prediction_card.text = prob_text

DisneyApp().run()