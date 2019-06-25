

class Flat(object):
    def __init__(self, url, title, image, price):
        self.url = url
        self.title = title
        self.image = image
        self.price = price

    def to_dict(self):
        return {
            "url" : self.url,
            "title" : self.title,
            "description" : self.description,
            "image" : self.image,
            "price" : self.price
        }

    def __str__(self):
       return "Url: {url}\nTitle: {title}\nImage URL: {image}\nPrice: {price}\n\n".format(
                                                                                        url=self.url,
                                                                                        title=self.title, 
                                                                                        image=self.image,
                                                                                        price=self.price
                                                                                    )
