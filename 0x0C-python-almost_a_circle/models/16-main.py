#!/usr/bin/python3
from rectangle import Rectangle


if __name__ == "__main__":
    l_i = [{"id": 89, "width": 10, "height": 4 }, {"id": 7, "width": 1, "height": 7 }]
    j_l_i = Rectangle.to_json_string(l_i)

    l_o = Rectangle.from_json_string(j_l_i)
    print("[{}] {}".format(type(l_i), l_i))
    print("[{}] {}".format(type(l_o), l_o))
