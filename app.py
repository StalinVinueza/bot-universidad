from src.moodle.login import MoodleClient


def main():
    moodle = MoodleClient()

    try:
        # Iniciar Playwright
        moodle.start()

        print("Abriendo Moodle...")

        # Iniciar sesión
        moodle.login()

        print("Verificando inicio de sesión...")

        # Verificar si el login fue exitoso
        if moodle.is_logged():
            print("✅ Login exitoso.")
            print(f"URL actual: {moodle.page.url}")
            input("\nPresiona ENTER para cerrar el navegador...")
        else:
            print("❌ Error: No fue posible iniciar sesión.")
            print(f"URL actual: {moodle.page.url}")

    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

    finally:
        # Cerrar navegador de forma segura
        try:
            moodle.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()