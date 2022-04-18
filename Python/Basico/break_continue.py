def run():
    for i in range(10000):
        print(i)
        if i == 5678:
            break

def run2():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)

if __name__ == '__main__':
   #  run()
    run2()