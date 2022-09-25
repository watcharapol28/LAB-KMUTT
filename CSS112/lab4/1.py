def mosteller(w, h):
    return (w * h)**0.5 / 60


def du_bois(w, h):
    return 7.184e-3 * w**4.25e-1 * h**7.25e-1


def fujimoto(w, h):
    return 8.883e-3 * w**4.44e-1 * h**6.63e-1


def main():
    weight = float(input())
    height = float(input())
    print("Mosteller = ", round((weight * height)**0.5 / 60, 5), sep = '')
    print("Du Bois = ", round(7.184e-3 * weight**4.25e-1 * height**7.25e-1, 5), sep = '')
    print("Fujimoto = ", round(8.883e-3 * weight**4.44e-1 * height**6.63e-1, 5), sep = '')


exec(input())