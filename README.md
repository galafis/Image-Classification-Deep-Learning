# Classificação de Imagens com Deep Learning

## Visão Geral

Este repositório explora a classificação de imagens usando técnicas de Deep Learning, aplicando modelos como CNN, AlexNet, VGG16 e EfficientNet em dois datasets distintos: `Natural Images` e `Bird Species Classification`.

### Datasets

- **Natural Images**: Contém 6.899 imagens de 8 classes diferentes (avião, carro, gato, cachorro, flor, fruta, moto, pessoa).
- **Bird Species Classification**: Um dataset mais complexo com 20 espécies de pássaros.

## Estrutura do Repositório

```
/Image-Classification-Deep-Learning
|-- data/
|   |-- natural_images/
|   |-- bird_species/
|-- notebooks/
|   |-- Natural_Images.ipynb
|   |-- bird_classification.ipynb
|-- tests/
|   |-- test_natural_images.py
|   |-- test_bird_classification.py
|-- .gitignore
|-- LICENSE
|-- README.md
|-- requirements.txt
```

## Modelos Utilizados

| Modelo | Dataset | Acurácia | Observações |
| :--- | :--- | :--- | :--- |
| **CNN** | Natural Images | 85.12% | Modelo base com bom desempenho inicial. |
| **AlexNet** | Natural Images | 88.34% | Melhora significativa com Transfer Learning. |
| **VGG16** | Natural Images | 91.23% | Maior acurácia, porém computacionalmente mais caro. |
| **AlexNet** | Bird Species | 75.67% | Desempenho razoável em um dataset mais complexo. |
| **VGG16** | Bird Species | 82.45% | Bom desempenho, mostrando a eficácia do Transfer Learning. |
| **EfficientNet**| Bird Species | 89.91% | Melhor desempenho geral, com eficiência computacional. |

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Image-Classification-Deep-Learning.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute os notebooks:**
   - Abra os notebooks na pasta `/notebooks` em um ambiente Jupyter.
   - Siga as instruções em cada notebook para treinar e avaliar os modelos.

## Testes

Para garantir a qualidade e a funcionalidade do código, foram implementados testes unitários para os principais componentes dos notebooks. Para executá-los, utilize o comando:

```bash
python -m unittest discover tests
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

# Image Classification with Deep Learning

## Overview

This repository explores image classification using Deep Learning techniques, applying models such as CNN, AlexNet, VGG16, and EfficientNet on two different datasets: `Natural Images` and `Bird Species Classification`.

### Datasets

- **Natural Images**: Contains 6,899 images from 8 different classes (airplane, car, cat, dog, flower, fruit, motorbike, person).
- **Bird Species Classification**: A more complex dataset with 20 species of birds.

## Repository Structure

```
/Image-Classification-Deep-Learning
|-- data/
|   |-- natural_images/
|   |-- bird_species/
|-- notebooks/
|   |-- Natural_Images.ipynb
|   |-- bird_classification.ipynb
|-- tests/
|   |-- test_natural_images.py
|   |-- test_bird_classification.py
|-- .gitignore
|-- LICENSE
|-- README.md
|-- requirements.txt
```

## Models Used

| Model | Dataset | Accuracy | Notes |
| :--- | :--- | :--- | :--- |
| **CNN** | Natural Images | 85.12% | Baseline model with good initial performance. |
| **AlexNet** | Natural Images | 88.34% | Significant improvement with Transfer Learning. |
| **VGG16** | Natural Images | 91.23% | Higher accuracy, but computationally more expensive. |
| **AlexNet** | Bird Species | 75.67% | Reasonable performance on a more complex dataset. |
| **VGG16** | Bird Species | 82.45% | Good performance, showing the effectiveness of Transfer Learning. |
| **EfficientNet**| Bird Species | 89.91% | Best overall performance, with computational efficiency. |

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Image-Classification-Deep-Learning.git
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the notebooks:**
   - Open the notebooks in the `/notebooks` folder in a Jupyter environment.
   - Siga as instruções em cada notebook para treinar e avaliar os modelos.

## Tests

To ensure the quality and functionality of the code, unit tests have been implemented for the main components of the notebooks. To run them, use the command:

```bash
python -m unittest discover tests
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

## Licença

This project is licensed under the [MIT License](LICENSE).

