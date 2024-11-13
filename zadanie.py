from openai import OpenAI

with open("artykul.txt", "r", encoding="utf8") as f:
    text = f.read()

client = OpenAI(
    api_key="TUTAJ KLUCZ (ZE WZGLEDOW BEZPIECZENSTWA NIE DODAJE GO PUBLICZNIE)")

print("Generowanie artykulu...")

artResponse = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": text + '\n\n\nPrzedstaw ten artykuł jako kod HTML, ale usuń z tekstu ```html. NIE DODAWAJ <body>. Podaj tylko to, co powinno się znaleźć POMIĘDZY tagami <body> i </body>. NIE ZAPISUJ TAGÓW <body>, <html> ani <head>. Określ, gdzie w tym artykule warto wstawić grafiki, w tych miejscach umieść tagi <img> z atrybutem src="image_placeholder.jpg". Dodaj atrybut alt do każdego obrazka z dokładnym promptem, który można użyć do wygenerowania grafiki. Umieść podpisy pod grafikami używając odpowiedniego tagu HTML. Pamiętaj, aby usunąć ```html.'
        }
    ]
)

art = artResponse.choices[0].message.content

with open("artykul.html", "w", encoding="utf-8") as f:
    f.write(art)

print("Artykul zostal wygenerowany pomyslnie!\n")

print("Generowanie szablonu...")

tempResponse = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": art + '\n\n\nWygeneruj szablon do podglądu tego artykułu. Zapisz go jako kod HTML, ale usuń z tekstu ```html. NIE DODAWAJ KONTENERA ".container". Sekcja <body> ma być pusta i gotowa na wklejenie artykułu. Użyj stylów CSS, które pozwolą na wizualizację artykułu po wklejeniu jego kodu do sekcji <body>. Pamiętaj, aby usunąć ```html.'
        }
    ]
)

with open("szablon.html", "w", encoding="utf-8") as f:
    f.write(tempResponse.choices[0].message.content)

print("Szablon zostal wygenerowany pomyslnie!")
input()
