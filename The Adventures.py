from time import sleep

from pygame import mixer

import pygame

import random

def gira():
    return random.randint(1, 6)

def perguntas(a, b, c, pergunta, alternativaA, alternativaB, alternativaC, consequenciaA, consequenciaB, consequenciaC):
    print(pergunta)
    sleep(2)
    print(alternativaA)
    print(alternativaB)
    print(alternativaC)
    resposta = input('Qual sua resposta?')
    if resposta == 'a':
        print(consequenciaA)
        return a
    elif resposta == 'b':
        print(consequenciaB)
        return b
    elif resposta == 'c':
        print(consequenciaC)
        return c

def jogadores(jogador):
    if jogador == 3:
        jogador = personagens[2]
    elif jogador == 1:
        jogador = personagens[0]
    elif jogador == 2:
        jogador = personagens[1]
    else:
        print('Esse personagem não existe.')
    return jogador

personagens = ['mago', 'elfo', 'guerreiro']

perguntasMago = [
    'No começo de sua jornada, você recebe uma notícia da ordem dos magos de que um mago aliado é mantido prisioneiro pelo Bruxo maligno da Fortaleza da Escuridão. Por se tratar de um inimigo muito poderoso, você necessita de aliados e tem que escolher entre três atitudes iniciais. O que você faz?',
    'Você e seus aliados se deparam com uma trilha que leva à um acampamento conhecido por você, ao chegar lá, você vê que o acampamento está sendo atacado por Trolls. O que você faz?',
    'Depois de uma árdua caminhada, você chega até a primeira base dos magos, O Pilar Central, o líder honorário lhe concede a permissão de escolher um dos artefatos do tesouro dos magos. Qual você escolhe?',
    'Depois de uma árdua jornada, você chega até a Fortaleza da Escuridão onde habita o Bruxo maligno e onde seu aliado é feito prisioneiro. O que você faz?', ]

alternativasMago = [
    ['a) Se aliar às Minas de Moria, o reino dos anões.', 'b) Se aliar ao Reduto Élfico, o reino dos elfos.',
     'c) Se aliar à Terra Nova, o reino dos guerreiros'],
    ['a) Empunha sua varinha e ataca os batedores e vigias do acampamento.',
     'b) Você é cuidadoso e acha que não dá conta daquela multidão de trolls, por isso decide esperar até a luz do sol que já estava próxima para aproveitar a fraqueza dos Trolls.',
     'c) Você espera seus aliados que vêm na sua retaguarda para lhe ajudar com os trolls'],
    ['a) Manto da invisibilidade.', 'b) Cetro do Caos', 'c) Chapéu da Levitação.'],
    [
        'a) Você traça um plano de entrar disfarçado na Fortaleza para salvar seu aliado e sair ileso, deixando o Bruxo Maligno impune.',
        'b) Você arma uma distração fora da fortaleza para atrair o Bruxo Maligno para uma emboscada.',
        'c) Você passa pelos portões da Fortaleza e desafia o Bruxo para uma luta direta.']]

consequenciasMago = [[
                         'Ao enviar um pedido de ajuda aos anões, eles negam com a justificativa de que a ordem dos magos não os ajudou em batalhas passadas, por causa disso sua jornada fica mais difícil. Volte 2 casas.',
                         'Ao enviar um pedido de ajuda aos elfos, eles se mostram ocupados pois estão envolvidos em diversas outras batalhas, e a sua ajuda não é à altura a de que o mago esperava. Avance 4 casas.',
                         'Você vai pessoalmente até o reino dos humanos por achar que apenas uma mensagem não resolveria a situação. A partir disso, você resolve suas pendências com os humanos e os laços de amizade entre a ordem dos magos e os guerreiros são novamente atados. Avance 2 casas'],
                     [
                         'Ao conjurar sua magia, você acaba percebendo que se tratava de uma armadilha criada por um dos bruxos aprendizes malignos, por causa disso você têm uma árdua batalha e acaba saindo ferido. Volte 3 casas',
                         'Você ganha tempo distraindo os trolls até o amanhecer, quando vê que que o sol raiou, desliza uma pedra de um ribanceira com sua magia e revela a luz do sol para os trolls, transformando-os em pedra. Avance 3 casas.',
                         'Até eles chegarem, um dos trolls percebem sua presença e parte pra cima de você, você consegue abatê-lo, mas os outros vêm logo em seguida e você foge em disparada. Volte 1 casas.'],
                     [
                         'Por causa do manto, você evita conflitos com hordas de Wargs e consegue seguir seu caminho rapidamente e sem pausas. Avance 4 casas.',
                         'Apesar de muito poderoso, ele é muito complicado de se manusear e você não consegue dominá-lo com perfeição, por isso ele acaba não sendo tão útil. Volte 4 casas.',
                         'Por se tratar de um artefato pouco conhecido pelos outros magos, era pouco recomendável e deveras arriscado escolhê-lo, você é audacioso e o escolhe mesmo assim. No meio da batalha com uma ordem de Wargs, você tenta usá-lo para se livrar, mas percebe a fraqueza do Chapéu, pois ele te levita apenas a 5 cm do chão, por causa disso você se fere bastante na luta. Volte 3 casas.'],
                     [
                         'Você usa um feitiço de disfarce para invadir a Fortaleza sem ser descoberto. Ao entrar, você vai até o calabouço e liberta seu aliado, e parte em disparada pois o feitiço tem um tempo pequeno de duração. Na saída da fortaleza, já bem longe da torre principal, o efeito acaba e você é obrigado, junto do seu aliado, a travar uma árdua luta com um exército de Orcs. Com um feitiço de fumaça, você foge juntamente de seu aliado, porém, muito ferido. Avance 3 casas.',
                         'Quando o Bruxo chega, ele pisa na armadilha de feitiço e é preso por magia, impedindo que ele consiga reagir. Você salva seu aliado e leva o Bruxo como prisioneiro. Avance 2 casas.',
                         'O Bruxo já tinha notícias de você, e preparou uma grande armadilha congelante, você é derrotado. Volte 3 casas.']]

perguntasElfo = [
    'Durante sua jornada, você se depara com um acampamento de Orcs à noite e acaba percebendo que entre eles há um prisioneiro. O que você faz?',
    'No começo de sua jornada você já precisava chegar ao reduto élfico para receber ordens de seu superior e ao anoitecer quando armava  uma fogueira para se alimentar, seu cavalo acabou fugindo. O que você faz?',
    'Ao chegar em um vilarejo, você ouve boatos a respeito do temível golem que está dificultando a travessia da montanha. O que você faz?',
    'ao chegar no reduto élfico, você recebe ordens do seu superior para você decidir sua próxima tarefa antes de continuar sua jornada. Qual você escolhe?']

alternativasElfo = [['a) Empunha seu arco e ataca os batedores e vigias do acampamento.',
                     'b) Você é cuidadoso e acha que não dá conta daquela multidão de orcs, por isso decide enviar uma mensagem para o reduto élfico em busca de reforços.',
                     'c) Você aproveita a fraqueza dos orcs à luz do sol e espera até o amanhecer para ter uma maior chance de sucesso.'],
                    [
                        'a) Você acha que não há tempo a perder e por ser um elfo, é rápido o suficiente para seguir jornada sozinho.',
                        'b) Ao amanhecer você procura pelo seu cavalo élfico na floresta e acha pistas em um vilarejo',
                        'c) Procura pela sua montaria imediatamente naquela floresta escura'],
                    ['a) Ao chegar lá você avista o golem e resolve atacá-lo na espreita',
                     'b) Ao avistá-lo, você resolve tentar passar sem que ele o perceba.',
                     'c) Ao ouvir os boatos, decide desafiá-lo à uma batalha'],
                    [
                        'a) A primeira tarefa se trata de escoltar o príncipe que levava uma mensagem para aliados dos elfos.',
                        'b) Os elfos encontraram um ninho de aranhas gigantes próximo ao reduto e você foi encarregado de contê-las.',
                        'c) Ficar de guarda na masmorra assegurando que seus superiores possam descansar com a promessa de que se tudo sair bem, você receberá uma recompensa.']]

consequenciasElfo = [[
                         'Você usa de sua agilidade e acaba alvejando todos os maiores orcs que davam conta da linha de frente do acampamento. Os orcs do acampamento ao perceberem que nenhum da linha de frente voltou, partiram em retirada por acharem que se tratava de uma multidão de homens, deixando os prisioneiros para trás, com isso você os liberta. Avance 4 casas.',
                         'Quando os reforços chegaram, nenhum orc se encontrava mais no acampamento e não havia rastros de prisioneiros. Volte 3 casas.',
                         'Ao amanhecer, apenas alguns orcs restaram no acampamento, você os alveja depois de uma árdua batalha e acaba saindo com alguns ferimentos, assim como os prisioneiros. Avance 2 casas.'],
                     [
                         'Partindo sozinho em disparada, no meio do caminho acaba encontrando o Grande Rio e percebe que sem sua montaria não vai conseguir passar, com isso terá que pegar um caminho mais longo e bem longe dali. Volte 3 casas.',
                         'Você encontra sua montaria com um camponês, porém ela está um pouco machucada e necessita de um tempo para se recuperar, além de depois ficar um pouco lenta. Volte 2 casas.',
                         'Por causa da sua habilidade élfica de enxergar no escuro, você rapidamente localiza seu cavalo antes que ele se perca de fato. Avance 4 casas.'],
                     [
                         'Ao brandir sua espada, você percebe que ele está dormindo, o golem acorda e você erra o ataque, sendo golpeado em seguida, escapando por pouco mas saindo gravemente ferido. Volte 3 casas',
                         'Você vê que ele está dormindo e percebe que o golem faz algum barulho quando você se aproxima, mas nada que o impeça de atravessar e sair ileso. Avance 4 casas',
                         'Numa batalha franca, você tem algum trabalho mas consegue derrotá-lo com uma flecha direto na nuca e sair com leves ferimentos. Avance 2 casas.'],
                     [
                         'No meio do caminho vocês se deparam com uma horda de Wargs que geram um certo transtorno, mas depois de algumas flechas, você e sua equipe conseguem afugentá-los. Avance 3 casas',
                         'Ao chegar lá, vocês logo percebem as armadilhas criadas pelas aranhas que já estavam a sua espera, vocês as desarmam e jogam um falso alarme para as aranhas, saltam das árvores e as abatem uma a uma sem quase nenhum ferimento e cumprindo sua missão. Você recebe uma recompensa do seu superior e pode avançar 2 casas.',
                         'No meio da noite, apesar de você estar alerta, vassalos do prisioneiro elfo traidor invadem o reduto na calada da noite, te enfeitiçam para que você caia em sono profundo e libertem o seu líder. Você é repreendido por seu superior e é obrigado a ficar mais tempo no reduto. Volte 3 casas.']]

perguntasGuerreiro = [
    'Você chegou na Forja e o ferreiro é grato à você por serviços prestados anteriormente e te oferece um aprimoramento em uma arma. Qual arma você escolhe?',
    'No seu vilarejo, muitos estão tendo problema de alimento e acusam um ladrão. Três pessoas dizem ter pistas dele. Onde você procura pistas?',
    'Depois de alguns dias de procura na floresta, você fica faminto e decide procurar alimento. O que você faz?',
    'Você chega na floresta e avista um suspeito dos crimes que aconteciam no vilarejo. O que você faz?']

alternativasGuerreiro = [['a) Cutelo', 'b) Adaga', 'c) Escudo'],
                         ['a) Vai atrás de pegadas', 'b) Vai ouvir testemunhas.', 'c) Usa um cão farejador.'],
                         ['a) Faz uma armadilha de coelhos.', 'b) Percebe rastros de um animal e decide o seguir',
                          'c)  Avista frutas na copa de uma árvore.'],
                         ['a) Interroga-lo com rispidez', 'b) Interroga-lo com educação.',
                          'c) Invade sua propriedade sem pedir permissão.']]

consequenciasGuerreiro = [
    ['O que você espera conseguir com um instrumento de cortar carne? Quer fazer um churrasco? Volte 4 casas',
     'Sem dúvida é um instrumento muito útil quando aprimorado, mas um guerreiro não se identifica tanto com armas que exigem que você haja na surdina. Avance 3 casas',
     'Muitas vezes você usou o ataque como defesa, mas às vezes um escudo é útil e pode ser elemento importante para vencer uma batalha. Avance 4 casas.'],
    [
        'Pessoas mostram pegadas à você, mas ao segui-las, já bem longe do vilarejo, Você descobre que elas eram do lenhador e você só perdeu tempo. Volte 3 casas.',
        'Ao ouvir todos, você ouve diversas versões diferentes e pouco daquilo te ajuda. Volte 2 casas.',
        'Logo que você leva o cachorro para farejar o depósito roubado, ele corre em disparada para a floresta e você vai atrás, ao chegar lá, você vê rastros da comida roubada e tem certeza que está no lugar certo para procurar pelo ladrão. Avance 3 casas.'],
    [
        'Você faz a armadilha mas depois de horas esperando você acaba caindo no sono, ao acordar, percebe que não tem nada e você só está mais faminto. Volte 2 casas.',
        'Depois de alguns minutos seguindo na surdina, você vê seu alvo, se tratava de um javali. Você empunha seu arco que você não sabe manusear muito bem e dispara, acerta em cheio. Você tem uma refeição completa e consegue seguir muito bem nutrido. Avance 3 casas.',
        'Depois de um grande trabalho para escalar a árvore, você colhe as frutas e depois de comê-las, percebe que está se sentindo mal. As frutas estavam estragadas. Volte 3 casas.'],
    [
        'Você assusta o suspeito com a sua arrogância e ele foge. Ao investigar sua propriedade, você vê todo o estoque de comida roubado e o recupera, porém o ladrão saiu impune. Avance apenas 2 casas.',
        'Você o interroga com educação e depois de longa conversa se fingindo de desentendido, ele confessa seus crimes e você pode recuperar tudo que foi roubado, levando o ladrão preso. Avance 3 casas.',
        'Você invade a propriedade mas o ladrão já havia preparado armadilhas para caso isso acontecesse, você é preso pelo ladrão. Volte 3 casas.']]

casasBonus = [
    'Você está na base da ordem dos magos, aqui você pode aprimorar sua magia para futuros desafios. Avance 10 casas',
    'Você chegou no reduto élfico e lá eles te oferecem descanso, onde você pode regenerar suas forças e seguir seu trajeto mais rapidamente. Avance 10 casas.',
    'No meio de seu trajeto, você encontra uma taverna em um lugar inóspito onde você jamais imaginaria encontrar, lá você pode descansar. Avance 10 casas.']

casasOnus = [
    'No meio de sua jornada, você se depara com o covil das aranhas gigantes, lugar onde magos são inimigos mortais, você tem que pegar um caminho mais longo e sua jornada fica mais lenta. Volte para a casa 10.',
    'Você invadiu a terra das Minas de Moria, o reino dos anões e é capturado como invasor. Por causa da rixa entre eles e seu povo, você só é liberto depois de muita negociação. Volte para a casa 8.',
    'Você encontra uma Forja e lá o ferreiro lhe oferece ótimos preços, mas ao usar as ferramentas, você descobre que se tratava de um péssimo metal. Volte para a casa 9 .']

jogador1 = jogadores(int(input('Qual personagem você escolhe entre mago, elfo e guerreiro? 1- mago 2-elfo 3-guerreiro:')))
print(jogador1)

jogador2 = jogadores(int(input('Qual personagem você escolhe entre mago, elfo e guerreiro? 1- mago 2-elfo 3-guerreiro:')))
print(jogador2)

mixer.init()
musica_de_fundo = mixer.music.load('musicadefundo.mp3')
mixer.music.play(-1)

contCasas1 = 34
contCasas2 = 34
casaAtual1 = contCasas1
casaAtual2 = contCasas2
casasCoringaMago = [30, 25, 19, 12, 7, 2]
casasCoringaElfo = [32, 27, 21, 14, 9, 4]
casasCoringaGuerreiro = [31, 26, 20, 13, 8, 3]

while jogador1 in list(personagens) and jogador2 in list(personagens) and contCasas1 >= 0 and contCasas2 >= 0:

    qualJog = int(input('Selecione o jogador:'))

    if qualJog == 1:

        dado = gira()
        sleep(1)

        barulho_dado = pygame.mixer.Sound('somdodado.wav')
        barulho_dado.play()
        print('O jogador 1 tirou', dado, 'no dado')

        contCasas1 = contCasas1 - dado

        if jogador1 == personagens[0]:
            if contCasas1 > 0:
                print('O', jogador1, 'está na casa', casaAtual1 - contCasas1)

            if contCasas1 in casasCoringaMago:
                barulho_casacoringa = pygame.mixer.Sound('somvitoria.wav')
                barulho_casacoringa.play()
                print('O', jogador1, 'caiu em uma casa especial')

                if contCasas1 == casasCoringaMago[0]:


                    m1 = perguntas(2, -4, -2, perguntasMago[0], alternativasMago[0][0], alternativasMago[0][1],
                                   alternativasMago[0][2], consequenciasMago[0][0], consequenciasMago[0][1],
                                   consequenciasMago[0][2])
                    contCasas1 = contCasas1 + m1

                elif contCasas1 == casasCoringaMago[1]:

                    m2 = perguntas(3, -3, 1, perguntasMago[1], alternativasMago[1][0], alternativasMago[1][1],
                                   alternativasMago[1][2], consequenciasMago[1][0], consequenciasMago[1][1],
                                   consequenciasMago[1][2])
                    contCasas1 = contCasas1 + m2

                elif contCasas1 == casasCoringaMago[3]:

                    m3 = perguntas(-4, 4, 3, perguntasMago[2], alternativasMago[2][0], alternativasMago[2][1],
                                   alternativasMago[2][2], consequenciasMago[2][0], consequenciasMago[2][1],
                                   consequenciasMago[2][2])
                    contCasas1 = contCasas1 + m3

                elif contCasas1 == casasCoringaMago[4]:

                    m4 = perguntas(-3, -2, 3, perguntasMago[3], alternativasMago[3][0], alternativasMago[3][1],
                                   alternativasMago[3][2], consequenciasMago[3][0], consequenciasMago[3][1],
                                   consequenciasMago[3][2])
                    contCasas1 = contCasas1 + m4

                elif contCasas1 == casasCoringaMago[2]:

                    print(casasBonus[0])
                    contCasas1 = contCasas1 - 10

                elif contCasas1 == casasCoringaMago[5]:

                    print(casasOnus[0])
                    contCasas1 = contCasas1 + 22

        if jogador1 == personagens[1]:
            if contCasas1 > 0:
                print('O', jogador1, 'está na casa', casaAtual1 - contCasas1)
            if contCasas1 in casasCoringaElfo:

                barulho_casacoringa = pygame.mixer.Sound('somvitoria.wav')
                barulho_casacoringa.play()
                print('O', jogador1, 'caiu em uma casa especial')

                if contCasas1 == casasCoringaElfo[0]:

                    e1 = perguntas(-4, 3, -2, perguntasElfo[0], alternativasElfo[0][0], alternativasElfo[0][1],
                                   alternativasElfo[0][2], consequenciasElfo[0][0], consequenciasElfo[0][1],
                                   consequenciasElfo[0][2])
                    contCasas1 = contCasas1 + e1

                elif contCasas1 == casasCoringaElfo[1]:

                    e2 = perguntas(3, 2, -4, perguntasElfo[1], alternativasElfo[1][0], alternativasElfo[1][1],
                                   alternativasElfo[1][2], consequenciasElfo[1][0], consequenciasElfo[1][1],
                                   consequenciasElfo[1][2])
                    contCasas1 = contCasas1 + e2

                elif contCasas1 == casasCoringaElfo[3]:

                    e3 = perguntas(3, -4, -2, perguntasElfo[2], alternativasElfo[2][0], alternativasElfo[2][1],
                                   alternativasElfo[2][2], consequenciasElfo[2][0], consequenciasElfo[2][1],
                                   consequenciasElfo[2][2])
                    contCasas1 = contCasas1 + e3

                elif contCasas1 == casasCoringaElfo[4]:

                    e4 = perguntas(-3, -2, 3, perguntasElfo[3], alternativasElfo[3][0], alternativasElfo[3][1],
                                   alternativasElfo[3][2], consequenciasElfo[3][0], consequenciasElfo[3][1],
                                   consequenciasElfo[3][2])
                    contCasas1 = contCasas1 + e4

                elif contCasas1 == casasCoringaElfo[2]:

                    print(casasBonus[1])
                    contCasas1 = contCasas1 - 10

                elif contCasas1 == casasCoringaElfo[5]:

                    print(casasOnus[1])
                    contCasas1 = contCasas1 + 22

        if jogador1 == personagens[2]:
            if contCasas1 > 0:
                print('O', jogador1, 'está na casa', casaAtual1 - contCasas1)

            if contCasas1 in casasCoringaGuerreiro:
                barulho_casacoringa = pygame.mixer.Sound('somvitoria.wav')
                barulho_casacoringa.play()
                print('O', jogador1, 'caiu em uma casa especial')

                if contCasas1 == casasCoringaGuerreiro[0]:

                    g1 = perguntas(4, -3, -4, perguntasGuerreiro[0], alternativasGuerreiro[0][0],
                                   alternativasGuerreiro[0][1], alternativasGuerreiro[0][2],
                                   consequenciasGuerreiro[0][0], consequenciasGuerreiro[0][1],
                                   consequenciasGuerreiro[0][2])
                    contCasas1 = contCasas1 + g1

                elif contCasas1 == casasCoringaGuerreiro[1]:

                    g2 = perguntas(3, 2, -3, perguntasGuerreiro[1], alternativasGuerreiro[1][0],
                                   alternativasGuerreiro[1][1], alternativasGuerreiro[1][2],
                                   consequenciasGuerreiro[1][0], consequenciasGuerreiro[1][1],
                                   consequenciasGuerreiro[1][2])
                    contCasas1 = contCasas1 + g2

                elif contCasas1 == casasCoringaGuerreiro[3]:

                    g3 = perguntas(2, -3, 3, perguntasGuerreiro[2], alternativasGuerreiro[2][0],
                                   alternativasGuerreiro[2][1], alternativasGuerreiro[2][2],
                                   consequenciasGuerreiro[2][0], consequenciasGuerreiro[2][1],
                                   consequenciasGuerreiro[2][2])
                    contCasas1 = contCasas1 + g3

                elif contCasas1 == casasCoringaGuerreiro[4]:

                    g4 = perguntas(-2, -3, 3, perguntasGuerreiro[3], alternativasGuerreiro[3][0],
                                   alternativasGuerreiro[3][1], alternativasGuerreiro[3][2],
                                   consequenciasGuerreiro[3][0], consequenciasGuerreiro[3][1],
                                   consequenciasGuerreiro[3][2])
                    contCasas1 = contCasas1 + g4

                elif contCasas1 == casasCoringaGuerreiro[2]:

                    print(casasBonus[2])
                    contCasas1 = contCasas1 - 10

                elif contCasas1 == casasCoringaGuerreiro[5]:

                    print(casasOnus[2])
                    contCasas1 = contCasas1 + 22

    if qualJog == 2:
        dado = gira()
        sleep(1)
        barulho_dado = pygame.mixer.Sound('somdodado.wav')
        barulho_dado.play()
        print('O jogador 2 tirou', dado, 'no dado')

        contCasas2 = contCasas2 - dado

        if jogador2 == personagens[0]:
            if contCasas2 > 0:
                print('O', jogador2, 'está na casa', casaAtual2 - contCasas2)

            if contCasas2 in casasCoringaMago:
                import pygame
                barulho_casacoringa = pygame.mixer.Sound('somvitoria.wav')
                barulho_casacoringa.play()
                print('O', jogador2, 'caiu em uma casa especial')

                if contCasas2 == casasCoringaMago[0]:

                    m1 = perguntas(2, -4, -2, perguntasMago[0], alternativasMago[0][0], alternativasMago[0][1],
                                   alternativasMago[0][2], consequenciasMago[0][0], consequenciasMago[0][1],
                                   consequenciasMago[0][2])
                    contCasas2 = contCasas2 + m1

                elif contCasas2 == casasCoringaMago[1]:

                    m2 = perguntas(3, -3, 1, perguntasMago[1], alternativasMago[1][0], alternativasMago[1][1],
                                   alternativasMago[1][2], consequenciasMago[1][0], consequenciasMago[1][1],
                                   consequenciasMago[1][2])
                    contCasas2 = contCasas2 + m2

                elif contCasas2 == casasCoringaMago[3]:

                    m3 = perguntas(-4, 4, 3, perguntasMago[2], alternativasMago[2][0], alternativasMago[2][1],
                                   alternativasMago[2][2], consequenciasMago[2][0], consequenciasMago[2][1],
                                   consequenciasMago[2][2])
                    contCasas2 = contCasas2 + m3

                elif contCasas2 == casasCoringaMago[4]:

                    m4 = perguntas(-3, -2, 3, perguntasMago[3], alternativasMago[3][0], alternativasMago[3][1],
                                   alternativasMago[3][2], consequenciasMago[3][0], consequenciasMago[3][1],
                                   consequenciasMago[3][2])
                    contCasas2 = contCasas2 + m4

                elif contCasas2 == casasCoringaMago[2]:

                    print(casasBonus[0])
                    contCasas2 = contCasas2 - 10

                elif contCasas2 == casasCoringaMago[5]:

                    print(casasOnus[0])
                    contCasas2 = contCasas2 + 22

        if jogador2 == personagens[1]:
            if contCasas2 > 0:
                print('O', jogador2, 'está na casa', casaAtual2 - contCasas2)

            if contCasas2 in casasCoringaElfo:
                barulho_casacoringa = pygame.mixer.Sound('somvitoria.wav')
                barulho_casacoringa.play()
                print('O', jogador2, 'caiu em uma casa especial')

                if contCasas2 == casasCoringaElfo[0]:

                    e1 = perguntas(-4, 3, -2, perguntasElfo[0], alternativasElfo[0][0], alternativasElfo[0][1],
                                   alternativasElfo[0][2], consequenciasElfo[0][0], consequenciasElfo[0][1],
                                   consequenciasElfo[0][2])
                    contCasas2 = contCasas2 + e1

                elif contCasas2 == casasCoringaElfo[1]:

                    e2 = perguntas(3, 2, -4, perguntasElfo[1], alternativasElfo[1][0], alternativasElfo[1][1],
                                   alternativasElfo[1][2], consequenciasElfo[1][0], consequenciasElfo[1][1],
                                   consequenciasElfo[1][2])
                    contCasas2 = contCasas2 + e2

                elif contCasas2 == casasCoringaElfo[3]:

                    e3 = perguntas(3, -4, -2, perguntasElfo[2], alternativasElfo[2][0], alternativasElfo[2][1],
                                   alternativasElfo[2][2], consequenciasElfo[2][0], consequenciasElfo[2][1],
                                   consequenciasElfo[2][2])
                    contCasas2 = contCasas2 + e3

                elif contCasas2 == casasCoringaElfo[4]:

                    e4 = perguntas(-3, -2, 3, perguntasElfo[3], alternativasElfo[3][0], alternativasElfo[3][1],
                                   alternativasElfo[3][2], consequenciasElfo[3][0], consequenciasElfo[3][1],
                                   consequenciasElfo[3][2])
                    contCasas2 = contCasas2 + e4

                elif contCasas2 == casasCoringaElfo[2]:

                    print(casasBonus[1])
                    contCasas2 = contCasas2 - 10

                elif contCasas2 == casasCoringaElfo[5]:

                    print(casasOnus[1])
                    contCasas2 = contCasas2 + 22

        if jogador2 == personagens[2]:
            if contCasas2 > 0:
                print('O', jogador2, 'está na casa', casaAtual2 - contCasas2)

            if contCasas2 in casasCoringaGuerreiro:
                barulho_casacoringa = pygame.mixer.Sound('somvitoria.wav')
                barulho_casacoringa.play()
                print('O', jogador2, 'caiu em uma casa especial')

                if contCasas2 == casasCoringaGuerreiro[0]:

                    g1 = perguntas(4, -3, -4, perguntasGuerreiro[0], alternativasGuerreiro[0][0],
                                   alternativasGuerreiro[0][1], alternativasGuerreiro[0][2],
                                   consequenciasGuerreiro[0][0], consequenciasGuerreiro[0][1],
                                   consequenciasGuerreiro[0][2])
                    contCasas2 = contCasas2 + g1

                elif contCasas2 == casasCoringaGuerreiro[1]:

                    g2 = perguntas(3, 2, -3, perguntasGuerreiro[1], alternativasGuerreiro[1][0],
                                   alternativasGuerreiro[1][1], alternativasGuerreiro[1][2],
                                   consequenciasGuerreiro[1][0], consequenciasGuerreiro[1][1],
                                   consequenciasGuerreiro[1][2])
                    contCasas2 = contCasas2 + g2

                elif contCasas2 == casasCoringaGuerreiro[3]:

                    g3 = perguntas(2, -3, 3, perguntasGuerreiro[2], alternativasGuerreiro[2][0],
                                   alternativasGuerreiro[2][1], alternativasGuerreiro[2][2],
                                   consequenciasGuerreiro[2][0], consequenciasGuerreiro[2][1],
                                   consequenciasGuerreiro[2][2])
                    contCasas2 = contCasas2 + g3

                elif contCasas2 == casasCoringaGuerreiro[4]:

                    g4 = perguntas(-2, -3, 3, perguntasGuerreiro[3], alternativasGuerreiro[3][0],
                                   alternativasGuerreiro[3][1], alternativasGuerreiro[3][2],
                                   consequenciasGuerreiro[3][0], consequenciasGuerreiro[3][1],
                                   consequenciasGuerreiro[3][2])
                    contCasas2 = contCasas2 + g4

                elif contCasas2 == casasCoringaGuerreiro[2]:

                    print(casasBonus[2])
                    contCasas2 = contCasas2 - 10

                elif contCasas2 == casasCoringaGuerreiro[5]:

                    print(casasOnus[2])
                    contCasas2 = contCasas2 + 22

if contCasas1 <= 0:
    sleep(2)
    print('O vencedor foi o', jogador1)

elif contCasas2 <= 0:
    sleep(2)
    print('O vencedor foi o', jogador2)