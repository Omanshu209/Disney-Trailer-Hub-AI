from kivymd.app import MDApp
from kivy.lang import Builder
from PIL import Image
from Deep_Learning.DisneyCharacterClassifier import DisneyCharacterClassifier

classifier = DisneyCharacterClassifier(model_path = "Deep_Learning/Model/DisneyCharactersClassifier_CNN_Model.pt")

class DisneyApp(MDApp):
	
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Blue"
		return Builder.load_file("Design.kv")
	
	def capture_and_predict(self):
		self.root.ids.camera.export_to_png("assets/clicked_image.png")
		image = classifier.transform_image(Image.open("assets/clicked_image.png"))
		self.root.ids.prediction.text = classifier.predict(image)

DisneyApp().run()