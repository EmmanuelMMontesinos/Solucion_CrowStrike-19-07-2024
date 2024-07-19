import winreg
import os

# Función para saber si el Sistema esta en Modo Seguro
def is_safe_mode():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SYSTEM\\CurrentControlSet\\Control\SafeBoot\\Option')
        value, _ = winreg.QueryValueEx(key, 'OptionValue')
        return value != 0
    except FileNotFoundError:
        return False

def exit_program():
    input("Pulse cualquier tecla para cerrar.")
# Programa Principal
if __name__ == "__main__":
    # Comprueba si esta en modo Seguro con la funcion is_safe
    if is_safe_mode():
        print("El sistema está en modo seguro.")
        # Comprueba si existe el archivo
        if os.path.exists(r"C:\\Windows\\System32\\drivers\\CrowdStrike\\C-00000291*.sys"):
            print("Borrando archivo problemático: 'C-00000291*.sys'")
            # Borra el archivo
            os.remove(r"C:\\Windows\\System32\\drivers\\CrowdStrike\\C-00000291*.sys")
            print("El archivo 'C-00000291*.sys' ha sido eliminado con exito.")
            print("Reinicie el equipo en modo normal.\nCreado por @EmmanuelMMontesinos con la solución de la comunidad")
        else:
            print("No existe el archivo problemático 'C-00000291*.sys'")
    # Si no esta en modo seguro
    else:
        print("El sistema no está en modo seguro.")
        print("Reinicie el PC en Modo seguro y vuelva a ejecutar el programa")
    
    exit_program() # En cualquiera de los casos enviamos el mensaje para salir
