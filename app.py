from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use("Agg")  # Configuración para modo sin cabeza
import matplotlib.pyplot as plt
from io import BytesIO
import base64


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bar', methods=['GET'])
def bar():
    selected = request.args.get('selected')
    with open('Output_ModeloSEPS_Predict_2020330.json', 'r') as json_file:
        data = json.load(json_file)
        # Filtra los datos para la cooperativa seleccionada
        cooperativa_data = next(item for item in data if item['NombreCooperativa'] == selected)
        # Extrae los valores de liquidez y ROE
        liquidez = cooperativa_data['Liquidez']
        roe = cooperativa_data['ROE']
        #scores = cooperativa_data['Score']
        # Crea los datos para la gráfica
        data = [
            {
                'x': ['liquidez', 'ROE'],
                'y': [liquidez, roe],
                'type': 'bar'
            }
        ]
    return jsonify(data)
######################## Aqui va el código###############
##score

@app.route('/boxplot', methods=['GET'])
def boxplot():
    selected = request.args.get('selected')
    with open('Output_ModeloSEPS_Predict_2020330.json', 'r') as json_file:
        data = json.load(json_file)
        # Filtra los datos para la fecha seleccionada
        cooperativas = [item['NombreCooperativa'] for item in data if item['FechaAnalisis'] == selected]
        scores = [item['Score'] for item in data if item['FechaAnalisis'] == selected]
         # Ordena los datos en orden descendente según el Score
        sorted_data = sorted(zip(cooperativas, scores), key=lambda x: x[1], reverse=True)
        cooperativas, scores = zip(*sorted_data)
        # Crea los datos para la gráfica de barras horizontales
        data = [
            {
                'x': cooperativas,
                'y': scores,
                'type': 'bar',
                #'orientation': 'h'
            }
        ]
    return jsonify(data)

##################
@app.route('/barlineas', methods=['GET'])
def lineasbar():
    selected = request.args.get('selected')
    with open('Output_ModeloSEPS_Predict_2020330.json', 'r') as json_file:
        data = json.load(json_file)
        # Filtra los datos para la fecha seleccionada
        roes = [item['ROE'] for item in data if item['FechaAnalisis'] == selected]
        cooperativas = [item['NombreCooperativa'] for item in data if item['FechaAnalisis'] == selected]
        liquidez = [item['Liquidez'] for item in data if item['FechaAnalisis'] == selected]
        
         # Ordena los datos en orden descendente según el Score
        #sorted_data = sorted(zip(cooperativas, scores), key=lambda x: x[1], reverse=True)
        #cooperativas, scores = zip(*sorted_data)
        # Crea los datos para la gráfica de barras horizontales
        data = [
            {
                'x':cooperativas,
                'y': liquidez,
                'type': 'bar',
                'name': 'liquidez',
            },
            {
                'x':cooperativas,
                'y': roes,
                'type': 'lines',
                'name': 'ROE',
            }
        ]
    return jsonify(data)


############### TIME SERIES #########################

@app.route('/timeseries', methods=['GET'])
def timeseries():
    selected = request.args.get('selected')
    with open('Output_ModeloTimeSeries_IndicadoresFinancieros.json', 'r') as json_file:
        data = json.load(json_file)
        # Filtra los datos para la cooperativa seleccionada
        cooperativa_data = next(item for item in data if item['NombreCooperativa'] == selected)
        
        # Extrae los valores de fecha y COBERTURA_CARTERA_PROBLEMATICA
        fecha_analisis = []
        cobertura_cartera = []
        
        for item in data:
            if item['NombreCooperativa'] == selected:
                fecha_analisis.append(item['FechaAnalisis'])
                cobertura_cartera.append(item['COBERTURA_CARTERA_PROBLEMATICA'])
        
        # Crea los datos para la gráfica
        data = [
            {
                'x': fecha_analisis,
                'y': cobertura_cartera,
                'type': 'line'  # Puedes usar 'line' para una gráfica de líneas
            }
        ]
        
    return jsonify(data)


######################grafico de PIE##############
@app.route('/pie', methods=['GET'])
def pie():
    selected = request.args.get('selected')
    with open('Output_ModeloSEPS_Predict_2020330.json', 'r') as json_file:
        data = json.load(json_file)
        # Filtra los datos para la cooperativa seleccionada
        cooperativa_data = next(item for item in data if item['NombreCooperativa'] == selected)
        
        # Extrae los valores que deseas representar en el gráfico de pastel
        total_cartera_neta90 = cooperativa_data['TOTAL_CARTERA_NETA90']
        total_cartera_bruta90 = cooperativa_data['TOTAL_CARTERA_BRUTA90']
        total_cartera_vencida90 = cooperativa_data['TOTAL_CARTERA_VENCIDA90']
        
        # Crea los datos para el gráfico de pastel
        labels = ['TOTAL_CARTERA_NETA90', 'TOTAL_CARTERA_BRUTA90', 'total_cartera_vencida90']
        values = [total_cartera_neta90, total_cartera_bruta90, total_cartera_vencida90]
        
        data = [
            {
                'labels': labels,
                'values': values,
                'type': 'pie'
            }
        ]
    return jsonify(data)


###########################
############# El número de muentras no permite generar un cluster##3
@app.route('/boxplot777', methods=['GET'])
def a():
    selected = request.args.get('selected')
    with open('Output_ModeloSEPS_Predict_2020330.json', 'r') as json_file:
        data = json.load(json_file)
        # Filtra los datos para la cooperativa seleccionada
        selected_coop_data = next(item for item in data if item['FechaAnalisis'] == selected)

        # Crea listas para almacenar los datos
        NombreCooperativa = []
        Score = []

        for item in data:
            NombreCooperativa.append(item['NombreCooperativa'])
            Score.append(item['Score'])

        # Ordena los datos en orden descendente según el Score
        sorted_data = sorted(zip(NombreCooperativa, Score), key=lambda x: x[1], reverse=True)
        NombreCooperativa, Score = zip(*sorted_data)

        # Crea los datos para la gráfica de barras
        data = [
            {
                'x': Score,
                'y': NombreCooperativa,
                'type': 'bar',
                'orientation': 'h'
            }
        ]

        # Crea la imagen del cluster en base64
        img_base64 = None
        if len(selected_coop_data) >= 3:  # Asegurarse de tener suficientes datos para el clustering
            kmeans = KMeans(n_clusters=3)
            cluster_labels = kmeans.fit_predict(np.array(selected_coop_data['Score']).reshape(-1, 1))

            # Crea el gráfico de dispersión de los clusters
            plt.figure(figsize=(8, 6))
            plt.scatter(selected_coop_data['Liquidez'], selected_coop_data['ROE'], c=cluster_labels, cmap='rainbow')
            plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='black', label='Centroides')
            plt.xlabel('Liquidez')
            plt.ylabel('ROE')
            plt.title('Gráfico de Cluster')
            plt.legend()
            plt.grid(True)

            # Convierte la imagen en base64
            img_buf = BytesIO()
            plt.savefig(img_buf, format='png')
            img_base64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
            img_buf.close()

            # Cierra la figura para liberar recursos
            plt.close()

        # Crea el diccionario de respuesta
        response_data = {
            'data': data,
            'cluster_plot': img_base64
        }

    return jsonify(response_data)
##########

if __name__ == '__main__':
    app.run(debug=True)