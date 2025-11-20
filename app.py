from flask import Flask,render_template,url_for , request, redirect, flash, session


app = Flask(__name__)
app.secret_key = '2423415414'


Usuarios_Registrados = {}

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombres = request.form.get('nombre')
        apellido = request.form.get('apellido')
        email = request.form.get('email')
        contraseña = request.form.get('password')  
        confirmarcontraseña = request.form.get('confirm')  
        
        if contraseña != confirmarcontraseña:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for('registro'))
        
        if email in Usuarios_Registrados:
            flash("Este email ya está registrado.", "error")
            return redirect(url_for('registro'))

        
        Usuarios_Registrados[email] = {
            'nombre': '' + nombres,
            'password': contraseña,
        }

        flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for('inicio'))

    return render_template('registro.html')

@app.route('/Validalogin', methods=['POST'])
def Validalogin():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    if not email or not password:
        flash('Por favor ingresa email y contraseña', 'error')
        return redirect(url_for('inicio'))

    if email in Usuarios_Registrados:
        usuario = Usuarios_Registrados[email]
        if usuario['password'] == password:
            session['usuario_email'] = email
            session['usuario'] = usuario['nombre']
            session['logueado'] = True
            flash(f'Bienvenido {usuario["nombre"]}', 'success')
            return redirect(url_for('base'))
        else:
            flash('Contraseña incorrecta', 'error')
    else:
        flash('Usuario no encontrado', 'error')

    return redirect(url_for('iniciar_se'))

@app.route('/logout')
def logout():
    session.clear()
    flash(f'Has cerrado sesión correctamente', 'info')
    return redirect(url_for('iniciar_se'))

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/iniciar_se')
def iniciar_se():
    return render_template('iniciar_se.html')


@app.route('/Educacion')
def Educacion():
    return render_template('Educacion.html')

@app.route('/modulo_herr')
def modulo_herr():
    return render_template('modulo_herr.html')

@app.route('/etiquetas')
def etiquetas():
    return render_template('etiquetas.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/mitos')
def mitos():
    return render_template('mitos.html')

@app.route('/guia')
def guia():
    return render_template('guia.html')

@app.route('/hidratacion')
def hidratacion():
    return render_template('hidratacion.html')




if __name__ == '__main__':
    app.run(debug=True)



