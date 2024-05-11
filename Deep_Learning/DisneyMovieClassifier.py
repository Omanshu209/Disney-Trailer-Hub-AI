from torch.nn import Linear as nn_Linear
from torch import argmax as torch_argmax
from torch import load as torch_load
from torch import no_grad as torch_no_grad
from torch.cuda import is_available as cuda_is_available
from torch.nn.functional import softmax as torch_softmax
from torchvision import transforms
from torchvision.models import resnet18

labels : dict = {
	0: "Coco",
	1: "Elemental",
	2: "Encanto",
	3: "Finding Dory",
	4: "Finding Nemo",
	5: "Frozen",
	6: "Moana",
	7: "Ralph Breaks The Internet",
	8: "Toy Story",
	9: "Wreck It Ralph",
	10: "Zootopia"
}

class DisneyMovieClassifier:
	
	def __init__(self, model_path = "Model/DisneyMovieClassifier_CNN_Model.pt"):
		
		self.transform = transforms.Compose(
			[
				transforms.Resize(size = (250, 250)),
				transforms.RandomRotation(degrees = (-45, 45)),
				transforms.ToTensor(),
				
				transforms.Normalize(
					mean = (0.5, 0.5, 0.5),
					std = (0.5, 0.5, 0.5)
				)
			]
		)
		
		self.device = "cuda" if cuda_is_available() else "cpu"
		self.Model = self.load_model(model_path)
		self.Model.eval()
	
	def load_model(self, model_path):
		Model = resnet18(pretrained = True)
		
		for p in Model.parameters():
			p.requires_grad = False
		
		Model.fc = nn_Linear(512, 11)
		
		Model.load_state_dict(
			torch_load(
				model_path, 
				map_location = self.device
			)
		)
		
		return Model
	
	def transform_image(self, image):
		transformed_image = self.transform(image.convert("RGB"))
		return transformed_image
	
	def predict(self, transformed_image):
		with torch_no_grad():
			y_pred = self.Model(transformed_image.unsqueeze(0).to(self.device))
			
			probabilities = torch_softmax(y_pred, dim = 1).squeeze().detach().numpy()
			percent_probabilities = {class_label: round(prob.item() * 100) for class_label, prob in zip(labels.values(), probabilities)}
			
			y_pred_tensor = int(torch_argmax(y_pred, 1))
			y_pred_string = labels[y_pred_tensor]
		
		return (y_pred_string, percent_probabilities)