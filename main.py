import os
import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact().strip()
    piglatinize_url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'

    response = requests.post(piglatinize_url,
                             data={'input_text': fact},
                             allow_redirects=False,)

    location_header = response.headers
    location_header = location_header['Location']

    return "<a href='{}'>{}</a>".format(location_header, location_header)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

