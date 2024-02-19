#
# --- Modul mit den zwei Funktion: swap_case() und PriceCalculator()
# 
def swap_case(s):
    st = ""
    st1 = ""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0, len(s)): 
        st = str(s[i])
        if st in lowercase: st = st.upper()
        else: st = st.lower() 
        st1 = st1 + st           
    return st1

if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
#
# ------
#
def PriceCalculator(schrauben, muttern, unterlegscheiben):
    Schraube= 7
    Mutter= 4
    Unterlegscheibe= 2
    gesamt= schrauben*Schraube+muttern*Mutter+unterlegscheiben*Unterlegscheibe
    print(gesamt)

if __name__ == "__main__":
    eingaben = input("Bitte geben Sie Mengen für Schrauben, Muttern und Unterlegschauben an (durch Leerzeichen getrennt): ")
    liste = list(map(int, eingaben.split(" ")))
    PriceCalculator(liste[0], liste[1], liste[2])