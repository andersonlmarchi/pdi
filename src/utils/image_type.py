class ImageType:

    def __init__(self, type, width, height, intensity, content):
        self.type = type
        self.width = width # largura
        self.height = height # altura
        self.intencity = intensity
        self.content = content

    def get_type(self):
        return self.type

    def get_size(self):
        return self.width + " " + self.height

    def get_header(self):
        intencity = self.intencity + "\n" if self.intencity > 1 else ""
        return self.type + "\n" + str(self.size()) + "\n" + str(intencity)
    
    def get_content(self):
        return self.content
    
    def get_intencity(self):
        return self.intencity
    