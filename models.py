from redisco import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Board(BaseModel):
    name = models.Attribute(required=True)
    desc = models.Attribute(required=False)


class Item(BaseModel):
    board_id = models.IntegerField(required=True)
    name = models.Attribute(required=True)


def get_boards(limit=10):
    return Board.objects.all().limit(limit).order("-created")


def get_board(board_id):
    return Board.objects.get_by_id(board_id)


def get_items(board_id):
   return Item.objects.filter(board_id=board_id)

