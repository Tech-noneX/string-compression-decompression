

class DeCompression:


    def __init__(self, input_string):
        self.input_string = input_string

    
    def initialize(self):
        if self.input_string[0].isdigit():
            return self.decompression(self.input_string)
        elif self.input_string[0].isalpha():
            return self.compression(self.input_string)
        else:
            return "Invalid input"


    def compression(self, compress):
        result = []
        seq = ''
        seq += compress[0]
        for i in compress[1:]:
            if i != seq[-1]:
                seq += ' '
            seq += i
        seq = seq.split()
        for i in seq:
            result.append(str(len(i)) + i[0])
        return ''.join(result)


    def decompression(self, decompress):
        result = []
        seq = ''
        for i in decompress:
            if i.isdigit():
                seq += i
            else:
                seq += ' ' + i + ' '
        seq = seq.split()
        while seq:
            seq1 = seq[:2]
            result.append(int(seq1[0]) * seq1[1])
            seq = seq[2:]
        return ''.join(result)

user_input = input("Enter seq of letters example:'aabbcc'"
                   " or number followed by letter example:'4a2b5n'\n:"
                   ).strip()
dc = DeCompression(input_string=user_input)
print(dc.initialize())
