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

@app.route('/RD')
def RD():
    return render_template('RD.html')

@app.route('/Educacion')
def Educacion():
    return render_template('Educacion.html')

@app.route('/Analizador')
def Analizador():
    return render_template('Analizador.html')

@app.route('/IMC', methods=['GET', 'POST'])
def IMC():
    resultado = None
    categoria = None

    if request.method == 'POST':
        try:
            peso = float(request.form.get('peso'))
            altura = float(request.form.get('altura')) / 100  
            imc = peso / (altura ** 2)
            imc = round(imc, 2)

            if imc < 18.5:
                categoria = "Bajo peso"
            elif 18.5 <= imc < 25:
                categoria = "Peso normal"
            elif 25 <= imc < 30:
                categoria = "Sobrepeso"
            else:
                categoria = "Obesidad"

            resultado = imc

        except:
            flash("Por favor ingresa valores válidos", "error")

    return render_template('IMC.html', resultado=resultado, categoria=categoria)

@app.route('/TMB', methods=['GET', 'POST'])
def TMB():
    resultado = None
    tdee = None

    if request.method == 'POST':
        try:
            peso = float(request.form.get('peso'))
            altura = float(request.form.get('altura'))
            edad = int(request.form.get('edad'))
            genero = request.form.get('genero')
            actividad = float(request.form.get('actividad'))

            if genero == "Hombre":
                tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
            else:
                tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

            resultado = round(tmb, 2)

            tdee = round(resultado * actividad, 2)

        except:
            flash("Por favor ingresa valores válidos", "error")

    return render_template('TMB.html', resultado=resultado, tdee=tdee)


@app.route('/GCT', methods=['GET', 'POST'])
def GCT():
    tmb = None
    gct = None

    if request.method == 'POST':
        try:
            peso = float(request.form.get('peso'))
            altura = float(request.form.get('altura'))
            edad = int(request.form.get('edad'))
            genero = request.form.get('genero')
            actividad = float(request.form.get('actividad'))

            if genero == "Hombre":
                tmb = (10 * peso) + (6.25 * altura) - (5 * edad) + 5
            else:
                tmb = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

            gct = round(tmb * actividad, 2)
            tmb = round(tmb, 2)

        except:
            flash("Por favor ingresa valores válidos.", "error")

    return render_template('GCT.html', tmb=tmb, gct=gct)


@app.route('/PCI', methods=['GET', 'POST'])
def PCI():
    peso_ideal = None

    if request.method == 'POST':
        try:
            altura = float(request.form.get('altura'))
            genero = request.form.get('genero')

            
            if genero == "Hombre":
                peso_ideal = 50 + 0.9 * (altura - 152)
            else:
                peso_ideal = 45.5 + 0.9 * (altura - 152)

            peso_ideal = round(peso_ideal, 2)

        except:
            flash("Por favor ingresa valores válidos.", "error")

    return render_template('PCI.html', peso_ideal=peso_ideal)


@app.route('/macronutrientes', methods=['GET', 'POST'])
def macronutrientes():
    calorias = None
    carbohidratos = None
    proteinas = None
    grasas = None

    if request.method == 'POST':
        try:
            calorias = float(request.form.get('calorias'))

            
            carbohidratos = round((0.50 * calorias) / 4, 2)  
            proteinas = round((0.20 * calorias) / 4, 2)      
            grasas = round((0.30 * calorias) / 9, 2)         

        except:
            flash("Por favor ingresa un valor válido de calorías.", "error")

    return render_template('macronutrientes.html',
                            calorias=calorias,
                            carbohidratos=carbohidratos,
                            proteinas=proteinas,
                            grasas=grasas)






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



