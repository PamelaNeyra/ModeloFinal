from flask import Flask 
from flask import flash
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from diagnostico.reglas import decidirRegla, decidirReglaFormeFruste, decidirReglaQueratocono, decidirReglaSubclinico, decidirReglaSano
import numpy as np 
import pandas as pd 
from flask import jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
import pickle
import json

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

api = Api(app)

class prediccion(Resource):
	def get(self,archivo):

		df = pd.read_csv('datosprueba/'+archivo)
		x = np.array(df[["Rh F (mm)","Rv F (mm)","Astig F (D)","Asph. Q F","Rh B (mm)","Rv B (mm)","K2 B (D)","Astig B (D)","Asph. Q B","Pachy Apex","Pachy Min","ISV","IVA","IHA","IHD","K1 (D)","K2 (D)","Astig","RPI Max","K max","I-S","AC Depth","Ecc Sup","Ecc Inf","Cor.Vol.","KPD","Ecc (Front)","Ecc (Back)","Sag. Height Mean [µm]","ACD Apex"]])

		prediccion = model.predict(x[0:1])
		resultado = prediccion.tolist()

		clasificacion = ''
		data = {}
		data['regla'] = []
		data['resultado'] = []

		if resultado[0] == 0:
			clasificacion = 'Forme Fruste'
			data['resultado'].append({
				'clasificacion':clasificacion
				})
			data['regla'].append(decidirReglaFormeFruste(x[0]))
			
		elif resultado[0] == 1:
			clasificacion = 'Queratocono'
			data['resultado'].append({
				'clasificacion':clasificacion
				})
			data['regla'].append(decidirReglaSubclinico(x[0]))
			
		elif resultado[0] == 2:
			clasificacion = 'Subclinico'
			data['resultado'].append({
				'clasificacion':clasificacion
				})
			data['regla'].append(decidirReglaQueratocono(x[0]))
			
		elif resultado[0] == 3:
			clasificacion = 'Ojo sano'
			data['resultado'].append({
				'clasificacion':clasificacion
				})
			data['regla'].append(decidirReglaSano(x[0]))
			

		return data


api.add_resource(prediccion,'/prediccion/<archivo>')

if __name__ == '__main__':
	app.run(debug=True)
