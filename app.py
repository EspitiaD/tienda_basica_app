from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Diccionario que guarda cantidades temporalmente
registro = {
    'azucar': 0,
    'harina': 0,
    'huevos': 0
}

# Guardar producto actual entre pasos
producto_seleccionado = {'nombre': ''}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/seleccionar/<producto>')
def seleccionar_producto(producto):
    if producto in registro:
        producto_seleccionado['nombre'] = producto
        return render_template('cantidad.html', producto=producto)
    return redirect(url_for('index'))

@app.route('/registrar', methods=['POST'])
def registrar():
    cantidad = request.form.get('cantidad')
    producto = producto_seleccionado['nombre']
    try:
        cantidad = float(cantidad)
        registro[producto] += cantidad
    except:
        pass
    return redirect(url_for('resumen'))

@app.route('/resumen')
def resumen():
    return render_template('resumen.html', registro=registro)

if __name__ == '__main__':
    app.run(debug=True)
