"""Textual TUI for Oblique Strategies - Simplified Version."""

from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container
from textual.screen import Screen
from textual import events
from .core import draw_strategy


class StrategyScreen(Screen):
    """Main screen displaying the strategy."""
    
    def __init__(self, lang="fr", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = lang
        self.current_strategy = ""
    
    def compose(self) -> ComposeResult:
        """Compose the screen UI."""
        with Container(id="main-container"):
            with Container(id="strategy-container"):
                yield Static(self.get_strategy(), id="strategy-text")
            yield Static("[SPACE] New Strategy  [F] French  [E] English  [Q] Quit", id="key-hint")
    
    def on_mount(self) -> None:
        """Initialize the screen."""
        self.update_strategy()
    
    def get_strategy(self) -> str:
        """Get a new strategy."""
        if not self.current_strategy:
            self.current_strategy = draw_strategy(self.lang)
        return self.current_strategy
    
    def update_strategy(self) -> None:
        """Update the displayed strategy."""
        self.current_strategy = draw_strategy(self.lang)
        self.query_one("#strategy-text", Static).update(self.current_strategy)
    
    async def on_key(self, event: events.Key) -> None:
        """Handle key presses."""
        if event.key == "space" or event.character == " ":  # Handle space key
            self.update_strategy()
        elif event.key == "q":
            self.app.exit()
        elif event.key == "f":
            self.lang = "fr"
            self.update_strategy()
        elif event.key == "e":
            self.lang = "en"
            self.update_strategy()


class ObliqueApp(App):
    """Main TUI application."""
    
    CSS_PATH = "tui.css"
    BINDINGS = [
        ("space", "draw", "New Strategy"),
        ("q", "quit", "Quit"),
        ("f", "fr", "French"),
        ("e", "en", "English"),
    ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lang = "fr"
    
    def on_mount(self) -> None:
        """Initialize the app."""
        self.push_screen(StrategyScreen(lang=self.lang))


def main():
    """Run the TUI application."""
    try:
        app = ObliqueApp()
        app.run()
    except Exception as e:
        print(f"Error running application: {str(e)}")


if __name__ == "__main__":
    main()
