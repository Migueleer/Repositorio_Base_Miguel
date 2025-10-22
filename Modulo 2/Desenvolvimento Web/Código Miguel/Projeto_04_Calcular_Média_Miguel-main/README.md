<div align="center">

# 🎵 Criador de Playlists Musicais

### 🎯 Projeto: Sistema de Recomendação de Artistas por Gênero

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com)

*Desafie suas habilidades em Python e criação de aplicações web interativas!*

</div>

---

## 📋 Descrição do Projeto

Você foi contratado por uma startup musical para desenvolver um sistema que ajudar usuários a descobrir novos artistas baseados em seus gêneros musicais preferidos.

Seu objetivo é criar uma aplicação web usando **Streamlit** que permita:
- Selecionar um gênero musical em uma sidebar
- Visualizar artistas relacionados a esse gênero em outra sidebar
- Criar uma experiência intuitiva e responsiva

---

## 🎯 Requisitos Obrigatórios

### 🎛️ Funcionalidades Básicas
- [ ] **Sidebar de Gêneros**: Um `st.selectbox` com pelo menos 5 gêneros musicais
- [ ] **Sidebar de Artistas**: Um `st.selectbox` que mostra artistas baseados no gênero selecionado
- [ ] **Dados em Dicionário**: Usar uma estrutura de dicionário Python para armazenar os artistas por gênero
- [ ] **Interatividade**: A segunda sidebar deve atualizar automaticamente ao mudar o gênero

### 💻 Tecnologias
- [ ] **Streamlit**: Para a interface web
- [ ] **Python**: Linguagem de programação
- [ ] **Estrutura de Dados**: Dicionários para mapear gêneros e artistas

---

## 🎨 Exemplo de Estrutura de Dados

```python
# Dicionário de gêneros e artistas (você pode adicionar mais!)
generos_artistas = {
    "Rock": ["Queen", "The Beatles", "Led Zeppelin", "Pink Floyd", "AC/DC"],
    "Pop": ["Taylor Swift", "Ed Sheeran", "Ariana Grande", "Justin Bieber", "Dua Lipa"],
    "Hip Hop": ["Kendrick Lamar", "Drake", "Eminem", "Cardi B", "Travis Scott"],
    "Eletrônica": ["Daft Punk", "Calvin Harris", "David Guetta", "Skrillex", "Marshmello"],
    "Sertanejo": ["Gusttavo Lima", "Marília Mendonça", "Jorge & Mateus", "Henrique & Juliano", "Maiara & Maraisa"]
}
