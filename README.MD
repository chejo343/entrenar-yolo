# Detección de objectos con YOLOv5
Estructura de carpetas
```
- dataset
    - train
        - images
        - labels
    - valid
        - images
        - labels
- images
- labeles

```
Distribuir las imagenes para entrenar y validar
```
python distribuir.py
```
Instalar dependencias
```
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```
Crear archivo de configuración ```dataset.yaml```
```
train: ../dataset/train/images
val: ../dataset/valid/images
nc: 2
names: [
  "fuego", "humo"
]
```
Ejecutar entrenemiento
```
python train.py --img 640 --batch 16 --epochs 5 --data dataset.yaml --weights yolov5s.pt
```
Probar modelo
```
python detect.py --weights runs/train/exp/weights/best.pt --img 640 --conf 0.4 --source ../test.jpg
```
Referencias
* https://www.youtube.com/c/NicolaiNielsenComputerVisionAI/videos
* https://medium.com/mlearning-ai/training-yolov5-custom-dataset-with-ease-e4f6272148ad