import colorgram

colors = colorgram.extract("image.jpg", 30)


def get_rgb_value_list(list_name):
    rgb_class_list = []
    for c in list_name:
        rgb_class_list.append(c.rgb)

    colors_list = []
    for c in rgb_class_list:
        r = c[0]
        g = c[1]
        b = c[2]
        tup = r, b, g
        colors_list.append(tup)

    return colors_list


rgb_colors_list = get_rgb_value_list(colors)
print(rgb_colors_list)
