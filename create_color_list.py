import colorgram

colors = colorgram.extract("image.jpg", 30)


def get_rgb_value_list(list_name):
    """This function returns list of rgb values"""
    rgb_class_list = []
    for color in list_name:
        rgb_class_list.append(color.rgb)

    colors_list = []
    for rgb_color in rgb_class_list:
        r = rgb_color[0]
        g = rgb_color[1]
        b = rgb_color[2]
        tup = r, b, g
        colors_list.append(tup)

    return colors_list


rgb_colors_list = get_rgb_value_list(colors)
print(rgb_colors_list)
