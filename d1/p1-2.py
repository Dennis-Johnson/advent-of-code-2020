import numpy as np

def main():
    data = np.loadtxt("input.txt")

    for i in data:
        for j in data: 
            for k in data: 
                if(i + j + k == 2020):
                    print(i * j * k)
                    return

if __name__ == "__main__":
    main()
