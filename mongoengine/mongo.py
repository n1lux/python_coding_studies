from mongoengine import *

connect("tumbleblog")


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User,reverse_delete_rule=CASCADE)  # These are similar to foreign key fields in traditional ORMs
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocument(Comment))

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


def main():
    user_00 = User(email="teste@gmail.com", first_name="David", last_name="Gilmour")
    user_00.save()


if __name__ == "__main__":
    main()
