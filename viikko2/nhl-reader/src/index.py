from rich.console import Console
from rich.table import Table
from player_reader import PlayerReader
from player_stats import PlayerStats

console = Console()


def get_season():
    season = console.input("[bold]Season[/] (): ").strip()
    if not season:
        season = "2024-25"
    return season


def initialize_stats(season):
    reader = PlayerReader(season)
    stats = PlayerStats(reader)
    if not stats.players:
        console.print("[red]Virheellinen kausi tai ei löytynyt pelaajia.[/red]")
        return None
    return stats


def get_nationality(stats):
    nationalities = sorted(
        list(
            set(player.nationality for player in stats.players if player.nationality)
        )
    )
    nat_list_str = "/".join(nationalities)
    prompt_msg = f"[bold]Nationality[/] [[cyan]{nat_list_str}[/cyan]] (): "
    return console.input(prompt_msg).strip().upper()


def create_player_table(players):
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Released", style="cyan", no_wrap=True)
    table.add_column("teams", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="bold yellow")

    for player in players:
        table.add_row(
            str(player.name),
            str(player.team),
            str(player.goals),
            str(player.assists),
            str(player.points),
        )
    return table


def process_nationality_and_print(season, stats):
    nationality = get_nationality(stats)
    players = stats.top_scorers_by_nationality(nationality)

    console.print(f"\n[bold]Season {season} players from {nationality}[/bold]\n")

    if not players:
        console.print(
            f"[yellow]Ei löytynyt pelaajia kansalaisuudelta {nationality}.[/yellow]"
        )
        return

    table = create_player_table(players)
    console.print(table)


def main():
    season = get_season()
    stats = initialize_stats(season)
    if stats:
        process_nationality_and_print(season, stats)


if __name__ == "__main__":
    main()
