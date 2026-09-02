from collections import Counter

class Tree:

    def count_chars(self, text):
        letters = {'a', 'b', 'c', 'd', 'e'}
        char_count = Counter(text)
        return {letter: char_count.get(letter, 0) for letter in letters}

    def build_tree(self, frequency):
        nodes = []
        for letter, freq in frequency.items():
            if freq > 0:
                nodes.append({
                    'chars': letter,
                    'frequency': freq,
                    'left': None,
                    'right': None
                })

        if not nodes:
            return None

        while len(nodes) > 1:
            nodes.sort(key=lambda x: x['frequency'])
            n1 = nodes.pop(0)
            n2 = nodes.pop(0)

            new_node = {
                'chars': n1['chars'] + n2['chars'],
                'frequency': n1['frequency'] + n2['frequency'],
                'left': n1,
                'right': n2
            }

            nodes.append(new_node)

        return nodes[0]

    def extract_codes(self, tree):
        codes = {}

        def build_codes(node, path=""):
            if node["left"] is None and node["right"] is None:
                for letter in node["chars"]:
                    codes[letter] = path or "0"
                return

            if node["left"] is not None:
                build_codes(node["left"], path + "1")

            if node["right"] is not None:
                build_codes(node["right"], path + "0")

        build_codes(tree)
        return codes

    def encode(self, text, codes):
        return ''.join(codes[ch] for ch in text)

    def decode(self, bits, codes):
        reverse = {v: k for k, v in codes.items()}
        current = ""
        decoded = ""

        for b in bits:
            current += b
            if current in reverse:
                decoded += reverse[current]
                current = ""

        return decoded

if __name__ == "__main__":
    tree = Tree()

    print("Enter an initial text (only letters a, b, c, d, e):")
    base_text = input("Initial text: ").strip()

    if not base_text:
        print("Error: Text cannot be empty.")
        exit()

    freq = tree.count_chars(base_text)
    root = tree.build_tree(freq)
    codes = tree.extract_codes(root)

    print("\nGenerated Codes:")
    for k, v in codes.items():
        print(f"{k} : {v}")

    print("\nWhat do you want to do?")
    print("1) Encode a text to bits")
    print("2) Decode bits to text")

    choice = input("Choice (1 or 2): ").strip()

    if choice == "1":
        user_text = input("Enter text to encode: ").strip()

        if not all(ch in codes for ch in user_text):
            print("Error: Text contains invalid characters.")
            exit()

        encoded = tree.encode(user_text, codes)
        print("\nEncoded result:")
        print(encoded)

    elif choice == "2":
        user_bits = input("Enter bits to decode: ").strip()

        if not set(user_bits) <= {"0", "1"}:
            print("Error: Bits must contain only 0 and 1.")
            exit()

        decoded = tree.decode(user_bits, codes)
        print("\nDecoded result:")
        print(decoded)

    else:
        print("Invalid choice.")