import sys
import brute_module as bm
import validation_module as vm
import security_module as sm


def main():
    option = bm.show_menu()
    mode = bm.show_mode_menu()
    time_limit = bm.get_time_limit()

    password = input("\nPasswort eingeben (6 Zeichen): ")

    # Validierung
    if not vm.validate_password(password, option):
        print("Fehler: Passwort entspricht nicht der Regel!")
        sys.exit()

    charset, rule = bm.get_charset_and_rule(option)

    # Modus-Auswahl
    if mode == 1:
        print("\nStarte Plaintext-Brute-Force...")
        attempts, duration = bm.brute_force_plain(
            password,
            charset,
            rule,
            time_limit
        )

    elif mode == 2:
        print("\nErzeuge Salt und Hash...")
        salt = sm.generate_salt()
        target_hash = sm.hash_password(password, salt)

        print("Starte Hash-Brute-Force...")
        attempts, duration = bm.brute_force_hash(
            target_hash,
            salt,
            charset,
            rule,
            time_limit
        )

    else:
        print("Ungültiger Modus")
        return


    # Ergebnis
    if duration is not None:
        print("\nPasswort gefunden!")
        print(f"Versuche: {attempts}")
        print(f"Zeit: {duration:.2f} Sekunden")
    else:
        print("\nZeitlimit erreicht oder Passwort nicht gefunden.")


if __name__ == "__main__":
    main()