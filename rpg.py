#RPG 

import random
from dataclasses import dataclass

@dataclass
class Player:
    classe: str
    hp: int
    max_hp: int
    poder: int
    defendendo: bool = False
    crit: int = 0 # %

@dataclass
class Monster:
    hp: int
    max_hp: int
    atk: int
    defendendo: bool = False

def escolhe_classe() -> str:
    while True:
        op = input("Escolha sua classe [G]Guerreiro / [M]Mago: ").strip().lower()
        if op in ("g", "guerreiro"):
            return "guerreiro"
        if op in ("m", "mago"):
            return "mago"
        print("Opção inválida.")

def cria_player(classe: str) -> Player:
    poder_inicial = random.randint(5, 10) if classe == "guerreiro" else random.randint(7, 15)
    return Player(classe=classe, hp=20, max_hp=20, poder=poder_inicial)

def cria_monstro(base_hp: int, base_atk: int) -> Monster:
    return Monster(hp=base_hp, max_hp=base_hp, atk=base_atk)

def rola_dano_player(p: Player) -> tuple[int, bool]:
    if p.classe == "guerreiro":
        dano = random.randint(3, 10)
    else:  # mago
        dano = random.randint(0, 8)
    critou = random.randint(1, 100) <= p.crit
    if critou and dano > 0:
        dano *= 2
    return dano, critou

def turno_player(p: Player, m: Monster):
    while True:
        print(f"\nVocê: HP {p.hp}/{p.max_hp} | Poder {p.poder} | Defesa {'ON' if p.defendendo else 'OFF'} | Crítico {p.crit}%")
        print(f"Monstro: HP {m.hp}/{m.max_hp} | Defesa {'ON' if m.defendendo else 'OFF'} | ATK {m.atk}")
        acao = input("Ações: [A]tacar (-2 poder) | [D]efender (Mago -1 poder) | [C]urar | [R]est/Descansar | [S]air\n> ").strip().lower()

        if acao in ("s", "sair"):
            return "sair"

        if acao in ("a", "atacar"):
            if p.poder < 2:
                print("Sem poder suficiente para atacar (precisa de 2).")
                continue
            p.poder -= 2
            dano, critou = rola_dano_player(p)
            if m.defendendo:
                print("O monstro se defendeu! Seu ataque foi anulado.")
                m.defendendo = False
                dano = 0
            else:
                m.hp = max(0, m.hp - dano)
            if critou and dano > 0:
                print(f"🔥 CRÍTICO! Você causou {dano} de dano.")
            else:
                print(f"Você causou {dano} de dano.")
            break

        if acao in ("d", "defender"):
            if p.classe == "mago":
                if p.poder < 1:
                    print("Mago sem poder para defender (precisa de 1).")
                    continue
                p.poder -= 1
            p.defendendo = True
            print("Você entrou em postura defensiva. O próximo ataque recebido será anulado.")
            break

        if acao in ("c", "curar"):
            cura = 1 if p.classe == "guerreiro" else 4
            antes = p.hp
            p.hp = min(p.max_hp, p.hp + cura)
            print(f"Você recuperou {p.hp - antes} de HP.")
            break

        if acao in ("r", "rest", "descansar"):
            ganho = random.randint(1, 5)
            p.poder += ganho
            print(f"Você descansou e recuperou {ganho} de poder.")
            break

        print("Ação inválida. Tente novamente.")
    return "ok"

def turno_monstro(p: Player, m: Monster):
    if m.hp <= 0:
        return
    acao = random.choice(("atacar", "defender"))
    if acao == "defender":
        m.defendendo = True
        print("🛡️ O monstro adotou postura defensiva.")
    else:
        if p.defendendo:
            print("🛡️ Sua defesa anulou o ataque do monstro!")
            p.defendendo = False
        else:
            p.hp = max(0, p.hp - m.atk)
            print(f"💥 O monstro atacou e causou {m.atk} de dano. (Seu HP: {p.hp}/{p.max_hp})")

def main():
    print("== RPG de Console (turnos) ==")
    classe = escolhe_classe()
    player = cria_player(classe)

    nivel = 1
    base_hp_monstro = 20
    base_atk_monstro = 3
    CRIT_CAP = 50

    while True:
        monstro = cria_monstro(base_hp_monstro, base_atk_monstro)
        print(f"\n--- Início do combate #{nivel} ---")

        while player.hp > 0 and monstro.hp > 0:
            res = turno_player(player, monstro)
            if res == "sair":
                print("Você decidiu encerrar o jogo. Até a próxima!")
                return
            if monstro.hp <= 0:
                break
            turno_monstro(player, monstro)

        if player.hp <= 0:
            print("\n💀 Você foi derrotado. Fim de jogo.")
            return

        print("\n🏆 Monstro derrotado!")
        op = input("Quer continuar? [S/N] ").strip().lower()
        if op != "s":
            print("Encerrando a aventura. Bom descanso!")
            return

        # Evoluções para o próximo monstro/rodada
        nivel += 1
        player.max_hp += 5
        player.hp = player.max_hp
        player.crit = min(CRIT_CAP, player.crit + 3)
        base_hp_monstro += 10
        base_atk_monstro += 3

        print(f"⚙️ Próximo monstro: HP {base_hp_monstro}, ATK {base_atk_monstro}.")
        print(f"💪 Você evoluiu: HP máx {player.max_hp}, crítico {player.crit}%.\n")

if __name__ == "__main__":
    main()