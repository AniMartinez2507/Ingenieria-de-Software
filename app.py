from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tareas
tareas = []

@app.route('/')
def index():
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar():
    tarea = request.form.get('tarea')
    if tarea:
        tareas.append(tarea)
    return redirect(url_for('index'))

@app.route('/eliminar/<int:tarea_id>')
def eliminar(tarea_id):
    if 0 <= tarea_id < len(tareas):
        tareas.pop(tarea_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
