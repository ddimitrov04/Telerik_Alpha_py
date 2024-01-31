class Comment:
    CONTENT_LEN_MIN = 3
    CONTENT_LEN_MAX = 200
    CONTENT_LEN_ERR = f'Content must be between {CONTENT_LEN_MIN} and {CONTENT_LEN_MAX} characters long!'

    def __init__(self, content: str, author: str):
        self.content = content
        self.author = author

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, con):
        if len(con) < self.CONTENT_LEN_MIN or len(con) > self.CONTENT_LEN_MAX:
            raise ValueError(self.CONTENT_LEN_ERR)

        self._content = con

    def __str__(self):
        return f"----------\n{self.content}\nUser: {self.author}\n----------"