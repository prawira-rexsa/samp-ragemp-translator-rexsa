import keyboard
import pyperclip
from deep_translator import GoogleTranslator, exceptions
import sys
import time
import re
import os

class SimpleTranslator:
    def __init__(self):
        self.running = True
        self.source_lang = 'id'  # Default: Indonesia
        self.target_lang = 'en'  # Default: Inggris
        self.load_settings()
        
    def load_settings(self):
        """Memuat pengaturan dari file jika ada"""
        try:
            if os.path.exists('translator_settings.txt'):
                with open('translator_settings.txt', 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if 'source=' in line:
                            self.source_lang = line.split('=')[1].strip()
                        elif 'target=' in line:
                            self.target_lang = line.split('=')[1].strip()
        except:
            pass
    
    def save_settings(self):
        """Menyimpan pengaturan ke file"""
        try:
            with open('translator_settings.txt', 'w') as f:
                f.write(f"source={self.source_lang}\n")
                f.write(f"target={self.target_lang}\n")
        except:
            pass
    
    def show_main_menu(self):
        """Menampilkan menu utama"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔════════════════════════════════════════╗")
        print("║      SAMP TRANSLATOR - PRAWIRA REXSA   ║")
        print("╚════════════════════════════════════════╝")
        print()
        print("╔════════════════════════════════════════╗")
        print("║              MENU UTAMA                ║")
        print("╠════════════════════════════════════════╣")
        print("║ [1] ║ Pengaturan Terjemahan            ║")
        print("║ [2] ║ Jalankan Bot Terjemahan          ║")
        print("║ [3] ║ Keluar                           ║")
        print("╚════════════════════════════════════════╝")
        print()
    
    def show_translation_settings(self):
        """Menampilkan pengaturan terjemahan"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔════════════════════════════════════════╗")
        print("║        PENGATURAN TERJEMAHAN           ║")
        print("╚════════════════════════════════════════╝")
        # print()
        print("╔════════════════════════════════════════╗")
        print("║          DAFTAR BAHASA                 ║")
        print("╠════════════════════════════════════════╣")
        print("║ Kode  ║ Bahasa                         ║")
        print("╠════════════════════════════════════════╣")
        print("║  id   ║ Indonesia                      ║")
        print("║  en   ║ Inggris                        ║")
        print("║  ar   ║ Arab                           ║")
        print("║  zh   ║ Mandarin                       ║")
        print("║  ko   ║ Korea                          ║")
        print("║  ja   ║ Jepang                         ║")
        print("║  es   ║ Spanyol                        ║")
        print("║  fr   ║ Prancis                        ║")
        print("║  de   ║ Jerman                         ║")
        print("║  pt   ║ Portugis                       ║")
        print("║  ru   ║ Rusia                          ║")
        print("║  nl   ║ Belanda                        ║")
        print("║  it   ║ Italia                         ║")
        print("║  tr   ║ Turki                          ║")
        print("║  vi   ║ Vietnam                        ║")
        print("║  th   ║ Thailand                       ║")
        print("╚════════════════════════════════════════╝")
        print()
        print(f"Bahasa Sumber Saat Ini: {self.get_language_name(self.source_lang)} ({self.source_lang})")
        print(f"Bahasa Target Saat Ini: {self.get_language_name(self.target_lang)} ({self.target_lang})")
        print()
        print("[1] Change source language")
        print("[2] Change source target")
        print("[3] Return menu page")
        print()
        
        choice = input("Pilih menu [1-3]: ").strip()
        
        if choice == '1':
            self.change_source_language()
        elif choice == '2':
            self.change_target_language()
        elif choice == '3':
            return
    
    def get_language_name(self, lang_code):
        """Mengembalikan nama bahasa dari kode"""
        language_names = {
            'id': 'Indonesia',
            'en': 'Inggris',
            'jw': 'Jawa',
            'su': 'Sunda',
            'ms': 'Melayu',
            'ar': 'Arab',
            'zh': 'Mandarin',
            'ko': 'Korea',
            'ja': 'Jepang',
            'es': 'Spanyol',
            'fr': 'Prancis',
            'de': 'Jerman',
            'pt': 'Portugis',
            'ru': 'Rusia',
            'nl': 'Belanda',
            'it': 'Italia',
            'tr': 'Turki',
            'vi': 'Vietnam',
            'th': 'Thailand'
        }
        return language_names.get(lang_code, f"Tidak Diketahui ({lang_code})")
    
    def change_source_language(self):
        """Mengubah bahasa sumber"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔════════════════════════════════════════╗")
        print("║          UBAH BAHASA SUMBER            ║")
        print("╚════════════════════════════════════════╝")
        print()
        print(f"Bahasa Sumber Saat Ini: {self.get_language_name(self.source_lang)}")
        print()
        print("Masukkan kode bahasa (contoh: id, en, jw, dll):")
        print("Tekan Enter saja untuk membatalkan")
        
        new_lang = input("\nKode bahasa baru: ").strip().lower()
        
        if new_lang:
            if len(new_lang) == 2:
                self.source_lang = new_lang
                self.save_settings()
                print(f"\n Bahasa sumber berhasil diubah ke: {self.get_language_name(self.source_lang)}")
            else:
                print("\nKode bahasa harus 2 karakter!")
            
            input("\nTekan Enter untuk melanjutkan...")
    
    def change_target_language(self):
        """Mengubah bahasa target"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔════════════════════════════════════════╗")
        print("║          UBAH BAHASA TARGET            ║")
        print("╚════════════════════════════════════════╝")
        print()
        print(f"Bahasa Target Saat Ini: {self.get_language_name(self.target_lang)}")
        print()
        print("Masukkan kode bahasa (contoh: id, en, jw, dll):")
        print("Tekan Enter saja untuk membatalkan")
        
        new_lang = input("\nKode bahasa baru: ").strip().lower()
        
        if new_lang:
            if len(new_lang) == 2:
                self.target_lang = new_lang
                self.save_settings()
                print(f"\nBahasa target berhasil diubah ke: {self.get_language_name(self.target_lang)}")
            else:
                print("\nKode bahasa harus 2 karakter!")
            
            input("\nTekan Enter untuk melanjutkan...")
    
    def show_running_info(self):
        """Menampilkan informasi saat bot berjalan"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("╔════════════════════════════════════════╗")
        print("║        SAMP TRANSLATOR RUNNING         ║")
        print("╚════════════════════════════════════════╝")
        print()
        print(f"Terjemahan: {self.get_language_name(self.source_lang)} → {self.get_language_name(self.target_lang)}")
        print()
        print("CARA PENGGUNAAN:")
        print("1. Pilih teks (Ctrl+A atau highlight manual)")
        print("2. Tekan F9 untuk menerjemahkan")
        print("3. Teks akan langsung diganti dengan terjemahan")
        print("4. Tekan Ctrl+Alt+X untuk kembali ke menu")
        print()
        print("-" * 40)
        print("Menunggu input... (F9 untuk translate)")
    
    def force_present_tense(self, text):
        # Hanya terapkan untuk terjemahan ke Inggris
        if self.target_lang != 'en':
            return text
            
        words = text.split()
        if not words:
            return text
        
        clear_past_indicators = ['yesterday', 'last', 'ago', 'before', 'earlier', 'previously']
        
        has_clear_past = any(indicator in text.lower() for indicator in clear_past_indicators)
        
        if has_clear_past:
            return text
        
        text = re.sub(r'\bwas\b', 'is', text)
        text = re.sub(r'\bwere\b', 'are', text)
        
        verb_conversions = {
            'opened': 'opens',
            'grabbed': 'grabs',
            'took': 'takes',
            'saw': 'sees',
            'did': 'does',
            'went': 'goes',
            'came': 'comes',
            'gave': 'gives',
            'had': 'has',
            'knew': 'knows',
            'thought': 'thinks',
            'said': 'says',
            'found': 'finds',
            'made': 'makes',
            'used': 'uses',
            'called': 'calls',
            'tried': 'tries',
            'asked': 'asks',
            'needed': 'needs',
            'felt': 'feels',
            'became': 'becomes',
            'left': 'leaves',
            'put': 'puts',
            'meant': 'means',
            'kept': 'keeps',
            'let': 'lets',
            'began': 'begins',
            'showed': 'shows',
            'heard': 'hears',
            'ran': 'runs',
            'moved': 'moves',
            'liked': 'likes',
            'lived': 'lives',
            'believed': 'believes',
            'held': 'holds',
            'brought': 'brings',
            'happened': 'happens',
            'wrote': 'writes',
            'sat': 'sits',
            'stood': 'stands',
            'lost': 'loses',
            'paid': 'pays',
            'met': 'meets',
            'included': 'includes',
            'continued': 'continues',
            'set': 'sets',
            'learned': 'learns',
            'changed': 'changes',
            'led': 'leads',
            'understood': 'understands',
            'watched': 'watches',
            'followed': 'follows',
            'stopped': 'stops',
            'created': 'creates',
            'spoke': 'speaks',
            'spent': 'spends',
            'grew': 'grows',
            'died': 'dies',
            'sent': 'sends',
            'built': 'builds',
            'stayed': 'stays',
            'fell': 'falls',
            'cut': 'cuts',
            'reached': 'reaches',
            'killed': 'kills',
            'remained': 'remains',
            'suggested': 'suggests',
            'raised': 'raises',
            'passed': 'passes',
            'sold': 'sells',
            'decided': 'decides',
            'returned': 'returns',
            'explained': 'explains',
            'hoped': 'hopes',
            'developed': 'develops',
            'carried': 'carries',
            'broke': 'breaks',
            'received': 'receives',
            'agreed': 'agrees',
            'supported': 'supports',
            'hit': 'hits',
            'produced': 'produces',
            'ate': 'eats',
            'covered': 'covers',
            'caught': 'catches',
            'drew': 'draws',
            'chose': 'chooses'
        }
        
        words = text.split()
        for i, word in enumerate(words):
            lower_word = word.lower()
            if lower_word in verb_conversions:
                if word[0].isupper():
                    words[i] = verb_conversions[lower_word].capitalize()
                else:
                    words[i] = verb_conversions[lower_word]
        
        text = ' '.join(words)
        
        def convert_regular_verb(match):
            verb = match.group(0)
            base_form = verb[:-2] if verb.endswith('ed') else verb[:-1]
            
            if base_form.endswith(('ch', 'sh', 'ss', 'x', 'z', 'o')):
                return base_form + 'es'
            elif base_form.endswith('y') and len(base_form) > 1 and base_form[-2] not in 'aeiou':
                return base_form[:-1] + 'ies'
            else:
                return base_form + 's'
        
        text = re.sub(r'\b\w+ed\b', convert_regular_verb, text)
        
        return text
    
    def correct_grammar_for_me(self, text):
        # Hanya terapkan untuk terjemahan ke Inggris
        if self.target_lang != 'en':
            return text
            
        if not text.startswith('/me '):
            return text
        
        action_text = text[4:].strip()
        
        action_text = self.force_present_tense(action_text)
        
        words = action_text.split()
        if words and words[0].endswith('ing'):
            if len(words) > 1 and words[0] not in ['is', 'am', 'are', 'was', 'were']:
                action_text = 'is ' + action_text
        
        passive_keywords = ['killed', 'shot', 'hit', 'arrested', 'caught', 'beaten', 'taken']
        for i, word in enumerate(words):
            if word in passive_keywords and i > 0:
                prev_word = words[i-1].lower()
                if prev_word not in ['is', 'am', 'are', 'was', 'were', 'be', 'been']:
                    action_text = action_text.replace(word, 'is ' + word, 1)
                    break
        
        return '/me ' + action_text
    
    def safe_translate(self, text):
        try:
            translator = GoogleTranslator(source=self.source_lang, target=self.target_lang)
            translated = translator.translate(text)
            
            if not translated or translated.strip() == '':
                print("Hasil terjemahan kosong, menggunakan teks asli")
                return text
            
            # Hanya terapkan koreksi grammar untuk terjemahan ke Inggris
            if self.target_lang == 'en':
                if translated.startswith('/me'):
                    translated = self.correct_grammar_for_me(translated)
                else:
                    translated = self.force_present_tense(translated)
            
            return translated
            
        except exceptions.TranslationNotFound:
            print("Terjemahan tidak ditemukan, menggunakan teks asli")
            return text
        except Exception as e:
            print(f"Error saat menerjemahkan: {e}, menggunakan teks asli")
            return text
    
    def translate_selected(self):
        try:
            original_clipboard = pyperclip.paste()
            
            keyboard.press_and_release('ctrl+c')
            time.sleep(0.15)
            
            selected_text = pyperclip.paste()
            
            pyperclip.copy(original_clipboard)
            
            if not selected_text or selected_text.strip() == '':
                print("Tidak ada teks yang terpilih atau teks kosong!")
                return
            
            if selected_text == original_clipboard:
                print("Tidak ada teks baru yang dipilih!")
                return
            
            display_text = selected_text[:100] + "..." if len(selected_text) > 100 else selected_text
            print(f"Teks terpilih: {display_text}")
            
            translated = self.safe_translate(selected_text)
            
            keyboard.write(translated)
            
            display_translated = translated[:100] + "..." if len(translated) > 100 else translated
            print(f"Teks diganti dengan: {display_translated}")
            print("-" * 40)
                
        except Exception as e:
            print(f"Error: {type(e).__name__}: {e}")
    
    def run_translation_bot(self):
        """Menjalankan bot terjemahan"""
        self.show_running_info()
        
        # Hapus semua hotkey sebelumnya
        keyboard.unhook_all()
        
        # Tambah hotkey baru
        keyboard.add_hotkey('f9', self.translate_selected)
        keyboard.add_hotkey('ctrl+alt+x', lambda: self.stop_translation_bot())
        
        # Tunggu sampai pengguna menekan Ctrl+Alt+X
        keyboard.wait('ctrl+alt+x')
    
    def stop_translation_bot(self):
        """Menghentikan bot terjemahan"""
        keyboard.unhook_all()
        print("\nBot terjemahan dihentikan. Kembali ke menu utama...")
        time.sleep(2)
    
    def run(self):
        """Menjalankan menu utama"""
        while self.running:
            self.show_main_menu()
            
            choice = input("Pilih menu [1-3]: ").strip()
            
            if choice == '1':
                self.show_translation_settings()
            elif choice == '2':
                self.run_translation_bot()
            elif choice == '3':
                print("\nTerima kasih telah menggunakan SAMP Translator!")
                self.running = False
                sys.exit(0)
            else:
                print("\nPilihan tidak valid! Silakan coba lagi.")
                time.sleep(1)

if __name__ == "__main__":
    translator = SimpleTranslator()
    translator.run()