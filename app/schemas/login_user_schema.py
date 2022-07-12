login_user_schema = {
    "type": "object",
    "properties": {
        "cpf": {
            "type": "string",
            "pattern": "[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}",
        },
        "password": {"type": "string", "minLength": 8},
    },
    "required": ["cpf", "password"],
}
