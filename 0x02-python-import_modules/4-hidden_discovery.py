#!/usr/bin/python3
if _name_ == "_main_":
    import hidden_4
    for name in sorted(dir(hidden_4)):
        if name[:2] != "__":
            print("{}".format(name))
