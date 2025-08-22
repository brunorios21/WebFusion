from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Si usas Gmail
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'tu_correo@gmail.com'  # Tu correo de Gmail
app.config['MAIL_PASSWORD'] = 'tu_contraseña'  # Tu contraseña (o contraseña de aplicación)
app.config['MAIL_DEFAULT_SENDER'] = 'tu_correo@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Crear el mensaje
        msg = Message(f"Nuevo mensaje de {nombre}",
                      recipients=["tu_correo@gmail.com"])  # Aquí va tu correo de destino
        msg.body = f"Nombre: {nombre}\nEmail: {email}\n\nMensaje:\n{mensaje}"

        # Enviar el correo
        try:
            mail.send(msg)
            print(f"Mensaje enviado de {nombre} ({email})")
            return render_template('gracias.html')
        except Exception as e:
            print("Error al enviar el mensaje:", e)
            return render_template('error.html', error=e)

    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)
