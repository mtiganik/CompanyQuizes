class Square:
    def draw(self):
        print(f'Inside Square::draw()')

    def resize(self):
        print(f'Inside Square::resize()')

class Circle:
    def draw(self):
        print(f'Inside Circle::draw()')
    
    def resize(self):
        print(f'Inside Circle::resize()')

class ShapeManager:
    def __init__(self, shapes):
        self._shapes = shapes
    
    def manage(self):
        for shape in self._shapes:
            shape.draw()
            shape.resize()
#if __name__ == '__main__':
shapes = [Square(), Square(), Circle(),Square(), Circle(),Circle(),Square(),Circle()]
shape_manager = ShapeManager(shapes)
shape_manager.manage()