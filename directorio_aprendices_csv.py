from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.text import Text
import pandas as pd
from typing import Optional

console = Console()
CSV_FILE = "aprendices.csv"


def crear_aprendiz(nombre: str, apellido: str, direccion: str, telefono: int, ficha: int) -> None:
    """
    Crea o agrega un aprendiz al archivo CSV.

    Args:
        nombre (str): Nombre del aprendiz.
        apellido (str): Apellido del aprendiz.
        direccion (str): Dirección del aprendiz.
        telefono (int): Teléfono del aprendiz.
        ficha (int): Ficha del aprendiz.

    Returns:
        None
    """
    nuevo = pd.DataFrame([{
        "Nombre": nombre,
        "Apellido": apellido,
        "Direccion": direccion,
        "Telefono": telefono,
        "Ficha": ficha
    }])

    try:
        df = pd.read_csv(CSV_FILE, dtype={"Telefono": int, "Ficha": int})
        df = pd.concat([df, nuevo], ignore_index=True)
    except FileNotFoundError:
        df = nuevo

    df.to_csv(CSV_FILE, index=False)
    console.print(Panel.fit(
        Text(f"Aprendiz {nombre} {apellido} agregado correctamente.", style="bold white on green"),
        title="[bold bright_white]✔ Éxito[/bold bright_white]",
        border_style="green"
    ))


def leer_aprendices() -> pd.DataFrame:
    """
    Lee y devuelve el contenido del archivo CSV con los aprendices.
    Muestra el índice de cada aprendiz.
    """
    try:
        df = pd.read_csv(CSV_FILE, dtype={"Telefono": int, "Ficha": int})
        console.print(Panel.fit(
            Text("LISTA DE APRENDICES", style="bold magenta underline"),
            title="[bold magenta]Directorio[/bold magenta]",
            border_style="magenta"
        ))
        if not df.empty:
            table = Table(title="[bold cyan]Directorio de Aprendices[/bold cyan]", header_style="bold cyan", border_style="cyan")
            table.add_column("Índice", justify="center", style="bold yellow")
            for col in df.columns:
                table.add_column(col, justify="center", style="bold white")
            for idx, row in df.iterrows():
                table.add_row(f"[bold yellow]{idx}[/bold yellow]", *[f"[white]{str(val)}[/white]" for val in row.values])
            console.print(table)
        else:
            console.print(Panel.fit(
                Text("No hay registros aún.", style="bold black on yellow"),
                title="[bold yellow]Advertencia[/bold yellow]",
                border_style="yellow"
            ))
        return df
    except FileNotFoundError:
        console.print(Panel.fit(
            Text("No hay registros aún.", style="bold black on yellow"),
            title="[bold yellow]Advertencia[/bold yellow]",
            border_style="yellow"
        ))
        return pd.DataFrame(columns=["Nombre", "Apellido", "Direccion", "Telefono", "Ficha"])


def actualizar_aprendiz_por_indice(indice: int, columna: str, nuevo_valor) -> bool:
    """
    Actualiza el valor de una columna específica de un aprendiz por índice.

    Args:
        indice (int): Índice del aprendiz en el DataFrame.
        columna (str): Nombre de la columna a actualizar.
        nuevo_valor: Nuevo valor para la columna.

    Returns:
        bool: True si se actualizó, False si no se encontró.
    """
    try:
        df = pd.read_csv(CSV_FILE, dtype={"Telefono": int, "Ficha": int})
    except FileNotFoundError:
        console.print(Panel.fit(
            Text("No hay registros para actualizar.", style="bold black on yellow"),
            title="[bold yellow]Advertencia[/bold yellow]",
            border_style="yellow"
        ))
        return False

    if indice < 0 or indice >= len(df):
        console.print(Panel.fit(
            Text(f"Índice {indice} no encontrado.", style="bold white on red"),
            title="[bold red]Error[/bold red]",
            border_style="red"
        ))
        return False

    if columna not in df.columns:
        console.print(Panel.fit(
            Text(f"Columna '{columna}' no válida.", style="bold white on red"),
            title="[bold red]Error[/bold red]",
            border_style="red"
        ))
        return False

    if columna in ["Telefono", "Ficha"]:
        try:
            nuevo_valor = int(nuevo_valor)
        except ValueError:
            console.print(Panel.fit(
                Text(f"El valor para '{columna}' debe ser un número entero.", style="bold white on red"),
                title="[bold red]Error[/bold red]",
                border_style="red"
            ))
            return False

    df.at[indice, columna] = nuevo_valor
    df.to_csv(CSV_FILE, index=False)
    console.print(Panel.fit(
        Text(f"Aprendiz en índice {indice} actualizado correctamente.", style="bold white on green"),
        title="[bold bright_white]✔ Éxito[/bold bright_white]",
        border_style="green"
    ))
    return True


def menu():
    """
    Muestra un menú interactivo para gestionar el directorio de aprendices.
    """
    while True:
        console.print(Panel.fit(
            Text("MENÚ PRINCIPAL", style="bold white on blue", justify="center"),
            title="[bold blue]★ SENA DIRECTORIO CSV ★[/bold blue]",
            border_style="blue"
        ))
        console.print("[bold bright_cyan]1.[/bold bright_cyan] [bold white]Crear aprendiz[/bold white]")
        console.print("[bold bright_cyan]2.[/bold bright_cyan] [bold white]Leer aprendices[/bold white]")
        console.print("[bold bright_cyan]3.[/bold bright_cyan] [bold white]Actualizar aprendiz[/bold white]")
        console.print("[bold bright_cyan]4.[/bold bright_cyan] [bold white]Salir[/bold white]")
        opcion = Prompt.ask("\n[bold cyan]Seleccione una opción[/bold cyan]", choices=["1", "2", "3", "4"])

        if opcion == "1":
            try:
                nombre = Prompt.ask("[bold green]Ingrese el nombre[/bold green]").strip()
                apellido = Prompt.ask("[bold green]Ingrese el apellido[/bold green]").strip()
                direccion = Prompt.ask("[bold green]Ingrese la dirección[/bold green]").strip()
                telefono = IntPrompt.ask("[bold green]Ingrese el teléfono (solo números)[/bold green]")
                ficha = IntPrompt.ask("[bold green]Ingrese la ficha (solo números)[/bold green]")
                crear_aprendiz(nombre, apellido, direccion, telefono, ficha)
            except ValueError:
                console.print(Panel.fit(
                    Text("Error: Teléfono y ficha deben ser números enteros.", style="bold white on red"),
                    title="[bold red]Error[/bold red]",
                    border_style="red"
                ))
        elif opcion == "2":
            leer_aprendices()
        elif opcion == "3":
            df = leer_aprendices()
            if df.empty:
                continue
            try:
                indice = IntPrompt.ask("[bold magenta]Ingrese el índice del aprendiz a actualizar[/bold magenta]")
                columnas = list(df.columns)
                columna = Prompt.ask(f"[bold magenta]Ingrese el nombre de la columna a actualizar.[/bold magenta]", choices=columnas)
                nuevo_valor = Prompt.ask(f"[bold magenta]Ingrese el nuevo valor para '{columna}'[/bold magenta]")
                actualizado = actualizar_aprendiz_por_indice(indice, columna, nuevo_valor)
                if not actualizado:
                    console.print(Panel.fit(
                        Text("No se pudo actualizar el aprendiz.", style="bold white on red"),
                        title="[bold red]Error[/bold red]",
                        border_style="red"
                    ))
            except ValueError:
                console.print(Panel.fit(
                    Text("Error: Entrada inválida.", style="bold white on red"),
                    title="[bold red]Error[/bold red]",
                    border_style="red"
                ))
        elif opcion == "4":
            console.print(Panel.fit(
                Text("Saliendo del programa. ¡Hasta luego!", style="bold white on blue"),
                title="[bold blue]★ FIN ★[/bold blue]",
                border_style="blue"
            ))
            break
        else:
            console.print(Panel.fit(
                Text("Opción no válida. Intente de nuevo.", style="bold white on red"),
                title="[bold red]Error[/bold red]",
                border_style="red"
            ))


if __name__ == "__main__":
    menu()
