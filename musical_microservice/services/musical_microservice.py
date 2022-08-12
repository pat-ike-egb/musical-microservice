import grpc

from generated.musical_server_pb2 import (
    MusicalParameters,
    TimeSignature,
    Tempo,
    GenerateMusicalFormParametersRequest,
    GenerateMusicalFormParametersResponse,
    MusicalForm,
    SCHERZO,
    WALTZ,
    MINUET
)

import generated.musical_server_pb2_grpc

class MusicalService(generated.musical_server_pb2_grpc.MusicalServer):
    def __init__(self, musical_parameter_processor):
        self.musical_parameter_processer = musical_parameter_processor

    def GenerateMusicalFormParameters(self, request, context):
        parameters = MusicalParameters(
            tempo=Tempo(beats_per_min=120),
            time_signature=(4, 4)
        )

        return GenerateMusicalFormParametersResponse(parameters)
