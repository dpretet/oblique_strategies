"""Textual TUI for Oblique Strategies."""

from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header, Static
from textual.containers import Container, VerticalScroll
from textual.screen import Screen
from .core import draw_strategy


class StrategyDisplay(Static):
    """Display the drawn strategy."""
    
    def __init__(self, lang="en", *args, **kwargs):
        super().__init__("Press D to draw a strategy", *args, **kwargs)
        self.lang = lang
        self.strategy = ""
    
    def on_mount(self) -> None:
        """Load a strategy when the widget is mounted."""
        self.draw_new_strategy()
    
    async def draw_new_strategy(self) -> None:
        """Draw a new strategy and update the display."""
        self.strategy = draw_strategy(self.lang)
        self.update(self.strategy)
    
    async def change_language(self, lang: str) -> None:
        """Change the language and redraw a strategy."""
        self.lang = lang
        await self.draw_new_strategy()


class ObliqueApp(App):
    """Main TUI application."""
    
    CSS_PATH = "tui.css"
    BINDINGS = [
        ("d", "draw", "Draw New Strategy"),
        ("q", "quit", "Quit"),
        ("f", "fr", "French"),
        ("e", "en", "English"),
    ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = "en"
        self.strategy_display = None
    
    def compose(self) -> ComposeResult:
        """Compose the app UI."""
        yield Header()
        yield Footer()
        with Container(id="app-container"):
            self.strategy_display = StrategyDisplay(id="strategy-display", lang=self.lang)
            yield self.strategy_display
            with Container(id="button-container"):
                yield Button("Draw New Strategy", id="draw-button", variant="primary")
                yield Button("French", id="fr-button")
                yield Button("English", id="en-button")
    
    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "draw-button":
            await self.draw_new_strategy()
        elif event.button.id == "fr-button":
            await self.change_language("fr")
        elif event.button.id == "en-button":
            await self.change_language("en")
    
    def action_draw(self) -> None:
        """Draw a new strategy."""
        self.draw_new_strategy()
    
    def action_fr(self) -> None:
        """Switch to French."""
        self.change_language("fr")
    
    def action_en(self) -> None:
        """Switch to English."""
        self.change_language("en")
    
    async def draw_new_strategy(self) -> None:
        """Draw a new strategy and update the display."""
        if self.strategy_display:
            await self.strategy_display.draw_new_strategy()
    
    async def change_language(self, lang: str) -> None:
        """Change the language and redraw a strategy."""
        self.lang = lang
        if self.strategy_display:
            await self.strategy_display.change_language(lang)


class HelpScreen(Screen):
    """Screen to display help information."""
    
    def compose(self) -> ComposeResult:
        yield Container(
            Static("Press [b]D[/b] to draw a new strategy."),
            Static("Press [b]F[/b] for French."),
            Static("Press [b]E[/b] for English."),
            Static("Press [b]Q[/b] to quit."),
            id="help-container",
        )


def main():
    """Run the TUI application."""
    app = ObliqueApp()
    app.run()


if __name__ == "__main__":
    main()
