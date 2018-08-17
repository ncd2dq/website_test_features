from flask import Blueprint, render_template, redirect, g, session, request, url_for


bp = Blueprint('home', __name__, url_prefix='/signup')


@bp.route('/', methods=['GET','POST'])
def main_form():
    
    if request.method == 'POST':
        quantity = request.form['quantity']
        item = request.form['item']
        session['payload'] = (quantity, item)
        
        return redirect(url_for('home.confirmation'))
    
    return render_template('main_form.html')



@bp.route('/confirmation', methods=['GET'])
def confirmation():
    
    payload = session['payload']
    
    return render_template('confirmation.html', payload=payload)


@bp.route('/test', methods=['GET'])
def test():
    
    
    return "test"