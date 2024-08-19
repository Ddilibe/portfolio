from puepy import Application, t, Page
from app import app


@app.page('')
class MenuBar(Page):
    def populate(self):
        with t.nav(classes=['navbar', 'bg-body-tertiary']) as navigation:
            with t.div(classes=['container-fluid']) as container:
                with t.a(classes=['navbar-brand']) as link:
                    img = t.img(src='', alt="Logo", width="30", height="24", classes="d-inline-block align-text-top")
                    title = t.p("Dilibe's Portfolio")
                    