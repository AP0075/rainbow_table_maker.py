import itertools

def generate(string,length):
    draft_perm = list(itertools.combinations(string,length))
    combinations = []
    for dft in draft_perm:
        permutations = list(itertools.permutations(dft))
        new_combinations = ["".join(p) for p in permutations]
        combinations.extend(new_combinations)
    return combinations

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def main():
	word = input("Enter the word: ")
	length = int(input("Enter the length of the password (length should not be learger than word) : "))
	passwd_lst = generate(word, length)
	shift = int(input("Enter the shift value: "))

	with open('rainbow_table.txt', 'w') as file:
		for passwd in passwd_lst:
			file.write(f"{passwd} : {encrypt(passwd,shift)} \n")

    with open('rainbow_table.txt', 'w') as file:
        for passwd in passwd_lst:
            file.write(f"{encrypt(passwd,shift)}\n")

	for passwd in passwd_lst:
		print(f"{passwd} : {encrypt(passwd,shift)}")

if __name__ == "__main__":
	main()