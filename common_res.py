from flask import jsonify


class CommonRes:

    def __init__(self):
        self.code = 0
        self.message = ''
        self.data = None

    def to_res(self):
        return jsonify(self.__dict__)
