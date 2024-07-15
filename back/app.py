from flask import Flask, render_template
from models import Auto  # Asegúrate de haber importado tus modelos
app = Flask(__name__)

@app.route('/disena_auto')
def disena_auto():
    return render_template('disena_auto.html')

if __name__ == '__main__':
    app.run(debug=True)