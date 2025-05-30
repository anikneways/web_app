from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth_main',__name__)



@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html",boolean = False)

@auth.route('/logout')
def logout():
    return render_template('home.html')

@auth.route('/login',methods=['GET','POST'])
@auth.route('/sign-up',)
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4:
            flash('Email must be greater than 3 characters.',category ='error')
            
        elif len(firstName)  <2:
            
              flash('First name  must be greater than 1 characters.',category ='error')
        elif password1 != password2:
             flash("Passwords don't match",category ='error')
        elif len(password1) < 7:
             flash('Password must be at least 7 characters',category ='error')
        else:
            flash('Account created!', category='success')
        
        
    return render_template('sign_up.html')

