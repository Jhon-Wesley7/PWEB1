from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <a href="/sobre">Sobre</a>
    <a href="/experiencia">Experiencia</a>
    <a href="/formacao">Formação</a>
    <a href="/contatos">Contatos</a>
    '''

#- página sobre eu
@app.route('/sobre')
def sobre():
    return "<h1>Sobre Mim</h1><p>Meu nome é Jhon Wesley, sou Icoense, tenho 20 anos, sou acadêmico de Sistemas, e curto basquete.</p>"


#página com minha experiência profissional
@app.route('/experiencia')
def experiencia():
    return  "<h1>Experiência Profissional</h1><ul><li><h4>Brisanet, Um estagio proporcionado pela EEEP Deputado José Walfrido Monteiro.</h4></li><li><h4>Agenciador de Propaganda na Ótica Ouro, 8 meses</h4></li></ul>"

#página com sua formação acadêmica
@app.route('/formacao')
def formacao():
    return "<h1>Formação</h1><ul><li><h4>Técnico em informática. E.E.E.P. Deputado José Walfrido Monteiro, conclusão em 2021</h4></li><li><h4>Graduação em Sistemas de Informação. Instituto Federal do Ceará, previsão de conclusão em 2025</h4></li></ul>"


#página com meus contatos
@app.route('/contatos')
def contato():
    return "<p><h1>Meus contatos :</h1></p><p>Email: jhon.wesley08@aluno.ifce.edu.br</p><p>Telefone: (88)981539294</p>"


if __name__ =="__main__":
    app.run(debug=True)