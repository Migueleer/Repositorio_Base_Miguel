-- Mostrando a tabela
SELECT * from musicas

-- 1. Músicas mais populares (mais streams)
SELECT titulo, artista, streaming_count 
FROM musicas 
ORDER BY streaming_count DESC 
LIMIT 10;

-- 2. Artistas com mais músicas na lista
SELECT artista, COUNT(*) as total_musicas, 
       SUM(streaming_count) as total_streams
FROM musicas 
GROUP BY artista 
HAVING COUNT(*) > 1
ORDER BY total_musicas DESC, total_streams DESC;

-- 3. Músicas por década
SELECT 
    (ano_lancamento / 10) * 10 as decada,
    COUNT(*) as total_musicas,
    AVG(duracao_segundos) as media_duracao
FROM musicas 
GROUP BY decada 
ORDER BY decada;

-- 4. Gêneros musicais mais populares
SELECT genero, COUNT(*) as total, 
       AVG(streaming_count) as media_streams
FROM musicas 
GROUP BY genero 
ORDER BY total DESC;

-- 5. Músicas mais longas
SELECT titulo, artista, duracao_segundos, genero
FROM musicas 
ORDER BY duracao_segundos DESC 
LIMIT 10;

-- 6. Top artistas por total de streams
SELECT artista, SUM(streaming_count) as total_streams
FROM musicas 
GROUP BY artista 
ORDER BY total_streams DESC 
LIMIT 10;


-- 7. Quero saber quais os albuns do Michael Jackson estão na lista e quais os anos de lançamento dos albuns

-- 8. Quero ver somente as musicas de Rock da playlist

-- 9. quero ver somente as musicas lançadas nos anos 90

-- 10. quero ver musicas lançadas apartir dos anos 2000

-- 11. Adicione as informações a respeito da sua musica favorita.

-- 12 .Adicione qualquer música de Funk que o professor odeia

-- 13. remova essa música que você acabou de adicionar.

-- 14. Conte quantas músicas a banda AC/DC tem 

-- 15. conte quantas músicas de POP tem na playlist 

-- 16. Ordene as musícas da mais velha para a mais nova.




