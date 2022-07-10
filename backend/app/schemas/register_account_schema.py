register_account_schema = {
    "type": "object",
    "properties": {
        "limiteSaqueDiario": {"type": "number"},
        "tipoConta": {
            "type": "string",
            "pattern": "(001)|(002)|(003)|(006)|(007)|(013)|(022)|(028)|(043)",
        },
    },
    "required": ["tipoConta", "limiteSaqueDiario"],
}
