import streamlit as st

# Dados de exemplo
generos = ["Sertanejo", "Funk", "Pop"]

# Dicionário relacionando gêneros musicais
artista_por_genero = {
    "Sertanejo": ["Marilia Mendonça", "Gusttavo Lima", "Zé Neto e Cristiano", "Jorge e Mateus"],
    "Funk": ["Mc Daleste", "Mc Pedrinho", "Mc Hariel", "Mc Livinho"],
    "Pop": ["Bruno Mars", "Michael Jackson", "Ariana Grande", "Billie Eilish"],
}

# Selectbox para escolher o gênero
st.sidebar.image('logo.png')
genero_selecionado = st.sidebar.selectbox("Escolha um gênero musical:", generos)

# Selectbox para escolher o artista (apenas do gênero selecionado)
if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox(
        "Selecione o artista:", 
        artista_por_genero[genero_selecionado]
    )

# Mostrar apenas o artista selecionado
if genero_selecionado == 'Sertanejo' and artista_selecionado == 'Marilia Mendonça':
    st.title('Marilia Mendonça\n')
    st.write('Marília Mendonça (1995 - 2021) foi cantora e compositora goiana, grande nome do sertanejo e conhecida como “rainha da sofrência”. Revelou-se em 2015 com Infiel, tornou-se fenômeno nacional com músicas sobre amor e empoderamento, e bateu recordes de público e streaming. Em 2020, suas lives marcaram a pandemia. Morreu tragicamente em 2021, aos 26 anos, em um acidente aéreo, deixando forte legado na música brasileira.\n')
    st.video('https://youtu.be/eCyMh-mZ1B0?si=RODJXIkzfupbpETf')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DXc5EXfkDXlmk?si=h3L9stGfTiiQxty-b4tAsg", label= "Spotify")

elif genero_selecionado == 'Sertanejo' and artista_selecionado == 'Gusttavo Lima':
    st.title('Gusttavo Lima\n')
    st.write('Gusttavo Lima (1989) é cantor e compositor mineiro, um dos maiores nomes do sertanejo universitário. Ficou famoso em 2011 com o hit “Balada (Tchê Tcherere Tchê Tchê)”, que alcançou repercussão internacional. Desde então, construiu carreira marcada por sucessos como Apelido Carinhoso e Homem de Família, além de megashows conhecidos como “Buteco do Gusttavo Lima”. É um dos artistas mais ouvidos do Brasil no streaming e consolidou-se como ícone do gênero.\n')
    st.video('https://youtu.be/14C28JSO-sg?si=y16DsnfTV7brAsxL')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO4BJeus?si=de9uT_byQ2WDt1uixTwZ3A", label= "Spotify")
    

elif genero_selecionado == 'Sertanejo' and artista_selecionado == 'Zé Neto e Cristiano':
    st.title('Zé Neto e Cristiano\n')
    st.write('Zé Neto & Cristiano são uma dupla sertaneja de São José do Rio Preto (SP), formada em 2011. Ganhou destaque nacional a partir de 2015 com o sucesso “Eu Ligo Pra Você” e se consolidou com hits como Largado às Traças, Notificação Preferida e Mulher Maravilha. Conhecidos por unir romantismo e sofrência, tornaram-se uma das duplas mais populares do Brasil, com forte presença em rádios, streaming e grandes festivais de música.\n')
    st.video('https://youtu.be/rYKOuKaWEjg?si=Aa62hscyqWl1ak8C')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO2pDoLC?si=idWVoiv1SUuCKrwgDELurw", label= "Spotify")

elif genero_selecionado == 'Sertanejo' and artista_selecionado == 'Jorge e Mateus':
    st.title('Jorge e Mateus\n')
    st.write('Jorge & Mateus são uma dupla sertaneja goiana, formada em 2005, considerada uma das mais importantes do gênero. Estouraram nacionalmente em 2007 com “Pode Chorar” e, desde então, emplacaram inúmeros sucessos como Voa Beija-Flor, Amo Noite e Dia e Tijolão. Reconhecidos pela mistura de romantismo e inovação no sertanejo universitário, acumulam recordes de público, vendas e streaming, sendo referência para novas gerações de artistas.\n')
    st.video('https://youtu.be/ICS6uKC93w0?si=IaLd9agcgeAcy_pJ')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO0FsQXS?si=kcoSjVjwQfOPqjprJl8rGQ", label= "Spotify")

elif genero_selecionado == 'Funk' and artista_selecionado == 'Mc Daleste':
    st.title('Mc Daleste\n')
    st.write('MC Daleste (1992–2013) foi um cantor e compositor paulista de funk ostentação. Ganhou fama com músicas como “Angra dos Reis”, “Mãe de Traficante” e “O Gigante Acordou”, que misturavam ostentação, crítica social e realidade das periferias. Tornou-se um dos nomes mais promissores do gênero, mas sua carreira foi interrompida tragicamente quando foi assassinado durante um show em Campinas, aos 20 anos, em 2013. Seu legado permanece forte no funk brasileiro.\n')
    st.video('https://youtu.be/jInKRB79wD4?si=ViSruJ2fcjQaJJOT')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO2vHzFK?si=4GD5hfoyRq2hgmf0BQFpBQ", label= "Spotify")

elif genero_selecionado == 'Funk' and artista_selecionado == 'Mc Pedrinho':
    st.title('Mc Pedrinho\n')
    st.write('MC Pedrinho (2002) é um cantor de funk paulista que ficou conhecido ainda criança com músicas de funk proibidão e depois consolidou a carreira explorando estilos como funk ostentação e funk melody. Com hits como Dom Dom Dom e Bipolar (parceria com MC Don Juan e DJ 900), tornou-se um dos funkeiros mais populares da nova geração, acumulando milhões de streams e grande presença nas redes sociais.\n')
    st.video('https://youtu.be/HupR7mehTog?si=jNlORskHJBzyrTPI')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO0FxwNq?si=UoHL-aPOTQqyfQy1z0sHng", label= "Spotify")

elif genero_selecionado == 'Funk' and artista_selecionado == 'Mc Hariel':
    st.title('Mc Hariel\n')
    st.write('MC Hariel (1997) é um cantor e compositor de funk paulista, referência no funk consciente. Ganhou destaque com músicas que falam da realidade da periferia, superação e crítica social, como Mundão Girou, Lei do Retorno e Vou Buscar. Consolidou-se como uma das vozes mais importantes da cena, sendo respeitado tanto por fãs quanto por outros artistas do gênero, com forte presença no streaming e nas quebradas.\n')
    st.video('https://youtu.be/mW8o_WDL91o?si=6tCo5fNa0edxCI2Y')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO0aGty0?si=54x_PujgSk2fUPlYyKTnYg", label= "Spotify")

elif genero_selecionado == 'Funk' and artista_selecionado == 'Mc Livinho':
    st.title('Mc Livinho\n')
    st.write('MC Livinho (1994) é um cantor e compositor de funk paulista, conhecido por sua versatilidade vocal e pela mistura de estilos como funk ostentação, proibidão, romântico e até MPB. Ficou famoso com hits como Tudo de Bom, Cheia de Marra e Fazer Falta, e se tornou um dos artistas mais respeitados do gênero, acumulando milhões de streams e explorando sonoridades além do funk tradicional.\n')
    st.video('https://youtu.be/VklymStK1Vo?si=C4eag8GJjxqc9xBf')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO4m2lsk?si=r5N85op_SHmtYVySc7k5hQ", label= "Spotify")

elif genero_selecionado == 'Pop' and artista_selecionado == 'Bruno Mars':
    st.title('Bruno Mars\n')
    st.write('Bruno Mars (1985) é um cantor, compositor, produtor e multi-instrumentista havaiano, reconhecido mundialmente por sua versatilidade ao transitar entre pop, R&B, funk, soul e reggae. Estourou em 2010 com “Just the Way You Are” e, desde então, lançou sucessos globais como Locked Out of Heaven, Uptown Funk (com Mark Ronson) e Leave the Door Open (com Anderson .Paak, no Silk Sonic). Premiado com múltiplos Grammy Awards, é considerado um dos maiores performers da atualidade, conhecido por shows enérgicos e influências da música retrô.\n')
    st.video('https://youtu.be/fLexgOxsZu0?si=sZhS88UcfS447i4x')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO03DwPK?si=NykzOZF2SiSBmrOyQnN_-Q", label= "Spotify")

elif genero_selecionado == 'Pop' and artista_selecionado == 'Michael Jackson':
    st.title('Michael Jackson\n')
    st.write('Michael Jackson (1958–2009) foi um cantor, compositor e dançarino norte-americano, conhecido como o “Rei do Pop”. Ganhou fama ainda criança com os Jackson 5 e se tornou ícone mundial com álbuns como Thriller, Bad e Dangerous. Revolucionou a música, a dança e os videoclipes, acumulou recordes de vendas e prêmios, e deixou um legado duradouro como um dos artistas mais influentes de todos os tempos.\n')
    st.video('https://youtu.be/Zi_XLOBDo_Y?si=7AIMmXO_n8YMR1GO')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DZ06evO1SVXaM?si=03lj6MHET_28aHXbVISIjQ", label= "Spotify")

elif genero_selecionado == 'Pop' and artista_selecionado == 'Ariana Grande':
    st.title('Ariana Grande\n')
    st.write('Ariana Grande (1993) é uma cantora, compositora e atriz norte-americana, conhecida por sua voz poderosa e alcance vocal impressionante. Ficou famosa inicialmente na TV, em Victorious e Sam & Cat, e depois estourou na música com hits como Problem, Thank U, Next e 7 Rings. Premiada com Grammys e recordes de streaming, é reconhecida por seu estilo pop contemporâneo, influências do R&B e presença marcante nas redes sociais e na cultura pop.\n')
    st.video('https://youtu.be/QYh6mYIJG2Y?si=3H6ydmSPFsN9GWL8')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DX1PfYnYcpw8w?si=8rvf9fKEQtOiYHraHdoxfA", label= "Spotify")

elif genero_selecionado == 'Pop' and artista_selecionado == 'Billie Eilish':
    st.title('Billie Eilish\n')
    st.write('Billie Eilish (2001) é uma cantora e compositora norte-americana conhecida por seu estilo único de pop alternativo e electropop, com letras introspectivas e som experimental. Ficou famosa com Ocean Eyes e consolidou a carreira com álbuns como When We All Fall Asleep, Where Do We Go? e Happier Than Ever. Premiada com Grammys e reconhecida mundialmente, é referência de uma nova geração de artistas que misturam inovação, estética marcante e autenticidade.\n')
    st.video('https://youtu.be/V1Pl8CzNzCw?si=xPp548fPCRpG1lz0')
    st.link_button(url = "https://open.spotify.com/playlist/37i9dQZF1DX6cg4h2PoN9y?si=70RXQomfSieUU7dgKNpPGg", label= "Spotify")


















