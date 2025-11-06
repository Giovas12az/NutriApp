from flask import Flask,render_template,url_for , request, redirect, flash, session


app = Flask(__name__)
app.secret_key = '2423415414'

Usuarios_Registrados = {
    'admin@correo.com': {
        'password': 'Admin123',
        'nombre': 'Gio insano',
        'fecha_nacimiento': '2009-11-19'
    }
}

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombres = request.form.get('nombres')
        apellido = request.form.get('apellido')
        email = request.form.get('numero')
        contraseña = request.form.get('pass')  
        confirmarcontraseña = request.form.get('confirm')  
        dia = request.form.get('dia')
        mes = request.form.get('Mes')
        año = request.form.get('Año')

        if contraseña != confirmarcontraseña:
            flash("Las contraseñas no coinciden.", "error")
            return redirect(url_for('registro'))


        print(f"Nuevo registro: {nombres} {apellido} - {email}")
        flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for('inicio'))

    return render_template('registro.html')


@app.route('/Validalogin', methods=['POST'])
def Validalogin():
    email = request.form.get('email', '').strip()
    password = request.form.get('password', '')

    if not email or not password:
        flash('Por favor ingresa email y contraseña', 'error')


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

    return redirect(url_for('inicio'))


@app.route('/logout')
def logout():
    session.clear()
    flash(f'Has cerrado sesión correctamente', 'info')
    return redirect(url_for('inicio'))



@app.route('/')
def base():
    return render_template('base.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')




if __name__ == '__main__':
    app.run(debug=True)
