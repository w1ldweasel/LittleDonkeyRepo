from flask import render_template, flash
from app import app
from app.forms import CityForm
import urllib.request
import json

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Number 6'}
    return render_template('index.html', title='Home', user=user)

@app.route('/city', methods=['GET','POST'])
def city():
    form = CityForm()
    if form.validate_on_submit():
        flash('Getting that for city {}'.format(form.city.data))
        city = {'name':form.city.data}
        state = {'name': form.state.data}
        url_data = "http://api.openweathermap.org/data/2.5/weather?q=Bristol,uk&appid=be1eadecdcbaa82aa548e731c8d230f4"
        webUrl = urllib.request.urlopen(url_data)
        json_data = json.loads(webUrl.read())
        #print(json_data)
        return render_template('/todays_weather.html', city=city)
    return render_template('city_weather.html', title='Party City', form=form)




