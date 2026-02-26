import sys
import brute_module as bm
import validation_module as vm
import security_module as sm


def main():
    option = bm.show_menu()
    mode = bm.show_mode_menu()

    password = input("\nPasswort eingeben (6 Zeichen): ")

    if not vm.validate_password(password, option):
        print("Fehler: Passwort entspricht nicht der Regel!")
        sys.exit()

    charset, rule = bm.get_charset_and_rule(option)

    if mode == 1:
        print("\nStarte Plaintext-Brute-Force...")
        attempts, duration = bm.brute_force_plain(password, charset, rule)

    elif mode == 2:
        print("\nErzeuge Salt und Hash...")
        salt = sm.generate_salt()
        target_hash = sm.hash_password(password, salt)

        print("Starte Hash-Brute-Force...")
        attempts, duration = bm.brute_force_hash(target_hash, salt, charset, rule)

    else:
        print("Ungültiger Modus")
        return

    if duration is not None:
        print("\nPasswort gefunden!")
        print(f"Versuche: {attempts}")
        print(f"Zeit: {duration:.2f} Sekunden")
    else:
        print("Passwort nicht gefunden.")


if __name__ == "__main__":
    main()