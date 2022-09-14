from app import app
from schs.movies_api import *
from schs.directors_api import *
from schs.genres_api import *

if __name__ == '__main__':
    app.run(debug=True)