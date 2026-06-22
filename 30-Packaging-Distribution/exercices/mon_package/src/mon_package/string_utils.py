def inverser(s):
    return s[::-1]

def compter_mots(texte):
    return len(texte.split())

def est_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
