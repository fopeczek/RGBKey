from dataclasses import dataclass


@dataclass
class RGB:
    R: int
    G: int
    B: int

    @staticmethod
    def FromString(rgb_string: str):
        """rgb_string has a syntax 'RGB(R,G,B)'"""
        rgb_string = rgb_string.replace('RGB(', '').replace(')', '')
        R, G, B = rgb_string.split(',')
        return RGB(int(R), int(G), int(B))
