import music21 as m21


class MeasureTokenFeature(m21.features.FeatureExtractor):
    def __init__(self, dataOrStream=None, *arguments, **keywords):
        super().__init__(dataOrStream, *arguments, **keywords)

    def _process(self):
        # TODO: FifthsPitchHistogramFeature
        # TODO: HarmonicityOfTwoStrongestRhythmicPulsesFeature
        # TODO: ImportanceOfBassRegisterFeature
        # TODO: MelodicIntervalHistogramFeature
        # TODO: PitchClassDistributionFeature
        # TODO: PrimaryRegisterFeature
        # TODO: SizeOfMelodicArcsFeature
        pass
