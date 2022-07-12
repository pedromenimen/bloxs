from app.utils.utils import pattern_messages
from flask import jsonify
from jsonschema import ValidationError


def bad_request(error):
    description: ValidationError = error.description
    if type(description) != str:
        if description.validator == "pattern":
            field = description.path[0]
            return jsonify({"erro": pattern_messages[field]}), 400
        if description.validator == "required":
            return (
                jsonify(
                    {
                        "erro": "O campo "
                        + description.message.split("'")[1]
                        + " é obrigatório."
                    }
                ),
                400,
            )
        if description.validator == "type":
            field = description.path[0]
            correct_type = description.validator_value
            return (
                jsonify({"erro": f"O campo {field} deve ser do tipo {correct_type}."}),
                400,
            )
        if description.validator == "minLength":
            field = description.path[0]
            min_length = description.validator_value
            return (
                jsonify(
                    {
                        "erro": f"O tamanho do campo {field} é de no mínimo {min_length} caracteres."
                    }
                ),
                400,
            )
        if description.validator == "multipleOf":
            field = description.path[0]
            min_length = description.validator_value
            return (
                jsonify(
                    {
                        "erro": f"O campo {field} aceita apenas valores de 2 casas decimais."
                    }
                ),
                400,
            )
    else:
        return jsonify({"erro": "O corpo da requisição deve ser do formato json."}), 400
