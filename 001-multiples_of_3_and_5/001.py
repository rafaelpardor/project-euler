from datetime import datetime

def main():
    time_init = datetime.now()
    accum = 0
    for i in range(0,1000):
        if i % 3 == 0 or i % 5 == 0:
            accum = accum + i
    time_total = datetime.now() - time_init
    return accum, time_total


if __name__ == '__main__':
    find_sum = main()
    print(find_sum)

