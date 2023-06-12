import musical_microservice.modules.musical_parameters as musical_parameters
import musical_microservice.services.generated.musical_server_pb2 as pb


def convert_form_pb_to_model(form: pb.MusicalForm) -> musical_parameters.MusicalForm:
    return musical_parameters.MusicalForm(form)


def convert_tempo_model_to_pb(tempo: musical_parameters.Tempo) -> pb.Tempo:
    return pb.Tempo(beats_per_min=tempo.beats_per_min, marking=tempo.marking)


def convert_time_signature_model_to_pb(
    time_signature: musical_parameters.TimeSignature,
) -> pb.TimeSignature:
    return pb.TimeSignature(
        beats_per_measure=time_signature.beats_per_measure,
        beat_value=time_signature.beat_value,
    )


def convert_musical_parameters_model_to_pb(
    parameters: musical_parameters.ParameterAnnotation,
) -> pb.MusicalParameters:
    pb_tempo = convert_tempo_model_to_pb(parameters.tempo)
    pb_time_signature = convert_time_signature_model_to_pb(parameters.time_signature)
    return pb.MusicalParameters(time_signature=pb_time_signature, tempo=pb_tempo)
