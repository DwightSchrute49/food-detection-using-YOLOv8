from roboflow import Roboflow

rf = Roboflow(api_key="WhkO46oGArsxkjHLp95p")
project = rf.workspace("indianfood").project("indian_food-pwzlc")
version = project.version(2)
dataset = version.download("yolov8")
