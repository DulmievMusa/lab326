from my_library import *
from mnk import *


color_combo_s = [
    ('#000000', '#E69F00', '#56B4E9'),  # Черный, оранжевый, голубой
    ('#009E73', '#D55E00', '#CC79A7'),  # Зеленый, оранжево-красный, розовый
    ('#0072B2', "#F0B642", '#CC79A7'),  # Синий, желтый, розовый
    ('#D55E00', '#009E73', '#56B4E9'),  # Оранжевый, зеленый, голубой
    ('#56B4E9', '#E69F00', '#009E73'),  # Голубой, оранжевый, зеленый
    ('#CC79A7', '#0072B2', "#45F042"),  # Розовый, синий, желтый
    ("#9D0A96", '#D55E00', '#009E73'),  # Желтый, оранжевый, зеленый
    ('#E69F00', '#56B4E9', '#CC79A7'),  # Оранжевый, голубой, розовый
    ('#009E73', '#0072B2', '#D55E00'),  # Зеленый, синий, оранжевый
    ('#CC79A7', "#4245F0", '#56B4E9')   # Розовый, желтый, голубой
]

slovar = get_all_columns_from_file("01_current_calibration.csv")

x_es = slovar[4]
i_es = slovar[7]

k, dk= origin_linear_regression(x_es, i_es)
print(f"k={k}, dk={dk}")
paint_line_function(k, 0, [0] + x_es, y_es=[0] + i_es, color_number=2, size=3)

set_end(x_label="x, см", y_label="I, мкА", show_origin=True)