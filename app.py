from flask import Flask, request, render_template_string

app = Flask(__name__)
app.secret_key = b'SECRET_KEY'

@app.route('/create', methods=['GET',])
def create():
        title = request.args.get('title')

        template = '''
        <!DOCTYPE html>
        <html>
          <head>
            <title>Created</title>
          </head>
          <body>
            <p>''' + title + '''</p>
          </body>
        </html>'''
        return render_template_string(template)

if __name__ == '__main__':
        app.run()
