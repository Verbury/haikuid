from secrets import randbelow

class HaikuID:
    _adjectives = [
        'aged', 'ancient', 'assorted', 'autumn', 'besmirched', 'billowing',
        'bitter', 'black', 'blue', 'bold', 'broad', 'broken', 'cold',
        'comical', 'cool', 'crimson', 'cryptic', 'curious', 'curly',
        'damp', 'dark', 'dawn', 'delicate', 'divine', 'dry', 'empowered',
        'empty', 'enlightening', 'enormous', 'falling', 'fancy',
        'firey', 'fizzy', 'floral', 'forgiving', 'fragrant', 'frosty',
        'gentle', 'gleaming', 'green', 'hidden', 'holy', 'icy',
        'impressive', 'ingenious', 'joyous', 'late', 'lingering', 'little',
        'lively', 'long', 'majestic', 'meandering', 'misty', 'moonlit',
        'morning', 'muddy', 'musing', 'mysterious', 'nameless', 'numerous',
        'old', 'onerous', 'patient', 'placid', 'pleasant', 'polished',
        'powerfull', 'pristine', 'profound', 'proud', 'purple',
        'questionable', 'quiet', 'radiant', 'rapid', 'raspy', 'red',
        'relaxed', 'restless', 'rough', 'shackled', 'shy', 'silent',
        'small', 'smoky', 'snowy', 'solitary', 'sparkling', 'spicy',
        'spring', 'sticky', 'still', 'summer', 'tempting', 'thrumming',
        'tidy', 'tiny', 'transparent', 'twilight', 'valuable', 'visible',
        'vivid', 'wandering', 'warm', 'weathered', 'white', 'wild', 'winter',
        'wispy', 'withered', 'yellow', 'young',
    ]
    _num_adjectives = len(_adjectives)

    _nouns = [
        'art', 'artwork', 'bay', 'beach', 'bird', 'boat', 'bonus', 'breeze',
        'brook', 'bush', 'butterfly', 'cabin', 'canal', 'cavern', 'cellar',
        'chalice', 'chamber', 'cherry', 'clock', 'cloud', 'coast', 'coffee',
        'constellation', 'cove', 'darkness', 'dawn', 'desert', 'dew',
        'door', 'dragon', 'dragonfly', 'dream', 'drift', 'dust', 'engine',
        'feather', 'field', 'fire', 'firefly', 'fireworks', 'flock',
        'flower', 'flute', 'fog', 'forest', 'frog', 'frost', 'glacier',
        'glade', 'glitter', 'grass', 'gull', 'hall', 'harbour', 'haze',
        'hill', 'kayak', 'lab', 'lake', 'lamp', 'leaf', 'lock', 'log',
        'math', 'meadow', 'moon', 'morning', 'mountain', 'murmation',
        'night', 'nomad', 'paper', 'pine', 'poetry', 'pond', 'port', 'rain',
        'range', 'resonance', 'river', 'rocket', 'saber', 'salad',
        'scene', 'sculpture', 'sea', 'shadow', 'shape', 'ship', 'silence',
        'sky', 'smoke', 'snow', 'snowflake', 'sound', 'star', 'storm', 'sun',
        'sunset', 'surf', 'sword', 'throne', 'thunder', 'tree', 'vase', 'violet',
        'voice', 'water', 'waterfall', 'wave', 'wildflower', 'wind', 'zephyr',
    ]
    _num_nouns = len(_nouns)

    _tokens = '0123456789abcdef'
    _num_tokens = len(_tokens)
    _token_length = 7

    _delimiter = "-"

    def generate(self):
        """
        Generate heroku like friendly ids
        in the noun-adjective-token form
        """
        adjective = self._adjectives[
            randbelow(self._num_adjectives)
        ]

        noun = self._nouns[
            randbelow(self._num_nouns)
        ]

        token = ''.join(self._tokens[randbelow(self._num_tokens)]
                        for _ in range(self._token_length))

        parts = [adjective, noun, token]

        return self._delimiter.join(filter(None, parts))
