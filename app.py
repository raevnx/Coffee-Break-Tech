# Coleta e análise de dados em JSON
import json
import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from models import db, Article
import os
import re

app = Flask(__name__)

def user_data():
    data = {
        "user_id": random.randint(1000, 9999),
        "session_length": round(random.uniform(1.0, 300.0), 2),  # in seconds
        "pages_visited": random.randint(1, 20),
        "click_events": random.randint(5, 50),
        "timestamp": datetime.now().isoformat()
    }
    return json.dumps(data)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'articles.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = True

db = SQLAlchemy(app)

# Definição de modelos
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    content1 = db.Column(db.Text, nullable=False)
    content2 = db.Column(db.Text, nullable=False)
    content3 = db.Column(db.Text, nullable=False)
    content4 = db.Column(db.Text, nullable=False)
    content5 = db.Column(db.Text, nullable=False)
    questions = db.relationship('Question', backref='article', lazy=True)
    curiosity1 = db.Column(db.Text)
    curiosity2 = db.Column(db.Text)
    curiosity3 = db.Column(db.Text)
    callout1 = db.Column(db.Text)
    callout2 = db.Column(db.Text)
    callout3 = db.Column(db.Text)
    audio = db.Column(db.String(200))
    youtube = db.Column(db.String(200))
    sovereignCat = db.Column(db.String(100))
    sovereignCatCaption = db.Column(db.String(100))
    stars = db.Column(db.Integer)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey('article.id'), nullable=False)
    question_text = db.Column(db.String(500), nullable=False)
    options = db.Column(db.JSON, nullable=False)
    correct_answer = db.Column(db.Integer, nullable=False)

# Função para carregar o conversor de áudio
def load_article_content(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

with app.app_context():

    db.drop_all()
    db.create_all()
    
    # Esquema de Artigos (elementos e módulos)
    articles = [
        Article(title="Pensamento Lógico Computacional",
                difficulty="básico", # Nível de dificuldade (serve para indicar a quantidade de copinhos de café em cima dos contêiners de artigos)
                curiosity1="Sabia que você pode treinar seu pensamento crítico e lógico com passatempos como sudoku, cubo mágico e jogos estratégicos, como o xadrez?",
                curiosity2="O pensamento lógico computacional envolve quatro pilares: decomposição, reconhecimento de padrões, abstração e algoritmos. Basicamente, é como montar um Lego mental.",
                curiosity3="Sabia que o conceito de algoritmos foi inventado na Idade Média?",
                callout1="— Qualquer problema pode ser resolvido computacionalmente… desde que você saiba como pensar logicamente sobre ele! Treine o seu cérebro para desenvolver seu pensamento crítico!",
                callout2="— Criatividade e organização são fundamentais para se tornar um bom programador! Aprenda como um computador funciona e como você que montar seu projeto antes de começar a programar!",
                callout3="— Pratique suas habilidades para que quando você estiver em uma equipe, seus companheiros possam saber que podem confiar em você!",
                audio="audio/logica.mp3",
                youtube="https://www.youtube.com/watch?v=pRpjYrdb9UY",
                # CONTEÚDO DO ARTIGO (o conteúdo dos artigos é dividido em 5 partes, ou módulos, para melhor organização no arquivo de artigos.)
                content1 = 
                """
                <h5><i>"—— A aprendizagem existe se houver a dúvida."</i></h5>
                O pensamento lógico computacional é a habilidade de reconhecer aspectos da computação no mundo e usar lógica para resolver problemas de maneira estratégica. Parece simples, não é? Isso é porque todos nós usamos de lógica para resolver problemas que enfrentamos, alguns mais conscientes disso, e outros menos.
                Por exemplo, pense que você está na escola, e recebe um problema de matemática para resolver. Não precisa ser uma equação muito complexa, apenas uma questão que envolva alguns números. Automaticamente, você irá perceber que aqueles números tem uma função no problema, e de maneira estratégica você irá organizar as informações que estão ali disponíveis para você e resolver a questão. 1 + 1 = 2. Você consegue chegar a essa conclusão facilmente sabendo o que cada elemento dessa conta significa, e usando a lógica entre eles para chegar ao resultado.
                Sem perceber, você acaba de usar o pensamento lógico computacional para resolver uma questão simples. 
                Uma questão simples como 1 + 1 é algo que a maioria de nós consegue fazer, mas quanto mais nos aprofundamos na complexidade de problemas parecidos, mas habilidosos temos que ser em nossa capacidade mental para resolver problemas que envolvam lógica. Felizmente, esta habilidade é algo que possa ser treinado e desenvolvido, mesmo que você não se dê muito bem com números.
                """,
                content2="""Mas para termos uma linha de raciocínio mais direcionada, aqui vão cinco núcleos do pensamento lógico computacional que você pode começar a aprender desde já:
                <b>1.</b> Algoritmos;
                <b>2.</b> Termos de Decomposição;
                <b>3.</b> Generalizações (identificar e fazer uso de padrões);
                <b>4.</b> Abstrações (escolher as representações mais adequadas de acordo com cada contexto);
                <b>5.</b> Termos de Avaliação.
                Apesar destas áreas de foco específico para programação, os setores de ensino deveriam ser responsáveis pelo ensino e treinamento de pensamento crítico e lógico, pois como pudemos ver é algo de extrema importância até mesmo além  do campo da computação.
                """,
                content3="""
                <h3><i>→  Agora que você já sabe a importância de pensar e resolver problemas de forma lógica, que tal focarmos mais na computação em si?</i></h3>
                <hr>
                Quando se trata de programação, antes mesmo de se sentar em frente a um computador e mexer com códigos, nós precisamos organizar nossa mente para entrar no "modo programador". Isso significa que temos algumas regras de boas práticas para seguir.
                - Fazer registros de suas observações através de textos, tabelas, gráficos e desenhos;
                - Guardar registros de suas observações ordenadamente;
                - Avaliar seus dados periodicamente;
                - observar e identificar com critérios uma determinada situação ou fenômeno;
                - debater com colegas sobre suas dúvidas e viabilidade das suas conclusões;
                - não ter medo de errrar e aprender a corrigir seus erros.
                """,
                content4="""
                <h5><i> A experiência constrói confiança! </i></h5>
                Quando você estiver praticando a resolução de problemas, ou até mesmo estudando computação na prática, seja a área que for, lembre-se disto: quanto mais você se expor ao que é desconfortável, mais você vai aprender. Quanto mais você aprender e praticar, mais confiante você vai se tornar. 
                Todo mundo começa de algum lugar, e não importa de onde é. Hoje em dia existem inúmeros materiais de ensino na internet, que possibilitam qualquer um a aprender o que quiser. E se você não tiver acesso fácil à internet em casa, não tem problema! Existem inúmeros livros sobre computadores, programação e o mundo digital. Sim, programadores também leem!
                De início, busque procurar estudar a ciência da computação, como funciona o código binário, como a memória de um computador funciona, onde os dados são armazenados, etc. Quando tudo isso começar a ficar claro, existem algumas habilidades que você deve começar a praticar:<br>
                <h6><i>1. Confiança</i></h6>
                Como acabamos de discutir, a confiança em desenvolver atividades intelectuais que envolvam raciocínio computacional é de extrema importância, inclusive aqueles problemas inusitados que surgem de repente. Conforme você for programando, você vai perceber que na maioria das vezes as coisas dão errado. Você verá cinco mensagens de erro no seu terminal para cada vez que seu código funcionar. Faz parte.<br>
                <h6><i>2. Companhirismo</i></h6>
                No mundo da programação, por muitas vezes você irá trabalhar com uma equipe de outros programadores, cada um em seu setor. Para que o projeto flua com leveza, é importante que haja respeito à palavra dos colegas, valorização do trabalho em equipe e troca de pontos de vista e ideias como fonte de aprendizagem.<br>
                <h6><i>3. Flexibilidade</i></h6>
                Coisas vão dar errado. Muitas. A habilidade de ter um ótimo pensamento tático é imprescindível para um bom programador. O interesse em desenvolver estratégias variadas e alternativas de resolver problemas a depender da situação é uma grande habilidade para se ter.<br>
                """,
                content5="""
                <h3>CONCLUSÃO</h3>
                Aprender sobre tecnologia e desenvolver a habilidade de programação são possíveis, mas o trabalho de verdade está além, no esforço para se tornar bom naquilo que faz. Com o conhecimento deste artigo você pode ir atrás de conteúdos mais especializados e se munir com conhecimento o suficiente para saber se virar, mas só com interesse de verdade é que você alcançará o pódio.
                Treine suas habilidades, pratique, ganhe confiança. Não é necessário ter um computador para aprender a lógica de computação, muito menos o pensamento lógico computacional. O mundo ao nosso redor está repleto de oportunidades para praticar o raciocínio crítico, basta saber o que está procurando.
                """,
                sovereignCat="img/pumpkinMaster.png", # Pumokin Master Cat image
                sovereignCatCaption="O Cavaleiro das Abóboras acredita na sua força para vencer bugs malvados!",
                stars = 1),
        Article(title="Programação em Python",
                difficulty="intermediário", # Nível de dificuldade (serve para indicar a quantidade de copinhos de café em cima dos contêiners de artigos)
                curiosity1="Python foi criado em 1989, mas só ganhou fama mundial muitos anos depois. O criador, Guido van Rossum, batizou a linguagem inspirado no grupo de comédia britânico 'Monty Python'!",
                curiosity2="O Zen of Python — uma lista de 19 princípios para escrever código Python de forma elegante — está escondida no interpretador. Digite 'import this' no terminal!",
                curiosity3="Python é usado por gigantes como Google, Netflix e NASA — sim, até missões espaciais usam Python!",
                callout1="Aprender uma linguagem de programação é como aprender uma nova língua — quanto antes você começar, mais fácil vai ser dominá-la!", 
                callout2="Organização e boas práticas são muito importantes na hora de programar, um código limpo e bem feito é mais fácil de lidar, por mais que às vezes pareça que pegar atalhos é melhor.",
                callout3="Python é a linguagem de programação mais popular do mundo por uma razão! É a mais fácil de se aprender entre iniciantes. E então, o que você está esperando?",
                youtube="https://www.youtube.com/watch?v=4p7axLXXBGU",
                # CONTEÚDO DO ARTIGO (o conteúdo dos artigos é dividido em 5 partes, ou módulos, para melhor organização no arquivo de artigos.)
                content1="""Programar de forma ética significa criar soluções que respeitem as pessoas e o meio ambiente digital. Python, com sua comunidade vibrante, incentiva práticas responsáveis, como o desenvolvimento de softwares sustentáveis e acessíveis. Aprender programação com essa mentalidade promove o uso consciente da tecnologia, alinhado aos princípios de ética e sustentabilidade digital.
                Por que Python é recomendado para iniciantes?
                1. Tem uma sintaxe clara, parecida com o inglês.
                2. É usada em diversas áreas: web, ciência de dados, inteligência artificial.
                3. Tem uma grande comunidade e muitos recursos gratuitos.
                """,
                content2="""Ao aprender os fundamentos do Python, é importante também desenvolver uma consciência ética sobre o impacto do seu código. Scripts mal-intencionados ou mal projetados podem prejudicar sistemas e pessoas. Por isso, desde o início, incentive o uso responsável da tecnologia, adotando práticas que priorizem a segurança, a sustentabilidade digital e o bem-estar coletivo.
                Principais elementos da linguagem:
                1. Variáveis: armazenam informações. Ex.: idade = 30
                2. Funções: conjuntos de comandos que realizam tarefas. Ex.: print("Olá!")
                3. Laços de repetição: executam comandos várias vezes. Ex.: for, while.
                4. Condicionais: criam decisões no código. Ex.: if, else.
                5. Python permite começar com poucos comandos e evoluir aos poucos.""",
                content3="""Parabéns, programador em formação! Além de dominar comandos, lembre-se de que cada linha de código tem um impacto. Praticar a programação com ética significa criar soluções que ajudem pessoas e respeitem normas de segurança e privacidade. Incentive o uso responsável da tecnologia, promovendo softwares que contribuam para uma sociedade mais sustentável e justa.
                Vamos escrever um programa simples em Python:
                nome = input("Digite seu nome: ")
                print("Olá,", nome, "!")
                - O que aconteceu?
                - O input pede ao usuário que digite algo.
                - O print exibe uma mensagem na tela.
                Parabéns! Você acabou de criar seu primeiro programa!""",
                content4="""Python está presente em muitos setores, e isso amplia nossa responsabilidade como desenvolvedores. Criar soluções que respeitem a ética, promovam inclusão e priorizem a sustentabilidade digital é essencial. Por exemplo, ao desenvolver aplicações de automação, devemos garantir que elas não sejam usadas para práticas abusivas ou danosas, mas sim para melhorar processos de maneira responsável.
                Python é muito versátil e está presente em várias áreas:
                - Desenvolvimento Web: com frameworks como Django e Flask.
                - Ciência de Dados: analisando informações com bibliotecas como Pandas.
                - Automação: realizando tarefas repetitivas automaticamente.
                - Jogos: criação de jogos simples ou complexos com Pygame.
                - Esses são só alguns exemplos! Python está em todo lugar.""",
                content5="""Ao evoluir na programação, é fundamental manter uma postura ética, criando códigos seguros e conscientes. Participar de comunidades e compartilhar conhecimento também significa incentivar boas práticas e o uso responsável da tecnologia. A sustentabilidade digital passa por aqui: disseminar práticas que promovam a eficiência, o respeito ao próximo e a proteção do ambiente digital.
                Programar é como aprender uma nova língua: exige prática e dedicação.
                - Dicas para seguir evoluindo:
                - Pratique pequenos programas todos os dias.
                - Participe de comunidades online.
                - Faça cursos gratuitos ou pagos.
                - Leia a documentação oficial do Python.
                - Lembre-se: errar faz parte do processo. O importante é não desistir!""",
                sovereignCat="img/majesty.png", # Queen Cat image
                sovereignCatCaption="A Rainha de Python abençoa a sua futura jornada no mundo da programação!",
                stars = 2),
        Article(title="Segurança Digital",
                difficulty="avançado", # Nível de dificuldade (serve para indicar a quantidade de copinhos de café em cima dos contêiners de artigos)
                curiosity1="O termo 'hacker' originalmente não era negativo! Nos anos 60, hackers era como descreviam programadores habilidosos e criativos.",
                curiosity2="90% dos ataques cibernéticos começam com engenharia social, ou seja, manipulação psicológica — a maior falha não é a máquina, é o humano!",
                curiosity3="Nem todos os hackers precisam ser criminosos. Existem profissionais que são pagos para invadir sistemas e testar a segurança de redes de empresas. Muita diversão, e muito dinheiro, o que poderia ser melhor do que isso?",
                callout1="A senha mais comum do mundo ainda é… '123456'. Por favor, não seja essa pessoa. 🙏",
                callout2="Blue Team ou Red Team? Você que decide.",
                callout3="Você pode configurar uma máquina virtual e testar vírus em laboratórios digitais, bem como invadir sistemas feitos para o treinamento de hackers éticos, e muito mais, tudo isso da sua própria casa!",
                audio="audio/logica.mp3",
                youtube="https://www.youtube.com/watch?v=gMQKilekm2g&list=PLAp37wMSBouB70jGTeT0JjW_LNC_JBHCo",
                # CONTEÚDO DO ARTIGO (o conteúdo dos artigos é dividido em 5 partes, ou módulos, para melhor organização no arquivo de artigos.)
                content1="""Segurança Digital não se trata apenas de proteger informações, mas também de agir com responsabilidade no mundo online. Adotar práticas éticas e sustentáveis, como evitar compartilhar fake news e respeitar a privacidade alheia, faz parte desse compromisso. Incentivar o uso responsável da tecnologia é essencial para criar uma internet mais segura e saudável para todos.
                Segurança Digital é o conjunto de práticas e ferramentas que protegem informações e sistemas na internet.
                Vivemos conectados: usamos redes sociais, bancos online e aplicativos de mensagem. Por isso, proteger nossos dados é essencial.
                Exemplos de onde usamos segurança digital:
                - Senhas fortes para proteger contas.
                - Aplicativos com autenticação de dois fatores.
                - Sites com cadeado de segurança (HTTPS).
                """,
                content2="""Criar senhas fortes não protege só você, mas também impede que criminosos comprometam sistemas e prejudiquem outras pessoas. A ética digital também passa por aqui: nada de tentar invadir contas alheias ou compartilhar senhas de terceiros! E lembre-se: proteger suas credenciais é um ato de sustentabilidade digital, evitando o desperdício de recursos com recuperações, investigações e prejuízos.
                Uma senha forte é a primeira barreira contra invasores.
                Dicas para criar boas senhas:
                1. Use letras maiúsculas e minúsculas.
                2. Adicione números e símbolos.
                3. Não use informações óbvias, como datas de nascimento.
                4. Nunca repita a mesma senha em diferentes contas.
                Exemplo:
                Segurança123! → Melhor do que 123456 ou senha.
                """,
                content3="""Além de proteger a si mesmo, ao evitar cair em golpes você também contribui para um ecossistema digital mais saudável. Compartilhar informações sobre golpes e alertar amigos faz parte de uma postura ética que valoriza o bem coletivo. Praticar a sustentabilidade digital significa também não propagar conteúdos fraudulentos ou suspeitos, evitando que mais pessoas sejam prejudicadas.
                Infelizmente, há muitas pessoas tentando enganar usuários na internet.
                Principais golpes:
                - Phishing: e-mails ou mensagens falsas que pedem seus dados.
                - Falsos sites de compras: prometem produtos baratos, mas não entregam.
                - Links suspeitos: podem instalar vírus.
                - Como se proteger:
                - Desconfie de mensagens urgentes demais.
                - Verifique o endereço do site.
                - Nunca compartilhe senhas.


                """,
                content4="""Cuidar dos seus dispositivos é um ato de responsabilidade não só consigo, mas com toda a comunidade digital. Um aparelho vulnerável pode ser usado para espalhar vírus e prejudicar outros usuários. Manter seus sistemas seguros e atualizados é parte fundamental de uma cultura de ética e sustentabilidade digital, reduzindo riscos e promovendo um ambiente online mais confiável e eficiente.
                Além de proteger suas contas, é importante cuidar dos dispositivos que você usa: celular, tablet, computador.
                Cuidados importantes:
                1. Mantenha os sistemas atualizados.
                2. Use antivírus confiáveis.
                3. Não instale aplicativos de fontes desconhecidas.
                4. Configure bloqueio de tela.
                """,
                content5="""Educar-se em segurança digital é também um compromisso ético: quanto mais conhecemos, mais podemos orientar outros e reduzir práticas nocivas na internet. Incentivar o uso responsável da tecnologia e adotar posturas sustentáveis contribui para um ambiente digital mais inclusivo, seguro e justo. A educação é a chave para transformar a tecnologia em uma ferramenta de evolução social.
                A segurança digital não é só responsabilidade dos especialistas, mas de todos.
                - Educar-se sobre boas práticas evita problemas e protege a sua privacidade.
                - O que você pode fazer:
                - Ensinar amigos e familiares.
                - Participar de palestras ou cursos sobre o tema.
                - Sempre desconfiar de coisas "boas demais para ser verdade".
                - Lembre-se: segurança digital é um hábito, não um evento único.

                """,
                sovereignCat="img/wizardCat.png",
                sovereignCatCaption="O Mago Místico conjura um feitiço de sabedoria e proteção contra hackers sobre você!",
                stars = 3)
    ]
    db.session.add_all(articles)
    db.session.commit()
    
    questions = [
        Question(
            article_id=1,
            question_text="Qual destes é um elemento fundamental do raciocínio lógico?",
            options=["Repetição", "Aleatoriedade", "Organização", "Adivinhação"],
            correct_answer=2
        ),
        Question(
            article_id=2,
            question_text="Qual é a principal característica de Python?",
            options=["Fortemente tipado", "Compilado", "Orientado a objetos", "Todas as anteriores"],
            correct_answer=3
        ),
        Question(
            article_id=3,
            question_text="Selecine a senha mais segura dentre as senhas a seguir:",
            options=["123456", "23/07/2004", "DUN.aler.2450", "AS#23.jkq$02"],
            correct_answer=3
        )
    ]
    db.session.add_all(questions)
    db.session.commit()

@app.route("/")
def home():
    # Configurações da ferramenta de busca
    search_query = request.args.get('q', '').strip().lower()
    results = []

    if search_query:
        search_terms = re.split(r'\s+', search_query)
        
        articles = Article.query.filter(or_(
            *[Article.content1.ilike(f'%{term}%') for term in search_terms],
            *[Article.content2.ilike(f'%{term}%') for term in search_terms],
            *[Article.content3.ilike(f'%{term}%') for term in search_terms],
            *[Article.content4.ilike(f'%{term}%') for term in search_terms],
            *[Article.content5.ilike(f'%{term}%') for term in search_terms]
        )).all()

        for article in articles:
            excerpts = []
            for content_field in [article.content1, article.content2, article.content3, 
                                 article.content4, article.content5]:
                if not content_field:
                    continue
                
                lower_content = content_field.lower()
                for term in search_terms:
                    start = 0
                    while True:
                        start = lower_content.find(term, start)
                        if start == -1:
                            break
                        end = start + len(term)
                        
                        snippet_start = max(0, start - 150)
                        snippet_end = min(len(content_field), end + 150)
                        snippet = content_field[snippet_start:snippet_end]
                    
                        highlighted = re.sub(
                            re.compile(f'({term})', re.IGNORECASE), 
                            r'<mark>\1</mark>', 
                            snippet
                        )
                        
                        excerpts.append(f"...{highlighted}...")
                        start = end

            if excerpts:
                results.append({
                    'article': article,
                    'excerpts': excerpts[:3]
                })

        return render_template("home.html", 
                            results=results,
                            search_query=search_query,
                            articles=[])
    
    return render_template("home.html", 
                         articles=Article.query.all(),
                         search_query=search_query)

@app.route("/article/<int:article_id>", methods=['GET', 'POST'])
def view_article(article_id):
    article = Article.query.get_or_404(article_id)
    
    if request.method == 'POST':
        score = 0
        user_answers = {}
        for question in article.questions:
            answer = request.form.get(f'question_{question.id}')
            user_answers[question.id] = answer
            if answer and int(answer) == question.correct_answer:
                score += 1
        return render_template("article.html", 
                             article=article,
                             user_answers=user_answers,
                             score=score,
                             total=len(article.questions))
    
    return render_template("article.html", article=article)

@app.template_filter('youtube_embed')
def youtube_embed(url):
    return url.replace('watch?v=', 'embed/')


@app.route('/data-collector', methods=['POST'])
def data_collector():
    print("Received analytics data.")
    return jsonify({"status": "success", "message": "data received."})

if __name__ == "__main__":
    app.run(debug=True)
