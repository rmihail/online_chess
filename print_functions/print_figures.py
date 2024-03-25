# вывод фигур на экран
def print_figures(screen, board, coordinates, pieces):
    f_piece_map = board.piece_map()
    for square in range(64):
        # проверка, есть ли в клетке фигура
        piece = board.piece_at(square)
        if piece is None:
            pass
        else:
            for key in coordinates.keys():
                if square in key:
                    horizontal = coordinates[key]
            screen.blit(pieces[str(piece)], ((square % 8) * 100, 700 - (
                        square // 8) * 100))  # тут я напишу свое расположение на доске, сейчас краденное со статьи
