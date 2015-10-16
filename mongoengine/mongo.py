from mongoengine import *

connect('tumbleblog', host="localhost", port=27017)


class User(Document):
    id = LongField(required=True, primary_key=True)
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User,reverse_delete_rule=CASCADE)  # These are similar to foreign key fields in traditional ORMs
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()



def create_user():
    user_00 = User(id=00000001, email="teste@gmail.com", first_name="David", last_name="Gilmour")
    user_00.save()
    user_01 = User(id=00000002,email="nilo@teste.com", first_name="Nilo", last_name="Alexandre")
    user_01.save()


def create_post():
    tp = TextPost()
    comment01 = Comment(name = "comment 01", content = 'Ola esse e meu primeiro comentario de post')
    comment02 = Comment(name = "comment 0s", content = 'Ola esse e meu segundo comentario de post')

    tp.title = "MEu primeiro post"
    tp.autor = User.objects(id = 1)
    tp.tags = ['mongo', 'nosql', 'teste']
    tp.comments = [comment01, comment02]
    tp.content = "Ola Meu nome e Nilo e estou aprendendo mongoengine agora..."

    tp.save()

def main():
    create_post()
if __name__ == "__main__":
    main()
