class Patent:
    def __init__(self, title, link, date, description, source) -> None:
        self.title = title
        self.link = link
        self.date = date
        self.description = description
        self.source = source
        self.itemSelected = False