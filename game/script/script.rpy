# Вы можете расположить сценарий своей игры в этом файле.
init -2:
    image ctc_blink:
        xpos 1.4      # Across from right
        ypos 1.3      # Up from bottom
        xanchor 1.0   # On Right
        yanchor 1.0   # On Bottom
        # alpha 0.0   # invisible
        "iac.png"
        # linear 0.75 alpha 1.0
        # linear 0.75 alpha 0.0
        linear 1.1 ypos 1.7
        linear 1.1 ypos 1.3 
        repeat

# Определение персонажей игры.
define narrator = Character(
    None,
    ctc="ctc_blink",
)
define N = Character(
    None,
    what_xalign=0.5, #Centers text within the window
    window_xalign=0.5, #Centers the window horizontally
    window_yalign=0.5, #Centers the window vertically
    what_text_align=0.5, #Centers text within the window, just in case
    window_background=None,#Removes the window, so only the text shows
    ctc="ctc_blink",
)
define P = Character('Порфирий Ливанов', color="#b5b5b5", ctc="ctc_blink")
define L = Character('Леха Черных', color="#b5b5b5", ctc="ctc_blink")
define Boris = Character('Борис', color="#b5b5b5", ctc="ctc_blink")
define Doc = Character('Доктор Денис', color="#b5b5b5", ctc="ctc_blink")
define Drunkard = Character('Алкаш', color="#b5b5b5", ctc="ctc_blink")
define Maiden = Character('Уборщица', color="#b5b5b5", ctc="ctc_blink")

transform default_pos:
    zoom 0.70
    xalign 0.5
    yalign 1.0

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь (entrypoint):
label start:
    stop music

    show bg black
    $ renpy.pause(3.0, hard=True)

    call chapter1
    
    label end_game:
        "Конец"
return
