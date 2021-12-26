from calc_fact import make_display, make_root, make_buttons, make_label
from calc_class import Calculator

def main():
    root = make_root()
    display = make_display(root)
    lable = make_label(root)
    buttons = make_buttons(root)
    calculator = Calculator(root, lable, display, buttons)
    calculator.start()
    

if __name__ == '__main__':
    main()
