

class DeCompression:


    def __init__(self, input_string):
        self.input_string = input_string

    
    def initialize(self):
        if self.input_string[0].isdigit():
            pass
        elif self.input_string[0].isalpha():
            pass
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
