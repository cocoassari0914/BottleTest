from bottle import route, run, view, static_file, url, get, post, request

@route('/static/<filepath:path>', name='static_file')
def static(filepath):
    return static_file(filepath, root="./static")

@route('/login')
@view("login")
def hello( ):
    return dict(url=url)

@route("/login", method='POST')
@view("top")
def gotoTop():
    mail = request.forms.get("mail")
    path = request.forms.get("path")
    return dict(url=url, mail=mail, path=path)

run(host='localhost', port=8080, debug=True, reloader=True)
