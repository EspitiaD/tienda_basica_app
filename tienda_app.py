from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Diccionario que guarda cantidades temporalmente
registro = {
    'azúcar': 0,
    'harina': 0,
    'huevos': 0
}

# Variable para guardar el producto seleccionado
producto_actual = {'nombre': ''}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/seleccionar/<producto>')
def seleccionar_producto(producto):
    if producto in registro:
        producto_actual['nombre'] = producto
        return render_template('cantidad.html', producto=producto)
    return redirect(url_for('index'))

@app.route('/registrar', methods=['POST'])
def registrar():
    cantidad = request.form.get('cantidad')
    producto = producto_actual['nombre']
    try:
        cantidad = float(cantidad)
        registro[producto] += cantidad
    except ValueError:
        pass
    return redirect(url_for('resumen'))

@app.route('/resumen')
def resumen():
    return render_template('resumen.html', registro=registro)

if __name__ == '__main__':
    app.run(debug=True)

