from collections.abc import Collection, Iterator
from typing import Any

import music21 as m21
from modules.data_structures.tree import TreeNode, TreeOperations


class Owned:
    def __init__(self) -> None:
        self.owner = None

    def set_owner(self, owner: Any):
        self.owner = owner


lowest = m21.pitch.Pitch("A0")
highest = m21.pitch.Pitch("C8")


# TODO: Melodies/Motifs can have a pitch-range as well
class PitchRange(Owned):
    # TODO: eventually will need to figure out how to incorporate
    #  dynamic capabilities within a range
    def __init__(self, low: m21.pitch.Pitch | None, high: m21.pitch.Pitch | None):
        super().__init__()

        if not low:
            low = lowest

        if not high:
            high = highest

        assert lowest <= low <= high <= highest
        self.low = low
        self.high = high

        self.pitch_line = (
            ["|"]
            + [" " for _i in range(self.low.midi)]
            + [self.low.nameWithOctave]
            + ["-" for _i in range(self.low.midi + 1, self.high.midi)]
            + [self.high.nameWithOctave]
            + [" " for _i in range(self.high.midi + 1, highest.midi)]
            + ["|"]
        )

    def __eq__(self, other: "PitchRange"):
        return self.low == other.low and self.high == other.high

    def __lt__(self, other: "PitchRange"):
        return self.low < other.low or (
            self.low == other.low and self.high < other.high
        )

    def __le__(self, other: "PitchRange"):
        return self.__eq__(other) or self.__lt__(other)

    # TODO: implement (for subrange as well as individual notes)
    def contains(self, other: "PitchRange"):
        pass

    def __str__(self):
        return "".join(self.pitch_line)


class Tuned(Owned):
    def __init__(self, pitch_range: PitchRange) -> None:
        super().__init__()
        self.pitch_range: PitchRange = pitch_range
        self.pitch_range.set_owner(self)

    def __eq__(self, other: "Tuned"):
        return self.pitch_range == other.pitch_range

    def __lt__(self, other: "Tuned"):
        return self.pitch_range < other.pitch_range

    def __le__(self, other: "Tuned"):
        return self.__eq__(other) or self.__lt__(other)


class Articulation(Tuned):
    def __init__(self, name: str, pitch_range: PitchRange):
        super().__init__()
        self.name = name

        self.characteristics = None

    def __str__(self):
        return f"{str(self.pitch_range)} [ {self.name} ]"


class TunedNode(TreeNode):
    def __init__(self, tuned: Tuned) -> None:
        super().__init__(tuned.pitch_range)
        self.max = tuned.pitch_range.high
        self.objects: list[Tuned] = [tuned]


class Roll(Collection[Tuned]):
    def __init__(self) -> None:
        self.root: TunedNode | None = None
        self.pitch = None

    def __len__(self) -> int:
        pass

    def __iter__(self) -> Iterator[Tuned]:
        pass

    def __contains__(self, __x: object) -> bool:
        pass

    def insert(self, tuned_object: Tuned):
        node = TunedNode(tuned_object)
        if not self.root:
            self.root = node
        else:
            self.root = TreeOperations.insert(self.root, node)

    # i.e. a Piano roll, for an instrument, which stores a set of pitch ranges.
    # The absolute lowest and absolute highest pitches within
    # the set of PitchRanges defines the overall range of the Roll
    # Todo: overlapping tuple algorithms for processing playable lines
    # Todo: what is the best data structure for a roll, given a set of articulations,
    #  and pitch ranges


class Instrument(Tuned):
    def __init__(
        self,
        name: str,
        pitch_range: PitchRange,
        transposition: m21.interval.GenericInterval = m21.interval.GenericInterval(
            "Unison"
        ),
    ) -> None:
        super().__init__(pitch_range)
        self.name = name

        self.articulations: Roll[Articulation] = Roll()
        self.transposition: m21.interval.GenericInterval = transposition

    def add_articulation(self, articulation: Articulation):
        articulation.set_owner(self)
        self.articulations.insert(articulation)
