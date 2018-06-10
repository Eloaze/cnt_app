from flask import Flask
from noteapp.views.index import bp as index_bp
import contentful

SPACE_ID = 'fw8winen696w'
ACCESS_TOKEN = '0b1f667ffa51de4415b6834a0f44226b0b821f0b9ae35b9732cf1e8cebb96812'

client = contentful.Client(SPACE_ID, ACCESS_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Hola!"

entry_id = '2JyUdgqVZSugYc0skOKcsU'
product_test = client.entry(entry_id)

print("Here's the list of your first 100 entries:")
for entry in entries:
    print("\t{0}".format(entry.id))

app.register_blueprint(index_bp)

