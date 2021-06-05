class CustomState:
    def __init__(self, position, visitedCorners):
        self.position = position
        self.visitedCorners = visitedCorners

    def __eq__(self, other):
        return isinstance(other, CustomState) and self.position == other.position and self.visitedCorners == other.visitedCorners

    def __hash__(self):
        return hash(self.position)

    def __str__(self):
        return f"(CustomState object) POSITION : {self.position} || VISITED CORNERS : {self.visitedCorners}"