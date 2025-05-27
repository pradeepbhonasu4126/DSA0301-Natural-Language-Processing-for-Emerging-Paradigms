class PluralFSM:
    def __init__(self):
        self.states = ['start', 'ends_with_sibilant', 'ends_with_y', 'pluralized']
        self.current_state = 'start'

    def is_sibilant_ending(self, word):
        sibilant_endings = ('s', 'x', 'z', 'ch', 'sh')
        return word.endswith(sibilant_endings)

    def is_consonant_before_y(self, word):
        if len(word) < 2:
            return False
        return word[-1] == 'y' and word[-2].lower() not in 'aeiou'

    def pluralize(self, word):
        self.current_state = 'start'

        if self.is_sibilant_ending(word):
            self.current_state = 'ends_with_sibilant'
            plural = word + 'es'

        elif self.is_consonant_before_y(word):
            self.current_state = 'ends_with_y'
            plural = word[:-1] + 'ies'

        else:
            plural = word + 's'

        self.current_state = 'pluralized'
        return plural


# Example usage:
fsm = PluralFSM()

words = ['cat', 'dog', 'bus', 'box', 'buzz', 'church', 'brush', 'city', 'day']

for w in words:
    plural_form = fsm.pluralize(w)
    print(f"{w} -> {plural_form}")
