from fastai.vision.all import *
import gradio as gr
import timm


learner = load_learner("./export.pkl")


categorias = learner.dls.vocab

def clasificar_imagen(img):
    prediccion, indice, probabilidades = learner.predict(img)
    return dict(zip(categorias,map(float,probabilidades)))

imagen = gr.inputs.Image(shape=(500,500))
etiqueta = gr.outputs.Label()

ejemplo = ['girasol.jpg']

interfaz = gr.Interface(fn=clasificar_imagen,inputs=imagen,outputs=etiqueta, examples=ejemplo)
interfaz.launch(inline=False)