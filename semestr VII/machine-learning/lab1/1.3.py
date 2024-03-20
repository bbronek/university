def squares_of_positives_in_a_list(input_list):
    output_list = [x**2 for x in input_list if x > 0]

    return output_list

def main():
    input_list = [int(x) for x in input("Wprowadz liczby oddzielone spacjami: ").split()]

    print(f"Output list: {squares_of_positives_in_a_list(input_list)}")

if __name__ == "__main__":
    main()
