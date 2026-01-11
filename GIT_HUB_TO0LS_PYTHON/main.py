# main.py
from __future__ import annotations

from algorithms import (
    count_vowels,
    factorial,
    fibonacci,
    is_palindrome,
    sum_even_numbers,
)


def _read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Digite um número inteiro válido.")


def _read_int_list(prompt: str) -> list[int]:
    """
    Reads a list of integers from input like:
    1 2 3 4
    or
    1,2,3,4
    """
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Digite pelo menos um número.")
            continue

        raw = raw.replace(",", " ")
        parts = [p for p in raw.split() if p]

        try:
            return [int(p) for p in parts]
        except ValueError:
            print("Entrada inválida. Use apenas inteiros. Ex: 1 2 3 4")


def menu() -> None:
    while True:
        print("\n=== Desafio GitHub + Python (Simples) ===")
        print("1) Verificar palíndromo")
        print("2) Fatorial")
        print("3) Fibonacci (primeiros N termos)")
        print("4) Contar vogais")
        print("5) Somar números pares de uma lista")
        print("0) Sair")

        option = input("Escolha uma opção: ").strip()

        if option == "1":
            text = input("Digite um texto: ")
            print("É palíndromo?" , "Sim" if is_palindrome(text) else "Não")

        elif option == "2":
            n = _read_int("Digite um inteiro n (>=0): ")
            try:
                print(f"{n}! = {factorial(n)}")
            except ValueError as e:
                print("Erro:", e)

        elif option == "3":
            n = _read_int("Quantos termos? (>=0): ")
            try:
                seq = fibonacci(n)
                print("Fibonacci:", seq)
            except ValueError as e:
                print("Erro:", e)

        elif option == "4":
            text = input("Digite um texto: ")
            print("Quantidade de vogais:", count_vowels(text))

        elif option == "5":
            nums = _read_int_list("Digite inteiros (ex: 1 2 3 4): ")
            print("Soma dos pares:", sum_even_numbers(nums))

        elif option == "0":
            print("Saindo...")
            return

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
