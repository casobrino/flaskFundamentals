from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.before_request
def before_request():
    print('ANTES de la Peticion')

@app.after_request
def after_request(response):
    print('DESPUES de la peticion #############')
    return response

@app.route('/')
def index():
    print('DURANTE la peticion')
    data={
    'titulo': 'Index',
    "encabezado": "Bienvenido(@)"
}
    return render_template('index.html', data=data)

@app.route('/hola-mundo')
def hola_mundo():
    return 'Hola mundo :D'

@app.route('/contacto')
def contacto():
    data={
    'titulo': 'Contacto',
    "encabezado": "Bienvenido(@)"
}
    return render_template('contacto.html', data=data)

@app.route('/saludo/<nombre>')
def saludo(nombre):
    #return "!HOLA :P"
    return "!HOLA {0}," .format(nombre)

@app.route('/suma/<int:valor1>/<int:valor2>')
def suma(valor1, valor2):
    return 'Lasuma es: {0}' .format(valor1 + valor2)

@app.route('/lenguajes')
def lenguajes():
    data={
        'hay_lenguajes':False,
        'lenguajes':{
            'PHP', 'Kotlin', 'C#'
        }
    }
    return render_template('lenguajes.html', data=data)

@app.route('/datos')
def datos():
    #print(request.args)
    nombre=request.args.get('nombre')
    return 'Estos son los datos {0}' .format(nombre)
    
if __name__ == '__main__' :
    app.run(debug=True, port=5005)
