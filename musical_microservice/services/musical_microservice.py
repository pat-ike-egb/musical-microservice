import grpc

import musical_microservice.models.util
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

from musical_microservice.business.music_parameter_processor import  MusicParameterProcessor

import generated.musical_server_pb2_grpc

class MusicalService(generated.musical_server_pb2_grpc.MusicalServerServicer):
    def __init__(self, musical_parameter_processor):
        super(MusicalService, self).__init__()
        self.musical_parameter_processer : MusicParameterProcessor = musical_parameter_processor

    def GenerateMusicalFormParameters(self, request : GenerateMusicalFormParametersRequest, context):
        parameters = self.musical_parameter_processer.generate_musical_parameters(
         musical_microservice.models.util.convert_form_pb_to_model(request.form)
        )

        return GenerateMusicalFormParametersResponse(
            musical_microservice.models.util.convert_musical_parameters_model_to_pb(parameters)
        )
