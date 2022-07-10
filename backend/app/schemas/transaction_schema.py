transaction_schema = {
    "type": "object",
    "properties": {
        "valor": {"type": "number", "multipleOf": 0.01},
    },
    "required": ["valor"],
}
