def main():
    for contador in range(1001):
        if contador % 2 != 0: #todos los numeros paren tienen de resto 0
            continue
        print(contador)


if __name__ == "__main__":
    main()