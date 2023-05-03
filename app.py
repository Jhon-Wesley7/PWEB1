from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <a href="/sobre">Sobre mim</a>
    <a href="/experiencia">Experiencia</a>
    <a href="/formacao">Formação</a>
    <a href="/contatos">Contato</a>
    '''

#Page Sobre mim
@app.route('/sobre')
def sobre():
    return "<h1>Sobre mim</h1> <p>Meu nome é Jhon Wesley Batista de Freitas, Sou técnico em informática e acadêmico de Sistemas da informação, gosto muito de musica e esportes, sendo basquete e futbool meus esportes prediletos</p>"

#Page Formação
@app.route("/formacao")
def formacao():
    return "<h1>Minha formação</h1> <p>Ensino médio completo + curso Tecnico de informática (E.E.E.P Deputado José Walfrido Monteiro), Graduando em Sistemas de informaçã(2025.1, possível data de conclusão)"

#Page Experiência no mercado de trabalho
@app.route("/experiencia")
def experiencia():
    return "<h1>Minhas experiências</h1> <p>Estágio na Brisanet (2021, 300h), Ótica Ouro(2023, 7 meses), Jovem Aprendiz Crediamigo(Atual)</p>"

#Page Contato
@app.route("/contatos")
def contatos():
    return "<h1>contatos</h1> <p> Telefone: (88) 98153-9294, E-mail: jhon.wesley08@aluno.ifce.edu.br"


if __name__ == '__main__':
    app.run(debug=True)