from flask import Flask, render_template
import plotly
import plotly.graph_objects as go
import chart_studio.plotly as csp
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_ujian.html')



if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)


# CATATAN : KALO DI RUN PAKE FLASK GA KE LOAD GAMBARNYA TAPI KALO DI RUN HTML-NYA BISA KE LOAD GAMBARNYA