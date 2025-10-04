import unittest
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image

# Importar a classe AlexNet do notebook (assumindo que ela seria exportada ou copiada para um módulo)
# Para fins de demonstração, vamos redefinir uma versão simplificada aqui.
class AlexNet(nn.Module):
    def __init__(self, num_classes=1000):
        super(AlexNet, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=11, stride=4, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(64, 192, kernel_size=5, padding=2),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
        )
        self.avgpool = nn.AdaptiveAvgPool2d((6, 6))
        self.classifier = nn.Sequential(
            nn.Dropout(),
            nn.Linear(256 * 6 * 6, 4096),
            nn.ReLU(inplace=True),
            nn.Dropout(),
            nn.Linear(4096, 4096),
            nn.ReLU(inplace=True),
            nn.Linear(4096, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

class TestNaturalImages(unittest.TestCase):

    def setUp(self):
        # Configuração para os testes
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.transform = transforms.Compose([
            transforms.Resize((227, 227)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def test_alexnet_model_instantiation(self):
        # Testa se o modelo AlexNet pode ser instanciado corretamente
        model = AlexNet(num_classes=6).to(self.device)
        self.assertIsInstance(model, AlexNet)
        self.assertEqual(model.classifier[6].out_features, 6)

    def test_alexnet_forward_pass(self):
        # Testa a passagem forward do modelo com um tensor de entrada simulado
        model = AlexNet(num_classes=6).to(self.device)
        dummy_input = torch.randn(1, 3, 227, 227).to(self.device) # Batch de 1, 3 canais, 227x227
        output = model(dummy_input)
        self.assertEqual(output.shape, (1, 6)) # Saída deve ser (batch_size, num_classes)

    def test_image_transformation(self):
        # Testa se as transformações de imagem funcionam como esperado
        # Criar uma imagem dummy
        dummy_image = Image.new("RGB", (256, 256), color = "red")
        transformed_image = self.transform(dummy_image)
        self.assertEqual(transformed_image.shape, (3, 227, 227)) # 3 canais, 227x227
        self.assertIsInstance(transformed_image, torch.Tensor)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

