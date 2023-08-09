class Patent:
    def __init__(self, title, link, date, descriprion, source) -> None:
        self.title = title
        self.link = link
        self.date = date
        self.descriprion = descriprion
        self.source = source
        self.itemSelected = False