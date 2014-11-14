from redisco import models


class BaseModel(models.Model):
    pass


class Board(BaseModel):
    name = models.Attribute(required=True)
    desc = models.Attribute(required=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Item(BaseModel):
    board_id = models.IntegerField(required=True)
    name = models.Attribute(required=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Response(BaseModel):
    username = models.Attribute(required=True)
    board_id = models.IntegerField(required=True)
    items = models.ListField(int)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


def get_boards(limit=10):
    return Board.objects.all().limit(limit)


def get_board(board_id):
    return Board.objects.get_by_id(board_id)


def get_items(board_id):
   return Item.objects.filter(board_id=board_id)


def get_responses(board_id, limit=3):
    return Response.objects.filter(board_id=board_id).order('-created')


def get_response(response_id):
    return Response.objects.get_by_id(response_id)

