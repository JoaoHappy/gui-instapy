from instapy import InstaPy
from instapy import smart_run
from PyQt5 import uic,QtWidgets


def enviar_dados():
    usernameJ 	 = tela_inicial.username.text()
    passwordJ 	 = tela_inicial.senha.text()
    tags	  	 = tela_inicial.tag.text()	
    comentario_1 = tela_inicial.comentarios.text()
    comentario_2 = tela_inicial.comentarios_2.text()
    quantidades	 = int(tela_inicial.quantidade.text())
    
    session = InstaPy(username = usernameJ, password = passwordJ)

    with smart_run(session):
        session.set_do_follow(enabled = True, percentage = 100)
        session.set_do_like(enabled = True, percentage= 100)

        session.like_by_tags([tags], amount = quantidades)

        comentarios = [comentario_1, comentario_2]
 
        session.set_do_comment(enabled=True, percentage=95)
        session.set_comments(comentarios, media= 'Photo')
        session.join_pods()

app = QtWidgets.QApplication([])
tela_inicial = uic.loadUi("design.ui")
tela_inicial.iniciar.clicked.connect(enviar_dados)

tela_inicial.show()
app.exec()