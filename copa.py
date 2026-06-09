#sorteia gols aleatórios e um banco de dados que já vem no python
import random
import sqlite3

#cria o arquivo do banco e o cursor é como se fosse uma caneta para escrever.
def criar_banco():
    conn = sqlite3.connect("copa2026.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS times (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS partidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fase TEXT NOT NULL,
            time1 TEXT NOT NUL  L,
            time2 TEXT NOT NULL,
            gols1 INTEGER,
            gols2 INTEGER,
            vencedor TEXT
        )
    """)

#aqui salva as mudanças e fecha a conexão
    conn.commit()
    conn.close()

#aqui já simula uma partida
def simular_partida(time1, time2):
    gols1 = random.randint(0, 4)
    gols2 = random.randint(0, 4)

    #em copa não pode empate vai para os penaltis
    if gols1 == gols2:

        #desempate nos penaltis: sorteia 1 ou 2
        if random.randint(1, 2) == 1:
            gols1 += 1 #time1 ganha nos penaltis
        else:
            gols2 += 1 #time2 ganha nos penaltis

    vencedor = time1 if gols1 > gols2 else time2
    return gols1, gols2, vencedor

#aqui já salva a partida no banco
def salvar_partida(fase, time1, time2, gols1, gols2, vencedor):
    conn = sqlite3.connect("copa2026.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO partidas (fase, time1, time2, gols1, gols2, vencedor)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (fase, time1, time2, gols1, gols2, vencedor))

    conn.commit()
    conn.close()

#aqui simula uma fase inteira, exemplo: Brasil x Colombia nas finais
def simular_fase(times, nome_fase):
    print(f"\n{'='*40}")
    print(f"       {nome_fase}")
    print(f"{'='*40}")

    vencedores = []

 #pega dois times por vez: [0,1], [2,3], [4,5] e etc...
    for i in range(0, len(times), 2):
        time1 = times[i]
        time2 = times[i + 1]

        gols1, gols2, vencedor = simular_partida(time1, time2)

        print(f"{time1} {gols1} x {gols2} {time2}  →  Passa: {vencedor}")

        salvar_partida(nome_fase, time1, time2, gols1, gols2, vencedor)
        vencedores.append(vencedor)

    return vencedores

#os 16 times das oitavas
def rodar_copa():
    times = [
        "Brasil", "México",
        "Argentina", "Austrália",
        "França", "Polônia",
        "Inglaterra", "Senegal",
        "Alemanha", "Japão",
        "Espanha", "Marrocos",
        "Portugal", "Suíça",
        "Holanda", "EUA"
    ]

    criar_banco()

#aqui roda cada fase
    oitavas   = simular_fase(times,    "Oitavas de Final")
    quartas   = simular_fase(oitavas,  "Quartas de Final")
    semifinal = simular_fase(quartas,  "Semifinal")
    final     = simular_fase(semifinal,"Final")

    campeao = final[0]
    print(f"\n🏆 Campeão da Copa 2026: {campeao} 🏆\n")

#inicia a copa!
rodar_copa()