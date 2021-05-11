class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words.reverse()
        lines = []
        while words:
            line = []
            line_length = 0
            while words:
                if (len(''.join(line)) + len(words[-1]) + len(line) - 1) < maxWidth:
                    line.append(words.pop())
                else:
                    break
            lines.append(line)

        for line in range(len(lines)):
            spaces = maxWidth - len(''.join(lines[line]))
            sp = 0
            if line == len(lines) - 1:
                for word in range(len(lines[line]) - 1):
                    lines[line][word] += ' '
                line_spaces = maxWidth - len(''.join(lines[line]))
                lines[line][-1] += ' ' * line_spaces
            elif len(lines[line]) == 1:
                lines[line][0] += ' ' * spaces
            else:
                while sp < spaces:
                    lines[line][sp % (len(lines[line]) - 1)] += ' '
                    sp += 1

        for line in range(len(lines)):
            lines[line] = ''.join(lines[line])
        return lines
