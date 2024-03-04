import pygame as pg

file = input('File to display: ')

code = open(file).read()


keys = ['set', 'import', 'add', '#CREATE', '@FOR', 'LANGUAGE']
sub_keys = ['child', 'title', 'css', 'js', 'MARKGO']


def print_code(code):
    b = False
    cc = False
    l = ''
    ans = ''
    for i in range(len(code)):
        c = code[i]
        if not b:
            if c == '<':
                ans += '\0334\0\033'
                cc = True
            elif c == '>':
                ans += '>\0330\0\033'
                cc = False
                continue
        if c == '\'' or c == '"':
            b = not b
            if b:
                ans += '\0332\0\033'
            else:
                ans += f'{c}\0330\0\033'
                continue
        if not cc and not b:
            if c == '?':
                ans += '\0336\0\033'
                l += c
            elif c == '!' or c == '@':
                ans += '\0331\0\033'
                l += c
            elif (c == ' ' or c == ';' or c == '\n'
                  or c == '.' or c == '{' or c == '}' or c == ':'):
                if l in keys:
                    ans += '\0333\0\033'
                elif l in sub_keys:
                    ans += '\0335\0\033'
                ans += l
                ans += '\0330\0\033'
                l = ''
                ans += c
            else:
                l += c
        else:
            ans += c

    return ans


pg.init()

font = pg.font.SysFont('consolas', 20)

s = print_code(code)

colors = [(255, 255, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
          (0, 0, 255), (255, 0, 255), (0, 255, 255)]

ss = [f.split('\033') for f in s.split('\n')]

clr = (255, 255, 255)

window = pg.display.set_mode((800, 600))

moveX = 0
moveY = 0
size = 1


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.MOUSEWHEEL:
            moveY += 5 * event.y
            moveX += 5 * event.x

    keys = pg.key.get_pressed()
    mouse = pg.mouse.get_pressed(5)

    size *= 1 + (keys[pg.K_EQUALS] - keys[pg.K_MINUS]) * 0.02

    window.fill((0, 0, 0))
    for i in range(len(ss)):
        x = i
        y = 0
        for j in ss[i]:
            if j.endswith('\0'):
                clr = colors[int(j.removesuffix('\0'))]
            else:
                text = font.render(j, True, clr)
                text = pg.transform.scale_by(text, size)
                textRect = text.get_rect()
                textRect.topleft = (y * 10 * size + moveX,
                                    x * 20 * size + moveY)
                window.blit(text, textRect)
            y += len(j)

    pg.display.flip()
