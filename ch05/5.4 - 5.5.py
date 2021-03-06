letter = """    Dear {salutation} {name},

    Thank you for your letter. We are sorry that our {product} {verbed} in your 
{room}. Please note that it should never be used in a {room}, especially near any 
{animals}.

    Send us your receipt and {amount} for shipping and handling. We will send you
another {product} that, in our tests, is {percent}% less likely to have {verbed}.

    Thank you for your support.
    Sincerely,
    {spokesman}
    {job_title}"""

salutation = "salutation"
name = "name"
product = "product"
verbed = "verbed"
room = "room"
animals = "animals"
amount = "amount"
percent = "percent"
spokesman = "spokesman"
job_title = "job_title"

print(letter.format(salutation="salu", name="nm", product="pd", verbed="ver", room="rm",
                    animals="anima", amount="amou", percent="pc", spokesman="sm",
                    job_title="j_t"))
