from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

# === MEET 1 ===
def meet1():
    console.print(Panel("MEET 1: Tabel Kebenaran Perbandingan Boolean", style="bold green"))
    a, b = 24, 53

    console.print(f"[cyan]a = {a}, b = {b}[/cyan]\n")

    console.print(f"[white]a < b[/white]     → {a} lebih kecil dari {b}     → [bold]{a < b}[/bold]")
    console.print(f"[white]a > b[/white]     → {a} lebih besar dari {b}    → [bold red]{a > b}[/bold red]")
    console.print(f"[white]a <= b[/white]    → {a} lebih kecil atau sama dengan {b} → [bold]{a <= b}[/bold]")
    console.print(f"[white]a != b[/white]    → {a} tidak sama dengan {b}  → [bold]{a != b}[/bold]")

    console.print(f"[white]a not b[/white]    → ekspresi tidak valid secara Python\n")
    console.print("[yellow]Note:[/] a not b bukan sintaks Python yang valid, gunakan 'not a' atau 'not b' untuk operasi logika.")


# === MEET 2 ===
def meet2():
    console.print(Panel("MEET 2: Operasi Logika (NOT & AND)", style="bold cyan"))

    x = True
    z = not x
    console.print(f"[white]x = {x} → NOT x artinya nilai kebalikan dari x[/white]")
    console.print(f"Nilai dari z = not x → [bold red]{z}[/bold red]\n")

    console.print("[bold]Tabel Operasi AND:[/bold]")
    kombinasi = [(True, True), (True, False), (False, True), (False, False)]
    for x, y in kombinasi:
        hasil = x and y
        warna = "green" if hasil else "red"
        console.print(f"[{warna}]{x} and {y} = {hasil}[/{warna}]  → {'Keduanya True' if hasil else 'Salah satu atau keduanya False'}")


# === MEET 3 & 4 ===
def meet3_dan_4():
    console.print(Panel("MEET 3 & 4: Luas dan Gambar Segitiga", style="bold yellow"))
    alas = int(input("Masukkan alas segitiga (cm): "))
    tinggi = int(input("Masukkan tinggi segitiga (cm): "))
    if alas > 0 and tinggi > 0:
        luas = 0.5 * alas * tinggi
        console.print(f"Luas segitiga adalah: [bold green]{luas:.2f} cm²[/bold green]\n")
        console.print("[bold]Gambar segitiga:[/bold]")
        for i in range(1, tinggi + 1):
            console.print(' ' * (tinggi - i) + '*' * (2 * i - 1))
    else:
        console.print("[red]Alas dan tinggi harus lebih dari 0![/red]")

# === MEET 5 ===
def meet5():
    console.print(Panel("MEET 5: Kalkulator Sederhana", style="bold blue"))
    operasi = input("Operasi (+, -, *, /): ")
    angka1 = float(input("Angka pertama: "))
    angka2 = float(input("Angka kedua: "))
    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/" and angka2 != 0:
        hasil = angka1 / angka2
    else:
        console.print("[red]Operasi tidak valid atau pembagian dengan nol.[/red]")
        return

    hasil_final = int(hasil) if hasil == int(hasil) else hasil
    console.print(f"Hasil = [bold green]{hasil_final}[/bold green]")

# === MEET 6 ===
def meet6():
    console.print(Panel("MEET 6: Hak Akses", style="bold red"))
    akses = input("Masukkan hak akses Anda: ").lower()
    if akses == "admin":
        console.print("[green]Full akses[/green]")
    else:
        console.print("[red]Akses denied[/red]")

# === MEET 7 ===
def meet7():
    console.print(Panel("MEET 7: Pengecekan Panjang Password", style="bold magenta"))
    
    password = input("Masukkan password: ")
    panjang = len(password)
    
    console.print(f"Panjang password yang Anda masukkan adalah: [cyan]{panjang} karakter[/cyan]")
    
    if panjang < 8:
        console.print("[bold red]❌ Karakter kurang![/bold red]")
        console.print("[yellow]Password harus minimal 8 karakter agar lebih aman.[/yellow]")
    else:
        console.print("[bold green]✅ Karakter cukup![/bold green]")
        console.print("[green]Password memenuhi syarat keamanan minimum.[/green]")


# === MEET 8 ===
def meet8():
    console.print(Panel("MEET 8: Manipulasi String Angka", style="bold cyan"))
    number = "1234567890"
    console.print("[bold yellow]String angka yang akan dianalisis:[/bold yellow]")
    console.print(f"[bold]{number}[/bold]\n")
    index_row = "Index  : " + " ".join([str(i) for i in range(len(number))])
    char_row  = "Char   : " + " ".join(list(number))
    console.print("[bold blue]Visualisasi Posisi Karakter:[/bold blue]")
    console.print(index_row)
    console.print(char_row + "\n")
    console.print("[bold green]Analisis:[/bold green]")
    console.print(f"a. [yellow]Data terakhir[/yellow] (index -1 atau {len(number)-1}): [bold cyan]{number[-1]}[/bold cyan]")
    console.print(f"b. [yellow]Data pertama[/yellow]  (index 0): [bold cyan]{number[0]}[/bold cyan]")
    console.print(f"c. [yellow]Data ke-3 sampai ke-6[/yellow] (index 2 s.d. 5): [bold cyan]{number[2:6]}[/bold cyan]")
    console.print("\n[dim]Catatan: String di Python bisa diakses seperti array dengan indeks.[/dim]")

# === MEET 9 & 10 ===
def meet9_10():
    console.print(Panel("MEET 9 & 10: Pemisahan Domain", style="bold green"))
    domain = input("Masukkan domain (contoh: rosiana.com/rosiana.co.id): ").strip()
    
    parts = domain.split(".")
    
    if len(parts) >= 2:
        nama = parts[0]
        ekstensi = ".".join(parts[1:])  # gabungkan semua sisanya
        console.print(f"Nama domain utama: [bold cyan]{nama}[/bold cyan]")
        console.print(f"Ekstensi domain: [bold magenta]{ekstensi}[/bold magenta]")
        console.print("[green]Domain valid dan berhasil dipisah![/green]")
    else:
        console.print("[red]❌ Format domain tidak valid. Harus ada titik (.)[/red]")


# === HEADER ===
def tampilkan_header():
    console.print(Panel(
        "[bold white]FINAL PROJECT UAS[/bold white]\n"
        "[yellow]Kelompok:[/yellow]\n"
        "- ROSIANA SUDRAJAD (24241157)",
        style="bold blue"
    ))

# === MAIN MENU ===
def main():
    while True:
        tampilkan_header()
        menu = Table(title="Daftar Program", show_header=True, header_style="bold magenta")
        menu.add_column("No", style="cyan", justify="center")
        menu.add_column("Program", style="white")
        menu.add_row("1", "MEET 1 (Perbandingan Boolean)")
        menu.add_row("2", "MEET 2 (Operasi Logika)")
        menu.add_row("3", "MEET 3 dan 4 (Segitiga dan Gambar)")
        menu.add_row("4", "MEET 5 (Kalkulator Sederhana)")
        menu.add_row("5", "MEET 6 (Hak Akses)")
        menu.add_row("6", "MEET 7 (Cek Password)")
        menu.add_row("7", "MEET 8 (Manipulasi String Angka)")
        menu.add_row("8", "MEET 9 dan 10 (Pemisahan Domain)")
        menu.add_row("0", "Keluar")
        console.print(menu)
        pilihan = Prompt.ask("Masukkan nomor program", default="0")
        if pilihan == "1":
            meet1()
        elif pilihan == "2":
            meet2()
        elif pilihan == "3":
            meet3_dan_4()
        elif pilihan == "4":
            meet5()
        elif pilihan == "5":
            meet6()
        elif pilihan == "6":
            meet7()
        elif pilihan == "7":
            meet8()
        elif pilihan == "8":
            meet9_10()
        elif pilihan == "0":
            console.print("[bold green]Terima kasih! Program selesai.[/bold green]")
            break
        else:
            console.print("[bold red]Pilihan tidak valid[/bold red]")
        Prompt.ask("\n[cyan]Tekan ENTER untuk kembali ke menu[/cyan]", default="")

main()