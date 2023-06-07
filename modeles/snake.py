def bump_wall(self):  # Проверка на столкновение со стеной
    __head_x = self.body[-1]['x']
    __head_y = self.body[-1]['y']
    if ((__head_x < ((self.CONST.SNAKE_THICKNESS.value // 2) + 1))
            or (__head_y < ((self.CONST.SNAKE_THICKNESS.value // 2) + 1))
            or (__head_x > (self.canv_width
                            - (self.CONST.SNAKE_THICKNESS.value // 2) + 1))
            or (__head_y > (self.canv_height
                            - (self.CONST.SNAKE_THICKNESS.value // 2) + 1))):
        self.explosive()
        return 'the end'
    else:
        return 0


def bump_body(self):  # Проверка на столкновение с телом змеи
    __head_x = self.body[-1]['x']
    __head_y = self.body[-1]['y']
    bump = 0
    for i in range(0, (len(self.body) - 1)):
        if ((__head_x == self.body[i]['x'])
                and (__head_y == self.body[i]['y'])):
            self.explosive()
            bump = 'the end'
    return bump
