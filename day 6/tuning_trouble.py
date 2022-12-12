# PART A and B: Find start index of set of unique chars 

class SignalProcessor:

    packet_marker_length = 4
    message_marker_length = 14

    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self.signal = list(f.read().strip())
    
    def start_of_packet(self) -> int:
        return self.convolve(0, self.packet_marker_length)
    
    def start_of_message(self) -> int:
        a = self.start_of_packet()
        return self.convolve(a, self.message_marker_length)

    def convolve(self, start: int, kernel_length: int) -> int:
        kernel = self.signal[start:start+kernel_length]
        if len(set(kernel)) == kernel_length:
            return start + kernel_length + 1
        for i, letter in enumerate(self.signal[start + kernel_length:]):
            kernel.pop(0)
            kernel.append(letter)
            if len(set(kernel)) == kernel_length:
                return i + start + kernel_length + 1


if __name__ == "__main__":
    sp = SignalProcessor('day 6/input.txt')
    print(sp.start_of_packet())
    print(sp.start_of_message())