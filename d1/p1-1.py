import numpy as np

def main():
    data = np.loadtxt("input.txt")

    for i in data:
        for j in data: 
            if(i + j == 2020):
                print(i * j)
                return

if __name__ == "__main__":
    main()
