import torch
import torch.nn as nn
from torchvision import transforms, models

labels : dict = {
	"Buzz Lightyear": 0, 
	"Dory": 1, 
	"Elsa": 2,
	"Judy Hopps": 3,
	"Mike Wazowski": 4,
	"Moana": 5,
	"Nick Wilde": 6,
	"Olaf": 7,
	"Ralph": 8,
	"Woody": 9
}

class DisneyCharacterClassifier:
	
	def __init__(self, model_path = "Model/DisneyCharactersClassifier_CNN_Model.pt"):
		
		self.transform = transforms.Compose(
			[
				transforms.Resize((250, 250)),
				transforms.ToTensor(),
				
				transforms.Normalize(
					mean = [0.485, 0.456, 0.406],
					std = [0.229, 0.224, 0.225]
				)
			]
		)
		
		self.device = "cuda" if torch.cuda.is_available() else "cpu"
		self.Model = self.load_model(model_path)
	
	def load_model(self, model_path):
		Model = models.resnet18(pretrained = True)
		
		for p in Model.parameters():
			p.requires_grad = False
		
		Model.fc = nn.Linear(512, 10)
		
		Model.load_state_dict(
			torch.load(
				model_path, 
				map_location = self.device
			)
		)
		
		return Model
	
	def transform_image(self, image):
		transformed_image = self.transform(image.convert("RGB"))
		return transformed_image
	
	def predict(self, transformed_image):
		self.Model.eval()
		with torch.no_grad():
			y_pred = self.Model(transformed_image.unsqueeze(0).to(self.device))
			y_pred_tensor = torch.max(y_pred, 1)[1]
			y_pred_string = [i for i in labels if labels[i] == y_pred_tensor][0]
		return y_pred_string