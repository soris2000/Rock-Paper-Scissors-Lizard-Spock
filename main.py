import flet as ft
import random
from time import sleep

list_options = ["paper", "rock", "scissors", "lizard", "spock"]
possible_results = [
    ["scissors-paper", "Scissors cuts Paper", "CPU"],
    ["paper-rock", "Paper covers Rock", "CPU"],
    ["rock-lizard", "Rock crushes Lizard", "CPU"],
    ["lizard-spock", "Lizard poisons Spock", "CPU"],
    ["spock-scissors", "Spock smashes Scissors", "CPU"],
    ["scissors-lizard", "Scissors decapitates Lizard", "CPU"],
    ["lizard-paper", "Lizard eats Paper", "CPU"],
    ["paper-spock", "Paper disproves Spock", "CPU"],
    ["spock-rock", "Spock vaporizes Rock", "CPU"],
    ["rock-scissors", "Rock crushes Scissors", "CPU"],
    ["paper-scissors", "Scissors cuts Paper", "PLAYER"],
    ["rock-paper", "Paper covers Rock", "PLAYER"],
    ["lizard-rock", "Rock crushes Lizard", "PLAYER"],
    ["spock-lizard", "Lizard poisons Spock", "PLAYER"],
    ["scissors-spock", "Spock smashes Scissors", "PLAYER"],
    ["lizard-scissors", "Scissors decapitates Lizard", "PLAYER"],
    ["paper-lizard", "Lizard eats Paper", "PLAYER"],
    ["spock-paper", "Paper disproves Spock", "PLAYER"],
    ["rock-spock", "Spock vaporizes Rock", "PLAYER"],
    ["scissors-rock", "Rock crushes Scissors", "PLAYER"],
]

cpu_points = 0
player_points = 0
count = 0


def main(page: ft.Page):
    page.title = "Play Rock, Paper, Scissors, Lizard, Spock"
    page.window_height = 650
    page.window_width = 1024
    page.bgcolor = ft.colors.INDIGO_700

    cpu_results = ft.Row()
    player_results = ft.Row()
    cpu_image = ft.Image(
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
        left=100,
        top=40,
        offset=ft.transform.Offset(-2, 0),
        animate_offset=ft.animation.Animation(500),
    )
    player_image = ft.Image(
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
        right=100,
        top=40,
        offset=ft.transform.Offset(2, 0),
        animate_offset=ft.animation.Animation(500),
    )
    result_txt = ft.Text(
        width=300,
        height=300,
        size=50,
        left=350,
        top=50,
        color=ft.colors.YELLOW,
        text_align=ft.TextAlign.CENTER,
    )

    def new_game(e):
        dlg_endgame.open = False
        reset()
        page.update()

    def close_welcome(e):
        dlg_welcome.open = False
        page.update()

        sleep(2)
        cpu_image.offset = ft.transform.Offset(-2, 0)
        player_image.offset = ft.transform.Offset(2, 0)
        result_txt.value = "Lets's go!"
        page.update()

    dlg_endgame = ft.AlertDialog(
        modal=True,
        content=ft.Image(width=300, height=300, fit=ft.ImageFit.CONTAIN),
        actions=[
            ft.TextButton("New Game", on_click=new_game),
            ft.TextButton("Exit", on_click=lambda e: page.window_destroy()),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    dlg_welcome = ft.AlertDialog(
        modal=True,
        open=True,
        title=ft.Text(value="The Rules", text_align=ft.TextAlign.CENTER),
        content=ft.Image(
            src="assets/rules.png", width=300, height=300, fit=ft.ImageFit.CONTAIN
        ),
        actions=[
            ft.TextButton("Play", on_click=close_welcome),
            ft.TextButton("Exit", on_click=lambda e: page.window_destroy()),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def get_winner(cpu, player):
        global cpu_points
        global player_points
        global count

        if cpu == player:
            result_txt.value = "Draw"
            cpu_results.controls[count].color = ft.colors.GREY
            player_results.controls[count].color = ft.colors.GREY

        else:
            search = str(cpu + "-" + player)
            i = 0
            while i < 20:
                if search in possible_results[i]:
                    win = possible_results[i][2]
                    result_txt.value = possible_results[i][1]
                    if win == "CPU":
                        cpu_points = cpu_points + 1
                        cpu_results.controls[count].color = ft.colors.GREEN
                        player_results.controls[count].color = ft.colors.RED
                    else:
                        player_points = player_points + 1
                        cpu_results.controls[count].color = ft.colors.RED
                        player_results.controls[count].color = ft.colors.GREEN
                    break
                i = i + 1
        count = count + 1
        result_txt.update()
        sleep(2)
        cpu_image.offset = ft.transform.Offset(-2, 0)
        player_image.offset = ft.transform.Offset(2, 0)
        result_txt.value = "Lets's go!"
        if count == 5:
            if cpu_points > player_points:
                image = "lose"
            elif cpu_points < player_points:
                image = "win"
            else:
                image = "draw"
            page.dialog = dlg_endgame
            dlg_endgame.content.src = f"assets/{image}.png"
            dlg_endgame.open = True

        page.update()

    def btn_click(e):
        index = random.randint(0, 4)
        cpu_option = list_options[index]
        player_option = e.control.data
        cpu_image.src = f"assets/{cpu_option}.png"
        player_image.src = f"assets/{player_option}.png"
        cpu_image.offset = ft.transform.Offset(0, 0)
        player_image.offset = ft.transform.Offset(0, 0)

        for i in range(0, len(cpu_board.controls)):
            cpu_board.controls[i].bgcolor = "amber" if i == index else "black12"

        page.update()
        sleep(0.5)
        get_winner(cpu_option, player_option)
        page.update()

    def on_hover(e):
        e.control.bgcolor = "blue" if e.data == "true" else "black12"
        e.control.update()

    def get_header(cpu, player):
        cpu.controls = [
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
        ]
        player.controls = [
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
            ft.Icon(name=ft.icons.CIRCLE, color=ft.colors.WHITE30),
        ]
        return ft.Row(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("CPU", size=25, weight=ft.FontWeight.BOLD),
                        cpu,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.Icon(
                            name=ft.icons.TABLET_MAC, size=50, color=ft.colors.AMBER
                        ),
                        ft.Text(
                            "VS",
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.YELLOW,
                        ),
                        ft.Icon(name=ft.icons.PERSON, size=50, color=ft.colors.AMBER),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text("PLAYER", size=25, weight=ft.FontWeight.BOLD),
                        player,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    def get_body(cpu, player, result):
        cpu.src = "assets/ready.png"
        player.src = "assets/ready.png"
        cpu.offset = ft.transform.Offset(0, 0)
        player.offset = ft.transform.Offset(0, 0)
        result.value = "Ready?"
        return ft.Stack(
            controls=[cpu, player, result],
            height=350,
        )

    def get_player_board():
        return ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/paper.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Paper"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="paper",
                    on_click=btn_click,
                    on_hover=on_hover,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/rock.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Rock"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="rock",
                    on_click=btn_click,
                    on_hover=on_hover,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/scissors.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Scissors"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="scissors",
                    on_click=btn_click,
                    on_hover=on_hover,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/lizard.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Lizard"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="lizard",
                    on_click=btn_click,
                    on_hover=on_hover,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/spock.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("spock"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="spock",
                    on_click=btn_click,
                    on_hover=on_hover,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )

    def get_cpu_board():
        return ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/paper.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Paper"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="paper",
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/rock.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Rock"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    data="rock",
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/scissors.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Scissors"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="scissors",
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/lizard.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("Lizard"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="lizard",
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(
                                src="assets/spock.png",
                                width=50,
                                height=50,
                                fit=ft.ImageFit.CONTAIN,
                            ),
                            ft.Text("spock"),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=5,
                    border_radius=5,
                    bgcolor=ft.colors.BLACK12,
                    data="spock",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )

    def get_footer(cpu, player):
        return ft.Row(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("CPU", size=25, weight=ft.FontWeight.BOLD),
                            cpu,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=400,
                    height=150,
                    border=ft.border.all(1, ft.colors.WHITE),
                    padding=5,
                    border_radius=20,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("PLAYER", size=25, weight=ft.FontWeight.BOLD),
                            player,
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    width=400,
                    height=150,
                    border=ft.border.all(1, ft.colors.WHITE),
                    padding=5,
                    border_radius=20,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    def reset():
        global cpu_points
        global player_points
        global count
        cpu_points = 0
        player_points = 0
        count = 0
        page.controls.clear()
        header = get_header(cpu_results, player_results)
        body = get_body(cpu_image, player_image, result_txt)
        footer = get_footer(cpu_board, player_board)
        page.add(ft.Column([header, body, footer]))
        sleep(2)
        cpu_image.offset = ft.transform.Offset(-2, 0)
        player_image.offset = ft.transform.Offset(2, 0)
        result_txt.value = "Lets's go!"
        page.update()

    # Create UI Game
    header = get_header(cpu_results, player_results)
    body = get_body(cpu_image, player_image, result_txt)
    cpu_board = get_cpu_board()
    player_board = get_player_board()
    footer = get_footer(cpu_board, player_board)
    page.dialog = dlg_welcome
    page.add(ft.Column([header, body, footer]))


if __name__ == "__main__":
    ft.app(target=main)
