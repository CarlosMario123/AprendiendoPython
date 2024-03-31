import hashlib

def identificar_tipo_hash(cadena):
    tipos_hash = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
    
    for tipo in tipos_hash:
        if len(cadena) == hashlib.new(tipo).digest_size * 2:
            return tipo
    return "Tipo de hash no identificado"

def identificar_salt(cadena):
    # Longitud típica de un salt (asumiendo que es 16 caracteres)
    longitud_salt = 16
    for i in range(len(cadena) - longitud_salt):
        if identificar_tipo_hash(cadena[i:]) != "Tipo de hash no identificado":
            return cadena[:i], cadena[i:]
    return "", cadena

def contar_saltos(salt):
    return salt.count('$')

cadena = input("Introduce la cadena a identificar el tipo de hash (con salt): ")
salt, hash_only = identificar_salt(cadena)
tipo_hash = identificar_tipo_hash(hash_only)

if salt:
    print("Salt:", salt)
    print("Número de saltos:", contar_saltos(salt))
print("Hash sin salt:", hash_only)
print("El tipo de hash de la cadena es:", tipo_hash)
