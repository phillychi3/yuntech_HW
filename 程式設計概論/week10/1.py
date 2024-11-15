import random

"""
想像你是遊戲的參賽者，現在節目的現場有三道門，門後分別有一台跑車、兩隻綿羊，主持人要你隨便挑一道門，如果門打開後面是跑車你就可以抱回家，但如果是綿羊的話就沒得到大獎啦～
現在你選了一道門，但隨即主持人說：現在我幫你打開一扇後面是綿羊的門，你仍要堅持你一開始選的門嗎？還是你要換呢？最後決定請選擇！
"""
def simulate_monty_hall():
    prize_door = random.randint(0, 2)
    player_choice = random.randint(0, 2)

    opened_door = None
    while True:
        opened_door = random.randint(0, 2)
        if opened_door != prize_door and opened_door != player_choice:
            break

    final_choice = None
    while True:
        final_choice = random.randint(0, 2)
        if final_choice != player_choice and final_choice != opened_door:
            break

    return final_choice == prize_door


def main():
    wins = 0
    trials = 10000

    for _ in range(trials):
        if simulate_monty_hall():
            wins += 1

    print(f"在 {trials} 次模擬中，改變選擇獲得獎品的次數：{wins}")


if __name__ == "__main__":
    main()
