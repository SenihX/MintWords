import random
import string


# MintWords Programı - Coder By SenihX

class MintWords:
    def __init__(self):
        self.default_charset = string.ascii_letters + string.digits + string.punctuation

    def generate_custom_wordlist(self, ad, yil, kelimeler, num_words=100):
        base_list = []

        # Ad ve takma ad kombinasyonları
        if ad:
            base_list.append(ad.lower())
            base_list.append(ad.upper())
            base_list.append(ad.capitalize())
        # Doğum yılı ile kombinasyonlar
        if yil:
            base_list.append(str(yil))
            if ad:
                base_list.append(f"{ad}{yil}")
                base_list.append(f"{yil}{ad}")
        # Özel anahtar kelimelerle kombinasyonlar
        if kelimeler:
            for kelime in kelimeler:
                base_list.append(kelime)
                base_list.append(kelime.lower())
                base_list.append(kelime.upper())
                if yil:
                    base_list.append(f"{kelime}{yil}")
                    base_list.append(f"{yil}{kelime}")

        # Rastgele ek kelimeler oluştur
        while len(base_list) < num_words:
            word = ''.join(random.choices(self.default_charset, k=random.randint(6, 12)))
            base_list.append(word)

        return list(set(base_list))  # Benzersiz kelimeler

    def generate_random_wordlist(self, charset, length=8, num_words=100, special_keywords=None):
        special_keywords = special_keywords or []
        wordlist = []

        # Özel kelimeleri ekle
        wordlist.extend(special_keywords)

        # Rastgele kelimeler oluştur
        for _ in range(num_words - len(special_keywords)):
            word = ''.join(random.choices(charset, k=length))
            wordlist.append(word)

        return wordlist

    def save_wordlist(self, filename, wordlist):
        with open(filename, 'w') as f:
            for word in wordlist:
                f.write(word + '\n')
        print(f"Wordlist başarıyla kaydedildi: {filename}\nSenihX tarafından tasarlandı!")


def select_language():
    languages = {
        "1": "Türkçe",
        "2": "Русский",
        "3": "English"
    }

    print("Lütfen dilinizi seçin / Пожалуйста, выберите ваш язык / Please select your language:")
    for key, value in languages.items():
        print(f"{key} - {value}")

    choice = input("Seçiminizi yapın: ")
    return languages.get(choice, "Türkçe")


def display_message(language, key):
    messages = {
        "Türkçe": {
            "welcome": "MintWords'e Hoş Geldiniz - Mr.SenihX tarafından tasarlandı!",
            "menu": "Seçenekler:\n1 - Kişiye özel wordlist oluştur\n2 - Rastgele wordlist oluştur\nSeçiminizi yapın: ",
            "ad_prompt": "Ad veya takma ad girin: ",
            "yil_prompt": "Doğum yılınızı girin (ör. 1990): ",
            "kelimeler_prompt": "Anahtar kelimeleri aralarına virgül koyarak girin ve arada boşluk bırakmayın (ör. araba,bilgisayar): ",
            "num_words_prompt": "Wordlist toplam kaç kelime içersin (varsayılan 100): ",
            "filename_prompt": "Wordlist dosyasının adını girin (varsayılan: mintwords.txt): ",
            "length_prompt": "Rastgele kelimelerin uzunluğunu girin (varsayılan 8): ",
            "charset_prompt": "Kullanılacak karakter kümesini seçin:\n1 - Harfler ve rakamlar\n2 - Harfler, rakamlar ve özel karakterler\nSeçiminizi yapın: ",
            "special_keywords_prompt": "Eklemek istediğiniz özel kelimeleri girin (virgülle ayırın): ",
            "success": "Wordlist başarıyla kaydedildi: {filename}"
        },
        "Русский": {
            "welcome": "Добро пожаловать в MintWords - Создано Mr.SenihX!",
            "menu": "Опции:\n1 - Создать персонализированный список\n2 - Создать случайный список\nВаш выбор: ",
            "ad_prompt": "Введите имя или псевдоним: ",
            "yil_prompt": "Введите ваш год рождения (например, 1990): ",
            "kelimeler_prompt": "Введите ключевые слова через запятую (например, машина,компьютер): ",
            "num_words_prompt": "Сколько слов должно быть в списке (по умолчанию 100): ",
            "filename_prompt": "Введите имя файла для списка (по умолчанию: mintwords.txt): ",
            "length_prompt": "Введите длину случайных слов (по умолчанию 8): ",
            "charset_prompt": "Выберите набор символов:\n1 - Буквы и цифры\n2 - Буквы, цифры и специальные символы\nВаш выбор: ",
            "special_keywords_prompt": "Введите дополнительные ключевые слова (разделенные запятыми): ",
            "success": "Список успешно сохранен: {filename}"
        },
        "English": {
            "welcome": "Welcome to MintWords - Designed by Mr.SenihX!",
            "menu": "Options:\n1 - Create personalized wordlist\n2 - Create random wordlist\nYour choice: ",
            "ad_prompt": "Enter your name or nickname: ",
            "yil_prompt": "Enter your birth year (e.g., 1990): ",
            "kelimeler_prompt": "Enter keywords separated by commas (e.g., car,computer): ",
            "num_words_prompt": "How many words should the wordlist contain (default 100): ",
            "filename_prompt": "Enter the name of the output file (default: mintwords.txt): ",
            "length_prompt": "Enter the length of random words (default 8): ",
            "charset_prompt": "Select character set:\n1 - Letters and numbers\n2 - Letters, numbers, and special characters\nYour choice: ",
            "special_keywords_prompt": "Enter additional keywords (separated by commas): ",
            "success": "Wordlist successfully saved: {filename}"
        }
    }
    return messages.get(language, messages["Türkçe"])[key]


if __name__ == "__main__":
    language = select_language()
    print(display_message(language, "welcome"))

    option = input(display_message(language, "menu"))

    wordlist_creator = MintWords()
    filename = input(display_message(language, "filename_prompt")) or "mintwords.txt"

    if option == "1":  # Kişiye özel wordlist
        ad = input(display_message(language, "ad_prompt"))
        yil = input(display_message(language, "yil_prompt"))
        kelimeler = input(display_message(language, "kelimeler_prompt")).split(",") if input else []
        num_words = input(display_message(language, "num_words_prompt"))
        num_words = int(num_words) if num_words.isdigit() else 100

        wordlist = wordlist_creator.generate_custom_wordlist(ad, yil, kelimeler, num_words)
    elif option == "2":  # Rastgele wordlist
        charset_choice = input(display_message(language, "charset_prompt"))
        charset = string.ascii_letters + string.digits if charset_choice == "1" else string.ascii_letters + string.digits + string.punctuation
        length = input(display_message(language, "length_prompt"))
        length = int(length) if length.isdigit() else 8
        num_words = input(display_message(language, "num_words_prompt"))
        num_words = int(num_words) if num_words.isdigit() else 100
        special_keywords = input(display_message(language, "special_keywords_prompt")).split(",") if input else []

        wordlist = wordlist_creator.generate_random_wordlist(charset, length, num_words, special_keywords)
    else:
        print("Geçersiz seçenek. Program sonlandırılıyor.")
        exit()

    wordlist_creator.save_wordlist(filename, wordlist)
