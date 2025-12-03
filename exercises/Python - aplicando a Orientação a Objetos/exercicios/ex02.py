class Musica:
    musicas = []  

    def __init__(self, nome, artista, duracao):
        self.nome = nome  
        self.artista = artista  
        self.duracao = duracao 
        Musica.musicas.append(self) 

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def r_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica1 = Musica('California Dreamin', 'The Mamas & The Papas', '260')
musica2 = Musica('Feels like We Only Go Backwards', 'Tame Impala', '320')

Musica.listar_musicas()