from flask import Flask, url_for

app = Flask(__name__)


@app.route('/carousel')
def carousel():
    return f'''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Пейзажи Марса</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        </head>
        <body>
            <h1 class="center-text">Пейзажи Марса</h1>
            <div class="container mt-5">
                <div id="marscarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
                    <div class="carousel-inner">
                        <div class="carousel-item active">
                            <img src="{url_for('static', filename='img/marspic1.jpg')}" class="d-block w-100" 
                            alt="Mars 1">
                        </div>
                        <div class="carousel-item">
                            <img src="{url_for('static', filename='img/marspic2.jpg')}" class="d-block w-100" 
                            alt="Mars 2">
                        </div>
                        <div class="carousel-item">
                            <img src="{url_for('static', filename='img/marspic3.jpg')}" class="d-block w-100" 
                            alt="Mars 3">
                        </div>
                    </div>
                </div>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        </body>
        </html>
    '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
